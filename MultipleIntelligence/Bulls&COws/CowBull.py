#Importing Required Modules
# if levelscore>1 then its a guess 
import pygame, random, sys, time
from pygame.locals import *

levelscore=0
levelread=3
#Initialising PyGame Module
pygame.init()

#Initialising Global Variables
Canvas = pygame.display.set_mode((0, 0))
pygame.display.set_caption("Bulls n Cows")
white = (255, 255, 255)
black = (0, 0, 0)
red = (139,35,35)
font1 = "Times New Roman"
font2 = "Arial"
toggleKey = ["  *" for i in range(0, 26)]

def finfScoreToSend(score,time):
    fscore=score*10/(time*.75)
    return fscore

def getLevelFile(level):
    level=int(level)
    if level==1:
        file=open('Wordlist.txt','r')
    elif level==2:
        file=open('Wordlist1.txt','r')
    elif level==3:
        file=open('Wordlist1.txt','r')
    return file

#Function To Show Text As Per The Required Parameters
def text(string, size, color, top, left, fonttype = None, bold = False, italic = False):
    font = pygame.font.SysFont(fonttype, size, bold, italic)
    textobj = font.render(string, 1, color)
    textrect = textobj.get_rect()
    textrect.top = top
    textrect.left = left
    Canvas.blit(textobj, textrect)
    pygame.display.update()

#Function To Set A Word From The Database
def set_word():
    file = getLevelFile(levelread)
    if levelread==1:
        rval=113
    else:
        rval=94
    ran = random.randrange(rval)
    s = ""
    for i in range(ran):
        s = file.readline()
    file.close()
    return(s[0:4])

#Function To Display Alphabets
def alph():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = 30
    for i in alpha:
        text(i, 55, black, 50, l)
        l = l + 40

#Function To Wait For An Input At Certain Screens
def waitforkey():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == MOUSEBUTTONDOWN:
                return

#Function To Kill The Program
def terminate():
    pygame.quit()
    sys.exit()

#Function to Display Timer
def displayTime(ret = False):
    timeCurrent = time.time()
    timer = float(timeCurrent-timeStart)
    timer = round(timer, 1)
    pygame.draw.rect(Canvas, white, (975 , 15, 120, 30))
    text("Time : " + str(timer), 23, black, 10, 975, font1, False, True)
    if ret:
        return timer
    
#Function To Display/Refresh The Game Screen
def dispGame(turn, words):

    Canvas.fill(white)  #Refresh The Game Scren
    alph()  #Display The Alphabets
    for i in range(26): #Display Toggle Keys
        text(toggleKey[i], 20, black, 95, 30 + i*40, font1)
    
    text("Your word has been chosen.", 25, black, 140, 30, font2, False, True)
    text("Choose from the above alphabets to guess the word.", 25, black, 170, 30, font2, False, True)
    
    a = "Turn : " + str(turn)
    text(a, 23, black, 10, 30, font1, False, True) 
    level = "Level: " + str(levelread) #Display Turn Count
    text(level, 23, black, 30, 30, font1, False, True)
    pygame.draw.line(Canvas, black, (20, 118), (1080, 118), 1)
    for i in range(4):
        text("_", 140, black, 330, i*100+100)   #Display Input Blanks
    for i in range(len(words)): #Display Previous Inputs
        text(str(i+1) + ". " + words[i][0], 22, black, 122+i*55, 930, font1)
        b = "B: " + str(words[i][1]) + " / C: " + str(words[i][2])
        text(b, 19, black, 145+i*55, 950, font1)
    
#Function To Update The Toggle Key
def helpKeys(index):
    if toggleKey[index] == "  *":
        toggleKey[index] = "  ?"
    elif toggleKey[index] == "  ?":
        toggleKey[index] = "  X"
    elif toggleKey[index] == "  X":
        toggleKey[index] = "  *"
    pygame.draw.rect(Canvas, white, (30 + index*40, 95, 40, 20))
    text(toggleKey[index], 20, black, 95, 30 + index*40, font1)
        
#Function To Display/Refresh User Input
def updateguess(guess = ""):
    
    #Command To Clear Old Input By Overlapping It With A Rectangle Of Background Color
    pygame.draw.rect(Canvas, white, (100 , 320, 400, 70))
    
    #Command To Display Updated Input
    for i in range(len(guess)):
        text(guess[i], 120, black, 320, i*100+100)
    pygame.display.update()
    
