from turtle import Turtle, Screen

def MovForward():
    tim.forward(10)


tim = Turtle()

screen = Screen()
screen.listen()
screen.onkey(key="space", fun=MovForward)
screen.exitonclick()
