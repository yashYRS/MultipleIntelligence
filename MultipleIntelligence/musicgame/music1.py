#! /usr/local/bin/python

import os
import pygame
from pygame.locals import *
from pygame.color import THECOLORS
from musicword import Word
import random
import sys
from musicfaces import Face
import time
global levelscore
levelscore=0
global timeStart
timeStart = time.time()+5



#startTime = time.time()
EXEC_DIR = os.path.dirname(__file__)  

### Test for platform since the .app bundle behaves strangely

if sys.platform == 'darwin':
    image_dir = os.walk("sounds")
else:
    image_dir = os.walk(os.path.join(EXEC_DIR, "sounds"))



pygame.init()
pygame.display.set_caption("MusicSMart")
img = pygame.image.load('speaker.png')
an1 = pygame.image.load('an1.png')
an2 = pygame.image.load('an2.png')
an3 = pygame.image.load('an3.png')
an5 = pygame.image.load('an5.png')
an6 = pygame.image.load('an6.png')
an7 = pygame.image.load('an7.png')
tr1 = pygame.image.load('tr1.png')
tr3 = pygame.image.load('tr3.png')
#### Globals
screen = pygame.display.set_mode((0, 0))
font = pygame.font.SysFont('Helvetica', 50)
font1 = pygame.font.SysFont('Helvetica', 20)
flashfont = pygame.font.SysFont("celtic", 35)
green = (0,255,0)
brown = (139,58,58)
yellow = (255,215,0)
blue = (135,206,255)
clock = pygame.time.Clock()
image_list = []
right = False
wrong = False
entered_text = []
screen_x, screen_y = screen.get_size()


#Generate list of files from the image folder 
for root, dir, files in image_dir:
    for file in files:
        if '.DS_Store' not in file:
            image_list.append(file)

rand = random.choice(image_list)
the_word = Word(rand)
image_list.remove(rand)
sname = 'sounds/' + str(rand)
global sound  
sound = pygame.mixer.Sound(sname)
sound1 = pygame.mixer.Sound(sname)
#the_word = Word('yo-yo.png')

def drawSkip():
    txt = "SKIP"
    st1 = font1.render(txt, 1, (0,0,0))
    skip_button = pygame.draw.rect(screen,(227,207,87),(850, 450, 70, 30))
    screen.blit(st1,(855,455))
    return skip_button

