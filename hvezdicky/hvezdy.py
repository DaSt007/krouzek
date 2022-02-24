from turtle import *
from random import randint

def ctverec(a, turtle_obj):
    turtle_obj.left(90)
    turtle_obj.forward(a/2)
    turtle_obj.right(90)
    turtle_obj.forward(a)
    turtle_obj.right(90)
    turtle_obj.forward(a)
    turtle_obj.right(90)
    turtle_obj.forward(a)
    turtle_obj.right(90)
    turtle_obj.forward(a/2)

def trojuhelnik(a, turtle_obj):
    turtle_obj.left(90)
    turtle_obj.forward(a/2)
    turtle_obj.right(180/3*2)
    turtle_obj.forward(a)
    turtle_obj.right(180/3*2)
    turtle_obj.forward(a)
    turtle_obj.right(180/3*2)
    turtle_obj.forward(a/2)

def krouzek(a, turtle_obj):
    for i in range(1, 1 + 1, 1):
        turtle_obj.circle(a * i)

def draw_shape(shape_id, turtle_obj):
    turtle_obj.color(randint(0, 255),
        randint(0, 255),
        randint(0, 255))
    turtle_obj.begin_fill()
    turtle_obj.penup()
    turtle_obj.goto(randint(-400, 400), randint(-400, 400))
    turtle_obj.pendown()

    if shape_id == 1:
        trojuhelnik(randint(15,200), turtle_obj)
    
    elif shape_id == 2:
        ctverec(randint(10, 150), turtle_obj)

    elif shape_id == 3:
        krouzek(randint(6,100), turtle_obj)

    turtle_obj.end_fill()


turtle = Turtle()

turtle.speed(speed=5)

colormode(255)

while True:
    draw_shape(randint(1, 3), turtle)

