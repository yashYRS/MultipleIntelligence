
from collections import defaultdict
import xml.etree.ElementTree as ET


class GameAgent():

    def __init__(self, game_xml_file):

        # Value for thresholds
        self.upper_t = 0.9
        self.lower_t = 0.4
        self.alpha_t = 0.7
        self.beta_t = 0.3
        # Initial state of maximum states
        self.max_states = defaultdict(int)
        self.curr_state = {}
        self.curr_score = {}

        # Levels per game present
        self.games_played = 0
        self.levels_done = []

        # Read the file, and load the xml data
        game_data = ET.parse(game_xml_file)
        game_root = game_data.getroot()
        self.game_data = game_root
        self.game_levels = [int(game.attrib['levels']) for game in game_root]

    # def initial_setup(self):
        self.get_max_states()
        self.reset_curr_state()

    def get_max_states(self):
        states = {}
        for idx, game in enumerate(self.game_data):
            for parameter in game:
                # Category refers to the smart type -> body, physical etc.
                for category in parameter.attrib:
                    param_score = self.game_levels[idx]*float(parameter.attrib[category])
                    states[category] = states.get(category, 0) + param_score
        self.max_states = states

    def reset_curr_state(self):
        for category in self.max_states:
            self.curr_state[category] = 0

    def get_game_info(self, game_id, level):
        # Default values
        mod_name, game_state = '', {}

        for game in self.game_data:
            if game.attrib['ID'] == str(game_id):
                # If game found, return module and level name
                mod_name = game.attrib['module_name' + str(level)]

                for param in game:
                    for category in param.attrib:
                        game_state[category] = float(param.attrib[category])

                break
        return mod_name, game_state

    def find_games_left(self):
        games_left_id = []
        for idx, val in enumerate(self.game_levels):
            if val - self.levels_done[idx] > 0:
                games_left_id.append(idx + 1)  # game id is 1 + indx
        return games_left_id

    def find_heuristic(self, game_id, level):

        _, game_state = self.get_game_info(game_id, level)

        # assume perfect score acheived no matter what game is played
        for key, game_value in game_state.items():
            self.curr_state[key] = self.curr_state.get(key, 0) + game_value
            self.curr_score[key] = self.curr_score.get(key, 0) + game_value

        # find max_score (% wise) in which intelligence type,
        # min_state (%) amongst all [ minimum in terms of games played ]
        score_percentages = {}
        state_percentages = {}

        for key, curr_value in self.curr_score.items():
            if curr_state[key] == 0:
                score_percentages[key] = 0
            else:
                score_percentages[key] = curr_value/curr_state[key]
            state_percentages[key] = curr_state[key]/self.max_states[key]

        # get the intelligence type with the highest percentage
        max_key = max(score_percentages, key=score_percentages.get)
        min_key = min(state_percentages, key=state_percentages.get)
        # get dist from upper threshold & that curr/max of intelligence type
        heur_val2 = self.upper_t - state_percentages[max_key]
        heur_val1 = self.lower_t - state_percentages[min_key]

        # no use going for this
        if game_state[min_key] == 0:
            return self.beta*heur_val2

        if heur_val1 > 0 and heur_val2 > 0:
            # Both positive, then take a weighted sum
            return self.alpha*self.heur_val1 + self.beta*self.heur_val2
        elif heur_val2 < 0 and heur_val1 > 0:
            # 1st heuristic positive, take only the positive value
            return self.alpha*heur_val1
        elif heur_val2 > 0 and heur_val1 < 0:
            # 2nd heuristic positive, take only the positive value
            return self.alpha*heur_val2

    def goal_test(self):
        """ Return True if goal achieved, else false """

        completion_dict = {}
        for category, curr_value in self.curr_state.items():
            completion_dict[key] = curr_value/self.maximum_state[key]

        max_reqt_list = [v > self.upper_t for v in completion_dict.values()]
        min_reqt_list = [v > self.lower_t for v in completion_dict.values()]

        # Test is passed if all categories have been tried
        # & at least 1 has been explored till the end
        if any(max_reqt_list) and all(min_reqt_list):
            return True
        return False

    def ai(self, score_variable, max_game_limit=10):
        global initial_state
        global maximum_state
        global levels_per_game
        global levels_done
        global games_played
        global curr_state
        global curr_score

        # Choose randomly, till a sizeable number of games have been played
        if self.games_played < 8:
            # # choose a game randomly
            game_choice_id = random.choice(range(1, max_game_limit))
            if self.levels_done[game_choice_id - 1] == 0:
                # # get the score and the updated state after playing the game
                module_name, game_state = self.get_info_game(game_choice_id, 1)
                # # score is the actual score
                for key in self.curr_state:
                    self.curr_score[key] = self.curr_score[key] + game_state[key]*score_variable
                    self.curr_state[key] = self.curr_state[key] + game_state[key]

                # update call_game function, it needs to simply return the module_name.
                self.games_played = self.games_played + 1
                # increment to show the level at which a player is
                self.levels_done[game_choice_id - 1] = 1
                return module_name
        else:
            if self.goal_test():
                return "game_ended"
            games_left = self.find_games_left()
            game_choice_id = 0
            max_heur_score = 0
            heur_scores = {g: self.find_heuristic(g, self.levels_done[g-1] + 1)
                           for g in games_left}

            # Choose the game with the highest heuristic score
            game_chosen = max(heur_scores, key=heur_scores.get)
            # -1 since the index is 1 less than actual id
            reqd_level = self.levels_done[game_chosen - 1] + 1

            module_name, game_state = self.get_info_game(game_chosen, reqd_level)

            # Update current score & state, based on the game selected
            for key in self.curr_state:
                self.curr_score[key] = self.curr_score[key] + game_state[key]*score_variable
                self.curr_state[key] = self.curr_state[key] + game_state[key]

            self.games_played = self.games_played + 1
            # increment to show the level at which a player is
            levels_done[game_choice_id - 1] = reqd_level + 1
            return module_name