ignored_keys = ('escape', 'return', 'backspace', 'enter', 'space', 'right shift'\
                ,'left shift', 'left meta', 'right meta', 'f1', 'f2', 'f3', 'f4', 'f5'\
                ,'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'caps lock')

### Faces and groups to hold them
happy = Face('happy') # For right answer (check happy.lifepan) faces.py
sad = Face('sad')  #For right answer (check sad.lifepan) faces.py
happy_group = pygame.sprite.GroupSingle()
sad_group = pygame.sprite.GroupSingle()
hyphen = False

def draw_tree(x,y):
    pygame.draw.rect(screen,(117,90,0),(x,y-100,50,100))
    pygame.draw.circle(screen,(27,117,0),(x+25,y-120),50)

def draw_house(x,y):
    pygame.draw.rect(screen,(255,171,244),(x,y-180,200,180))
    pygame.draw.rect(screen,(89,71,0),(x+80,y-60,40,60))
    pygame.draw.circle(screen,(255,204,0),(x+112,y-30),4)
    pygame.draw.polygon(screen, (125,125,125), ( (x,y-180),(x+100,y-250),(x+200,y-180) ) )
    draw_window(x+20,y-90)
    draw_window(x+130,y-90)

def draw_window(x,y):
    pygame.draw.rect(screen,(207,229,255),(x,y-50,50,50))
    pygame.draw.rect(screen,(0,0,0),(x,y-50,50,50),5)
    pygame.draw.rect(screen,(0,0,0),(x+23,y-50,5,50))
    pygame.draw.rect(screen,(0,0,0),(x,y-27,50,5))

def draw_cloud(x,y,size):
    pygame.draw.circle(screen,(255,255,255),(x,y),int(size*.5))
    pygame.draw.circle(screen,(255,255,255),(int(x+size*.5),y),int(size*.6))
    pygame.draw.circle(screen,(255,255,255),(x+size,int(y-size*.1)),int(size*.4))

def displayRules():
    txt1= "Hello player! Some basic rules:"
    txt2= "Listen carefully to the sound"
    txt3= "Guess the animal it belings to"
    txt4= "Type in and press enter"
    txt5= "Next sound will be played"
    txt6= "You have 20 seconds. Timer is displayed above"
    st1 = font1.render(txt1, 1, green)
    st2 = font1.render(txt2, 1, green)
    st3 = font1.render(txt3, 1, green)
    st4 = font1.render(txt4, 1, green)
    st5 = font1.render(txt5, 1, green)
    st6 = font1.render(txt6, 1, green)
    screen.blit(st1,(930,100))
    screen.blit(st2,(930,130))
    screen.blit(st3,(930,160))
    screen.blit(st4,(930,190))
    screen.blit(st5,(930,220))
    screen.blit(st6,(930,250))

def displayGameOver():    
    txt = "Time's up! GAME OVER"
    stt = font1.render(txt, 1, green)
    screen.blit(stt,(450,1100))
    pygame.display.flip()


def background():
    text1 = "Music is like a dream. One that I cannot hear."
    text2 = "Music is the shorthand of emotion."
    txt1 = flashfont.render(text1,1,green)
    txt2 = flashfont.render(text2,1,green)
    #screen.blit(txt1,(10,250))
    #screen.blit(txt2,(10,290))
    screen.blit(tr3, (1090,300))
    screen.blit(tr3, (1140,300))
    screen.blit(tr3, (950,300))
    screen.blit(tr3, (1000,300))
    screen.blit(tr3, (1050,300))
    screen.blit(tr1, (20,170))
    screen.blit(tr1, (90,170))
    screen.blit(tr1, (150,170))
    screen.blit(tr1, (10,300))
    screen.blit(tr1, (70,300))
    screen.blit(tr1, (120,300))
    screen.blit(tr1, (160,300))
    screen.blit(tr1, (220,300))
    screen.blit(an1, (10,470))
    screen.blit(an2, (310,470))
    screen.blit(an3, (610,470))
    screen.blit(an5, (1190,300))
    screen.blit(an6, (910,470))
    screen.blit(an7, (1100,470))
    screen.blit(img,(550,100))

def displayspeaker():
    return 1
    
# main function and loop 

def main():
    levelscore=0
    levelread = 2
    global the_word
    global entered_text
    global ignored_keys
    global wrong
    global right
    global hyphen
    running = True
    pygame.key.set_repeat(0,0)

    yes=1
    flag=True
    while running:
        if int(time.time())-int(timeStart) > 30:
            levelscore/=11
            print(levelscore)
            displayGameOver()
            time.sleep(1)
            exit()
        cursor = 0
        displayspeaker()
        letter_position = dict()
        key = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        screen.fill((255,240,245))
        background()
        skipbutton=drawSkip()
        #pygame.display.update()
        displayRules()
        textq="Who am I?"
        cdnts=(560,300)
        st = font.render(textq, 1, (255, 100, 200))
        screen.blit(st,cdnts)
        timer = int(time.time())-int(timeStart)
        t = "Timer: " + str(timer)
        s = font.render(t, 1, (100, 100, 100))
        screen.blit(s,(1100,40))
        t = "Score " + str(levelscore)
        s = font.render(t, 1, (100, 100, 100))
        screen.blit(s,(100,100))
        if yes==1:
            while flag:
                sound1.play()
                flag=False
        else:
            flag=True
            while flag:
                sound.play()
                flag = False
        #the_word.draw(screen, (screen_x/2 - the_word.width/2), 50)

        ### Begin calculations for total width of area for typing
        num_lines = len(the_word.letters)  ##Number of lines
        underline_width = 40                     # Width of underlines
        text_total_width = (num_lines * underline_width) + ((num_lines - 1) * 20) ### Total width of lines and spaces
        line_x1 = screen_x/2 - text_total_width/2
        
        ##list to hold where to begin each letter
        letter_beginning_list = []
        
        # Beginning letter position, will be updated 
        letter_beginning = screen_x/2 - text_total_width/2
        
        #x2 = letter_beginning
        red = (255, 10, 10)
        white = (255, 255, 255)
        
        ### This establishes the keys for the dict ###
        letter_keys = range(0, the_word.length)
        
        ##Create lines for beneath letters and get size and position to draw letters 
        #letter_position_dict = dict.fromkeys(letter_keys)
        
        
        for letter in the_word.letters:
            letter_size = font.size(letter)
            #print(letter_size[0])
            letter_beginning_list.append([letter_beginning + (underline_width/2 - letter_size[0]/2), letter])
            correct_letter = font.render(letter, 1, (255, 10, 10))
            letter_size = font.size(letter)                        
            if letter == "-":
                screen.blit(correct_letter, [letter_beginning + (underline_width/2 - letter_size[0]/2), 400])             
            letter_beginning += underline_width + 20 
            
           
            line_x2 = line_x1 + underline_width 
            pygame.draw.line(screen, THECOLORS['black'], (line_x1, 430), (line_x2, 430), 2)
            line_x1 += underline_width + 20 
            line_x2 += underline_width + 20 
        
        #print(letter_beginning_list)

        letter_dict = dict(zip(letter_keys, letter_beginning_list))
        #print(letter_dict)
        
        
        
        #print(letter_position_dict)

        #### (Wrong answer)sad face lufespan
        if sad.lifespan == 0:
            sad_group.empty()
            wrong = False
        sad_group.update()
        
        #(Right answer)happy face lifespan 
        if happy.lifespan == 0:
            yes=0
            happy_group.empty()
            right = False
            rand = random.choice(image_list)
            image_list.remove(rand)
            the_word = Word(rand)
            sname = 'sounds/' + str(rand)
            sound  = pygame.mixer.Sound(sname)
            levelscore+=1
            happy.reset()
        happy_group.update()
        
        #### Handle answer ####
        if right:
            text = font.render("Correct!", 1, (100, 100, 200))
            screen.blit(text,(550,450)) 
            entered_text = []
        if wrong:
            text = font.render("Wrong!", 1, (100, 100, 200))
            screen.blit(text,(550,450))            
            entered_text = []

        #if key[pygame.K_ESCAPE]:
         #   sys.exit()
        elif (mods & KMOD_META):
            if key[pygame.K_q]:
                sys.exit()
        if hyphen:
            entered_text.append('-')
            hyphen = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                    sys.exit()
                
            #typed letters 
            if event.type == pygame.KEYDOWN:
                key_value = pygame.key.name(event.key)
                if key_value == 'backspace':
                    if entered_text:
                        entered_text.pop()

                if key_value not in ignored_keys:
                    entered_text.append(key_value)
                    print(entered_text)
                
                if key_value == 'return':
                    hyphen_pos = [i for i,x in enumerate(the_word.letters) if x == '-']
                    print(hyphen_pos)
                    if hyphen_pos:
                        del(the_word.letters[int(hyphen_pos[0])])

                    if entered_text == the_word.letters:
                        happy_group.add(happy)
                        right = True
                    else:
                        sad.reset()
                        sad_group.add(sad)
                        wrong = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  
                if skipbutton.collidepoint(mouse_pos):
                    rand = random.choice(image_list)
                    image_list.remove(rand)
                    the_word = Word(rand)
                    sname = 'sounds/' + str(rand)
                    sound  = pygame.mixer.Sound(sname)
                    sound.play()

        
            
        #### Render typed letters on screen ####
        try:
            for letter in entered_text:                                          
                if not letter == 'backspace':
                    if letter_dict.get(cursor)[1] == '-':
                        cursor += 1

                    correct_letter = font.render(letter, 1, (255, 10, 10))
                    letter_size = font.size(letter)                        
                    screen.blit(correct_letter, [letter_dict.get(cursor)[0], 380])             
                    cursor += 1
        except:
            print("Exception")
            text = font.render("Wrong!", 1, (100, 100, 200))
            screen.blit(text,(550,500)) 

        
        pygame.display.update()                                              
        
if __name__ == "__main__":
    main()

