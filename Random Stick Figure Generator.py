#Using turtle to generate a stick figure at different sizes and positions
import turtle
import random

#Setting up screen and such
my_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.fillcolor("black")
my_turtle.penup()
my_turtle.setpos(0,0)
my_turtle.pendown()

#making methods for controlled drawing
def draw_arm_or_leg(length):
    my_turtle.pendown()
    my_turtle.seth(270)
    my_turtle.left(45)
    my_turtle.fd(length)
    my_turtle.up()
    my_turtle.bk(length)
    my_turtle.seth(270)
    my_turtle.down()
    my_turtle.right(45)
    my_turtle.fd(length)
    my_turtle.up()
    my_turtle.bk(length)
    my_turtle.seth(0)
    my_turtle.penup()
def draw_head(length):
    my_turtle.circle(length)
    my_turtle.fillcolor("black")
    
    my_turtle.up()
    my_turtle.seth(90)
    my_turtle.fd(length * 1.5)
    my_turtle.seth(180)
    my_turtle.fd(length*.5)
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.circle(length/6)
    my_turtle.end_fill()
    my_turtle.up()
    my_turtle.seth(0)
    my_turtle.fd(length*1)
    my_turtle.down
    my_turtle.seth(180)
    my_turtle.begin_fill()
    my_turtle.circle(length/6)
    my_turtle.end_fill()
    my_turtle.up
    my_turtle.seth(180)
    my_turtle.fd(length*1.5)
    my_turtle.seth(90)
    my_turtle.fd(length*.3)
    my_turtle.seth(0)
    my_turtle.down()
    my_turtle.fd(length*2)
    my_turtle.seth(90)
    my_turtle.circle(length, 180)
    my_turtle.seth(270)
    my_turtle.penup()
    my_turtle.fd(length*1.8)
    my_turtle.seth(0)
    my_turtle.fd(length)
    my_turtle.down()


def draw_random_stick_with_hat(times):
    stick_count = 0
    while stick_count < times:
        my_turtle.penup()
        proportion = random.randint(25,75)
        randomx = random.randint(-100,100)
        randomy = random.randint(-100,100)
        my_turtle.seth(0)
        my_turtle.setpos(randomx, randomy)
        my_turtle.pendown()
        draw_head(proportion*.5)
        my_turtle.seth(270)
        my_turtle.fd(proportion)
        draw_arm_or_leg(proportion*.25)
        my_turtle.seth(90)
        my_turtle.fd(proportion*.75)
        draw_arm_or_leg(proportion * .25)
        my_turtle.seth(0)

#just a test function
draw_random_stick_with_hat(15)


