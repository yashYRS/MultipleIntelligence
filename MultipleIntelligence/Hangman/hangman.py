#!/usr/bin/env python
from pygame.event import *
import random
import pygame, sys, time
from pygame.locals import *

levelread = 2
levelscore=0
pygame.init()
mainClock = pygame.time.Clock()
event = pygame.event.poll()

WINDOWWIDTH = 800
WINDOWHEIGHT = 800
windowSurface = pygame.display.set_mode((0,0))
pygame.display.set_caption('Welcome to HANGMAN')

BLACK = (0, 0, 0)
RED = (255, 0, 0)
DGREEN = (0,100,0)
BLUE = (0, 0, 255)
#LBLUE = (0, 200, 255)
LBLUE= (0,0,205)
BROWN = (128,0,0)
WHITE = (255,255,255)
SKIN = (233,150,122)
DGREY = (0,206,209)
GREY = (74,112,139)
LGREY = (0,104,139)
GREEN = (0,139,0)

def getFinalScore(score,time):
    return score*10/(time*1.75)

correctSound = pygame.mixer.Sound('sound/correct.wav')
hahahaSound = pygame.mixer.Sound('sound/hahaha.wav')
mwahahaSound = pygame.mixer.Sound('sound/mwahaha.wav')
wrongSound = pygame.mixer.Sound('sound/wrong.wav')
playerWinSound = pygame.mixer.Sound('sound/cheer.wav')
yaySound = pygame.mixer.Sound('sound/yay.wav')
startTime=time.time()+10
guess = ''
missedLetters = ''
correctLetters = ''
curser = [240, 190, 50, 50]
option = ['New Game','Rules: Guess the word correctly You Have 60seconds.','The category word belongs to is displayed in top right area.','You get 8 tries.','Have fun!',0,'',0]
#option = [0,'New Game']
score = [0,0,'',0,0]
gameIsDone = False
s = 0   # Stage counter
h = [280,259,1,40,40,1,100,100,0,0,150,240,13]
p = [150,259,1,40,40,0,100,100,0,0,150,240,13]
guessed = [0,'Guess a letter,Player!',0]
infoDisplayText = ['Hangman for Kids','','by','','PySociety','']
banner =[50,50,0,0,0,0,0,0]
show = [0,60,True,True]# 0-Actual FPS, 1-Max FPS, 2-Gradient Sky, 3-Background
textFile = open('wordlist.txt','r')
roundNo = 0

MOVESPEED = 50

# fonts
smallFont = pygame.font.SysFont(None, 20)
FlashFont = pygame.font.SysFont(None, 100)
basicFont = pygame.font.SysFont(None, 24)
guessFont = pygame.font.SysFont(None, 36)
titleFont = pygame.font.SysFont(None, 48)
bannerFont = pygame.font.SysFont(None, 64)

# set up the dictionary - First line of text file is category. (9 categories originally, right now considering only 3)
roundOrder = textFile.readline().split()
wordList0 = textFile.readline().split()
wordList1 = textFile.readline().split()
wordList2 = textFile.readline().split()
wordList3 = textFile.readline().split()
wordList4 = textFile.readline().split()
wordList5 = textFile.readline().split()
wordList6 = textFile.readline().split()
wordList7 = textFile.readline().split()
wordList8 = textFile.readline().split()
words={roundOrder[0]:wordList0,roundOrder[1]:wordList1,roundOrder[2]:wordList2,roundOrder[3]:wordList3,roundOrder[4]:wordList4,roundOrder[5]:wordList5,roundOrder[6]:wordList6,roundOrder[7]:wordList7,roundOrder[8]:wordList8}
textFile.close()

# Random Word generator
def getRandomWord(wordDict):
    wordKey = random.choice(list(wordDict.keys()))
    wordIndex = random.randrange(0,len(wordDict[wordKey]))
    return [wordDict[wordKey][wordIndex], wordKey]


# Sequential game word generator
def getNextRound(wordDict,level):
    if level==1:
        roundNo=0
    elif level==2:
        roundNo=1
    elif level==3:
        roundNo=2
    wordKey = roundOrder[roundNo]
    wordIndex = random.randrange(0,len(wordDict[wordKey]))
    return [wordDict[wordKey][wordIndex], wordKey]

