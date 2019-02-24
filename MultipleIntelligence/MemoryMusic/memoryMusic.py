import random
import arcade
import time
import traceback 
## -- Sprite scaling factors -- ## 
SPRITE_SCALING_BLACK = 0.5
SPRITE_SCALING_CUBE = 0.5
SPRITE_SCALING_TILE = 0.5
### -- End -- ## 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCALE_CAR = 0.2
SCALE_COIN = 0.2
SCALE_BELL = 0.2
SCALE_STAPLE = 0.2
SCALE_STEPS = 0.2
SCALE_HAMMER = 0.2
SCALE_GUN = 0.2
SCALE_CUBE = 0.2
SCALE_ROBOT = 0.2
SCALE_PUNCH = 0.2
SCALE_WAVES = 0.2
## image source , scale , angle of rendering

DATA = [ [arcade.Sprite('data/carskid.jpeg', SCALE_CAR ), arcade.load_sound('data/carskid.mp3') , arcade.Sprite('data/carskid.jpeg', SCALE_CAR )] ,\
 	[arcade.Sprite('data/coins.jpeg', SCALE_COIN) , arcade.load_sound('data/coins.wav')  ,arcade.Sprite('data/coins.jpeg', SCALE_COIN)] ,\
	 [arcade.Sprite('data/doorbell.jpg', SCALE_BELL) , arcade.load_sound('data/doorbell.mp3'),arcade.Sprite('data/doorbell.jpg', SCALE_BELL)] , \
 	[arcade.Sprite('data/staple.jpg', SCALE_STAPLE) , arcade.load_sound('data/staple.mp3'),arcade.Sprite('data/staple.jpg', SCALE_STAPLE)] ,\
	[arcade.Sprite('data/hammer.jpeg', SCALE_HAMMER) , arcade.load_sound('data/hammer.mp3'),arcade.Sprite('data/hammer.jpeg', SCALE_HAMMER)] ,\
 	[arcade.Sprite('data/icecubes.jpeg', SCALE_CUBE) , arcade.load_sound('data/icecubes.wav'),arcade.Sprite('data/icecubes.jpeg', SCALE_CUBE)] , \
 	[arcade.Sprite('data/machinegun.jpeg', SCALE_GUN) , arcade.load_sound('data/machinegun.wav'),arcade.Sprite('data/machinegun.jpeg', SCALE_GUN)] ,\
 	[arcade.Sprite('data/robot.jpeg', SCALE_ROBOT) , arcade.load_sound('data/robot.mp3'),arcade.Sprite('data/robot.jpeg', SCALE_ROBOT)] ,\
 	[arcade.Sprite('data/waves.jpeg', SCALE_WAVES) , arcade.load_sound('data/waves.mp3'),arcade.Sprite('data/waves.jpeg', SCALE_WAVES)]
 	]
