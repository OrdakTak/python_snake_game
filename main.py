from tkinter.ttk import setup_master
from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) - 1, 0, -1):
        newX = segments[seg_num -1].xcor()
        newY = segments[seg_num-1].ycor()
        segments[seg_num].goto(newX, newY)

    segments[0].forward(20)







screen.exitonclick()