# who zooms out of the screen to talk to the player
def infoDisplay(who,time):
    count=0
    who[12]=13# Zoom target
    who[11]=240# Vertical Target
    who[10]=150# Horizontal target
    text = basicFont.render(infoDisplayText[0] + infoDisplayText[1], True, BLUE,WHITE)
    text1 = basicFont.render(infoDisplayText[2] + infoDisplayText[3], True, BLUE,WHITE)
    text2 = basicFont.render(infoDisplayText[4] + infoDisplayText[5], True, BLUE,WHITE)
    while count < time:
        if who[2] == who[12]:
            count+=1
        if who[2]< who[12]:
            who[2] += 1
        if who[2] >who[12]:
            who[2] -= 1
        if who[0] > who[10]:
            who[0]-=10
        if who[0] < who[10]:
            who[0]+=10
        if who[1] > who[11]:
            who[1]-=10
        if who[1] < who[11]:
            who[1]+=10
        if count >(time-11):
            who[12]=1
            h[10]=280
            p[10]=150
            who[11]=259
        background()
        gallows()
        noose()
        displayBoard(s, missedLetters, correctLetters, secretWord)
        if p[2] >= h[2]:# This sets the draw order so whoever is zoomed most is in front
            hangman()
            player()
        else:
            player()
            hangman()
        if count >14:
           if count <(time-11): #speech bubble arrow locations
                if who==h:
                    pygame.draw.polygon(windowSurface, WHITE,((355,170),(who[0]+15,who[1]-10),(355,144)))
                    pygame.draw.line(windowSurface,BLACK,(355,170),(who[0]+15,who[1]-10),2)
                    pygame.draw.line(windowSurface,BLACK,(355,144),(who[0]+15,who[1]-10),2)
                else:
                    pygame.draw.polygon(windowSurface, WHITE,((355,170),(who[0]+35,who[1]-50),(355,144)))
                    pygame.draw.line(windowSurface,BLACK,(355,170),(who[0]+35,who[1]-50),2)
                    pygame.draw.line(windowSurface,BLACK,(355,144),(who[0]+35,who[1]-50),2)
                pygame.draw.circle(windowSurface, WHITE, (355,157),32,0)
                pygame.draw.circle(windowSurface, WHITE, (545,157),32,0)
                pygame.draw.circle(windowSurface, BLACK, (355,157),32,2)
                pygame.draw.circle(windowSurface, BLACK, (545,157),32,2)
                pygame.draw.rect(windowSurface, WHITE,(355,125, 190,64))
                if who==h:
                    pygame.draw.polygon(windowSurface, WHITE,((355,168),(who[0]+13,who[1]-8),(355,142)))
                else:
                    pygame.draw.polygon(windowSurface, WHITE,((356,169),(who[0]+37,who[1]-50),(356,144)))
                pygame.draw.line(windowSurface,BLACK,(355,125),(545,125),2)
                pygame.draw.line(windowSurface,BLACK,(355,188),(545,188),2)
                windowSurface.blit(text, (350,130))
                windowSurface.blit(text1, (350,150))
                windowSurface.blit(text2, (350,170))
        framerate()
        pygame.display.update()

# background hills
def background():
    if show[2] == False:
        windowSurface.fill(LBLUE)
    else:
        sky = pygame.draw.rect(windowSurface, LBLUE,((0,0,1500,1500)))
        fill_gradient(windowSurface,LBLUE,WHITE,sky,True,True)
    if show[3] == False:
        windowSurface.fill(GREEN)
    else:
        pygame.draw.polygon(windowSurface, DGREY,((banner[6],325),(banner[6]+200,25),(banner[6]+400,325)))
        pygame.draw.polygon(windowSurface, WHITE,((banner[6]+100,175),(banner[6]+200,25),(banner[6]+300,175),(banner[6]+250,200),(banner[6]+200,175),(banner[6]+150,200)))
        pygame.draw.rect(windowSurface, GREY,(0,320, 800, 130))
        pygame.draw.polygon(windowSurface, GREY,((banner[2]+500,320),(banner[2]+700,125),(banner[2]+900,320)))
        pygame.draw.polygon(windowSurface, GREY,((banner[2]+50,320),(banner[2]+200,145),(banner[2]+350,320)))
        pygame.draw.polygon(windowSurface, GREY,((banner[2]-400,320),(banner[2]-200,100),(banner[2],320)))
        pygame.draw.polygon(windowSurface, GREY,((banner[2]-750,320),(banner[2]-550,125),(banner[2]-350,320)))
        pygame.draw.polygon(windowSurface, GREY,((banner[2]-1200,320),(banner[2]-1050,145),(banner[2]-900,320)))
        pygame.draw.rect(windowSurface, LGREY,(0,370, 800, 110))
        pygame.draw.polygon(windowSurface, LGREY,((banner[3]+500,370),(banner[3]+700,145),(banner[3]+900,370)))
        pygame.draw.polygon(windowSurface, LGREY,((banner[3]+50,370),(banner[3]+200,165),(banner[3]+350,370)))
        pygame.draw.polygon(windowSurface, LGREY,((banner[3]-400,370),(banner[3]-200,150),(banner[3],370)))
        pygame.draw.polygon(windowSurface, LGREY,((banner[3]-750,370),(banner[3]-550,145),(banner[3]-350,370)))
        pygame.draw.polygon(windowSurface, LGREY,((banner[3]-1200,370),(banner[3]-1050,165),(banner[3]-900,370)))
        pygame.draw.rect(windowSurface, DGREEN,(0,400, 800, 80))
        pygame.draw.circle(windowSurface, DGREEN, (banner[4]-1250,480),250,0)
        pygame.draw.circle(windowSurface, DGREEN, (banner[4]-50,480),250,0)
        pygame.draw.circle(windowSurface, DGREEN, (banner[4]-650,400),175,0)
        pygame.draw.circle(windowSurface, DGREEN, (banner[4]-950,440),175,0)
        pygame.draw.circle(windowSurface, DGREEN, (banner[4],480),250,0)
        pygame.draw.circle(windowSurface, DGREEN, (banner[4]+300,440),175,0)
        pygame.draw.circle(windowSurface, DGREEN, (banner[4]+600,400),175,0)
        pygame.draw.circle(windowSurface, DGREEN, (banner[4]+900,480),250,0)
        pygame.draw.rect(windowSurface, GREEN,(0,440,800,40))
        pygame.draw.circle(windowSurface, GREEN, (banner[5]-1250,520),240,0)
        pygame.draw.circle(windowSurface, GREEN, (banner[5]-350,540),240,0)
        pygame.draw.circle(windowSurface, GREEN, (banner[5]-650,480),240,0)
        pygame.draw.circle(windowSurface, GREEN, (banner[5]-950,500),240,0)
        pygame.draw.circle(windowSurface, GREEN, (banner[5],520),250,0)
        pygame.draw.circle(windowSurface, GREEN, (banner[5]+300,500),240,0)
        pygame.draw.circle(windowSurface, GREEN, (banner[5]+600,480),240,0)
        pygame.draw.circle(windowSurface, GREEN, (banner[5]+900,540),240,0)
        time_string = "Timer: {} ".format(str(int(time.time() - startTime)))
        text = FlashFont.render(time_string, True, BLACK)
        windowSurface.blit(text, (900,40))

