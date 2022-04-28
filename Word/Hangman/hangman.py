import pygame
import math
import random

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 30)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("Word/Hangman/hangman" + str(i) + ".png")
    images.append(image)

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw(word, hangman_status, guessed):
    win.fill(WHITE)

    # draw title
    text = TITLE_FONT.render("Guess the letters of the words. 6 Wrong Letters and you Lose", 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    # draw word
    display_word = ""
    for letter in word:
        if letter in ''.join(guessed).lower():
            display_word += letter + " "
        else:
            display_word += "_ "
    # print("D:", display_word, "G:", guessed, "W:", word, "HS:", hangman_status)
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # draw buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def game_loop(word):

    hangman_status = 0
    guessed = []
    FPS = 30
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()

                for letter in letters:
                    x, y, ltr, visible = letter

                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr.lower() not in word:
                                hangman_status += 1
        draw(word, hangman_status, guessed)
        won = True
        for letter in word:
            if letter not in ''.join(guessed).lower():
                won = False
                break

        if won:
            display_message("You WON!")
            break

        if hangman_status == 6:
            display_message("GAME OVER :( Correct ->" + word)
            break

    found = 0
    for letter in word:
        if letter in ''.join(guessed).lower():
            found += 1
    return found/len(word)


def start_game(level):

    if level == 1:
        words = ["salt", "read", "hear", "love", "hate", "good", "rock",
                 "park", "pet", "like", "dead", "hope", "sorry", "best"]
    elif level == 2:
        words = ["keyboard", "monitor", "printer", "scanner", "network",
                 "internet", "hardware", "virus", "website", "laptop"]
    elif level == 3:
        words = ["repulsive", "important", "zealous", "hepless", "grumpy",
                 "fierce", "embarrassed", "bewildered", "sideway"]

    word = random.choice(words)
    print("Word - ", word)
    score = game_loop(word)
    pygame.quit()
    print("score, ", score)
    return score


if __name__ == "__main__":
    score = start_game(1)
