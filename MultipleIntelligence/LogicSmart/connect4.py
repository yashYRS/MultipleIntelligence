# import numpy as np 
# import pygame 


# def make_board() : 
# 	board = np.zeros(shape = (6,7))
# 	return board 

# def computer_turn(board) : 
# 	move = best_move(board)
# 	board[move[0]][move[1]] = -1
# 	return board 

# def user_turn(board) : 
# 	while (1) : 
# 		try : 
# 			row = int(input("Enter Row number -> "))
# 			col = int(input("Enter column number -> "))
# 			break 
# 		except Exception as e : 
# 			printf(" Try Again ")

# 	board[row][col] = 1 

# 	return board 

# def check_winner(nrows, ncols , board) : 
	
# 	boards = [board , board.T]
# 	col_len = [ncols, nrows]
# 	## check for elements in the row and column 
# 	for i in range(len(boards)) : 
# 		for row in boards[i] : 
# 			rowSum = [ sum(row[ind: ind+4]) for ind in range(col_len[i] - 3)]
# 			if 4 in rowSum : 
# 				return 1 
# 			elif -4 in rowSum : 
# 				return -1 
# 	for rowNo in range(nrows - 3) : 
# 		for colNo in range(ncols) : 
# 			seq = 0 
# 			if (colNo - 4 >= 0 ) : 
# 				seq = sum( [ board[rowNo+ind][colNo - ind] for ind in range(4)] )

# 			elif (colNo + 4 < ncols) : 
# 				seq = sum( [ board[rowNo+ind][colNo + ind] for ind in range(4)] )
			
# 			if seq == 4 : 
# 				return 1 
# 			elif seq == -4 : 
# 				return -1 

# 	return 0 

# def get_moves_possible(nrows, ncols , board) : 
# 	moves = [] 
# 	boardTrans = board.T 
# 	for colNo in range(ncols) : 
# 		for rowNo in range(nrows) :
# 			if (boardTrans[colNo][rowNo] != 0) : 
# 				moves.append((rowNo - 1, colNo))
# 				break 
# 			elif rowNo == nrows - 1  : 
# 				moves.append((rowNo ,colNo))
# 	return moves 

# def minimax(board,depth,Max) :			 # Max - True for maximizer , False for minimizer
# 	nrows , ncols = np.shape(board)
# 	value_board = check_winner(nrows, ncols , board)
# 	#printer(board,value_board)
# 	if value_board != 0 : 
# 		return value_board 					# if game-over return winner..
# 	moves = get_moves_possible(nrows, ncols, board)
# 	if Max : 
# 		best = -99
# 		for move in moves: 
# 			board[move[0]][move[1]] = -1
# 			val = minimax(board,depth+1,False)
# 			best = max(best,val)
# 			board[move[0]][move[1]] = 0
# 		return best
# 	else : 
# 		best = 99
# 		for move in moves:
# 			board[move[0]][move[1]] = 1 
# 			val = minimax(board,depth+1,True)
# 			best = min(best,val)
# 			board[move[0]][move[1]] = 0
# 		return best

# def best_move(board):
# 	best_move = -1 # worst case -- losss 
# 	score = -1
# 	nrows , ncols = np.shape(board)
# 	moves = get_moves_possible(nrows, ncols, board)
# 	for move in moves :
# 		board[move[0]][move[1]] = -1 
# 		current_score = minimax(board,0,False)
# 		if (current_score >= score) :
# 			best_move = move
# 			score = current_score
# 		board[move[0]][move[1]] = 0
# 	return best_move

# def draw_board(board):
# 	ROW_COUNT , COLUMN_COUNT = np.shape(board)
# 	for c in range(COLUMN_COUNT):
# 		for r in range(ROW_COUNT):
# 			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
# 			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
# 	for c in range(COLUMN_COUNT):
# 		for r in range(ROW_COUNT):		
# 			if board[r][c] == 1:
# 				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
# 			elif board[r][c] == 2: 
# 				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
# 	pygame.display.update()

# def game() : 
	
# 	board = make_board() 
# 	nrows , ncols = np.shape(board)
	
# 	pygame.init()
# 	SQUARE_SIZE = 150 
# 	WIDTH = ncols * SQUARE_SIZE
# 	HEIGHT = (nrows+1) * SQUARE_SIZE

# 	size = (WIDTH , HEIGHT)
# 	screen = pygame.display.set_mode(size)
# 	draw_board(board)
	