def fill_gradient(surface, color, gradient, rect=None, vertical=True, forward=True):
    if rect is None: rect = surface.get_rect()
    x1,x2 = rect.left, rect.right
    y1,y2 = rect.top, rect.bottom
    if vertical: h = y2-y1
    else:        h = x2-x1
    if forward: a, b = color, gradient
    else:       b, a = color, gradient
    rate = (
        float(b[0]-a[0])/h,
        float(b[1]-a[1])/h,
        float(b[2]-a[2])/h
    )
    fn_line = pygame.draw.line
    if vertical:
        for line in range(y1,y2):
            color = (
                min(max(a[0]+(rate[0]*(line-y1)),0),255),
                min(max(a[1]+(rate[1]*(line-y1)),0),255),
                min(max(a[2]+(rate[2]*(line-y1)),0),255)
            )
            fn_line(surface, color, (x1,line), (x2,line))
    else:
        for col in range(x1,x2):
            color = (
                min(max(a[0]+(rate[0]*(col-x1)),0),255),
                min(max(a[1]+(rate[1]*(col-x1)),0),255),
                min(max(a[2]+(rate[2]*(col-x1)),0),255)
            )
            fn_line(surface, color, (col,y1), (col,y2))

# build the gallows
def gallows():
    pygame.draw.rect(windowSurface, BLACK,(400, 70, 30, 290))
    pygame.draw.rect(windowSurface, BLACK,(120, 40, 340, 30))
    pygame.draw.rect(windowSurface, BLACK,(100, 360, 400, 30))
    pygame.draw.rect(windowSurface, BLACK,(460, 390, 30, 80))
    pygame.draw.polygon(windowSurface, BLACK,((0,470),(0,450),(25,450),(25,430),(50,430),(50,410),(75,410),(75,390),(130,390),(130,470)))
    pygame.draw.polygon(windowSurface, BLACK,((400,300),(340,360),(370,360),(400,330)))
    pygame.draw.polygon(windowSurface, BLACK,((430,300),(490,360),(460,360),(430,330)))
    pygame.draw.polygon(windowSurface, BLACK,((400,130),(340,70),(370,70),(400,100)))
    pygame.draw.rect(windowSurface, BROWN,(401, 71, 28, 288))
    pygame.draw.rect(windowSurface, BROWN,(121, 41, 338, 28))
    pygame.draw.rect(windowSurface, BROWN,(101, 361, 398, 28))
    pygame.draw.rect(windowSurface, BROWN,(461, 391, 28, 78))
    pygame.draw.polygon(windowSurface, BROWN,((1,469),(1,451),(26,451),(26,431),(51,431),(51,411),(76,411),(76,391),(129,391),(129,469)))
    pygame.draw.polygon(windowSurface, BROWN,((399,302),(342,359),(369,359),(400,329)))
    pygame.draw.polygon(windowSurface, BROWN,((430,301),(489,359),(461,359),(430,329)))
    pygame.draw.polygon(windowSurface, BROWN,((399,128),(341,70),(369,70),(399,100)))
    pygame.draw.circle(windowSurface, GREY, (410,60),3,0)
    pygame.draw.circle(windowSurface, GREY, (420,60),3,0)
    pygame.draw.circle(windowSurface, GREY, (410,370),3,0)
    pygame.draw.circle(windowSurface, GREY, (420,370),3,0)

# Draw the nooses(players) - the ellipses move down and the rectangles elongate
def noose():
    pygame.draw.rect(windowSurface, BLACK,(277, 70, 6,h[6]-80))
    pygame.draw.rect(windowSurface, BROWN,(278, 71, 4,h[6]-76))
    pygame.draw.ellipse(windowSurface, BLACK, (267,h[6]-15,26,46),6)
    pygame.draw.ellipse(windowSurface, BROWN, (268,h[6]-14,25,44),4)
    pygame.draw.rect(windowSurface, BLACK,(p[0]-3, 70, 6,p[6]-80))
    pygame.draw.rect(windowSurface, BROWN,(p[0]-2, 71, 4,p[6]-76))
    pygame.draw.ellipse(windowSurface, BLACK, (p[0]-13,p[6]-15,26,46),6)
    pygame.draw.ellipse(windowSurface, BROWN, (p[0]-12,p[6]-14,25,44),4)

# Controls who swings!
def gameover(who):
    while who[6]<who[7]:
        who[6]+=2
        update()
    who[7]=200
##    noooSound.play()
    while who[6]>who[7]:
        who[6]-=2
        who[1]-=2
        who[5]='Noooo!!'
        update()

