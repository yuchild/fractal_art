## from https://www.youtube.com/watch?v=_ABdBoW4DV8

from turtle import *

shape("turtle")
speed(0) # 0 sets max speed 1 slowest

def tree(size, levels, angle):
    # base case
    if levels == -1:
        color("green")
        dot(size)
        color("black") # change back to black so branch is black during traversal
        return
    
    forward(size)
    right(angle) # go right
    
    tree(size * 0.8, levels - 1, angle)
    
    left(angle * 2) # go Left
    
    tree(size * 0.8, levels - 1, angle)
    
    right(angle) #straighten 
    backward(size)
 
#left(90)
# tree(100, 3, 45)

def koch_side(length, levels):
    if levels == 0:
        forward(length)
        return
    
    length /= 3.0
    koch_side(length, levels - 1)
    
    left(60)
    koch_side(length, levels - 1)
    
    right(120)
    koch_side(length, levels - 1)
    
    left(60)
    koch_side(length, levels - 1)

def koch_star(sides, length):
    colors = ["red", "blue", "green", "pink"]
    for i in range(sides):
        color(colors[i])
        koch_side(length, sides)
        right(360/sides)

left(90)
koch_star(4, 300)

mainloop() #does not close turtle canvas, close using X on window


