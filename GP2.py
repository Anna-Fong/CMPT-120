# Proup Project 2 (turtles)

# Purpose: Create a drawing following the criteria/requirements listed on canvas 
#          for group project 2
# Authors: Kaitlyn Lum and Anna Fong
# Date: July 12, 2023

import turtle
import random

# list of dress colours
dressColours = ["magenta","#d85c64","purple","light blue","light green"]

# list of shoe colours
shoeColours = ["black","grey","#65350f"]

# function to draw ground
def ground(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(600)

# function to draw one leg
def leg(x,y):
    turtle.penup()
    turtle.goto(x,y)
    #turtle.shape("classic")
    turtle.color("#ffacdc")
    turtle.pensize(10)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(47)
    turtle.pensize(1)

# function to draw one shoe
def shoe(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(random.choice(shoeColours))  
    turtle.shape("circle")
    turtle.shapesize(1,3)
    turtle.stamp()
    turtle.shape("classic")
    turtle.shapesize(1,1)

# function to draw dress
def dress():
    turtle.penup()
    turtle.color(random.choice(dressColours))
    turtle.goto(-150,-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(300)
    turtle.left(90)
    for i in range (63):
        turtle.forward(5)
        turtle.left(1)
    turtle.setheading(270)
    turtle.forward(255)
    turtle.end_fill()
    turtle.goto(-150,-200)
    turtle.setheading(90)
    turtle.begin_fill()
    for i in range(63):
        turtle.forward(5)
        turtle.right(1)
    turtle.setheading(270)
    turtle.forward(255)
    turtle.end_fill()

# function to draw head
def head():
    turtle.pencolor("#ee4eaa")
    turtle.fillcolor("#ffacdc")
    turtle.penup()
    turtle.goto(0,180)
    turtle.pendown()
    turtle.begin_fill()
    turtle.setheading(0)
    for i in range(310):
        turtle.right(1)
        turtle.forward(1.8)
    turtle.end_fill()

    # draw nose shape
    turtle.begin_fill()
    for i in range(40):
        turtle.forward(5.5)
        turtle.right(1.5)
    for i in range(60):
        turtle.forward(1.5)
        turtle.right(1.9)
    for i in range(14):
        turtle.forward(5.5)
        turtle.right(2.6)
    turtle.end_fill()

    # draw tip of nose
    turtle.setheading(240)
    turtle.penup()
    turtle.goto(105,219)
    turtle.pendown()
    for i in range(100):
        turtle.left(1.3)
        turtle.forward(1)

# function to draw one nostril
def nostril(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.shape("circle")
    turtle.shapesize(0.5)
    turtle.color("#f48cc8")
    turtle.stamp()

# function to draw ears
def ears():
    # draw left ear
    turtle.shape("classic")
    turtle.penup()
    turtle.goto(-70,145)
    turtle.pendown()
    turtle.fillcolor("#ffacdc")
    turtle.begin_fill()
    turtle.setheading(150)
    for i in range(20):
        turtle.forward(2)
        turtle.right(1.3)
    for i in range (55):
        turtle.right(2.9)
        turtle.forward(1)
    for i in range(18):
        turtle.forward(2)
        turtle.right(1.4)
    turtle.end_fill()

    #draw right ear
    turtle.penup()
    turtle.goto(-27,185)
    turtle.setheading(130)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(18):
        turtle.forward(2)
        turtle.right(1.1)
    for i in range (53):
        turtle.right(3.3)
        turtle.forward(1)
    for i in range(17):
        turtle.forward(2)
        turtle.right(1.4)
    turtle.end_fill()

# function to draw blush
def blush():
    turtle.penup()
    turtle.goto(-50, 70)
    turtle.pendown()
    turtle.shape("circle")
    turtle.color("#ff80cb")
    turtle.shapesize(3)
    turtle.stamp()

# function to draw one eye
def eye(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.shapesize(1.9)
    turtle.color("#f48cc8")
    turtle.stamp()
    turtle.shapesize(1.3)
    turtle.color("white")
    turtle.stamp()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(3)
    turtle.left(90)
    turtle.forward(3)
    turtle.pendown()
    turtle.color("black")
    turtle.shapesize(0.6)
    turtle.stamp()

# function to draw mouth
def mouth():
    turtle.penup()
    turtle.shape("classic")
    turtle.color("#d8448c")
    turtle.goto(-6, 49)
    turtle.pendown()
    turtle.pensize(1.5)
    turtle.setheading(286)
    for i in range(165):
        turtle.left(1)
        turtle.forward(0.7)
    turtle.shape("circle")

# function to draw arms
def arms():
    # draw left arm
    turtle.penup()
    turtle.pensize(10)
    turtle.color("#ffacdc")
    turtle.goto(-85,-30)
    turtle.pendown()
    turtle.setheading(150)
    turtle.forward(90)
    turtle.back(35)
    turtle.right(35)
    turtle.forward(35)
    turtle.back(35)
    turtle.left(65)
    turtle.forward(30)

    # draw right arm
    turtle.penup()
    turtle.setheading(30)
    turtle.goto(100,-30)
    turtle.pendown()
    turtle.forward(90)
    turtle.back(35)
    turtle.left(35)
    turtle.forward(35)
    turtle.back(35)
    turtle.right(65)
    turtle.forward(30)

# function to draw tail
def tail():
    turtle.penup()
    turtle.goto(-140,-140)
    turtle.setheading(240)
    turtle.pendown()
    for i in range(50):
        turtle.right(3)
        turtle.forward(1.2)
    turtle.right(30)
    for i in range(60):
        turtle.right(4)
        turtle.forward(0.8)
    for i in range(23):
        turtle.right(1.2)
        turtle.forward(1.45)

# set turtle speed
turtle.speed(10)

# call all the functions to draw image
ground(-300,-250)
leg(-50,-195) # left leg
leg(50,-195) # right leg
shoe(70,-242) # left shoe
shoe(-30,-242) # right shoe
dress()
head()
nostril(120,185) # left nostril
nostril(135,188) # right nostril
ears()
blush()
eye(-12,160) # left eye
eye(30,179) # right eye
mouth()
arms()
tail()

turtle.hideturtle()
turtle.exitonclick()