# draw Hangman
def hangman():# draw Hangman [Horizontal,Vertical,Timer,Scale]
    pygame.draw.polygon(windowSurface, BLACK,((h[0]-30*h[2],h[1]),(h[0]-15*h[2],h[1]+50*h[2]),(h[0]+15*h[2],h[1]+50*h[2]),(h[0]+30*h[2],h[1]),(h[0],h[1]-10*h[2])))
    pygame.draw.polygon(windowSurface, GREY,((h[0]-28*h[2],h[1]),(h[0]-13*h[2],h[1]+48*h[2]),(h[0]+13*h[2],h[1]+48*h[2]),(h[0]+28*h[2],h[1]),(h[0],h[1]-8*h[2])))
    pygame.draw.polygon(windowSurface, BLACK,((h[0]-25*h[2],h[1]-0),(h[0],h[1]+15*h[2]),(h[0]+25*h[2],h[1]-0),(h[0],h[1]-35*h[2])))
    pygame.draw.polygon(windowSurface, BLACK,((h[0]-15*h[2],h[1]+50*h[2]),(h[0]-25*h[2],h[1]+100*h[2]),(h[0],h[1]+50*h[2])))
    pygame.draw.polygon(windowSurface, BLACK,((h[0]+15*h[2],h[1]+50*h[2]),(h[0]+25*h[2],h[1]+100*h[2]),(h[0],h[1]+50*h[2])))
    pygame.draw.polygon(windowSurface, SKIN,((h[0]-30*h[2],h[1]),(h[0]-65*h[2],h[1]+40*h[2]),(h[0]-24*h[2],h[1]+20*h[2])))
    pygame.draw.line(windowSurface,BLACK,(h[0]-30*h[2],h[1]),(h[0]-65*h[2],h[1]+40*h[2]),2)
    pygame.draw.line(windowSurface,BLACK,(h[0]-24*h[2],h[1]+20*h[2]),(h[0]-65*h[2],h[1]+40*h[2]),2)
    pygame.draw.polygon(windowSurface, SKIN,((h[0]+30*h[2],h[1]),(h[0]+65*h[2],h[1]+40*h[2]),(h[0]+24*h[2],h[1]+20*h[2])))
    pygame.draw.line(windowSurface,BLACK,(h[0]+30*h[2],h[1]),(h[0]+65*h[2],h[1]+40*h[2]),2)
    pygame.draw.line(windowSurface,BLACK,(h[0]+24*h[2],h[1]+20*h[2]),(h[0]+65*h[2],h[1]+40*h[2]),2)
    if h[8] <= h[9]:# This is the blinking logic
        h[9]=0
        h[8]=random.randint(45,120)
        return
    elif h[9] > h[8] - 10:
        h[9] += 1
        return
    else:
        pygame.draw.circle(windowSurface, WHITE, (h[0]-8*h[2],h[1]-10*h[2]),2*h[2],0)
        pygame.draw.circle(windowSurface, WHITE, (h[0]+8*h[2],h[1]-10*h[2]),2*h[2],0)
        h[9] += 1
        return

# Decides what the Hangman is going to say in response to the players guess
def backchat():
    neg='Try! stupid! Lame! Boring! LOL! Hehe! Hahaha! Hohoho! Yawn!'.split()
    chat = 'Wow! Crazy! Awesome! Talent! Fun!'.split()
    if h[5]==1:
        abuse = chat
    else:
        abuse = neg
    insult= random.randint(0,len(abuse) - 1)
    h[5]=abuse[insult]

# draw Player
def player():# draw player [Horizontal,Vertical,Timer,Scale]
    pygame.draw.polygon(windowSurface, BLUE,((p[0]-25*p[2],p[1]),(p[0]-15*p[2],p[1]+50*p[2]),(p[0]+15*p[2],p[1]+50*p[2]),(p[0]+25*p[2],p[1]),(p[0],p[1]-10*p[2])))
    pygame.draw.polygon(windowSurface,WHITE,((p[0]-15*p[2],p[1]-4*p[2]),(p[0],p[1]+15*p[2]),(p[0]+15*p[2],p[1]-4*p[2]),(p[0],p[1]-10*p[2])))
    pygame.draw.polygon(windowSurface, SKIN,((p[0]-25*p[2],p[1]),(p[0]-65*p[2],p[1]+p[3]*p[2]),(p[0]-21*p[2],p[1]+20*p[2])))
    pygame.draw.polygon(windowSurface, SKIN,((p[0]+25*p[2],p[1]),(p[0]+65*p[2],p[1]+p[4]*p[2]),(p[0]+21*p[2],p[1]+20*p[2])))
    pygame.draw.line(windowSurface,BLACK,(p[0]-25*p[2],p[1]),(p[0]-15*p[2],p[1]+50*p[2]),2)
    pygame.draw.line(windowSurface,BLACK,(p[0]-15*p[2],p[1]+50*p[2]),(p[0]+15*p[2],p[1]+50*p[2]),2)
    pygame.draw.line(windowSurface,BLACK,(p[0]+15*p[2],p[1]+50*p[2]),(p[0]+25*p[2],p[1]),2)
    pygame.draw.line(windowSurface,BLACK,(p[0]-25*p[2],p[1]),(p[0],p[1]-10*p[2]),2)
    pygame.draw.line(windowSurface,BLACK,(p[0]+25*p[2],p[1]),(p[0],p[1]-10*p[2]),2)
    pygame.draw.line(windowSurface,BLACK,(p[0]-15*p[2],p[1]-4*p[2]),(p[0],p[1]+15*p[2]),2)
    pygame.draw.line(windowSurface,BLACK,(p[0]+15*p[2],p[1]-4*p[2]),(p[0],p[1]+15*p[2]),2)
    pygame.draw.circle(windowSurface, SKIN,(p[0],p[1]-15*p[2]),15*p[2],0)
    pygame.draw.circle(windowSurface, BLACK,(p[0],p[1]-15*p[2]),15*p[2],2)
    pygame.draw.polygon(windowSurface, BLACK,((p[0]-14*p[2],p[1]-20*p[2]),(p[0]-10*p[2],p[1]-35*p[2]),(p[0]-5*p[2],p[1]-30*p[2]),(p[0],p[1]-40*p[2]),(p[0]+5*p[2],p[1]-30*p[2]),(p[0]+10*p[2],p[1]-35*p[2]),(p[0]+14*p[2],p[1]-20*p[2]),(p[0]+7*p[2],p[1]-25*p[2]),(p[0],p[1]-20*p[2]),(p[0]-7*p[2],p[1]-25*p[2])))
    pygame.draw.circle(windowSurface, BLACK, (p[0]-7*p[2],p[1]-15*p[2]),3*p[2],1)
    pygame.draw.circle(windowSurface, BLACK, (p[0]+7*p[2],p[1]-15*p[2]),3*p[2],1)
    pygame.draw.line(windowSurface,BLACK,(p[0]-25*p[2],p[1]),(p[0]-65*p[2],p[1]+p[3]*p[2]),2)
    pygame.draw.line(windowSurface,BLACK,(p[0]-21*p[2],p[1]+20*p[2]),(p[0]-65*p[2],p[1]+p[3]*p[2]),2)
    pygame.draw.line(windowSurface,BLACK,(p[0]+25*p[2],p[1]),(p[0]+65*p[2],p[1]+p[4]*p[2]),2)
    pygame.draw.line(windowSurface,BLACK,(p[0]+21*p[2],p[1]+20*p[2]),(p[0]+65*p[2],p[1]+p[4]*p[2]),2)
    pygame.draw.polygon(windowSurface, BLACK,((p[0]-15*p[2],p[1]+50*p[2]),(p[0]-25*p[2],p[1]+100*p[2]),(p[0],p[1]+50*p[2])))
    pygame.draw.polygon(windowSurface, BLACK,((p[0]+15*p[2],p[1]+50*p[2]),(p[0]+25*p[2],p[1]+100*p[2]),(p[0],p[1]+50*p[2])))
    if p[8] <= p[9]:# Blinking logic
        p[9]=0
        p[8]=random.randint(45,120)
        return
    elif p[9] > p[8] - 10:
        p[9] += 1
        return
    else:
        pygame.draw.circle(windowSurface, WHITE, (p[0]-7*p[2],p[1]-15*p[2]),2*p[2],0)
        pygame.draw.circle(windowSurface, WHITE, (p[0]+7*p[2],p[1]-15*p[2]),2*p[2],0)
        p[9] += 1
        return

