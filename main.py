import time
from turtle import Screen, Turtle
from snake_body import Snake_Body
from food import Food
from scoreboard import Scoreboard

#setting up screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

#tracer(0) block (freeze) the automatic loading of the screen untill user don't reactive it
screen.tracer(0)

snake = Snake_Body()
food = Food()
scoreboard = Scoreboard()

#untill there is specified condition continue with the game, unless stop the programm
game_is_on = True
while game_is_on:

    screen.update() #screen.update() reattivated the screen tracer block, that i applied before
    time.sleep(0.1)
    snake.move()
    scoreboard.upgrade_scoreboard()

    #collision with food
    if snake.head.distance(food) < 15:
        print("gnam gnam gnam")
        scoreboard.increase_score()
        snake.extend()
        food.reflesh()
    #collision with wall
    if (snake.head.xcor() > 290) or (snake.head.xcor() < -290) or\
            (snake.head.ycor() > 290) or (snake.head.ycor() < -290):
        scoreboard.game_over()
        game_is_on = False

    #Detect colision with tail

    for element in snake.segments[1:]:
        if element.distance(snake.head) < 15:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()