# 	while True :  
# 		print(get_moves_possible(nrows, ncols , board))
# 		board = user_turn(board)
# 		if( check_winner(nrows, ncols , board)  == 1 ): 
# 			print(" Player wins ")
# 			break
# 		print(board)
# 		print(get_moves_possible(nrows, ncols , board))
# 		board = computer_turn(board)
# 		if( check_winner(nrows, ncols , board)  == -1 ): 
# 			print(" Computer wins ")
# 			break		
# 		print(board)


#minimax(make_board, )
#game() 
# import numpy as np
# import random
# import pygame
# import sys
# import math

# BLUE = (0,0,255)
# BLACK = (0,0,0)
# RED = (255,0,0)
# YELLOW = (255,255,0)

# ROW_COUNT = 6
# COLUMN_COUNT = 7

# PLAYER = 0
# AI = 1

# EMPTY = 0
# PLAYER_PIECE = 1
# AI_PIECE = 2

# WINDOW_LENGTH = 4

# def create_board():
# 	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
# 	return board

# def drop_piece(board, row, col, piece):
# 	board[row][col] = piece

# def is_valid_location(board, col):
# 	return board[ROW_COUNT-1][col] == 0

# def get_next_open_row(board, col):
# 	for r in range(ROW_COUNT):
# 		if board[r][col] == 0:
# 			return r

# def print_board(board):
# 	print(np.flip(board, 0))

# def winning_move(board, piece):
# 	# Check horizontal locations for win
# 	for c in range(COLUMN_COUNT-3):
# 		for r in range(ROW_COUNT):
# 			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
# 				return True

# 	# Check vertical locations for win
# 	for c in range(COLUMN_COUNT):
# 		for r in range(ROW_COUNT-3):
# 			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
# 				return True

# 	# Check positively sloped diaganols
# 	for c in range(COLUMN_COUNT-3):
# 		for r in range(ROW_COUNT-3):
# 			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
# 				return True

# 	# Check negatively sloped diaganols
# 	for c in range(COLUMN_COUNT-3):
# 		for r in range(3, ROW_COUNT):
# 			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
# 				return True

# def evaluate_window(window, piece):
# 	score = 0
# 	opp_piece = PLAYER_PIECE
# 	if piece == PLAYER_PIECE:
# 		opp_piece = AI_PIECE

# 	if window.count(piece) == 4:
# 		score += 100
# 	elif window.count(piece) == 3 and window.count(EMPTY) == 1:
# 		score += 5
# 	elif window.count(piece) == 2 and window.count(EMPTY) == 2:
# 		score += 2

# 	if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
# 		score -= 4

# 	return score

# def score_position(board, piece):
# 	score = 0

# 	## Score center column
# 	center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
# 	center_count = center_array.count(piece)
# 	score += center_count * 3

# 	## Score Horizontal
# 	for r in range(ROW_COUNT):
# 		row_array = [int(i) for i in list(board[r,:])]
# 		for c in range(COLUMN_COUNT-3):
# 			window = row_array[c:c+WINDOW_LENGTH]
# 			score += evaluate_window(window, piece)

# 	## Score Vertical
# 	for c in range(COLUMN_COUNT):
# 		col_array = [int(i) for i in list(board[:,c])]
# 		for r in range(ROW_COUNT-3):
# 			window = col_array[r:r+WINDOW_LENGTH]
# 			score += evaluate_window(window, piece)

# 	## Score posiive sloped diagonal
# 	for r in range(ROW_COUNT-3):
# 		for c in range(COLUMN_COUNT-3):
# 			window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
# 			score += evaluate_window(window, piece)

# 	for r in range(ROW_COUNT-3):
# 		for c in range(COLUMN_COUNT-3):
# 			window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
# 			score += evaluate_window(window, piece)

# 	return score

# def is_terminal_node(board):
# 	return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0

