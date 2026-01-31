from turtle import Screen, Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("green")
        self.speed("fastest")
        self.goto(randint(-250, 250), randint(-250, 250))

    def refresh(self):
        self.goto(randint(-250, 250), randint(-250, 250))