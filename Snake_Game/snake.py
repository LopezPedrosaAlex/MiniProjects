from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.tail = self.snake_body[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_part = Turtle()
            snake_part.color("green")
            snake_part.shape("square")
            snake_part.penup()
            snake_part.goto(position)
            self.snake_body.append(snake_part)
    
    def extend(self):
            snake_part = Turtle()
            snake_part.color("green")
            snake_part.shape("square")
            snake_part.penup()
            if self.head.heading() == 90 or self.head.heading() == 270: 
                snake_part.goto(self.tail.xcor(), self.tail.ycor() - 20)
            else:
                snake_part.goto(self.tail.xcor() - 20, self.tail.ycor())
                
            self.snake_body.append(snake_part)

    
    def move(self):
        for snake_pos in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake_pos - 1].xcor()
            new_y = self.snake_body[snake_pos - 1].ycor()
            self.snake_body[snake_pos].goto(new_x, new_y)

        self.head.forward(20)

    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        self.snake_body.clear()
        self.create_snake()