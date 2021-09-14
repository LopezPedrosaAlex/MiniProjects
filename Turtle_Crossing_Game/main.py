import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
turtle = Player()
cars = CarManager()

screen.listen()
screen.onkey(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    cars.add_car()
    cars.move()

    i = 0
    for car in cars.list_of_cars:
        if car.xcor() < -300:
            cars.del_car(i)
        i += 1

        #Detect collision with cars
        if car.distance(turtle) < 20:
           score.game_over() 
           game_is_on = False
    
    #Cross the road
    if turtle.ycor() > 280:
        turtle.level_up()
        cars.level_up()
        score.level_up()

    screen.update()

screen.exitonclick()