# Gets the players guess & ensures guess is valid (and insults if it isn't)
def getGuess(alreadyGuessed):
    while event.type == KEYDOWN:
        global guess
        guessed[0]=1
        guessed[2]=15
        guess = event.dict['unicode']
        guess = guess.lower()
        if event.key == K_9:#Show FPS
            if show[0] == 1:
                show[0] = 0
            else:
                show[0] = 1
        if event.key == K_8:#Show Gradiated Sky
            if show[2] == True:
                show[2] = False
            else:
                show[2] = True
        if event.key == K_7:#Show Detailed Background
            if show[3] == True:
                show[3] = False
            else:
                show[3] = True
        if event.key == K_EQUALS:#Increase max FPS
            show[1] += 5
        if event.key == K_MINUS:#Decrease max FPS
            show[1] -= 5
        if len(guess) != 1:
                    guessed[0]=0
                    guessed[1]='Please enter a single letter'
                    h[5]='1 letter at a time!'
                    break
        elif str(guess) in alreadyGuessed:
                    guessed[0]=0
                    guessed[1]='Pick a different letter'
                    h[5]='You\'ve already picked that!'
                    ##numptySound.play()
                    break
        elif str(guess) not in 'abcdefghijklmnopqrstuvwxyz':
                    guessed[0]=0
                    guessed[1]='Please enter a letter'
                    h[5]='Kid! I said only LETTERS!'
                    break
        else:
                    guessed[1]='Guess a letter in my secret word!'
                    return guess
    else:
        guessed[0]=0
        guessed[2]=0
        return

# Player & Hangmans speech bubbles
def playerguess():
    if guess == '':
        return
    else:
        text = smallFont.render(guess.upper() + '?', True, BLACK,WHITE)
        pygame.draw.polygon(windowSurface, WHITE,((p[0]-35,p[1]-17),(p[0]-15,p[1]-10),(p[0]-35,p[1]-23)))
        pygame.draw.line(windowSurface,BLACK,(p[0]-35,p[1]-17),(p[0]-15,p[1]-10),2)
        pygame.draw.line(windowSurface,BLACK,(p[0]-35,p[1]-23),(p[0]-15,p[1]-10),2)
        pygame.draw.circle(windowSurface, WHITE, (p[0]-40,p[1]-20),10,0)
        pygame.draw.circle(windowSurface, WHITE, (p[0]-60,p[1]-20),10,0)
        pygame.draw.circle(windowSurface, BLACK, (p[0]-40,p[1]-20),10,2)
        pygame.draw.circle(windowSurface, BLACK, (p[0]-60,p[1]-20),10,2)
        pygame.draw.rect(windowSurface, WHITE,(p[0]-60, p[1]-30, 20,20))
        pygame.draw.polygon(windowSurface, WHITE,((p[0]-35,p[1]-17),(p[0]-15,p[1]-10),(p[0]-35,p[1]-23)))
        pygame.draw.line(windowSurface,BLACK,(p[0]-60,p[1]-30),(p[0]-40,p[1]-30),2)
        pygame.draw.line(windowSurface,BLACK,(p[0]-60,p[1]-11),(p[0]-40,p[1]-11),2)
        windowSurface.blit(text, (p[0]-59,p[1]-27))
        text = smallFont.render(str(h[5]), True, BLACK,WHITE)
        pygame.draw.polygon(windowSurface, WHITE,((h[0]+35,h[1]-17),(h[0]+15,h[1]-10),(h[0]+35,h[1]-23)))
        pygame.draw.line(windowSurface,BLACK,(h[0]+35,h[1]-17),(h[0]+15,h[1]-10),2)
        pygame.draw.line(windowSurface,BLACK,(h[0]+35,h[1]-23),(h[0]+15,h[1]-10),2)
        pygame.draw.circle(windowSurface, WHITE, (h[0]+40,h[1]-20),10,0)
        pygame.draw.circle(windowSurface, WHITE, (h[0]+40+(len(str(h[5]))*8),h[1]-20),10,0)
        pygame.draw.circle(windowSurface, BLACK, (h[0]+40,h[1]-20),10,2)
        pygame.draw.circle(windowSurface, BLACK, (h[0]+40+(len(str(h[5]))*8),h[1]-20),10,2)
        pygame.draw.rect(windowSurface, WHITE,(h[0]+40,h[1]-30,len(str(h[5]))*8,20))
        pygame.draw.polygon(windowSurface, WHITE,((h[0]+35,h[1]-17),(h[0]+15,h[1]-10),(h[0]+35,h[1]-23)))
        pygame.draw.line(windowSurface,BLACK,(h[0]+40+(len(str(h[5]))*8),h[1]-30),(h[0]+40,h[1]-30),2)
        pygame.draw.line(windowSurface,BLACK,(h[0]+40+(len(str(h[5]))*8),h[1]-11),(h[0]+40,h[1]-11),2)
        windowSurface.blit(text, (h[0]+39,h[1]-27))

