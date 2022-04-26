import random
from collections import defaultdict
import xml.etree.ElementTree as ET


class GameAgent():

    def __init__(self, game_xml_file):

        # Minimum fulfillment criteria for our best performing category
        self.upper_t = 0.9
        # Minimum fulfillment criteria for all categories
        self.lower_t = 0.4
        # Weightage of choosing a category, which we have not tried
        self.explore_t = 0.7
        # Weightage of choosing a category, where we are performing well
        self.exploit_t = 0.3

        self.session_id = 1
        self.initial_story = 'static/game_text/initial_story.txt'

        # Initial state of maximum states
        self.max_states = defaultdict(int)
        self.curr_state = {}
        self.curr_score = {}

        # ID of the game being played
        self.curr_game = -1
        self.curr_level = 0
        # Levels per game present
        self.games_played = 0

        # Read the file, and load the xml data
        game_data = ET.parse(game_xml_file)
        game_root = game_data.getroot()
        self.game_data = game_root
        self.game_levels = [int(game.attrib['levels']) for game in game_root]
        self.levels_done = []
        # Total Games
        self.num_games = len(self.game_levels)

    def get_initial_info(self):
        """Returns:str: text to show on screen when the game first starts"""
        game_text = ''
        with open(self.initial_story) as f:
            game_text = f.read()
        return game_text

    def get_max_states(self):
        """The parameters of a game contain the weightage of that particular
        game, distributed across the intelligence types (since many games
        require diverse skill sets). For each intelligence type, calculate the
        max state possible without repetition of any game at the same level.
        """
        states = {}
        for idx, game in enumerate(self.game_data):
            for parameter in game:
                # Category refers to the smart type -> body, physical etc.
                for category in parameter.attrib:
                    param_score = self.game_levels[idx]*float(parameter.attrib[category])
                    states[category] = states.get(category, 0) + param_score
        self.max_states = states

    def reset_curr_state(self):
        """Initial state and score set to 0 for each category
        """
        for category in self.max_states:
            self.curr_state[category] = 0
            self.curr_score[category] = 0
        self.levels_done = [0 for game in self.game_data]

    def get_game_info(self, game_id, level):
        """
        Args:
            game_id (int): Game id to identify the game in the XML
            level (int): The level of the game, for which the info
                needs to be extracted

        Returns:
            str: The url for the game requested
            str: The back story for the game & level requested
            dict: The distribution across intelligence types for the game
        """
        mod_name, game_text, game_state = '', '', {}

        for game in self.game_data:
            if game.attrib['ID'] == str(game_id):
                # If game found, return module and level name
                mod_name = game.attrib['name']
                story_file = game.attrib.get('story' + str(level), "")
                if story_file == "":
                    story_file = game.attrib['story1']
                with open(story_file) as f:
                    game_text = f.read()

                for param in game:
                    for category in param.attrib:
                        game_state[category] = float(param.attrib[category])

                break
        return mod_name, game_text, game_state

    def find_games_left(self):
        """list: Return game ids for whom all levels haven't been covered"""
        games_left_id = []
        for idx, val in enumerate(self.game_levels):
            if val - self.levels_done[idx] > 0:
                games_left_id.append(idx + 1)  # game id is 1 + indx
        return games_left_id

    def get_game_probability(self, game_id, level):
        """Get a heuristic score on whether to choose the game details
        given. Based on the game's requirement of each intelligence type,
        and the current overall game situation, it is decided whether we
        should exploit (choose games with intelligence types, where we are
        doing well) or explore (choose games with intelligence types, which
        we have not yet seen)

        Args:
            game_id (int): Game id, for which score needs to be calculated
            level (int): Level at which the game will be played

        Returns:
            float: A score between 0 and 1. Higher score, implies higher
                chance of getting selected
        """
        _, _, game_state = self.get_game_info(game_id, level)

        state_with_game = {}
        score_with_game = {}
        # assume perfect score acheived for the current candidate game
        for key, game_value in game_state.items():
            state_with_game[key] = self.curr_state.get(key, 0) + game_value
            score_with_game[key] = self.curr_score.get(key, 0) + game_value

        score_percentages = {}
        state_percentages = {}

        for key, curr_value in score_with_game.items():
            # Find ratio of score achieved to max score for all categories
            if state_with_game[key] == 0:
                score_percentages[key] = 0
            else:
                score_percentages[key] = curr_value/state_with_game[key]
            # Find ratio of completion for each category
            state_percentages[key] = state_with_game[key]/self.max_states[key]

        # Get the category where player has acheived highest scores
        max_key = max(score_percentages, key=score_percentages.get)
        # Get the category, which has been played the least
        min_key = min(state_percentages, key=state_percentages.get)

        # Exploit: choose a game where we are already doing well
        exploit_heur = self.upper_t - state_percentages[max_key]
        # Explore: choose a game with a category, we have not tried enough
        explore_heur = self.lower_t - state_percentages[min_key]

        # If the game we are going to choose, does not have the category
        # we want to explore, only add the exploit heuristic
        if game_state[min_key] == 0:
            return self.exploit_t*exploit_heur

        # Both exploitation and exploration are valid strategies, in case
        # both values are positive, since there is room for both
        if exploit_heur > 0 and exploit_heur > 0:
            return self.explore_t*explore_heur + self.exploit_t*exploit_heur
        elif exploit_heur < 0 and explore_heur > 0:
            # We have exploited enough, hence values have crossed even our
            # thresholds. So we have to start exploring all categories, in
            # order to reach our goal.
            return self.explore_t*explore_heur
        elif explore_heur < 0 and exploit_heur > 0:
            # We have explored all categories, thus now it is time to start
            # finding out which of all the categories are we best at.
            return self.exploit_t*exploit_heur

    def goal_test(self):
        """Game can be ended if all intelligence types have been tried, and
        at least 1 of the intelligence types has been explored till the very
        end.

        Returns:
            bool: True, if game can be ended
        """

        completion_dict = {}
        for category, curr_value in self.curr_state.items():
            completion_dict[category] = curr_value/self.max_states[category]

        max_reqt_list = [v > self.upper_t for v in completion_dict.values()]
        min_reqt_list = [v > self.lower_t for v in completion_dict.values()]

        if any(max_reqt_list) and all(min_reqt_list):
            return True
        return False

    def update_score(self, score_value):
        if self.curr_game < 0:
            return
        # Get information about the game played
        _, _, game_state = self.get_game_info(self.curr_game, self.curr_level)
        # Update the current state achieved, and the current score achieved
        for key in self.curr_state:
            self.curr_state[key] = self.curr_state[key] + game_state[key]
            self.curr_score[key] = self.curr_score[key] + game_state[key]*score_value
        # Update the number of games played
        self.games_played = self.games_played + 1
        # Update the number of levels completed for the current game
        self.levels_done[self.curr_game-1] = self.levels_done[self.curr_game-1] + 1

    def get_next_game(self):
        # Choose randomly, till a sizeable number of games have been played
        if self.games_played < 8:
            while True:
                # Choose a game has not been played yet
                game_choice_id = random.choice(range(1, self.num_games))
                if self.levels_done[game_choice_id - 1] == 0:
                    break
            # get the information about the game chosen
            module_name, game_text, game_state = self.get_game_info(game_choice_id, 1)
            # Set the current game & current level
            self.curr_game = game_choice_id
            self.curr_level = 1
            return module_name, game_text
        else:
            if self.goal_test():
                return "end_game", ""
            games_left = self.find_games_left()
            # Find heuristic probability scores for each game that is left
            heur_scores = {g: self.get_game_probability(g, self.levels_done[g-1] + 1)
                           for g in games_left}

            # Choose the game with the highest heuristic score
            game_chosen = max(heur_scores, key=heur_scores.get)
            # -1 since the index is 1 less than actual id
            reqd_level = self.levels_done[game_chosen - 1] + 1

            module_name, game_text, game_state = self.get_game_info(game_chosen, reqd_level)
            # Set the current game & level
            self.curr_game = game_chosen
            self.curr_level = reqd_level

            return module_name, game_text

    def give_final_verdict(self):
        """ Based on the game performance, some professions are recommended"""
        score_percentages = {}
        for key, curr_value in self.curr_score.items():
            # Find ratio of score achieved to max score for all categories
            if self.curr_state[key] > 0:
                score_percentages[key] = (100*curr_value)/self.curr_state[key]

        # Get the category where player has acheived highest scores
        best_category = max(score_percentages, key=score_percentages.get)
        return score_percentages


if __name__ == '__main__':
    from Game import GameAgent
    ga = GameAgent('game_details.xml')
    ga.get_max_states()
    ga.reset_curr_state()
    for i in range(30):
        n, t = ga.get_next_game()
        print("NEXT:", n, "LEVEL", ga.curr_level)
        if n == 'end_game':
            break
        ga.update_score(0.7)
