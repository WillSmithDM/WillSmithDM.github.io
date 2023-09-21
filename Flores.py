from turtle import *
import math

speed(30)
bgcolor("black")
h = 0
penup()
goto(210, 150)
pendown()
for i in range(2):
    for j in range(21):
        color("#C70039")
        h += 0.001
        rt(90)
        circle(95 -j * 5, 90)
        lt(50)
        circle(95 -j * 5, 90)
        rt(180)
    circle(30, 24)
penup()
goto(210, 150)
pendown()
for i in range(2):
    for j in range(21):
        color("#C70039")
        h += 0.001
        rt(90)
        circle(95 -j * 5, 90)
        lt(50)
        circle(95 -j * 5, 90)
        rt(180)
    circle(30, 24)
penup()
goto(600, -40)
pendown()
for i in range(1):
    for j in range(21):
        color("#9400FF")
        h += 0.001
        rt(90)
        circle(95 -j * 5, 90)
        lt(50)
        circle(95 -j * 5, 90)
        rt(180)
    circle(30, 24)
penup()
goto(600, -40)
pendown()
for i in range(2):
    for j in range(22):
        color("#9400FF")
        h += 0.001
        rt(90)
        circle(95 -j * 5, 90)
        lt(50)
        circle(95 -j * 5, 90)
        rt(180)
    circle(30, 24)



penup()
goto(-450, 100)
pendown()
for i in range(16):
    for j in range(18):
        color("#F8DE22")
        h += 0.005
        rt(90)
        circle(150 -j * 6, 90)
        lt(90)
        circle(150 -j * 6, 90)
        rt(180)
    circle(40, 24)
    
penup()
goto(-220, 0)
pendown()
for i in range(3):
    for j in range(20):
        color("#1A5D1A")
        h += 0.001
        rt(90)
        circle(95 -j * 5, 90)
        lt(50)
        circle(95 -j * 5, 90)
        rt(180)
    circle(30, 24)


penup()
goto(-430, 175)
pendown()
color("brown")
begin_fill()
circle(44)
end_fill()

#corazon

speed(10)
penup()
goto(580,170)
pendown()
begin_fill()
fillcolor("red")
setheading(0)
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

def write_name(name):
    penup()
    goto(140, -150)
    pendown()
    color("white")
    write(name, align="center", font=("Aril", 12, "bold"))
def write_name1(name):
    penup()
    goto(140, -180)
    pendown()
    color("#D80032")
    write(name, align="center", font=("Arial", 12, "bold"))
flower_name = "No son flores reales por ahora"
flower_name1 = "pero programe estas para ti, mi amor 💕💕❤️"
write_name(flower_name)
write_name1(flower_name1)

done()
