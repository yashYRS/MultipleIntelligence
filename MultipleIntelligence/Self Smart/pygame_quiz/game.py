import pygame
import sys
from text_block import TextBlock
from answer_button import AnswerButton
from question_object import Question_Object
from colors import Color
import os

surface = pygame.display.set_mode((0, 0))
background = pygame.image.load("bg.png").convert()
nscore=0
flag = 0

class GameState:
    menu, game, game_over = range(3)


class Game:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.question_height = 100
        self.answer_height = 100
        self.clock = pygame.time.Clock()
        self.mouse_handlers = []
        self.objects = []
        self.answer_objects = []
        self.current_question = None
        self.current_question_i = -1
        self.score = 0     
        self.state = GameState.game
        self.questions = [Question_Object('How in touch with your feelings are you?', ('Not so much . I tend to live more in my head', 'Somewhat.I know when I am having emotions , but I can\'t influence them very much',  'Very in touch. I know what I feel and can experience emotions thoroughly'),2 ) ,
 Question_Object('Personal beliefs about yourself and your capabilities?',('I don\'t know what I believe. I don\'t think in terms of beliefs about myself',' I understand the concept of personal belief but I couldn\'t necessarily make you a specific list of my positive and negative beliefs' , 'I can make you a list of several beliefs I have about myself and my capabilities in life' ),2),
 Question_Object('What role do goals play in your life?',('Hey , I\'m just going with the flow here. Don\'t talk to me about what I really want',' I can\'t say that I intentionally pursue goals on a regular basis' , 'Goal-setting is one of the regular tools I use in my life' ),2) ,
  Question_Object('Life values: What\'s most important to you in life?',('I honestly don\'t know what\'s most important to me in life','I have some ideas about what\'s most important to me in life,but not tons of clarity' , 'Yes,I do know my life values. I am very clear on what is most important to me ' ),2) ,
  Question_Object('Life values: What\'s most important to you in life?',('I honestly don\'t know what\'s most important to me in life','I have some ideas about what\'s most important to me in life,but not tons of clarity' , 'Yes,I do know my life values. I am very clear on what is most important to me' ),2),
  Question_Object('Inner Conflicts: What divides you?',('I really have no idea how my beliefs or desires confict','I don\'t have much clarity on how I am conflicted' , 'I\'ve identified and worked with my inner conflicts  ' ),2)
  ]
  
  
        #self.score_text_block = TextBlock(500, 10, 250, 50, "Score: {0}/{1}".format(str(self.score), str(len(self.questions))))
        #self.objects.append(self.score_text_block)
        self.nextQuestion()
        self.game_over_text_block = TextBlock(300, 300, 350, 100, "Well , Thanks for sharing ")

    def update(self):
            for item in self.objects:
                item.update()

            for item in self.answer_objects:
                item.update()

    def draw(self):
        for item in self.objects:
            item.draw(surface)

        for item in self.answer_objects:
            item.draw(surface)

    def handleEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type in (pygame.MOUSEBUTTONDOWN,
                                pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def addTextBlock(self, x, y, w, h, text):
       # self.questions.append(TextBlock(x, y, w, h, text,0))
        self.answer_objects.append(TextBlock(x, y, w, h, text))


    def addAnswerButton(self, x, y, w, h, text, onclick_func, is_it_correct):
        button1 = AnswerButton(x, y, w, h, text, onclick_func, is_it_correct)
        self.answer_objects.append(button1)
        self.mouse_handlers.append(button1.handleMouseEvent)

    def checkAnswer(self, obj):
        if obj.is_it_correct_answer is True:
            self.score += 1
        #self.score_text_block.text = "Score: {0}/{1}".format(str(self.score), str(len(self.questions)))
        self.nextQuestion()


    def gameOver(self):
        self.state = GameState.game_over
        self.cleanScreen()
        self.game_over_text_block.text = "Thanks for sharing your thoughts!"
        self.objects.append(self.game_over_text_block)
        
    def cleanScreen(self):
        del self.answer_objects[:]
        del self.objects[:]
        del self.mouse_handlers[:]

    def nextQuestion(self):
        del self.answer_objects[:]
        del self.mouse_handlers[:]
        self.current_question_i += 1
        if self.current_question_i >= len(self.questions):
            self.gameOver()
        else:
            self.current_question = self.questions[self.current_question_i]
            self.addTextBlock(50, 70, 1250, self.question_height,
                              self.current_question.question_text)

            answers = self.current_question.answers

            i = 0

            for item in answers:
                if self.current_question.correct_answer == i:
                    is_it_correct = True
                else:
                    is_it_correct = False

                self.addAnswerButton(50, self.question_height+80+i*(self.answer_height+10),
                                     1250, self.answer_height, item, self.checkAnswer, is_it_correct)
                i += 1

    def run(self):
        while True:
            surface.blit(background,[0, 0])
            #surface.fill(Color.BLACK)
            self.handleEvents()
            self.draw()
            self.update()
            pygame.display.update()
            self.clock.tick(60)
 


Game1 = Game()


Game1.run()
