from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    def __init__(self):
        self.list_of_cars = []
        self.speed_level_up = 0
        self.quantity_level_up = 30
        for _ in range(0, 29):
            turtle = Turtle()
            turtle.shape("square")
            turtle.penup()
            turtle.shapesize(stretch_len=3, stretch_wid=1)
            turtle.color(COLORS[random.randint(0, 5)])
            turtle.goto(random.randint(-300, 300), random.randint(-250, 250))
            self.list_of_cars.append(turtle)

    def add_car(self):
        if len(self.list_of_cars) < self.quantity_level_up:
            turtle = Turtle()
            turtle.shape("square")
            turtle.penup()
            turtle.shapesize(stretch_len=3, stretch_wid=1)
            turtle.color(COLORS[random.randint(0, 5)])
            turtle.goto(320, random.randint(-250, 250))
            self.list_of_cars.append(turtle)

    def move(self):
        for car in self.list_of_cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE - self.speed_level_up
            car.goto(new_x, car.ycor())

    def del_car(self, car_pos):
        self.list_of_cars[car_pos].hideturtle()
        self.list_of_cars.pop(car_pos)

    def level_up(self):
        self.speed_level_up += 5
        #self.quantity_level_up += 5
        
        
    
