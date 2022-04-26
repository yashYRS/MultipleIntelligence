import os
import random
import time
import turtle
import tkinter as T


def exitfunc():
    return


class Sprite(turtle.Turtle):
    # turtles act as sprites(objects on the screen)
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        # speed of animation, 0 is the fastest
        self.speed(0)
        # sprites wont draw anything on the screen
        self.penup()
        self.color(color) 
        # to make it appear
        self.fd(0)
        # go to the starting point
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        # move the sprite forward at its speed
        self.fd(self.speed)

    # Boundary detection
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)  
        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self, other ):
        if(self.xcor() >= (other.xcor() -20)) and \
        (self.xcor() <= (other.xcor() +20)) and \
        (self.ycor() >= (other.ycor() -20)) and \
        (self.ycor() <= (other.ycor() +20)) :
            return True
        else:
            return False


class Player(Sprite):  

    def __init__(self, spriteshape, color, startx, starty, player_speed):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = player_speed
        #self.lives = 3

    def turn_left(self):
        self.lt(25)

    def turn_right(self):
        self.rt(25)


class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty, enemy_speed):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = enemy_speed
        # random heading when it starts
        self.setheading(random.randint(0, 360))


class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty, ally_speed):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = ally_speed
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)
        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)
        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)


class Cannon(Sprite):
    def __init__(self, spriteshape, color, startx, starty, player):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        # make it shorter than others
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"
        self.player = player
        # starts off the screen
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            # Play cannon sound
            os.system("aplay Laser.wav&")
            self.goto(self.player.xcor(), self.player.ycor())
            self.setheading(self.player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.goto(-1000, 1000)
        if self.status == "firing":
            self.fd(self.speed)   #go forward

    # Border check
        if self.xcor() < -290 or self.xcor() > 290 or \
            self.ycor() < -290 or self.ycor() > 290:                 
            self.goto(-1000, 1000)              #take it off the screen
            self.status = "ready"


class EnemyCannon(Sprite):
    def __init__(self, spriteshape, color, startx, starty, enemy_canon_speed, player):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.status = "ready"
        self.speed = enemy_canon_speed
        self.heading_offset = 0
        self.player = player

    def fire(self, startx, starty, heading):
        if self.status == "ready":
            self.status = "shoot"
            self.goto(startx, starty)
            #self.setheading(heading)
            #Get heading to Player
            px = self.player.xcor()
            py = self.player.xcor()
            heading = 0
            if px > self.xcor() and py > self.ycor():
                heading = random.randint(25, 65)
            elif px < self.xcor() and py > self.ycor():
                heading = random.randint(115, 155)
            if px > self.xcor() and py < self.ycor():
                heading = random.randint(195, 335)
            if px < self.xcor() and py < self.ycor():
                heading = random.randint(200, 245)
                
            self.setheading(heading)
                        
    def move(self):
        if self.status == "ready":
            self.hideturtle()
            #Move the turtle offscreen
            self.goto(-1000,1000)
            
        
        if self.status == "shoot":
           # os.system("aplay missile.mp3&")
            self.showturtle()
            self.status = "firing"
                
        if self.status == "firing":
            self.fd(self.speed)
        
        #Border Check   
        if self.xcor() < -290 or self.xcor() > 290 \
            or self.ycor() < -290 or self.ycor() > 290:
            self.status = "ready"           


class Particle(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000, -1000)
        self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0,360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > 15:
            self.frame = 0
            self.goto(-1000, 1000)
        #border check
        if self.xcor() < -290 or self.xcor() > 290 \
            or self.ycor() < -290 or self.ycor() > 290:
            self.frame = 0
            self.goto(-1000, -1000)


class Game():
    # game object to draw the info on the screen
    def __init__(self):
        self.level = 1
        self.state = "playing"
        self.score = 0
        # create a new turtle to draw things
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        #Draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):  
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()   
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        if self.lives > 0:
            msg = "Level: %s   Lives: %s   Score: %s" %(self.level, self.lives, self.score)
        else:
            msg = "Game Over ! Score : %s" %(self.score)
        self.pen.penup() #not draw anything
        self.pen.goto(-110, 310)
        self.pen.write(msg, font=("Arial", 16, "normal")) 

    def show_splash(self):
        turtle.bgpic("splash8.png")
        turtle.update()
        time.sleep(6)
        turtle.bgpic("starfield.gif")
        self.state = "setup"


def game_loop(player_speed, ally_speed, enemy_speed, enemy_canon_speed):
    window = turtle.Screen()
    window.screensize()
    window.setup(width=1.0, height=1.0, startx=None, starty=None)

    # creating the actual screen (required by macos)
    turtle.fd(0)
    # control the speed of animation
    turtle.speed(0)
    turtle.bgcolor("black") 
    turtle.bgpic("splash8.png")
    turtle.title("Space War")
    turtle.ht()
    # limits the amount of memory the turtle module uses (saves the memory)
    turtle.setundobuffer(1)
    # limits the amount of memory the turtle module uses (saves the memory)
    turtle.tracer(0)

    gscore = 0
    nscore = 0
    lives = 3
    mins = 0

    # Register shapes
    turtle.register_shape("enemy.gif")
    turtle.register_shape("ally.gif")

    # Create game object
    game = Game()

    # Draw the game border
    game.draw_border()

    # Show the game show_status
    game.show_status()

    game.show_splash()

    if game.state == "setup":
        # Create my sprites
        player = Player("triangle", "white", 0, 0, player_speed=player_speed)
        # enemy = Enemy("circle", "red", -100, 0)
        cannon = Cannon("triangle", "yellow", 0, 0, player=player)
        # ally = Ally("square", "blue", 100, 0)
        enemycannon = EnemyCannon("triangle", "red", 0.0, 0.0,
                                  enemy_canon_speed=enemy_canon_speed,
                                  player=player)

        enemies = []
        for i in range(4):
            enemies.append(Enemy("enemy.gif", "red", -100, 0, enemy_speed=enemy_speed))

        allies = []
        for n in range(2):
            allies.append(Ally("ally.gif", "blue", 100, 0, ally_speed=ally_speed))

        particles = []
        for i in range(20):
            particles.append((Particle("circle", "orange", 0, 0)))

    # Keyboard bindings
    turtle.onkey(player.turn_left, "Left")
    turtle.onkey(player.turn_right, "Right")
    # turtle.onkey(player.accelarate, "Up")
    # turtle.onkey(player.decelarate, "Down")
    turtle.onkey(cannon.fire, "space")
    # to listen to the key presses
    turtle.listen()

    start_time = time.time()
    # Main game loop
    while True:
        # stops the updating until we get here
        if time.time() - start_time > 40:
            return gscore, lives
        turtle.update()
        time.sleep(0.02)

        player.move()
        enemycannon.move()

        # Check Collision for enemy cannon
        if player.is_collision(enemycannon):
            enemycannon.status = "ready"
            # os.system("aplay explosion.mp3&")
            player.color("red")
            for particle in particles:
                particle.explode(player.xcor(), player.ycor())
            player.rt(random.randint(100, 200))
            game.lives -= 1
            game.score -= 50
            gscore -= 5
            if game.lives < 1:
                game.state = "gameover"
            game.show_status()
            player.color("white")

        cannon.move()
        for enemy in enemies:
            enemy.move()

            # Check for collision with player
            if player.is_collision(enemy):
                # os.system("aplay explosion.mp3&")
                player.color("red")
                for particle in particles:
                    particle.explode(enemy.xcor(), enemy.ycor())
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                enemy.goto(x, y)
                game.score -= 50
                gscore -= 5
                game.lives -= 1
                if game.lives < 1:
                    game.state = "gameover" 
                game.show_status()
                player.color("white")

            # Check for collision between the cannon and the enemy
            if cannon.is_collision(enemy):
                # os.system("aplay explosion.mp3&")
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                enemy.goto(x, y)
                cannon.status = "ready"
                # Increase the score
                game.score += 100
                gscore += 10
                game.show_status()
                # Do the explosion
                for particle in particles:
                    particle.explode(cannon.xcor(), cannon.ycor())

            # Fire bullet at player
            if random.randint(1, 1200/game.level) == 1:
                if enemycannon.status == "ready":
                    enemycannon.fire(enemy.xcor(), enemy.ycor(), enemy.heading())

        for ally in allies:
            ally.move()
            # Check for collision between the cannon and the ally
            if cannon.is_collision(ally):
                #  os.system("aplay explosion.mp3&")
                for particle in particles:
                    particle.explode(ally.xcor(), ally.ycor())
                x = random.randint(-250, 250)
                y = random.randint(-250, 250)
                ally.goto(x, y)
                cannon.status = "ready"
                # Decrease the score
                game.score -= 50
                gscore -= 5
                game.show_status()

        for particle in particles:
            particle.move()

        if game.state == "gameover":
            return gscore, lives
    return gscore


def start_game(level):
    game_score = 0
    if level == 1:
        player_speed = 3
        enemy_speed = 4
        ally_speed = 3
        enemy_canon_speed = 8
    elif level == 2:
        player_speed = 4
        enemy_speed = 4
        ally_speed = 4
        enemy_canon_speed = 8
    elif level == 3:
        player_speed = 5
        enemy_speed = 5
        ally_speed = 4
        enemy_canon_speed = 10

    try:

        game_score, lives = game_loop(player_speed, ally_speed, enemy_speed, enemy_canon_speed)
        if game_score < 0:
            return 0.1
        if lives > 0:
            game_score = game_score*lives
        if game_score > 500:
            return 0.95
        else:
            return game_score/500

    except Exception as e:
        print(e)
    return game_score


if __name__ == "__main__":
    score = start_game(3)
    print("Score - ", score)
