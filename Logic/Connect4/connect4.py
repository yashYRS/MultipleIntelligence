import numpy as np
import random
import pygame
import sys
import math
import pygame.mixer
import time

YELLOW_BG = (255, 255, 150)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (0, 191, 255)

ROW_COUNT = 6
COLUMN_COUNT = 7

PLAYER = 0
AI = 1

EMPTY = 0
PLAYER_PIECE = 1
AI_PIECE = 2

WINDOW_LENGTH = 4


def text_objects(text, font):
    textSurface = font.render(text, True, (25, 255, 255))
    return textSurface, textSurface.get_rect()


def message_display(w, h, texts, screen):
    largeText = pygame.font.Font('freesansbold.ttf', 15)
    for hindex, text in enumerate(texts):
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((w/10), (hindex + 1)*h/10)
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(0.5)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill(BLACK)
                    return


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


def print_board(board):
    print(np.flip(board, 0))


def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


def evaluate_window(window, piece):
    score = 0
    opp_piece = PLAYER_PIECE
    if piece == PLAYER_PIECE:
        opp_piece = AI_PIECE

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2

    if window.count(opp_piece) == 3 and window.count(EMPTY) == 1:
        score -= 4

    return score


def score_position(board, piece):
    score = 0

    # # Score center column
    center_array = [int(i) for i in list(board[:, COLUMN_COUNT//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    # # Score Horizontal
    for r in range(ROW_COUNT):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(COLUMN_COUNT-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # # Score Vertical
    for c in range(COLUMN_COUNT):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(ROW_COUNT-3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window, piece)

    # # Score posiive sloped diagonal
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window, piece)

    return score


def is_terminal_node(board):
    return winning_move(board, PLAYER_PIECE) or winning_move(board, AI_PIECE) or len(get_valid_locations(board)) == 0


def minimax(board, depth, alpha, beta, maximizingPlayer):
    valid_locations = get_valid_locations(board)
    is_terminal = is_terminal_node(board)

    if depth == 0 or is_terminal:
        if is_terminal:
            if winning_move(board, AI_PIECE):
                return (None, 100000000000000)
            elif winning_move(board, PLAYER_PIECE):
                return (None, -10000000000000)
            else:
                # Game is over, no more valid moves
                return (None, 0)
        else:
            # Depth is zero
            return (None, score_position(board, AI_PIECE))
    if maximizingPlayer:
        value = -math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, AI_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, False )[1]
            if new_score > value:
                value = new_score
                column = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return column, value

    else:
        # Minimizing player
        value = math.inf
        column = random.choice(valid_locations)
        for col in valid_locations:
            row = get_next_open_row(board, col)
            b_copy = board.copy()
            drop_piece(b_copy, row, col, PLAYER_PIECE)
            new_score = minimax(b_copy, depth-1, alpha, beta, True)[1]
            if new_score < value:
                value = new_score
                column = col
            beta = min(beta, value)
            if alpha >= beta:
                break
        return column, value


def get_valid_locations(board):
    valid_locations = []
    for col in range(COLUMN_COUNT):
        if is_valid_location(board, col):
            valid_locations.append(col)
    return valid_locations


def pick_best_move(board, piece):

    valid_locations = get_valid_locations(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = get_next_open_row(board, col)
        temp_board = board.copy()
        drop_piece(temp_board, row, col, piece)
        score = score_position(temp_board, piece)
        if score > best_score:
            best_score = score
            best_col = col

    return best_col


def draw_board(board, screen, SQUARESIZE, RADIUS, height, width):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, YELLOW_BG, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == PLAYER_PIECE:
                pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
            elif board[r][c] == AI_PIECE:
                pygame.draw.circle(screen, LIGHT_BLUE, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
    pygame.display.update()


def start_game(level):
    board = create_board()

    pygame.init()
    coinSound = pygame.mixer.Sound('Logic/Connect4/coin.wav')
    rules = []
    rules.append("Use the mouse to drop coins on the board")
    rules.append("After your turn we do the same")
    rules.append("Create a line with at least 4 coins, before we do.")
    rules.append("The line could be horizontal vertical or diagonal")
    rules.append("Press Space to continue")
    SQUARESIZE = 100
    TotalMoves = 0
    Score = 0
    winner = 0

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE/2 - 5)

    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

    message_display(infoObject.current_w, infoObject.current_h, rules, screen)
    draw_board(board, screen, SQUARESIZE, RADIUS, height, width)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    turn = random.randint(PLAYER, AI)

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == PLAYER:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                # Ask for Player 1 Input
                if turn == PLAYER:
                    posx = event.pos[0]
                    col = int(math.floor(posx/SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        coinSound.play()
                        drop_piece(board, row, col, PLAYER_PIECE)
                        if winning_move(board, PLAYER_PIECE):
                            label = myfont.render(" YOU WON !!!!", 1, RED)
                            winner = 1
                            screen.blit(label, (40, 10))
                            game_over = True

                        turn += 1
                        turn = turn % 2

                        draw_board(board, screen, SQUARESIZE, RADIUS, height, width)
                        TotalMoves = TotalMoves + 1

        # # Ask for Player 2 Input
        if turn == AI and not game_over:

            # col = random.randint(0, COLUMN_COUNT-1)
            # col = pick_best_move(board, AI_PIECE)
            if level == 3:
                col, minimax_score = minimax(board, 5, -math.inf, math.inf, True)

                if is_valid_location(board, col):
                    # pygame.time.wait(500)
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, AI_PIECE)

                    if winning_move(board, AI_PIECE):
                        label = myfont.render("You lost!!", 1, LIGHT_BLUE)
                        winner = 2
                        screen.blit(label, (40, 10))
                        game_over = True
                    draw_board(board, screen, SQUARESIZE, RADIUS, height, width)
                    turn += 1
                    turn = turn % 2
            elif level == 2:
                col, minimax_score = minimax(board, 3, -math.inf, math.inf, True)

                if is_valid_location(board, col):
                    # pygame.time.wait(500)
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, AI_PIECE)

                    if winning_move(board, AI_PIECE):
                        label = myfont.render("You lost!!", 1, LIGHT_BLUE)
                        winner = 2
                        screen.blit(label, (40, 10))
                        game_over = True
                    draw_board(board, screen, SQUARESIZE, RADIUS, height, width)

                    turn += 1
                    turn = turn % 2
            elif level == 1:
                col, minimax_score = minimax(board, 1, -math.inf, math.inf, True)

                if is_valid_location(board, col):
                    # pygame.time.wait(500)
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, AI_PIECE)

                    if winning_move(board, AI_PIECE):
                        label = myfont.render("You lost!!", 1, LIGHT_BLUE)
                        winner = 2
                        screen.blit(label, (40, 10))
                        game_over = True
                    draw_board(board, screen, SQUARESIZE, RADIUS, height, width)

                    turn += 1
                    turn = turn % 2
                # do something

        if game_over:
            # player lost
            if winner == 2:
                score = TotalMoves/42
            # player wins
            elif winner == 1:
                score = 0.5 + (22 - TotalMoves)/42
            else:
                score = 0.5
            print(TotalMoves, score)
            pygame.time.wait(2000)
            pygame.quit()
            break
    return score


if __name__ == "__main__":
    start_game(1)
