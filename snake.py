from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    # Initialisation of snake
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.tail = self.segment[1:2]
        self.speed = 0.5

    # Creating the base snake
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segment.append(new_segment)

    # Makes the snake move smoothly replacing the seg in front of the current seg
    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

    # Adding a new segment to extend the snake when snake eats food
    def addseg(self):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.speed("fastest")
        new_x = self.segment[len(self.segment) - 1].xcor()
        new_y = self.segment[len(self.segment) - 1].ycor()
        new_segment.goto(new_x, new_y)
        new_segment.color("white")
        self.segment.append(new_segment)
        self.update_speed()

    # Everytime snake gets longer the refresh time gets smaller making the snake faster
    def update_speed(self):
        self.speed = self.speed/2

    # Checks if snake is currently moving down if not changes direction to up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Checks if snake is currently moving up if not changes direction to down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Checks if snake is currently moving right if not changes direction to left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Checks if snake is currently moving left if not changes direction to right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
