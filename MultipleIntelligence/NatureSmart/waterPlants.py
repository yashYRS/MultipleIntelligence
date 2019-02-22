import random
import arcade
import time

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GRASS = 1
SPRITE_SCALING_DEAD_GRASS = 1
SPRITE_SCALING_KNIFE= 0.2
GRASS_COUNT = 15
DEAD_GRASS_COUNT = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 4
BULLET_SPEED = 5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Manage Farm" , fullscreen = True )

        # Variables that will hold sprite listss
        self.player_list = None
        self.grass_list = None
        self.knife_list = None
        width, height = self.get_size() 
        self.set_viewport(0,width, 0 , height)
        print(width,height)
        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.grass_list = arcade.SpriteList()
        self.knife_list = arcade.SpriteList()
        self.dead_grass_list = arcade.SpriteList()
        # Set up the player
        self.score = 0

        # Image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0
        self.player_list.append(self.player_sprite)

        left, screen_width, bottom , screen_height = self.get_viewport()
        # Create the grasss
        for i in range(GRASS_COUNT):

            # Create the grass instance
            # Coin image from kenney.nl
            grass = arcade.Sprite("grass.jpg", SPRITE_SCALING_GRASS)

            # Position the grass
            grass.center_x = random.randrange(screen_width)
            grass.center_y = random.randrange(120, screen_height)

            # Add the grass to the lists
            self.grass_list.append(grass)

        # Create the dead grasss
        for i in range(DEAD_GRASS_COUNT):

            # Create the grass instance
            # Coin image from kenney.nl
            deadgrass = arcade.Sprite("deadGrass.jpg", SPRITE_SCALING_DEAD_GRASS)

            # Position the grass
            deadgrass.center_x = random.randrange(screen_width)
            deadgrass.center_y = random.randrange(120, screen_height)

            # Add the grass to the lists
            self.dead_grass_list.append(deadgrass)           
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
        self.knife_list.draw()
        self.player_list.draw()

        # Render the text
        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = - MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y =  MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = - MOVEMENT_SPEED
            
    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0


    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called whenever the mouse button is clicked.
        """

        # Create a knife
        knife = arcade.Sprite("knife.png", SPRITE_SCALING_KNIFE)

        # The image points to the right, and we want it to point up. So
        # rotate it.

        # Position the knife
        knife.center_x = self.player_sprite.center_x + 35
        knife.bottom = self.player_sprite.center_y - 30

        # Add the knife to the appropriate lists
        self.knife_list.append(knife)

    def update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites
        self.grass_list.update()
        self.knife_list.update()
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

        # Loop through each knife
        for knife in self.knife_list:

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


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
