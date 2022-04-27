import pygame
import sys
from text_block import TextBlock
from answer_button import AnswerButton
import question_list as QL
from question_object import Question_Object
from colors import Color
import os

surface = pygame.display.set_mode((0, 0))
background = pygame.image.load("People/Quiz/bg.png").convert()
nscore = 0
flag = 0
screen_h = pygame.display.Info().current_h
screen_w = pygame.display.Info().current_w


class GameState:
    menu, game, game_over = range(3)


class Game:

    def __init__(self, level):
        pygame.init()
        pygame.font.init()
        self.level = level
        self.question_height = 130
        self.answer_height = 70
        self.clock = pygame.time.Clock()
        self.mouse_handlers = []
        self.objects = []
        self.answer_objects = []
        self.current_question = None
        self.current_question_i = 4*self.level-5
        self.score = 0
        self.state = GameState.game
        temp_list = []
        question_list = []
        for key in QL.Questions:
            value = QL.Questions[key]
            temp_list.append(value)
            for key2 in value:
                val_quest = value[key2]
                question_list.append(Question_Object(key2, val_quest[0], val_quest[1]))

        # according to the level appropriate situtations taken
        self.situation_list = temp_list[level*2: (level+1)*2]

        self.questions = question_list[level*4: (level+1)*4]

        self.nextQuestion()
        self.game_over_text_block = TextBlock((screen_w-1250)/2, 300,
                                              350, 100, "  ", True)

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

    def addTextBlock(self, x, y, w, h, text, isquestion=False):
        # self.questions.append(TextBlock(x, y, w, h, text,0))
        self.answer_objects.append(TextBlock(x, y, w, h, text, True))

    def addAnswerButton(self, x, y, w, h, text, onclick_func, scores_weight):
        button1 = AnswerButton(x, y, w, h, text, onclick_func, scores_weight)
        self.answer_objects.append(button1)
        self.mouse_handlers.append(button1.handleMouseEvent)

    def checkAnswer(self, obj):
        # 4 question, total 3 score possible
        self.score = self.score + obj.score_weight*0.5*0.25
        print(self.score)
        self.nextQuestion()

    def gameOver(self):
        self.state = GameState.game_over
        self.cleanScreen()
        self.game_over_text_block.text = "Your response has been noted"
        self.objects.append(self.game_over_text_block)
        pygame.quit()
        a = 1/0

    def cleanScreen(self):
        del self.answer_objects[:]
        del self.objects[:]
        del self.mouse_handlers[:]

    def nextQuestion(self):
        del self.answer_objects[:]
        del self.mouse_handlers[:]
        self.current_question_i += 1
        if self.current_question_i >= 4*(self.level):
            self.gameOver()
        else:
            self.current_question = self.questions[self.current_question_i]
            self.addTextBlock((screen_w-1250)/2, 100, 1250, self.question_height,
                              self.current_question.question_text,True)

            answers = self.current_question.answers

            answer_weight = self.current_question.correct_answer

            for index in range(len(answers)):
                self.addAnswerButton((screen_w-1250)/2,
                                     self.question_height+(screen_h-self.question_height)/4+index*(self.answer_height+30),
                                     1250, self.answer_height, answers[index],
                                     self.checkAnswer, answer_weight[index])

    def run(self):
        while True:
            surface.blit(background, [0, 0])
            # surface.fill(Color.CADETBLUE)
            self.handleEvents()
            self.draw()
            self.update()
            pygame.display.update()
            self.clock.tick(60)


def start_game(level):
    score = 0
    try:
        Game1 = Game(level)
        Game1.run()
    except ZeroDivisionError as e:
        pass
    score = Game1.score
    print("GOT SCORE = ", score)
    if score > 1:
        return 0.95
    return score


if __name__ == "__main__":
    start_game(1)
