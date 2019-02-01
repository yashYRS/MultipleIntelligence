
import os
import sys
import random
import pygame
from pygame.locals import * #to add some of the constants and functions 


# constants
Window_Width = 500
Window_Height = 500
Background_Color = (255, 255, 255) #white 
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
BLACK = (0, 0, 0)
FPS = 40
Num_Random = 100


# exit
def Stop():
	pygame.quit()
	sys.exit()


# determine if the game is over
def isOver(board, blankCell, size):
	Num_Cell = size * size
	for i in range(Num_Cell-1):
		if board[i] != i:
			return False
	return True


# Move the Cell to the left of the blank Cell to the blank Cell position.
def moveR(board, blankCell, columns):
	if blankCell % columns == 0:
		return blankCell
	board[blankCell-1], board[blankCell] = board[blankCell], board[blankCell-1]
	return blankCell-1


# The Cell to the right of the blank Cell moves to the left of the blank Cell position.
def moveL(board, blankCell, columns):
	if (blankCell+1) % columns == 0:
		return blankCell
	board[blankCell+1], board[blankCell] = board[blankCell], board[blankCell+1]
	return blankCell+1


# Move the Cell above the blank Cell down to the blank Cell position
def MoveD(board, blankCell, columns):
	if blankCell < columns:
		return blankCell
	board[blankCell-columns], board[blankCell] = board[blankCell], board[blankCell-columns]
	return blankCell-columns


# Move the Cell under the blank Cell to the blank Cell position
def MoveU(board, blankCell, row, columns):
	if blankCell >= (row-1) * columns:
		return blankCell
	board[blankCell+columns], board[blankCell] = board[blankCell], board[blankCell+columns]
	return blankCell+columns


# Get the messy puzzle
def CreateBoard(row, columns, Num_Cell):
	board = []
	for i in range(Num_Cell):
		board.append(i)
	# Remove the block in the lower right corner
	blankCell = Num_Cell - 1
	board[blankCell] = -1
	for i in range(Num_Random):  #numrandom=100
		# 0: left
		# 1: right
		# 2: up
		# 3: down
		direction = random.randint(0, 3)
		if direction == 0:
			blankCell = moveL(board, blankCell, columns)
		elif direction == 1:
			blankCell = moveR(board, blankCell, columns)
		elif direction == 2:
			blankCell = MoveU(board, blankCell, row, columns)
		elif direction == 3:
			blankCell = MoveD(board, blankCell, columns)
	return board, blankCell


# Personal Selection
def GetImagePath(filepath):
	imgs = os.listdir(filepath)
	if len(imgs) == 0:
		print('[Error]: No pictures in filepath...')
	return os.path.join(filepath, random.choice(imgs))

