from  turtle import  Screen
import time

import snake
from food import Food
from scoreboard import Scoreboard
from snake import  Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


my_snake = Snake()
my_snake.create()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.tracer(0)
    my_snake.move()
    screen.update()
    time.sleep(0.1)

    # detect collision with food
    if my_snake.head.turtle.distance(food) < 15:
        my_snake.eat()
        scoreboard.increase_score()
        food.refresh()

    # detect collision with wall
    if (my_snake.head.turtle.xcor() > 280 or my_snake.head.turtle.xcor() < -280
            or my_snake.head.turtle.ycor() > 280 or my_snake.head.turtle.ycor() < -280):
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for seg in my_snake.segments[1:]:
        if my_snake.head.turtle.distance(seg.turtle) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()