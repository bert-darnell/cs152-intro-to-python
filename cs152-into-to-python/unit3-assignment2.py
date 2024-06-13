# Draws 3 sets of shapes of varying lengths
#   Draw a rectangle
#   Draw a line the length of the rectangle's perimeter
#   Draw a circle with the same area as the rectangle
### Calculates fruitful function for perimiter of each rectangle
### Calculates fruitful function for radius of each cirlce
###
### Each revision for unit 3 questions is marked with "###"
###
### Bert Darnell
### 4-2-21
### cs152

import turtle
import math

def next_y_position(y,ht):
    """ Returns the next y-position, given current position y and height ht """
    next = y + ht + 30
    return next

def drawRect(t, len, wid):
   """ Draws a rectangle using turtle t with sides len and wid """
   for side in [len, wid, len, wid]:
      t.forward(side)
      t.left(90)

def skipForward(t, len):
    ### Move a little to the right of the line
    t.up()
    t.forward(len)
    t.down()

def skipTo(t,x,y):
    ### Moves the turtle t to coordinates (x,y) without drawing anything.
        t.pu()
        t.goto(x,y)
        t.pd()

def perimeter(len,wid):
    ### calculates the perimeter of each rectangle
    p = ((len*2)+(wid*2))
    return p

def circ_rad(len,wid):
    ### calculates given equation
    r = math.sqrt(len*wid/math.pi)
    return r

def main():
    # named constants
    screen_size = 500
    screen_startx = 60 # x coordinate of the left edge of the graphics window

    # Set up the window and its attributes
    wn = turtle.Screen()              
    wn.bgcolor("lightblue")
    wn.setup(screen_size, screen_size, screen_startx, 0)
    

    alex = turtle.Turtle()

    # Initial turtle position near left edge, toward the bottom
    xpos = -screen_size/2 + 20 
    ypos = -screen_size/2 + 50

    ### used to initially set first position of turtle
    skipTo(alex,xpos,ypos)
    
    # y-dimension of each rectangle
    width = 50
    
    # draw three sets of shapes - same width(y-dimension) but different lengths
    for length in [25, 50, 75]:

        # Draw the rectangle
        drawRect(alex, length, width)

        ### Move a little to the right of the rectangle
        skipForward(alex, length+10)

        # Draw the line the same length as the perimeter of the rectangle
        per = 2 * (length + width)
        alex.forward(per)

        ### Move a little to the right of the line
        skipForward(alex,20)

        # Draw a circle with the same area as the rectangle
        alex.begin_fill()
        rad = math.sqrt(length*width/math.pi)
        alex.circle(rad)
        alex.end_fill()

        # Next vertical position for a set of shapes
        ypos = next_y_position(ypos, width)

        ###calculate the perimeter of rectangle
        p = perimeter(length, width)

        ###calculates circ_rad
        r = circ_rad(length,width)
        
        ### Put turtle to left side of screen at correct height
        skipTo(alex,xpos,ypos)
        

# Run the main function. This should be the last statement in the file.
main()


