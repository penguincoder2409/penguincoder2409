import turtle
import datetime

sc= turtle.Screen()
sc.setup(500,600)
sc.bgcolor("#170c59")

sc.tracer(0)

ben=turtle.Turtle()
ben.hideturtle()
ben.speed(0)

def drawClock():
    clock=turtle.Turtle()
    clock.speed(0)
    clock.shape("turtle")
    clock.color(0.32,0.64,0.87)
    clock.dot(400)
    clock.color(0.323,0.312,0.312)
    clock.up()
    a=360
    for x in range(12):
        clock.setheading(a)
        a=a-30
        clock.forward(170)
        clock.stamp()
        clock.home()
    clock.hideturtle()

drawClock()
