class MyGame(arcade.Window):
	""" Main application class. """

	def __init__(self):
		""" Initializer """
		# Call the parent class initializer
		super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Manage Farm" )

		# Variables that will hold sprite listss
		self.curr_state = "Instructions"
		width, height = self.get_size() 
		self.set_viewport(0,width, 0 , height)
		self.level_tile_mapping = None 
		self.tiles_in_row = None 
		self.opened = 0 
		self.sound_of_first = -1

		# individual sprites 
		self.temp_sprite_list = None 
		self.object_sound = None 
		self.object_sprite = None 
		self.object_sprite_list = None
		self.cube_sprite = None 
		
		## Sprite lists 
		self.object_sounds = []
		self.cube_sprites = None 
		self.cube_sprites_dict = {}
		self.picture_sprites = None
		self.picture_sprites_another = None
		self.first_cube = None
		self.first_cube_id = -1  
		self.map_sounds = {}
		self.normalize = 0 
		arcade.set_background_color(arcade.color.BLACK)

	def setup(self , level):

		""" Set up the game and initialize the variables. """

		# Sprite lists

		self.score = 0
		self.curr_state = "Instructions"
		self.initialTime = time.time()

		self.level_tile_mapping = [2,3]
		self.tiles_in_row = self.level_tile_mapping[level-1]

		left, screen_width, bottom , screen_height = self.get_viewport()
		
		self.temp_sprite_list = arcade.SpriteList()
		self.cube_sprites = arcade.SpriteList()
		self.object_sprite_list = arcade.SpriteList() 
		self.cube_sprites_dict = {}
		self.picture_sprites = arcade.SpriteList()
		self.picture_sprites_another = arcade.SpriteList() 
		for i in range( len(DATA) ) : 
			self.object_sounds.append(DATA[i][1])
			self.picture_sprites.append(DATA[i][0])
			self.picture_sprites_another.append(DATA[i][2])

		fraction = self.tiles_in_row + 2 
		addX = (screen_width - left)/fraction
		addY = (screen_height - bottom)/(self.tiles_in_row+1)

		SPRITE_SCALING_CUBE = 0.3
		
		total = int(self.tiles_in_row*(self.tiles_in_row+1)) 
		done = [False for i in range(total) ]
		self.normalize = total/2

		for rowID in range(1,self.tiles_in_row + 1) : 
			for colID in range(1,self.tiles_in_row+2) :
				self.cube_sprite = arcade.Sprite("cube.png" , SPRITE_SCALING_CUBE )
				self.cube_sprite.center_x = colID*addX
				self.cube_sprite.center_y = rowID*addY
				self.cube_sprites.append(self.cube_sprite)
				## set up a mapping from a square to a sound 
				ID = (rowID-1)*(self.tiles_in_row + 1) + colID - 1
				self.cube_sprites_dict[ID] = self.cube_sprite
				index_sound = random.choice( range(len(DATA)) ) # take some random sound 
				
				while True and False in done:
					index1_cube = random.choice( range(total) )
					if not done[index1_cube] : 
						index2_cube = random.choice( range(total) )
						if not done[index2_cube] and not index1_cube == index2_cube  : 
							done[index1_cube] = True
							done[index2_cube] = True
							self.map_sounds[index1_cube] = index_sound
							self.map_sounds[index2_cube] = index_sound
							break
		arcade.set_background_color(arcade.color.BLACK)

	def draw_instructions(self) : 
		left, screen_width, bottom , screen_height = self.get_viewport() 
		midX = (left + screen_width)/2
		midY = (bottom + screen_height)/2
		### -- Change the Instructions to be displayed -- ### 
		arcade.draw_text(f" INSTRUCTIONS ", midX/2 + 100 , 6*(screen_height - bottom)/7 , arcade.color.YELLOW , 40)
		arcade.draw_text(f" Basic Memory Game  ", midX/2, 5*(screen_height - bottom)/7 , arcade.color.YELLOW , 30)
		arcade.draw_text(f" Basic rules " ,midX/2, 4*(screen_height - bottom)/7, arcade.color.YELLOW , 30 )
		arcade.draw_text(f" Some more shit  " ,midX/2, 3*(screen_height - bottom)/7, arcade.color.YELLOW , 30 )
		arcade.draw_text(f" Final Shit  " ,midX/2, 2*(screen_height - bottom)/7 , arcade.color.YELLOW , 30)
		arcade.draw_text(f" That's about it " ,midX/2 + 150 , 1*(screen_height - bottom)/7 , arcade.color.YELLOW , 15)



	def draw_game(self): 
		# Draw all the sprites.


		self.cube_sprites.draw() 
		self.object_sprite_list.draw() 
		# Render the text
		arcade.draw_text(f"Time Remaining: {60 - int(time.time() - self.initialTime)}", 10, 40, arcade.color.WHITE, 14)
		curr_time = 50 - int(time.time() - self.initialTime)
		if curr_time < 1 or self.score == self.normalize : 
			self.score = ((50 - curr_time)/50)*0.3 + (self.score*0.7)/self.normalize
			print(self.score)
			exit(0)
			#self.curr_state = "GameOver


	def on_draw(self):
		"""
		Render the screen.
		"""
		# This command has to happen before we start drawing
		arcade.start_render()
		if self.curr_state == "Instructions" : 
			self.draw_instructions()
		elif self.curr_state == "Game" : 
			self.draw_game()
		elif self.curr_state == "GameOver" : 
			self.draw_end_screen() 


	def on_key_release(self, key, modifiers):
		""" Called whenever a user releases a key. """
		if key == arcade.key.SPACE : 
			if self.curr_state == "Instructions" : 
				self.curr_state = "Game"




	def on_mouse_press(self, x, y, button, modifiers):
		"""
		Called whenever the mouse button is clicked.
		"""
		temp_spr = arcade.Sprite('temp.jpeg', 0.01)
		temp_spr.center_x = x
		temp_spr.center_y = y       
		

		self.temp_sprite_list.append(temp_spr)

	def update(self, delta_time):
		""" Movement and game logic """
		left, screen_width, bottom , screen_height = self.get_viewport() 
		self.cube_sprites.update() 
		self.object_sprite_list.update() 
		del_flag = False
		for ID in self.cube_sprites_dict : 
			cube = self.cube_sprites_dict[ID]
			hit_list = arcade.check_for_collision_with_list(cube, self.temp_sprite_list)
			del_flag = False
			if len(hit_list) > 0  : 
				for spr in self.temp_sprite_list : 
					spr.kill() 
				self.opened = self.opened + 1 
				soundID = self.map_sounds[ID]
				try:
					arcade.play_sound(self.object_sounds[soundID])
					time.sleep(0.1)
				except Exception as e:
					pass 
				if self.opened == 2 : 
					if soundID == self.sound_of_first and not ID==self.first_cube_id :  ## no match 
						cube.kill() 
						self.first_cube.kill() 
						del_flag = True 
						to_del = [ID ,self.first_cube_id]
						self.opened = 0 
						self.score = self.score + 1 
					else : 
						self.opened = 1
						self.sound_of_first = soundID 
						self.first_cube = cube
						self.first_cube_id = ID 
				else : 
					self.sound_of_first = soundID 
					self.first_cube = cube 
					self.first_cube_id = ID 
		if del_flag : 
			del self.cube_sprites_dict[ID]
			del self.cube_sprites_dict[self.first_cube_id]			

def main():
	level = int(input("Enter level - "))
	window = MyGame()
	window.setup(level)
	arcade.run()


if __name__ == "__main__":
	main()
