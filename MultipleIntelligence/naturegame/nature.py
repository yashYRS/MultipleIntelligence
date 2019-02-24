#! /usr/local/bin/python

import os
import pygame
from pygame.locals import *
from pygame.color import THECOLORS
from word import Word
import random
import sys
from faces import Face
import time
global levelread
global timeStart
levelread = 2 
timeStart = time.time()+10



#startTime = time.time()
EXEC_DIR = os.path.dirname(__file__)  

### Test for platform since the .app bundle behaves strangely

if levelread==1:
    if sys.platform == 'darwin':
        image_dir = os.walk("word_files")
    else:
        image_dir = os.walk(os.path.join(EXEC_DIR, "word_files"))
elif levelread==2:
    if sys.platform == 'darwin':
        image_dir = os.walk("animals")
    else:
        image_dir = os.walk(os.path.join(EXEC_DIR, "animals"))
#elif levelread==3:
 #   image_dir=getImage('animals')


pygame.init()
pygame.display.set_caption("Guess the word")
#### Globals
screen = pygame.display.set_mode((0, 0))
font = pygame.font.SysFont('Helvetica', 50)
font1 = pygame.font.SysFont('Helvetica', 20)
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

the_word = Word(random.choice(image_list),levelread)
#the_word = Word('yo-yo.png')

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
    txt2= "Answer the question displayed below the photos"
    txt3= "As fast as you can"
    txt4= "If your answer is correct"
    txt5= "Next qustion will be diplayed"
    txt6= "You have 60 seconds. Timer is displayed"
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


def background():
    pygame.draw.arc(screen, yellow, (40,40,150,150), 0, 180,70)
    pygame.draw.polygon(screen, brown, [[200, 30], [10, 270],[400, 270]])
    pygame.draw.polygon(screen, brown, [[300, 100], [100, 270],[450, 270]])
    pygame.draw.polygon(screen, brown, [[1100, 400], [860, 600],[1260, 600]])
    pygame.draw.polygon(screen, brown, [[1200, 500], [1100, 600],[1300, 600]])
    pygame.draw.ellipse(screen, blue, [1000, 1000, 100, 150],10)
    draw_tree(80,340)
    draw_tree(30,340)
    draw_tree(110,360)
    draw_tree(250,370)
    draw_tree(180,380)
    draw_tree(330,380)
    draw_tree(100,400)
    draw_tree(320,460)
    draw_tree(300,460)
    draw_tree(200,480)
    draw_tree(280,480)
    draw_tree(20,500) #x and y location are the bottom left of tree trunk
    draw_tree(100,500)
    draw_tree(100,600)
    draw_tree(50,600)
    draw_tree(50,490)
    draw_tree(280,550)
    draw_tree(200,600)
    draw_tree(300,650)
    draw_tree(150,700)
    draw_tree(230,700)
    draw_tree(280,700)
    draw_tree(340,700)
    draw_tree(420,700)
    draw_house(20,700)
    draw_cloud(170,120,70)
    draw_cloud(30,50,40)
    draw_cloud(80,100,50)
    draw_cloud(130,100,40)
    draw_cloud(1120,1180,40)
    draw_cloud(1140,1140,60)

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
    
    while running:
        if int(time.time())-int(timeStart) > 20:
            print(levelscore)
            displayGameOver()
            time.sleep(2)
            exit()
        cursor = 0
        letter_position = dict()
        key = pygame.key.get_pressed()
        mods = pygame.key.get_mods()
        screen.fill((255,240,245))
        background()
        #pygame.display.update()
        displayRules()
        if levelread==1:
            textq="Guess the place"
            cdnts=(450,350)
        elif levelread==2:
            textq="Guess my Offsping's name"
            cdnts=(430,350)
        elif levelread==3:
            textq="Guess my habitat"
            cdnts=(440,350)
        st = font.render(textq, 1, (255, 100, 200))
        screen.blit(st,cdnts)
        timer = int(time.time())-int(timeStart)
        t = "Timer: " + str(timer)
        s = font.render(t, 1, (100, 100, 100))
        screen.blit(s,(1100,40))
        the_word.draw(screen, (screen_x/2 - the_word.width/2), 50)

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
            pygame.draw.line(screen, THECOLORS['black'], (line_x1, 460), (line_x2, 460), 2)
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
            happy_group.empty()
            right = False
            the_word = Word(random.choice(image_list),levelread)
            happy.reset()
        happy_group.update()
        
        #### Handle answer ####
        if right:
            text = font.render("Correct!", 1, (100, 100, 200))
            screen.blit(text,(550,500)) 
            entered_text = []
        if wrong:
            text = font.render("Wrong!", 1, (100, 100, 200))
            screen.blit(text,(550,500))            
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
       
        
            
        #### Render typed letters on screen ####
        try:
            for letter in entered_text:                                          
                if not letter == 'backspace':
                    if letter_dict.get(cursor)[1] == '-':
                        cursor += 1

                    correct_letter = font.render(letter, 1, (255, 10, 10))
                    letter_size = font.size(letter)                        
                    screen.blit(correct_letter, [letter_dict.get(cursor)[0], 400])             
                    cursor += 1
        except:
            print("Exception")
            text = font.render("Wrong!", 1, (100, 100, 200))
            screen.blit(text,(550,500)) 

        
        pygame.display.update()                                              
        
if __name__ == "__main__":
    main()

