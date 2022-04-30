# Importing Required Modules
# if levelscore>1 then its a guess
import sys
import time
import os
import random
import pygame
from pygame.locals import *

levelscore = 0
level = 3
# Initialising PyGame Module
pygame.init()

WIDTH, HEIGHT = 800, 500
# Initialising Global Variables
Canvas = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Bulls n Cows")
white = (255, 255, 255)
black = (0, 0, 0)
red = (139, 35, 35)
font1 = "Times New Roman"
font2 = "Arial"


def get_score_to_send(score, time):
    fscore = score / (time * 0.75)
    return fscore


def getLevelFile(level):
    level = int(level)
    if level == 1:
        file = open("Word/BullsAndCows/Wordlist.txt", "r")
    elif level == 2:
        file = open("Word/BullsAndCows/Wordlist1.txt", "r")
    elif level == 3:
        file = open("Word/BullsAndCows/Wordlist1.txt", "r")
    return file


# Function To Show Text As Per The Required Parameters
def text(string, size, color, top, left, fonttype=None, bold=False, italic=False):
    font = pygame.font.SysFont(fonttype, size, bold, italic)
    textobj = font.render(string, 1, color)
    textrect = textobj.get_rect()
    textrect.top = top
    textrect.left = left
    Canvas.blit(textobj, textrect)
    pygame.display.update()


# Function To Set A Word From The Database
def set_word():
    file = getLevelFile(level)
    if level == 1:
        rval = 113
    else:
        rval = 94
    ran = random.randrange(rval)
    s = ""
    for i in range(ran):
        s = file.readline()
    file.close()
    return s[0:4]


# Function To Display Alphabets
def alph():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    start_coord = WIDTH*0.02
    for i in alpha:
        text(i, size=30, color=black, top=HEIGHT*0.2, left=start_coord)
        start_coord += 30


# Function To Wait For An Input At Certain Screens
def waitforkey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                return


# Function To Kill The Program
def terminate():
    pygame.quit()
    sys.exit()


# Function to Display Timer
def displayTime(ret=False):
    timeCurrent = time.time()
    timer = float(timeCurrent - timeStart)
    timer = round(timer, 1)
    pygame.draw.rect(Canvas, white, (WIDTH*0.28, HEIGHT*0.1, 200, 30))
    text("Time : " + str(timer), size=25, color=black, top=HEIGHT*0.1,
         left=WIDTH*0.3, fonttype=font2, bold=False, italic=True)
    if ret:
        return timer


# Function To Display/Refresh The Game Screen
def dispGame(turn, words):

    Canvas.fill(white)  # Refresh The Game Scren
    alph()  # Display The Alphabets

    text("Turn " + str(turn) + ":", size=20, color=black, top=HEIGHT*0.5,
         left=WIDTH*0.1, fonttype=font2, bold=False, italic=True)

    # pygame.draw.line(Canvas, black, (0, 118), (1080, 118), 1)
    # Display Input Blanks
    for i in range(4):
        text("_", size=60, color=black, top=HEIGHT*0.5, left=WIDTH*0.25 + i*70)

    for i in range(len(words)):  # Display Previous Inputs
        reqd_text = str(i + 1) + ". " + words[i][0] + " | B:" + str(words[i][1]) + " / C:" + str(words[i][2])
        text(reqd_text, 20, black,
             HEIGHT*0.3 + i*30, WIDTH*0.7, font1)


# Function To Display/Refresh User Input
def updateguess(guess=""):

    # Command To Clear Old Input By Overlapping It With A Rectangle Of Background Color
    pygame.draw.rect(Canvas, white, (WIDTH*0.24, HEIGHT*0.44, 300, 60))

    # Command To Display Updated Input
    for i in range(len(guess)):
        text(guess[i], 50, black, HEIGHT*0.45, WIDTH*0.25 + i*70)
    pygame.display.update()


