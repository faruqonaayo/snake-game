from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Segment:
    def __init__(self, x, y):
        self.turtle = Turtle("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.goto(x, y)

class Snake:
    def __init__(self):
        self.segments = []
        self.head = None

    def create(self):
        for n in range(3):
            seg_x_position = n * -MOVE_DISTANCE
            new_segment = Segment(seg_x_position, 0)
            self.segments.append(new_segment)

        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_cor = self.segments[seg_num - 1].turtle.pos()
            self.segments[seg_num].turtle.goto(new_cor)
        self.segments[0].turtle.forward(MOVE_DISTANCE)

    def up(self):
        snake_head = self.segments[0].turtle
        if snake_head.heading() != DOWN:
            snake_head.setheading(UP)

    def down(self):
        snake_head = self.segments[0].turtle
        if snake_head.heading() != UP:
            snake_head.setheading(DOWN)

    def left(self):
        snake_head = self.segments[0].turtle
        if snake_head.heading() != RIGHT:
            snake_head.setheading(LEFT)

    def right(self):
        snake_head = self.segments[0].turtle
        if snake_head.heading() != LEFT:
            snake_head.setheading(RIGHT)

    def eat(self):
        last_seg_position = self.segments[-1].turtle.position()
        self.segments.append(Segment(last_seg_position[0], last_seg_position[1]))

    def reset(self):
        for seg in self.segments:
            seg.turtle.goto(1000, 1000)
        self.segments.clear()
        self.create()