# Update the screen with the guesses, correct letters
def displayBoard(display,missedLetters, correctLetters, secretWord):
    blanks = '_' * len(secretWord)
    blankText = titleFont.render(blanks, True, WHITE,)
    windowSurface.blit(blankText, (150,440))
    pygame.draw.rect(windowSurface, BLACK,(560,20,320,440),1)
    pygame.draw.rect(windowSurface, WHITE,(561,21,318,89))
    pygame.draw.rect(windowSurface, BLACK,(560,24,320,35),1)
    pygame.draw.rect(windowSurface, BLACK,(560,62,320,48),1)
    title = titleFont.render('PYHangman', True, BLUE,)
    titles = titleFont.render('PYHangman', True, BLACK,)
    intro = basicFont.render('The chosen category is...', True, BLUE,)
    category = basicFont.render(secretKey + ' - ' + str(len(secretWord)) + ' letters', True, BLUE,)
    guessText = basicFont.render(guessed[1], True, WHITE,)
    guessTexts = basicFont.render(guessed[1], True, BLACK,)
    windowSurface.blit(guessTexts, (148,398))
    windowSurface.blit(guessText, (150,400))
    windowSurface.blit(titles,(583,23))
    windowSurface.blit(title,(585,25))
    windowSurface.blit(intro,(570,70))
    windowSurface.blit(category,(570,90))
    if score[2]!='':
        pygame.draw.rect(windowSurface, WHITE,(561,349,318,61))
        pygame.draw.rect(windowSurface, BLACK,(560,349,320,61),1)
        result = titleFont.render(score[2], True, BLUE,)
        windowSurface.blit(result, (580,365))
    for i in range (len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks [i+1:]
            correctText = titleFont.render(blanks, True, WHITE,)
            pygame.draw.rect(windowSurface, GREEN,(150, 440, 300,40))
            windowSurface.blit(correctText, (150,440))
    if display == 0:
            noose()
    elif display >=1:
        pygame.draw.rect(windowSurface, WHITE,(561,109,318,32))
        pygame.draw.rect(windowSurface, BLACK,(560,109,320,32),1)
        text1a = guessFont.render('1.', True, BLACK,)
        text1b = guessFont.render(missedLetters[0].upper(), True, BLUE,)
        text1c = titleFont.render('X', True, RED,)
        windowSurface.blit(text1a, (570,115))
        windowSurface.blit(text1b, (660,115))
        windowSurface.blit(text1c, (750,111))
        if display >= 2:
            pygame.draw.rect(windowSurface, WHITE,(561,141,318,32))
            pygame.draw.rect(windowSurface, BLACK,(560,141,320,32),1)
            text2a = guessFont.render('2.', True, BLACK,)
            text2b = guessFont.render(missedLetters[1].upper(), True, BLUE,)
            text2c = titleFont.render('X', True, RED,)
            windowSurface.blit(text2a, (570,145))
            windowSurface.blit(text2b, (660,145))
            windowSurface.blit(text2c, (750,141))
            if display >= 3:
                pygame.draw.rect(windowSurface, WHITE,(561,173,318,34))
                pygame.draw.rect(windowSurface, BLACK,(560,173,320,34),1)
                text3a = guessFont.render('3.', True, BLACK,)
                text3b = guessFont.render(missedLetters[2].upper(), True, BLUE,)
                text3c = titleFont.render('X', True, RED,)
                windowSurface.blit(text3a, (570,177))
                windowSurface.blit(text3b, (660,177))
                windowSurface.blit(text3c, (750,174))
                if display >= 4:
                    pygame.draw.rect(windowSurface, WHITE,(561,205,318,32))
                    pygame.draw.rect(windowSurface, BLACK,(560,205,320,32),1)
                    text4a = guessFont.render('4.', True, BLACK,)
                    text4b = guessFont.render(missedLetters[3].upper(), True, BLUE,)
                    text4c = titleFont.render('X', True, RED,)
                    windowSurface.blit(text4a, (570,208))
                    windowSurface.blit(text4b, (660,208))
                    windowSurface.blit(text4c, (750,206))
                    if display >= 5:
                        pygame.draw.rect(windowSurface, WHITE,(561,237,318,30))
                        pygame.draw.rect(windowSurface, BLACK,(560,237,320,30),1)
                        text5a = guessFont.render('5.', True, BLACK,)
                        text5b = guessFont.render(missedLetters[4].upper(), True, BLUE,)
                        text5c = titleFont.render('X', True, RED,)
                        windowSurface.blit(text5a, (570,240))
                        windowSurface.blit(text5b, (660,240))
                        windowSurface.blit(text5c, (750,238))
                        if display >= 6:
                            pygame.draw.rect(windowSurface, WHITE,(561,267,318,30))
                            pygame.draw.rect(windowSurface, BLACK,(560,267,320,30),1)
                            text6a = guessFont.render('6.', True, BLACK,)
                            text6b = guessFont.render(missedLetters[5].upper(), True, BLUE,)
                            text6c = titleFont.render('X', True, RED,)
                            windowSurface.blit(text6a, (570,270))
                            windowSurface.blit(text6b, (660,270))
                            windowSurface.blit(text6c, (750,268))
                            if display >=7:
                                pygame.draw.rect(windowSurface, WHITE,(561,297,318,31))
                                pygame.draw.rect(windowSurface, BLACK,(560,297,320,31),1)
                                text6a = guessFont.render('7.', True, BLACK,)
                                text6b = guessFont.render(missedLetters[6].upper(), True, BLUE,)
                                text6c = titleFont.render('X', True, RED,)
                                windowSurface.blit(text6a, (570,300))
                                windowSurface.blit(text6b, (660,300))
                                windowSurface.blit(text6c, (750,298))
                                if display >=8:
                                    pygame.draw.rect(windowSurface, WHITE,(561,328,318,32))
                                    pygame.draw.rect(windowSurface, BLACK,(560,328,320,32),1)
                                    text6a = guessFont.render('8.', True, BLACK,)
                                    text6b = guessFont.render(missedLetters[7].upper(), True, BLUE,)
                                    text6c = titleFont.render('X', True, RED,)
                                    windowSurface.blit(text6a, (570,330))
                                    windowSurface.blit(text6b, (660,330))
                                    windowSurface.blit(text6c, (750,328))
                            

# draw the window onto the screen
def update():
    background()
    gallows()
    noose()
    displayBoard(s, missedLetters, correctLetters, secretWord)
    hangman()
    player()
    playerguess()
    framerate()
    pygame.display.update()

def start():
    background()
    gallows()
    noose()
    hangman()
    player()
    infoDisplay(p,150)
    framerate()
    pygame.display.update()

def framerate():
    mainClock.tick(show[1])
    fps=int(mainClock.get_fps())
    if show[0]==1:
        texts = smallFont.render(str(fps), True, BLACK,)
        text = smallFont.render(str(fps), True, WHITE,)
        windowSurface.blit(texts, (780,460))
        windowSurface.blit(text, (781,461))
        text1s = smallFont.render(str(show[1]), True, BLACK,)
        text1 = smallFont.render(str(show[1]), True, WHITE,)
        windowSurface.blit(text1s, (780,450))
        windowSurface.blit(text1, (781,451))

# Opening menu
def menu():
    # run the menu loop
    moveUp = False
    moveDown = False
    while option[5]==0:# Option [5] is the selection output bit
        # check for events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                    # change the keyboard variables
                    if event.key == K_UP or event.key == ord('w'):#Curser Up
                        moveDown = False
                        moveUp = True
                    if event.key == K_DOWN or event.key == ord('s'):#Curser Down
                        moveUp = False
                        moveDown = True
                    if event.key == K_9:#Show FPS
                        if show[0] == 1:
                            show[0] = 0
                        else:
                            show[0] = 1
                    if event.key == K_8:#Show Gradiated Sky
                        if show[2] == True:
                            show[2] = False
                        else:
                            show[2] = True
                    if event.key == K_7:#Show Detailed Background
                        if show[3] == True:
                            show[3] = False
                        else:
                            show[3] = True
                    if event.key == K_EQUALS:#Increase max FPS
                        show[1] += 5
                    if event.key == K_MINUS:#Decrease max FPS
                        show[1] -= 5
                    if event.key == K_RETURN or event.key == K_SPACE:#Select current option
                        if curser[1]==190:
                            option[5]=1
                            secretWord,secretKey = getNextRound(words,levelread)
            if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_UP or event.key == ord('w'):
                        moveUp = False
                    if event.key == K_DOWN or event.key == ord('s'):
                        moveDown = False

        # move the Curser
        if moveDown and curser[1] < 300:
            curser[1] += MOVESPEED
            moveDown = False
        if moveUp and curser[1] > 200:
            curser[1] -= MOVESPEED
            moveUp = False

        # draw the background onto the surface & draw the banner
        background()
        drawBanner()

        # draw the curser onto the surface
        pygame.draw.rect(windowSurface, BLACK, (240, 190, 250, 50),1)

        # draw the options onto the surface
        text1s = guessFont.render(option[0], True, BLUE,)
        text1 = guessFont.render(option[0], True, WHITE,)
        text2s = guessFont.render(option[1], True, BLACK,)
        text2 = guessFont.render(option[1], True, WHITE,)
        text3s = guessFont.render(option[2], True, BLACK,)
        text3 = guessFont.render(option[2], True, WHITE,)
        text4s = guessFont.render(option[3], True, BLACK,)
        text4 = guessFont.render(option[3], True, WHITE,)
        text5s = guessFont.render(option[4], True, BLACK,)
        text5 = guessFont.render(option[4], True, WHITE,)
        text6s = bannerFont.render("PYHangman",True, BLACK,)
        text6 = bannerFont.render("PYHangman",True, BLUE,)
        windowSurface.blit(text1s, (250,200))
        windowSurface.blit(text1, (252,202))
        windowSurface.blit(text2s, (250,250))
        windowSurface.blit(text2, (252,252))
        windowSurface.blit(text3s, (250,300))
        windowSurface.blit(text3, (252,302))
        windowSurface.blit(text4s, (250,350))
        windowSurface.blit(text4, (252,352))
        windowSurface.blit(text5s, (250,400))
        windowSurface.blit(text5, (251,401))
        windowSurface.blit(text6s, (banner[0]-2,banner[1]-2))
        windowSurface.blit(text6, (banner[0],banner[1]))
        backgroundAnim()
        framerate()
        # draw the window onto the screen
        pygame.display.update()

def drawBanner():
    pygame.draw.line(windowSurface,WHITE,(0,70),(1400,70),50)
    pygame.draw.line(windowSurface,BLACK,(0,47),(1400,47),1)
    pygame.draw.line(windowSurface,BLACK,(0,93),(1400,93),1)

def backgroundAnim():
        if banner[0]<=800:# Animate the banner text and background
            banner[0]+=1
        if banner[0]>800:
            banner[0]=-240
        if banner[2]<=1250:
            banner[2]+=1
        if banner[2]>1250:
            banner[2]=0
        if banner[3]<=1250:
            banner[3]+=2
        if banner[3]>1250:
            banner[3]=0
        if banner[4]<=1250:
            banner[4]+=3
        if banner[4]>1250:
            banner[4]=0
        if banner[5]<=1250:
            banner[5]+=4
        if banner[5]>1250:
            banner[5]=0
        if banner[6]>750:
            banner[6]=-350
        banner[7]+=1
        if banner[7]>10:
            banner[7]=0
            banner[6]+=1



# run the game loop
secretWord,secretKey = getNextRound(words,levelread)
menu()
start()
infoDisplayText = ['Think you can beat me?','','Hahahah kid!','','You can try!','']
infoDisplay(h,int(show[1]*4.5))
infoDisplayText = ['Well done player!','','You finally beat me!',secretKey]
while True:
    # check for the QUIT event
    if int(time.time() - startTime) > 60:
        text = FlashFont.render("Game Over!", True, BLACK)
        windowSurface.blit(text, (900,100))
        time.sleep(5)
        levelscore=getFinalScore(0,(int(time.time() - startTime)))
        exit()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Animate the nooses
    if h[6]<h[7]:
        h[6]+=1
    if p[6]<p[7]:
        p[6]+=1
    update()
    if guessed[2]>0:# Guess input keyboard delay
        guessed[2]-=1
    else:
        if guessed[0] == 0:
            getGuess(missedLetters + correctLetters)
        else:
            guessed[0]=0
            if str(guess) in secretWord:
                h[7]+=150/len(secretWord)
                h[5]=1
                correctSound.play()
                backchat()
                correctLetters = correctLetters + guess
                foundAllLetters = True
                for i in range(len(secretWord)):
                    if secretWord[i] not in correctLetters:
                        foundAllLetters = False
                        break
                if foundAllLetters:
                    h[7]=h[1]
                    score[2]='You Got It!'
##                    noooSound.play()
                    gameover(h)
                    levelscore=getFinalScore(1,(int(time.time() - startTime)))
                    print(levelscore)
                    exit()
            else:
                missedLetters = missedLetters + str(guess)
                p[7]+=25
                h[5]=2
                backchat()
                noose()
                s+= 1
                if h[5] == 'LOL!':
                    hahahaSound.play()
                elif h[5] == 'Hahaha!':
                    hahahaSound.play()
                elif h[5] == 'Hehe!':
                    hahahaSound.play()
                elif h[5] == 'Mwahaha!!':
                    mwahahaSound.play()
                elif h[5] == 'Hohoho!':
                    hahahaSound.play()
                else:
                    wrongSound.play()
                if len(missedLetters) == 8:
                            p[7]=p[1]
                            score[2]='You Lost!'
                            score[4]+=1
                            displayBoard(s, missedLetters, correctLetters, secretWord)
                            gameover(p)
                            mwahahaSound.play()
                            infoDisplayText = ['Hahaha ','You Lost!','You had reached round ',str(roundNo+1),'The word was ',secretWord.title()]
                            infoDisplay(h,int(show[1]*4.5))
                            infoDisplayText = ['You can beat anything,Kid','','You Got This','','Better luck next time!','']
                            infoDisplay(p,int(show[1]*4.5))
                            gameIsDone = True
                            score[1]+=1
                            levelscore=getFinalScore(0,(int(time.time() - startTime)))
                            print(levelscore)
                            exit()

            if gameIsDone:
                    roundNo=0
                    score[2]=''
                    guess = ''
                    missedLetters = ''
                    correctLetters = ''
                    option[5]=0
                    menu()
                    if option[5]==1:
                        secretWord,secretKey = getNextRound(words,levelread)
                    else:
                        secretWord,secretKey = getRandomWord(words)
                    infoDisplayText = ['Welcome to Hangman','','Round ',str(roundNo+1),'Subject - ',secretKey]
                    gameIsDone = False
                    guessed=[0,'Guess a letter in my secret word!',0]
                    s = 0
                    h = [280,259,1,40,40,0,100,100,0,0,150,240,13]# [0-X,1-Y,2-Scale,3-left hand,4-right hand,5-backchat,6-noose,7-new noose,8-blink count,9-blink timer]
                    p = [150,259,1,40,40,0,100,100,0,0,150,240,13]# [0-X,1-Y,2-Scale,3-left hand,4-right hand,5-spare,6-noose,7-new noose,8-blink count,9-blink timer]
                    start()

