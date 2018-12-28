import turtle
import math
import random
import winsound
                                                                           #background
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")
#Register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

                                                                            #Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

                                                                            #SET THE SCORE TO 0
score = 0
#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 300)
scorestring = "score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()
                                                                            #Create the player turtle
player =turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -280)
player.setheading(90)

playerspeed = 40

                                #choose the number of enemies
number_of_enemies = 5
                                #Create an empty list of enemies
enemies = []
                                # Add enemies to the list
for i in range(number_of_enemies):
                                                                            # Create the enemy
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("green")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    enemy.setposition(-200, 200)
    enemy.shapesize(2, 2)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

enemyspeed = 4

                                                                            #Create the player's bullet
bullet = turtle.Turtle()
bullet.color("white")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 55

                #Define bullet state
                #ready-ready to fire
                #fire - bullet is firing
bulletstate = "ready"


                #move the player left
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

                #move the player right
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate                                                      #global  here!
    if bulletstate == "ready":
        winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
                #Move the bullet
        x = player.xcor()
        y = player.ycor() + 5
        bullet.setposition(x, y + 5)
        bullet.showturtle()


                #key bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


def isCollision(t1, t2):
    distance = math.hypot(t1.xcor() - t2.xcor(), t1.ycor()-t2.ycor())
    if distance < 25:
        return True
    else:
        return False

                                                                            #Main game loop
while True:

    for enemy in enemies:                                  #Move the enemies
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

                                        #Enemy boundaries and reverse movement
        if enemy.xcor() > 280:
            #Moves all of the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if enemy.xcor() < -280:
            # Moves all of the enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
            # Check for collision bullet-enemy

        if isCollision(bullet, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            # reset the bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            #update the score
            score += 100
            scorestring = "score %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, enemy):
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy.hideturtle()
            print("game over")
            break

                                    #Move the bullet once fired
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)
                                    # Check to see if the bullet has reached the top
    if bullet.ycor() > 285:
         bullet.hideturtle()
         bulletstate = "ready"






wn.mainloop()
#so the program runs on 3.6