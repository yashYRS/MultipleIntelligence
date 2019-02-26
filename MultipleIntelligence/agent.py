import xml.etree.ElementTree as ET 

#### -------- --------------  GLOBAL VARIABLES -------- --------------------  #### 


def get_total_each(filename , levels_per_game) : 
	""" Returns total score possible in each module """
	maximum_state = { "picture" : 0, "word" : 0 , "nature" : 0, "people" : 0, "self" : 0, "logic" : 0, "body" :  0, "music" :0  }  
	data = ET.parse(filename)
	root = data.getroot() 
	for indx,game in enumerate(root) : 
		for param in game : 
			for str_key in param.attrib : 
				maximum_state[str_key] = maximum_state[str_key] + float(param.attrib[str_key])*levels_per_game[indx]
	return maximum_state

def get_levels(filename) : 
	data = ET.parse(filename)
	root = data.getroot() 
	levels_per_game = [] 
	for game in root : 
		levels_per_game.append(int(game.attrib['levels']))
	return levels_per_game


def find_heuristic(game_id, level, curr_state, maximum_state , curr_score) : 

	# get game_state 
	_, _ , game_state =  get_info_game( filename , game_id, level )
	
	# assume perfect score acheived no matter what game is played [under-estimate of path]
	for key in game_state : 
		curr_state[key] = curr_state[key] + game_state[key]
		curr_score[key] = curr_score[key] + game_state[key]

	# find max_score (% wise ) in which intelligence type, min_state (%) amongst all [ minimum in terms of games played ]
	score_percentages = {}
	state_percentages = {} 
	for key in curr_score : 	
		if curr_state[key] == 0 : 
			score_percentages[key] = 0 # thus scores_percentage = 0 
		else : 
			score_percentages[key] = curr_score[key]/curr_state[key] 
		state_percentages[key] = curr_state[key]/maximum_state[key]
	# get the intelligence type with the highest percentage 
	max_key = max ( score_percentages , key = score_percentages.get ) 
	min_key = min ( state_percentages , key = state_percentages.get )
	# get the dist from upper threshold amd that curr/max of that intelligence type 
	heur_val2 = thld_one - state_percentages[max_key]
	heur_val1 = thld_common - state_percentages[min_key]
	
	if game_state[min_key] == 0 : ## no use going for this 
		return beta*heur_val2 

	if heur_val1 > 0 and heur_val2 > 0: 
		return alpha*heur_val1 + beta*heur_val2 
	elif heur_val2 < 0 and heur_val1 > 0 : 
		return alpha*heur_val1
	elif heur_val2 > 0 and heur_val1 < 0 : 
		return alpha*heur_val2 




def goal_test( maximum_state , curr_state , thld_one , thld_common ) : 
	""" Return True if goal achieved, else false """
	temp_dict = {}
	for key in curr_state : 
		temp_dict[key] = curr_state[key]/maximum_state[key]
	score_check1 = [v > thld_one for v in temp_dict.values()]
	score_check2 = [v > thld_common for v in temp_dict.values()]
	if False in score_check2 : ## minimum requirement of each state not met 
		return False
	if True in score_check1 : ## all requirements fulfilled 
		return True	
	return False 	## no clear maximum 
	


def find_games_left(levels_per_game , levels_done) : 
	""" returns the actual game id """ 
	games_left_id = [] 
	for indx , val in enumerate(levels_per_game) : 
		if val - levels_done[indx] > 0 : 
			games_left_id.append(indx + 1)  # game id is 1 + indx 
	return games_left_id 


def setup_initial(filename) : 
	""" Initial Setup of parameters """ 
	levels_per_game = get_levels(filename)
	maximum_state = get_total_each(filename ,levels_per_game)
	initial_state = {}
	for indx, key in enumerate(maximum_state) : 
		initial_state[key] = 0 
	return initial_state , maximum_state , levels_per_game 
	
def get_info_game( filename , idx , level) : 
	data = ET.parse(filename)
	root = data.getroot()
	game_state = {} 
	for game in root : 
		if game['ID'] == str(idx) : 
			mod_name = game['module_name']
			mod_story = game['module_story' + str(level)]
			for param in game : 
				for key in param.attrib : 
					game_state[key] = float(param.attrib[key])
				
	return mod_name , mod_story , game_state

def call_game(filename , game_idx , level , curr_state , curr_score) : 

	## get backstory of level and game module of the level , update curr_state 
	game_module , story_module , game_state = get_info_game( filename, game_idx, level)
	actual_game_call (game_module , story_module )
	score_file = open("score.txt" , "r")
	curr_score = float(score_file.read())
	for key in curr_state : 
		curr_score[key] = curr_score[key] + game_state[key]*curr_score 
		curr_state[key] = curr_state[key] + game_state[key]
	return curr_score , curr_state
	## update the state after getting the score 


def start_search(filename) : 
	"""" For testing """
	initial_state , maximum_state , levels_per_game = setup_initial(filename)
	levels_done = [0 for i in levels_per_game]
	games_played = 0 
	curr_state = initial_state 
	curr_score = [0 for i in maximum_state] ## current score 

	while games_played < 8 : 
		
		## choose a game randomly 
		game_choice_id = random.choice(range(1,17))
		if levels_done[game_choice_id - 1] == 0 : 
			## get the score and the updated state after playing the game 
			curr_score , curr_state = call_game(game_choice_id , 1 , curr_state , curr_score) ## score is the actual score
			games_played = games_played + 1
			levels_done[game_choice_id - 1] = 1 # increment to show the level at which a player is

	while True : 
		if goal_test(curr_state) : 
			break 
		games_left_id = find_games_left(levels_per_game , levels_done)	
		
		game_choice_id = 0 
		max_heur_score = 0 
		
		for game_id in games_left_id :
			temp_heur_score  = find_heuristic(game_id , levels_done[game_id - 1]  + 1 ,  curr_state , maximum_state , curr_score) 
			if temp_heur_score > max_heur_score : 
				max_heur_score = temp_heur_score
				game_choice_id = game_id
		
		curr_score, curr_state = call_game(game_choice_id ,  levels_done[game_choice_id - 1] + 1 , curr_state , curr_score ) # -1 since the index is 1 less than actual id 
		games_played = games_played + 1 
		levels_done[game_choice_id - 1] = levels_done[game_choice_id - 1] + 1 ## increment to show the level at which a player is

	return ## return implies exit 