# def minimax(board, depth, alpha, beta, maximizingPlayer):
# 	valid_locations = get_valid_locations(board)
# 	is_terminal = is_terminal_node(board)
# 	if depth == 0 or is_terminal:
# 		if is_terminal:
# 			if winning_move(board, AI_PIECE):
# 				return (None, 100000000000000)
# 			elif winning_move(board, PLAYER_PIECE):
# 				return (None, -10000000000000)
# 			else: # Game is over, no more valid moves
# 				return (None, 0)
# 		else: # Depth is zero
# 			return (None, score_position(board, AI_PIECE))
# 	if maximizingPlayer:
# 		value = -math.inf
# 		column = random.choice(valid_locations)
# 		for col in valid_locations:
# 			row = get_next_open_row(board, col)
# 			b_copy = board.copy()
# 			drop_piece(b_copy, row, col, AI_PIECE)
# 			new_score = minimax(b_copy, depth-1, alpha, beta, False)[1]
# 			if new_score > value:
# 				value = new_score
# 				column = col
# 			alpha = max(alpha, value)
# 			if alpha >= beta:
# 				break
# 		return column, value

# 	else: # Minimizing player
# 		value = math.inf
# 		column = random.choice(valid_locations)
# 		for col in valid_locations:
# 			row = get_next_open_row(board, col)
# 			b_copy = board.copy()
# 			drop_piece(b_copy, row, col, PLAYER_PIECE)
# 			new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
# 			if new_score < value:
# 				value = new_score
# 				column = col
# 			beta = min(beta, value)
# 			if alpha >= beta:
# 				break
# 		return column, value

# def get_valid_locations(board):
# 	valid_locations = []
# 	for col in range(COLUMN_COUNT):
# 		if is_valid_location(board, col):
# 			valid_locations.append(col)
# 	return valid_locations

# def pick_best_move(board, piece):

# 	valid_locations = get_valid_locations(board)
# 	best_score = -10000
# 	best_col = random.choice(valid_locations)
# 	for col in valid_locations:
# 		row = get_next_open_row(board, col)
# 		temp_board = board.copy()
# 		drop_piece(temp_board, row, col, piece)
# 		score = score_position(temp_board, piece)
# 		if score > best_score:
# 			best_score = score
# 			best_col = col

# 	return best_col

# def draw_board(board):
# 	for c in range(COLUMN_COUNT):
# 		for r in range(ROW_COUNT):
# 			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
# 			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
# 	for c in range(COLUMN_COUNT):
# 		for r in range(ROW_COUNT):		
# 			if board[r][c] == PLAYER_PIECE:
# 				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
# 			elif board[r][c] == AI_PIECE: 
# 				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
# 	pygame.display.update()

# board = create_board()
# print_board(board)
# game_over = False

# pygame.init()

# SQUARESIZE = 100

# width = COLUMN_COUNT * SQUARESIZE
# height = (ROW_COUNT+1) * SQUARESIZE

# size = (width, height)

# RADIUS = int(SQUARESIZE/2 - 5)

# screen = pygame.display.set_mode(size)
# draw_board(board)
# pygame.display.update()

# myfont = pygame.font.SysFont("monospace", 75)

# turn = random.randint(PLAYER, AI)

# while not game_over:

# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			sys.exit()

# 		if event.type == pygame.MOUSEMOTION:
# 			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
# 			posx = event.pos[0]
# 			if turn == PLAYER:
# 				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)

# 		pygame.display.update()

# 		if event.type == pygame.MOUSEBUTTONDOWN:
# 			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
# 			#print(event.pos)
# 			# Ask for Player 1 Input
# 			if turn == PLAYER:
# 				posx = event.pos[0]
# 				col = int(math.floor(posx/SQUARESIZE))

# 				if is_valid_location(board, col):
# 					row = get_next_open_row(board, col)
# 					drop_piece(board, row, col, PLAYER_PIECE)

# 					if winning_move(board, PLAYER_PIECE):
# 						label = myfont.render("Player 1 wins!!", 1, RED)
# 						screen.blit(label, (40,10))
# 						game_over = True

# 					turn += 1
# 					turn = turn % 2

# 					print_board(board)
# 					draw_board(board)


# 	# # Ask for Player 2 Input
# 	if turn == AI and not game_over:				

# 		#col = random.randint(0, COLUMN_COUNT-1)
# 		#col = pick_best_move(board, AI_PIECE)
# 		col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

# 		if is_valid_location(board, col):
# 			#pygame.time.wait(500)
# 			row = get_next_open_row(board, col)
# 			drop_piece(board, row, col, AI_PIECE)

# 			if winning_move(board, AI_PIECE):
# 				label = myfont.render("Player 2 wins!!", 1, YELLOW)
# 				screen.blit(label, (40,10))
# 				game_over = True

# 			print_board(board)
# 			draw_board(board)

# 			turn += 1
# 			turn = turn % 2

# 	if game_over:
# 		pygame.time.wait(3000)