#Show game and screen
def Show_End_Interface(Demo, width, height):
	Demo.fill(Background_Color)
	font = pygame.font.Font('./font/Roboto-Black.ttf', width//8)  #(Filename,size)create a new Font object from a file
	title = font.render('Congratulations !', True, (233, 150, 122)) #draw text on a new Surface
	

	rect = title.get_rect() #Returns a new rectangle covering the entire surface.
	rect.midtop = (width/2, height/2.5) #to move and align rect
	Demo.blit(title, rect) # draw one image onto another (source ,destination)
	pygame.display.update() #If no argument is passed it updates the entire Surface area
	pygame.time.wait(500) #pause
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				Stop()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					Stop()


# Display game start interface
def Show_Start_Interface(Demo, width, height ,img , imgrect):
	Demo.fill(Background_Color)
	tfont = pygame.font.Font('./font/Roboto-Black.ttf', width//8)
	cfont = pygame.font.Font('./font/Roboto-Black.ttf', width//40)
	title = tfont.render('Sliding Puzzle', True, Red)
	content1 = cfont.render('Press H or M or L to start the game', True, Blue)
	content2 = cfont.render('H is 5*5 mode, M is 4*4 mode, L is 3*3 mode', True, Blue)
	trect = title.get_rect()
	trect.midtop = (width/2, height/10)
	crect1 = content1.get_rect()
	crect1.midtop = (width/2, height/2.2)
	crect2 = content2.get_rect()
	crect2.midtop = (width/2, height/1.8)
	Demo.blit(title, trect)  #Draws a source Surface onto this Surface. 
	Demo.blit(content1, crect1)
	Demo.blit(content2, crect2)
	pygame.display.update()
	while True:
		size = None
		for event in pygame.event.get():
			if event.type == QUIT:
				Stop()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					Stop()
				if event.key == ord('l'):
					size = 3
					Demo.blit(img,imgrect)
					pygame.display.flip()
					pygame.time.delay(4000)
				elif event.key == ord('m'):
					size = 4
					Demo.blit(img,imgrect)
					pygame.display.flip()
					pygame.time.delay(4000)
				elif event.key == ord('h'):
					size = 5
					Demo.blit(img,imgrect)
					pygame.display.flip()
					pygame.time.delay(4000)
		if size:
			break
	return size


# main function
def main(filepath):

	#Initialization
	pygame.init()
	mainClock = pygame.time.Clock() # create an object to help track time
	#Loading images
	gameImg = pygame.image.load(GetImagePath(filepath)) # load new image from a file(create a surface object)
	ImgRect = gameImg.get_rect() #get the rectangular area of the Surface
	#Settings window
	Demo = pygame.display.set_mode((ImgRect.width, ImgRect.height)) # 	Initialize a window or screen for display
	pygame.display.set_caption('Sliding Puzzle')  #Set the current window caption

	# Start interface
	size = Show_Start_Interface(Demo, ImgRect.width, ImgRect.height,gameImg,ImgRect)
	if isinstance(size, int): #Boolean stating whether the object is an instance or subclass of another object
		row, columns = size, size
		Num_Cell = size * size
	else:
		print('[Error]: Parameter Size error...')
		Stop()
	# Does the game end?
	cellWidth = ImgRect.width // columns
	cellHeight = ImgRect.height // row
	
	over = False
	# Avoid initializing to the original image
	while True:
		gameBoard, blankCell = CreateBoard(row, columns, Num_Cell)
		if not isOver(gameBoard, blankCell, size):
			break
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				Stop()
			if over:
				Show_End_Interface(Demo, ImgRect.width, ImgRect.height)
			# Keyboard operation
			if event.type == KEYDOWN:
				if event.key == K_LEFT or event.key == ord('a'):
					blankCell = moveL(gameBoard, blankCell, columns)
				elif event.key == K_RIGHT or event.key == ord('d'):
					blankCell = moveR(gameBoard, blankCell, columns)
				elif event.key == K_UP or event.key == ord('w'):
					blankCell = MoveU(gameBoard, blankCell, row, columns)
				elif event.key == K_DOWN or event.key == ord('s'):
					blankCell = MoveD(gameBoard, blankCell, columns)
			# Mouse operation
			if event.type == MOUSEBUTTONDOWN and event.button == 1:  #left click
				x, y = pygame.mouse.get_pos() #The position is relative the the top-left corner of the display.
				x_pos = x // cellWidth
				y_pos = y // cellHeight
				idx = x_pos + y_pos * columns
				if idx==blankCell-1 or idx==blankCell+1 or idx==blankCell+columns or idx==blankCell-columns:
					gameBoard[blankCell], gameBoard[idx] = gameBoard[idx], gameBoard[blankCell]
					blankCell = idx
		if isOver(gameBoard, blankCell, size):
			gameBoard[blankCell] = Num_Cell-1
			over = True
		Demo.fill(Background_Color)
		for i in range(Num_Cell):
			if gameBoard[i] == -1:
				continue
			x_pos = i // columns
			y_pos = i % columns
			rect = pygame.Rect(y_pos*cellWidth, x_pos*cellHeight, cellWidth, cellHeight) #(left,top,width,height)
			#pygame object for storing rectangular coordinates. 
			ImgArea = pygame.Rect((gameBoard[i]%columns)*cellWidth, (gameBoard[i]//columns)*cellHeight, cellWidth, cellHeight)
			Demo.blit(gameImg, rect, ImgArea) #(src,dest,area) An optional area rectangle can be passed as well.
			# This represents a smaller portion of the source Surface to draw.
		for i in range(columns+1):
			pygame.draw.line(Demo, BLACK, (i*cellWidth, 0), (i*cellWidth, ImgRect.height)) #line(Surface, color, start_pos, end_pos) -> Rect
		for i in range(row+1):
			pygame.draw.line(Demo, BLACK, (0, i*cellHeight), (ImgRect.width, i*cellHeight))
		pygame.display.update()
		mainClock.tick(FPS)  # This can be used to help limit the runtime speed of a game.


if __name__ == '__main__':
	filepath = './pictures'
	main(filepath)