import os
import sys
import time
import random
import pygame


WIDTH = 800
HEIGHT = 600
FPS = 12
pygame.init()
pygame.display.set_caption('sliding tiles- TechVivdan')
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
brown = (100, 40, 0)


font = pygame.font.SysFont('comicsans', 70)


class Generate_Puzzle:
    def __init__(self, gridsize, tilesize, margin):

        self.gridsize, self.tilesize, self.margin = gridsize, tilesize, margin

        # Get the total number of Tiles
        self.tiles_no = gridsize[0]*gridsize[1]-1
        # Tile coordinates
        self.tiles = [(x, y) for y in range(gridsize[1]) for x in range(gridsize[0])]

        # Tile Positions. Remains the same throughout. Is used to display
        self.tilepos = {(x, y): (x*(tilesize+margin)+margin, y*(tilesize+margin) +margin) for y in range(gridsize[1]) for x in range(gridsize[0])}  #tile position
        self.prev = None

        self.tile_images = []
        font = pygame.font.Font(None, 80)

        for i in range(self.tiles_no):
            # Create a Tile Image
            image = pygame.Surface((tilesize, tilesize))
            image.fill(brown)
            # Tile Number printed on screen
            text = font.render(str(i+1), 2, (255, 255, 255))

            width, height = text.get_size()
            # display number in the middle of tile
            image.blit(text, ((tilesize-width)/2, (tilesize-height)/2))
            self.tile_images += [image]

    def Blank_pos(self):
        return self.tiles[-1]

    def set_Blank_pos(self, pos):

        self.tiles[-1] = pos
    # get and set the pos of blank
    opentile = property(Blank_pos, set_Blank_pos)

    def switch_tile(self, tile):
        self.tiles[self.tiles.index(tile)] = self.opentile
        self.opentile = tile
        self.prev = self.opentile

    def check_in_grid(self, tile):
        return tile[0] >= 0 and tile[0] < self.gridsize[0] and tile[1] >=0 and tile[1] < self.gridsize[1]

    def close_to(self):
        x, y = self.opentile
        return (x-1, y), (x+1, y), (x, y-1), (x, y+1)

    def set_tile_randomly(self):
        adj = self.close_to()
        adj = [pos for pos in adj if self.check_in_grid(pos) and pos != self.prev]
        tile = random.choice(adj)
        self.switch_tile(tile)

    def update_tile_pos(self, dt):

        mouse = pygame.mouse.get_pressed()
        mpos = pygame.mouse.get_pos()

        if mouse[0]:
            x, y = mpos[0] % (self.tilesize+self.margin), mpos[1] % (self.tilesize + self.margin)
            if x > self.margin and y > self.margin:
                tile = mpos[0]//self.tilesize, mpos[1]//self.tilesize
                if self.check_in_grid(tile) and tile in self.close_to():
                    self.switch_tile(tile)

    def check_game_finish(self):
        rows, cols = self.gridsize
        curr_positions = [j*cols + i for i, j in self.tiles]
        # print(curr_positions, all([i == idx+1 for i, idx in enumerate(curr_positions)]))
        # If all positions are correct, return True, else return False
        return all([i == idx for i, idx in enumerate(curr_positions)])

    def draw_tile(self, gameDisplay):
        for i in range(self.tiles_no):
            x, y = self.tilepos[self.tiles[i]]
            gameDisplay.blit(self.tile_images[i], (x, y))


def level1():

    program = Generate_Puzzle((3, 3), 80, 5)
    start_time = time.time()
    success = False
    for i in range(100):
        program.set_tile_randomly()
    while True:
        dt = clock.tick()/1000
        time_remaining = int(180 - (time.time() - start_time))
        if time_remaining < 0:
            break
        gameDisplay.fill(WHITE)
        draw_text(gameDisplay, "Time Left:" + str(time_remaining), 90, WIDTH*0.75, HEIGHT*0.75)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            # program.events(event)
        program.update_tile_pos(dt)
        if program.check_game_finish():
            success = True
            break
    return draw_end_screen(success, time_remaining)


def level2():
    program = Generate_Puzzle((4, 4), 80, 5)
    start_time = time.time()
    success = False
    for i in range(100):
        program.set_tile_randomly()
    while True:
        dt = clock.tick()/1000
        time_remaining = int(180 - (time.time() - start_time))
        if time_remaining < 0:
            break
        gameDisplay.fill(WHITE)
        draw_text(gameDisplay, "Time Left:" + str(time_remaining), 90, WIDTH*0.75, HEIGHT*0.75)
        program.draw_tile(gameDisplay)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            # program.events(event)
        program.update_tile_pos(dt)
        if program.check_game_finish():
            success = True
            break
    return draw_end_screen(success, time_remaining)


# Generic method to draw fonts on the screen
font_name = pygame.font.match_font('comic.ttf')


def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, brown)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameDisplay.blit(text_surface, text_rect)


def draw_end_screen(result, time_remaining):
    gameDisplay.fill(WHITE)

    if result:
        result_text = "Game Won! Well Done  :)"
        score = 0.6
    else:
        result_text = "Better Luck Next Time :("
        score = 0.1

    if time_remaining > 0:
        time_text = "You took " + str(180 - time_remaining) + "seconds"
        if time_remaining > 80:
            score = 1
        else:
            score = score + (time_remaining)/100
    else:
        time_text = "Your time ran out"

    draw_text(gameDisplay, result_text, 70, WIDTH / 2, HEIGHT / 4)
    draw_text(gameDisplay, time_text, 70, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()

    time.sleep(2)
    pygame.quit()
    return score


def game_front_screen():
    gameDisplay.fill(WHITE)
    draw_text(gameDisplay, "Arrange the numbers in order!", 70, WIDTH / 2, HEIGHT / 4)
    draw_text(gameDisplay, "Press a key to begin!", 70, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


# ####mainloop

def start_game(level):
    try:
        game_front_screen()
        if level == 1:
            score = level1()
        elif level == 2:
            score = level2()
        print(score)
    except Exception as e:
        print(e)
        score = 0
    return score


if __name__ == "__main__":
    start_game(2)
