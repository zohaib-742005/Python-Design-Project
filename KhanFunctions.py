#Khanfunctions
import turtle
bob = turtle.Turtle()

def polygon(sides,distance,c):
    angle = 360/sides
    bob.color(c)
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()

def star(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(5):
        bob.forward(distance)
        bob.right(144)
    bob.end_fill()

def explosion(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
    bob.end_fill()

def portal():
    for times in range(60):
        c = (times*4,times*4,times*4)#r,g,b values increasingly white
        polygon(3,125-times*2,c)#value of distance decreases by twice the value
        bob.right(92)#choose an interesting value














    