# Main Game Loop
def startGame(level, total_guesses):
    turn = 1
    words = []
    word = set_word()
    while len(word) != 4:
        word = set_word()

    dispGame(turn, words)
    pygame.display.update()

    while turn < total_guesses:
        letter = 1
        B = 0
        C = 0
        guess = ""
        submit = True
        sub = True
        erase = True

        # 'Letter' Loop
        while submit:
            while erase:
                text("ERASE", size=20, color=black, top=HEIGHT*0.8,
                     left=WIDTH*0.5, fonttype=font2)
                erase = False

            # To initiate timer
            displayTime()

            # Detect Certain Events Such As Mouse Motion And Mouse Clicks
            for event in pygame.event.get():

                # Underline The Alphabet That The Mouse Cursor Is Hovering On
                if event.type == MOUSEMOTION:
                    mouse_w, mouse_h = event.pos
                    # size=30 top=HEIGHT*0.2, left=WIDTH*0.02 + 30
                    if (HEIGHT*0.2 + 30 > mouse_h > HEIGHT*0.19 and
                            WIDTH > mouse_w > WIDTH*0.01):
                        x = int((mouse_w - WIDTH*0.02) / 30)
                        pygame.draw.line(Canvas, white, (0, HEIGHT*0.2+30), (WIDTH, HEIGHT*0.2+30), 2)
                        pygame.draw.line(
                            Canvas, black, (x*30 + 10, HEIGHT*0.2+30), (x*30 + 35, HEIGHT*0.2+30), 2
                        )
                        pygame.display.update()

                if event.type == MOUSEBUTTONDOWN:
                    mouse_w, mouse_h = event.pos

                    # Detect Click On Erase Button
                    if (letter > 1 and (HEIGHT*0.8 + 20 > mouse_h > HEIGHT*0.8)
                            and (WIDTH*0.5 + 80 > mouse_w > WIDTH*0.48)):
                        letter = letter - 1
                        guess = guess[0:-1]
                        updateguess(guess)

                    # Detect Click On A Certain Alphabet
                    if (HEIGHT*0.2 + 30 > mouse_h > HEIGHT*0.19 and
                            WIDTH > mouse_w > WIDTH*0.01):
                        x = int((mouse_w - WIDTH*0.02) / 30)
                        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        # print(string[x])
                        if letter == 1:
                            guess = guess + string[x]
                            updateguess(guess)
                            letter = letter + 1
                        else:
                            # Avoid Any Alphabet From Being Re-entered
                            if (string[x] in guess) or (letter == 5):
                                pass
                            else:
                                guess = guess + string[x]
                                updateguess(guess)
                                letter = letter + 1
                if letter == 5:
                    if sub:
                        text("SUBMIT", size=20, color=black, top=HEIGHT*0.8,
                             left=WIDTH*0.2, fonttype=font2)
                        sub = False

                    # Detect Click On Submit Button And Exit The 'Letter' Loop
                    if event.type == MOUSEBUTTONDOWN:
                        mouse_w, mouse_h = event.pos
                        if (HEIGHT*0.78 + 25 > mouse_h > HEIGHT*0.78 and
                                WIDTH*0.2 + 80 > mouse_w > WIDTH*0.2):
                            submit = False

        # Analysing The Input
        for i in range(4):
            if guess[i] in word:
                if word.index(guess[i]) == i:
                    B = B + 1
                else:
                    C = C + 1

        # End Game If User Wins Else Restart
        repeat = False
        for i in range(len(words)):
            if guess in words[i]:
                repeat = True
        if B == 4:
            return endGame(word, True, turn, displayTime(True), B, C)
        elif repeat:
            dispGame(turn, words)
        else:
            turn = turn + 1
            words.append([guess, B, C])
            dispGame(turn, words)

    # End Game Once All 10 Turns Are Used Up
    return endGame(word, False, turn, displayTime(True), B, C)


# Function To Display The End Game Screen
def endGame(word, result, turn, timer, B, C):
    Canvas.fill(white)
    reqd_text = "HIDDEN CODE: " + word
    text(reqd_text, size=40, color=black, top=HEIGHT*0.35,
         left=WIDTH*0.25, fonttype=font2)
    # Give full marks for bull guesses, half for cows, quarter for guess left
    score = B/4 + C/8 + turn/4
    if score > 1:
        score = 1

    if result:
        result_text = "Game Won! Well Done  :)"
    else:
        result_text = "Better Luck Next Time :("

    text(result_text, size=40, color=black, top=HEIGHT*0.55,
         left=WIDTH*0.2, fonttype=font2)
    time.sleep(2)
    pygame.quit()
    return score


def game_loop(level=1):
    # Main Function
    Canvas.fill(white)
    text("Bulls & Cows", size=30, color=black, top=HEIGHT*0.05,
         left=WIDTH*0.3, fonttype=font1, bold=True)
    text("The Misson is to guess the hidden 4 letter word", size=20,
         color=black, top=HEIGHT*0.2, left=WIDTH*0.15, fonttype=font2)    

    if level == 3:
        guess_text = "You get 7 guesses to crack the code",
        total_guesses = 8
    elif level == 2:
        guess_text = "You get 9 guesses to crack the code",
        total_guesses = 3
    elif level == 1:
        guess_text = "You get 11 guesses to crack the code"
        total_guesses = 12

    text("The hidden word will never have repeating characters", size=20,
         color=black, top=HEIGHT*0.3, left=WIDTH*0.15, fonttype=font2)
    text("At every turn, select any 4 distinct letters and submit a guess",
         size=20, color=black, top=HEIGHT*0.4, left=WIDTH*0.15, fonttype=font2)
    text("Every guess is given 2 scores viz. Bull (B) score and Cow (C) score",
         size=20, color=black, top=HEIGHT*0.5, left=WIDTH*0.15, fonttype=font2)
    text("B: number of letters from the guess, in the correct position.",
         size=20, color=black, top=HEIGHT*0.6, left=WIDTH*0.15, fonttype=font2)
    text("C: number of letters from the guess, that are part of the word",
         size=20, color=black, top=HEIGHT*0.7, left=WIDTH*0.15, fonttype=font2)
    text("but are in incorrect position", size=20, color=black,
         top=HEIGHT*0.75, left=WIDTH*0.3, fonttype=font2)

    text(guess_text, size=20, color=black, top=HEIGHT*0.85,
         left=WIDTH*0.25, fonttype=font2)
    text("Click to start!", size=20, color=black, top=HEIGHT*0.95,
         left=WIDTH*0.4, fonttype=font2)

    waitforkey()
    global timeStart
    timeStart = time.time()
    score = startGame(level, total_guesses)
    print("SCORE", score)


if __name__ == "__main__":
    game_loop()
