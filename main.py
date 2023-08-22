import turtle
import time
import random

delay = 0.1

score = 0
high_score = 0

window = turtle.Screen()
window.title("Snake Game")
window.bgcolor("green")
window.setup(width=600, height=600)
window.tracer(0)

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("yellow")
head.penup()
head.goto(0,0)
head.direction = "stop"


eye1 = turtle.Turtle()
eye1.speed(0)
eye1.shape("circle")
eye1.color("white")
eye1.penup()
eye1.goto(-8, 10)
eye1.shapesize(0.5)
eye1.direction = "stop"

ebl = turtle.Turtle()
ebl.speed(0)
ebl.shape("circle")
ebl.color("black")
ebl.penup()
ebl.goto(-8, 10)
ebl.shapesize(0.25)
ebl.direction = "stop"

eye2 = turtle.Turtle()
eye2.speed(0)
eye2.shape("circle")
eye2.color("white")
eye2.penup()
eye2.goto(8, 10)
eye2.shapesize(0.5)
eye2.direction = "stop"

ebr = turtle.Turtle()
ebr.speed(0)
ebr.shape("circle")
ebr.color("black")
ebr.penup()
ebr.goto(8, 10)
ebr.shapesize(0.25)
ebr.direction = "stop"


segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


def go_up():
    if head.direction != "down":
        head.direction = "up"
        eye1.direction = "up"
        eye2.direction = "up"
        ebr.direction = "up"
        ebl.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
        eye1.direction = "down"
        eye2.direction = "down"
        ebr.direction = "down"
        ebl.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"
        eye1.direction = "left"
        eye2.direction = "left"
        ebr.direction = "left"
        ebl.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
        eye1.direction = "right"
        eye2.direction = "right"
        ebr.direction = "right"
        ebl.direction = "right"


def move():
    if head.direction == "up":
        y1 = head.ycor()
        head.sety(y1+20)

        y2 = eye1.ycor()
        eye1.sety(y2+20)
        y3 = eye2.ycor()
        eye2.sety(y3+20)

        y4 = ebl.ycor()
        ebl.sety(y4+20)
        y5 = ebr.ycor()
        ebr.sety(y5+20)


    if head.direction == "down":
        y1 = head.ycor()
        head.sety(y1-20)

        y2 = eye1.ycor()
        eye1.sety(y2-20)
        y3 = eye2.ycor()
        eye2.sety(y3-20)

        y4 = ebl.ycor()
        ebl.sety(y4-20)
        y5 = ebr.ycor()
        ebr.sety(y5-20)

    if head.direction == "left":
        x1 = head.xcor()
        head.setx(x1-20)

        x2 = eye1.xcor()
        eye1.setx(x2-20)
        x3 = eye2.xcor()
        eye2.setx(x3-20)

        x4 = ebl.xcor()
        ebl.setx(x4-20)
        x5 = ebr.xcor()
        ebr.setx(x5-20)

    if head.direction == "right":
        x1 = head.xcor()
        head.setx(x1+20)

        x2 = eye1.xcor()
        eye1.setx(x2+20)
        x3 = eye2.xcor()
        eye2.setx(x3+20)

        x4 = ebl.xcor()
        ebl.setx(x4+20)
        x5 = ebr.xcor()
        ebr.setx(x5+20)

window.listen()
window.onkeypress(go_up, "Up")
window.onkeypress(go_down, "Down")
window.onkeypress(go_left, "Left")
window.onkeypress(go_right, "Right")


while True:
    window.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        eye1.goto(-8, 10)
        ebl.goto(-8, 10)
        eye2.goto(8, 10)
        ebr.goto(8, 10)
        head.direction = "stop"
        eye1.direction = "stop"
        eye2.direction = "stop"
        ebl.direction = "stop"
        ebr.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear() 

        score = 0

        delay = 0.1

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)



    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            eye1.goto(-8, 10)
            ebl.goto(-8, 10)
            eye2.goto(8, 10)
            ebr.goto(8, 10)
            head.direction = "stop"
            eye1.direction = "stop"
            eye2.direction = "stop"
            ebl.direction = "stop"
            ebr.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear() 

            score = 0

            delay = 0.1

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)



window.mainloop()