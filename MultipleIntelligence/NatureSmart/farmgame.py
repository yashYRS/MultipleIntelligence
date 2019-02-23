import random
import arcade
import time

SPRITE_SCALING_PLAYER = 0.6
SPRITE_SCALING_DEAD_GRASS = 0.3
SPRITE_SCALING_WASTE_HARM = 0.15
SPRITE_SCALING_KNIFE= 0.2
SPRITE_SCALING_TRASH= 0.3
SPRITE_SCALING_SAPLING= 0.2
SPRITE_SCALING_BROOM= 0.05

DEAD_GRASS_COUNT = 15
WASTE_HARM_COUNT = 5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BROOM_SPEED = 3
MOVEMENT_SPEED = 4
BULLET_SPEED = 5
EQUIPMENT = [ ['knife.png', SPRITE_SCALING_KNIFE, 0 ] ,  ['broom.png' ,SPRITE_SCALING_BROOM , 300] , ['grass.png' , SPRITE_SCALING_SAPLING , 0] ]
## image source , scale , angle of rendering

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Manage Farm" , fullscreen = True )

        # Variables that will hold sprite listss
        self.player_list = None
        self.grass_list = None
        self.wasteHarm_list = None
        self.equipment_list = None
        self.plant_sapling_list = None
        width, height = self.get_size() 
        self.set_viewport(0,width, 0 , height)
        print(width,height)
        # Set up the player info
        self.dustBin_sprite = None
        self.changeScreen = False
        self.player_sprite = None
        self.score = 0
        self.initialTime = 0 
        self.curr_equip = 0 
        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.grass_list = arcade.SpriteList()
        self.equipment_list = arcade.SpriteList()
        self.plant_sapling_list = arcade.SpriteList() 
        self.wasteHarm_list = arcade.SpriteList()
        self.static_objects_list = arcade.SpriteList() 
        # Set up the player
        self.score = 0
        self.initialTime = time.time()
        self.curr_equip = 1 
        left, screen_width, bottom , screen_height = self.get_viewport()
        
        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("characterRight.png", SPRITE_SCALING_PLAYER)
        for i in range(2) : 
            self.dustBin_sprite = arcade.Sprite("trash.png", SPRITE_SCALING_TRASH)
            self.dustBin_sprite.center_x = left + i*(screen_width - 600) + 300
            self.dustBin_sprite.center_y = bottom + i*(screen_height - 600) + 300
            self.static_objects_list.append(self.dustBin_sprite)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0  
        self.player_list.append(self.player_sprite)

        # Create the grasss
        for i in range(DEAD_GRASS_COUNT):

            # Create the grass instance
            # Coin image from kenney.nl
            grass = arcade.Sprite("deadgrass.png", SPRITE_SCALING_DEAD_GRASS)

            # Position the grass
            grass.center_x = random.randrange(screen_width)
            grass.center_y = random.randrange(120, screen_height)

            # Add the grass to the lists
            self.grass_list.append(grass)

        # Create the dead grasss
        for i in range(WASTE_HARM_COUNT):

            # Create the grass instance
            # Coin image from kenney.nl
            wasteHarm = arcade.Sprite("waste.png", SPRITE_SCALING_WASTE_HARM)

            # Position the grass
            wasteHarm.center_x = random.randrange(screen_width)
            wasteHarm.center_y = random.randrange(120, screen_height)
            wasteHarm.change_x = 0 
            wasteHarm.change_y = 0 
            # Add the grass to the lists
            self.wasteHarm_list.append(wasteHarm)           
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.grass_list.draw()
        self.wasteHarm_list.draw() 
        self.equipment_list.draw()
        self.plant_sapling_list.draw() 
        self.player_list.draw()
        self.static_objects_list.draw() 
        # Render the text
        arcade.draw_text(f"Time Remaining: {120 - int(time.time() - self.initialTime)}", 10, 40, arcade.color.WHITE, 14)
        if 120 - int(time.time() - self.initialTime) < 1 : 
            exit(0)
            


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = - MOVEMENT_SPEED - 1 
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED + 1 
        elif key == arcade.key.UP:
            self.player_sprite.change_y =  MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = - MOVEMENT_SPEED        
        elif key == arcade.key.SPACE :
            ind = self.curr_equip
            equip_sprite = arcade.Sprite(EQUIPMENT[ind][0], EQUIPMENT[ind][1])
            # Position the equipment
            equip_sprite.center_x = self.player_sprite.center_x + 25
            equip_sprite.center_y = self.player_sprite.center_y - 30
            equip_sprite.angle = EQUIPMENT[ind][2]
            # Add the equipment to the appropriate lists
            if ind == 2 : 
                self.plant_sapling_list.append(equip_sprite)
            else : 
                self.equipment_list.append(equip_sprite)

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0

        elif key == arcade.key.SPACE : 
            for equip in self.equipment_list : 
                equip.kill()
        elif key == arcade.key.S : 
            self.curr_equip = (self.curr_equip +1)%len(EQUIPMENT)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """
        

    def update(self, delta_time):
        """ Movement and game logic """
    
        self.grass_list.update()
        self.wasteHarm_list.update() 
        self.equipment_list.update()
        self.plant_sapling_list.update()
        self.player_sprite.center_x = self.player_sprite.center_x + self.player_sprite.change_x
        self.player_sprite.center_y = self.player_sprite.center_y + self.player_sprite.change_y

       	left, screen_width, bottom , screen_height = self.get_viewport() 
       	
       	if self.player_sprite.center_x < left + 10 :
            self.player_sprite.center_x = 10

        if self.player_sprite.center_x > screen_width - 10:
            self.player_sprite.center_x = screen_width - 10

        if self.player_sprite.center_y < 20:
            self.player_sprite.center_y = 20

        if self.player_sprite.center_y > screen_height - 20:
            self.player_sprite.center_y = screen_height - 20

        if arcade.check_for_collision(self.player_sprite , self.dustBin_sprite) :
            self.player_sprite.change_x = -self.player_sprite.change_x
            self.player_sprite.change_y = -self.player_sprite.change_y
            # self.openStore = True
            # self.changeScreen = True

        for grass in self.grass_list: 
            destroy_list = arcade.check_for_collision_with_list(grass, self.static_objects_list)
            
            if len(destroy_list) > 0 : 
                grass.kill() 

        for wasteHarm in self.wasteHarm_list : 
            destroy_list = arcade.check_for_collision_with_list(wasteHarm, self.static_objects_list)
            if len(destroy_list) > 0 : 
                wasteHarm.kill() 

        # Loop through each knife
        for equip in self.equipment_list:
            if self.curr_equip == 0 : 
                knife = equip 
            # Check this knife to see if it hit a grass
                hit_list = arcade.check_for_collision_with_list(knife, self.grass_list)

                # If it did, get rid of the knife
                if len(hit_list) > 0:
                    knife.kill()

                # For every grass we hit, add to the score and remove the grass
                for grass in hit_list:
                    grass.kill()
                    self.score += 1

                # If the knife flies off-screen, remove it.
                if knife.bottom > SCREEN_HEIGHT:
                    knife.kill()
            
            elif self.curr_equip == 1 : 
                broom = equip 
                move_list = arcade.check_for_collision_with_list(broom , self.wasteHarm_list) 
                for waste in move_list : 
                    if waste.center_x < broom.center_x : 
                        waste.center_x = waste.center_x - BROOM_SPEED
                    else : 
                        waste.center_x = waste.center_x + BROOM_SPEED 
                    if waste.center_y < broom.center_y : 
                        waste.center_y = waste.center_y - BROOM_SPEED 
                    else : 
                        waste.center_y = waste.center_y + BROOM_SPEED 

            elif self.curr_equip == 2 : 
                sapling = equip 


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
