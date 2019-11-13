#color
#explore color values
from KhanFunctions import*
turtle.colormode(255)#brings in colormode
turtle.bgcolor(0,0,0)
bob.speed(0)

for times in range(50):
    c = (250-times*2,250-times*2,250-times*2)
    polygon(3,250-times*5,c)
    bob.right(120)
