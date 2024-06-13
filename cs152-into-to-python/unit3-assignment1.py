# This program draws 4 random sized circles
#
# Bert Darnell
# 4-3-21
# cs152

#function to draw each circle
def start(t,rad):
    a = (-75,75)
    b = (75,75)
    c = (-75,-150)
    d = (75,-150)
    for xy in (a,b,c,d):
        t.pu()
        t.goto(xy)
        t.pd()
        t.color('black')
        t.begin_fill()
        t.circle(rad,180)
        t.end_fill()
        t.circle(rad,180)
        
        
def main():
    import random
    import turtle

# Sets screen and turtle attributes
    franklin=turtle.Turtle()
    franklin.hideturtle()
    franklin.speed(0)
    franklin.delay(500)  #played with speed and delay
    
    wn=turtle.Screen()    
    wn.exitonclick()

# sets a random randius and starts the program
    radius = random.randrange(25,60)

    start(franklin,radius)
    
    
main()



                  