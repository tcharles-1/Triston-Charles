#-------------------------------------------------------------------------------
# Name:        module 1
# Purpose:     4.9 Exercise 2
#
# Author:      Triston Charles
#
# Created:     02/23/2025
# Copyright:   (c) johnk 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(3)
 
def draw_square(tess, size):
    for i in range(4):
	    tess.forward(size)
	    tess.left(90)
    tess.penup()
    tess.backward(10)
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()


for i in range(5):
    draw_square(tess,20 + 20*i)

wn.mainloop()
