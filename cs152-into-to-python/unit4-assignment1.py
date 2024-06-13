### this program has two turtles move around randomly, the first tirtle moves 5 times before the second. It also writes which turtle is on top in the center of the screen
import random
import turtle

#moves the turtles
def moveRandom(t,d):
    coin = random.randrange(0,2)
    if coin == 0:
        t.left(90)
    else:
        t.right(90)

    t.forward(d)

## checks if turtles are outside of the screen and moves them back in. Returns true if still in screen
def isInScreen(w, t):
#gets screen widtth and height 
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()
#checks if in screen
    stillIn = True
    if turtleX > rightBound or turtleX < leftBound:
        t.left(180)
        t.forward(100)
    elif turtleY > topBound or turtleY < bottomBound:
        t.left(180)
        t.forward(100)
    return stillIn

## writes in the center of screen with which turtle is on top
def pos(t):
    current = t.pos()
    t.pu()
    t.goto(0,0)
    t.write('top turt') 
    t.goto(current)
    t.pd()
    
# sets the attributes for turtle and screen, also sets the program in motion.
def main():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    wn = turtle.Screen()

#turtle shape and color
    t1.shape('turtle')  
    t2.shape('turtle')
    t1.color('green')
    t2.color('red')
#turtle start position
    t1.up()
    t1.goto(100,100)
    t1.down()

    t2.up()
    t2.goto(-100,-100)
    t2.down()
#calls move turtles, calls if turtles are in screen, calls write function
    while isInScreen(wn, t1) and isInScreen(wn, t2):
        moveRandom(t2,50)
        for i in range(5):  
            moveRandom(t1,100)
            stillin=isInScreen(wn, t1) and isInScreen(wn, t2)
            
        if t1.ycor() > t2.ycor():
            pos(t1)

        else:
            pos(t2)
            
    wn.exitonclick()
    
main()