#Main Game Loop
def startGame():
    turn = 1
    words = []
    word = set_word()
    while len(word)!=4:
        word=set_word()
    
    dispGame(turn, words)
    pygame.display.update()

    #'Turn' Loop
    if levelread==3:
        tval=6
    else:
        tval=11
    while turn<tval:
        letter = 1
        B = 0
        C = 0
        guess = ""
        submit = True
        sub = True
        erase = True
        
        #'Letter' Loop
        while submit:
            while erase:
                text("Erase", 50, black, 620, 950, font2)
                erase = False
                
            #To initiate timer
            displayTime()
            
            #Detect Certain Events Such As Mouse Motion And Mouse Clicks
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()

                #Underline The Alphabet That The Mouse Cursor Is Hovering On
                if event.type == MOUSEMOTION:
                    if event.pos[0]>30 and event.pos[0]<1070 and event.pos[1]>50 and event.pos[1]<120:
                        x = int((event.pos[0] - 30)/40)
                        pygame.draw.line(Canvas, white, (1, 90), (1099, 90), 2)
                        pygame.draw.line(Canvas, black, (x*40+25, 90), (x*40 + 60, 90), 2)
                        pygame.display.update()
                        
                #Detect Click On Toggle Keys
                if event.type == MOUSEBUTTONDOWN:
                    if event.pos[0]>30 and event.pos[0]<1070 and event.pos[1]>95 and event.pos[1]<120:
                        x = int((event.pos[0] - 30)/40)
                        helpKeys(x)
                        
                #Detect Click On Erase Button
                if event.type == MOUSEBUTTONDOWN:
                    if letter>1 and event.pos[0]>950 and event.pos[0]<1070 and event.pos[1]>620 and event.pos[1]<670:
                        letter = letter - 1
                        guess = guess[0:-1]
                        updateguess(guess)
                        
                    #Detect Click On A Certain Alphabet
                    if event.pos[0]>30 and event.pos[0]<1070 and event.pos[1]>50 and event.pos[1]<95:
                        x = int((event.pos[0] - 30)/40)
                        string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                        if letter == 1:
                            guess = guess + string[x]
                            updateguess(guess)
                            letter = letter + 1
                        else:
                            #Avoid Any Alphabet From Being Re-entered
                            if (string[x] in guess) or (letter == 5):
                                pass
                            else:
                                guess = guess + string[x]
                                updateguess(guess)
                                letter = letter + 1
                if letter == 5:
                    if sub:
                        text("Submit", 60, black, 550, 80, font2)
                        sub = False

                    #Detect Click On Submit Button And Exit The 'Letter' Loop
                    if event.type == MOUSEBUTTONDOWN:
                        if event.pos[0]>80 and event.pos[0]<270 and event.pos[1]>550 and event.pos[1]<600:
                            submit = False

        #Analysing The Input
        for i in range(4):
            if guess[i] in word:
                if word.index(guess[i]) == i:
                    B = B + 1
                else:
                    C = C + 1
                    
        #End Game If User Wins Else Restart
        repeat = False
        for i in range(len(words)):
            if guess in words[i]:
                repeat = True
        if B == 4:
            return endGame(word, True, turn, displayTime(True))
        elif repeat:
            dispGame(turn, words)
        else:
            turn = turn + 1
            words.append([guess, B, C])
            dispGame(turn, words)

    #End Game Once All 10 Turns Are Used Up
    return endGame(word, False, turn, displayTime(True))

#Function To Display The End Game Screen
def endGame(word, result, turn, timer):
    Canvas.fill(red)
    text("The required answer was", 50, white, 125, 200)
    text(word, 100, white, 200, 325)
    if result:
        if levelread=3:
            score=6-turn
        else:
            score=11-turn
        text("Congratulations! You guessed the word correctly.", 50, white, 325, 200)
        text("Score: " + str(score), 75, white, 425, 320)
        levelscore=finfScoreToSend(score,timer)
        print("Score: "+str(levelscore))
    else:
        text("Oops! You failed to guess the word correctly.", 50, white, 325, 200)
        text("Score : 0", 75, white, 425, 320)
    text("Time : " + str(timer) + "s", 75, white, 500, 320)
    
    #To Detect 'Escape' Key Being Pressed And Restart The Game
    text("To play again, press Escape key.", 50, white, 600, 200)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

#Main Function
Canvas.fill(red)
txt = "Welcome to Bulls & Cows! Current Level: "+str(levelread)
text(txt, 60, white, 50, 100, font1, True)
text("Simple Rules: You have to guess the word I'm Thinking!", 35, white, 150, 20, font2)
text("Fill in the blanks with letters that make up a word you want to guess.", 35, white, 220, 20, font2, True)
text("Select the letters by clicking on them.(No repeating letters)", 35, white, 290, 20, font2, True)
text("Your result is displayed in the top right corner.", 35, white, 360, 20, font2, True)
text("'B' is bulls which denotes how many letters are in the correct position.", 35, white, 430, 20, font2, True)
text("'C' is cows which tells you how many letters are in the wrong position.", 35, white, 500, 20, font2,True)
if levelread==3:
    text("You get 5 guesses and the time is recorded. Have Fun!", 40, white, 570, 20, font2, True)
else:
    text("You get 10 guesses and the time is recorded. Have Fun!", 40, white, 570, 20, font2, True)
text("Click to start!", 50, white, 640, 450, font1, True)


waitforkey()
global timeStart
timeStart = time.time()
start = startGame()
while start:
    toggleKey = ["  *" for i in range(0, 26)]
    timeStart = time.time()
    start = startGame()
