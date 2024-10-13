from turtle import *
speed(30)

#we want to paint a house

#step 1: draw a square
color("blue")
width(7)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door
begin_fill()
forward(70)
color("yellow")

left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end drawing a door

#drawing a windows
begin_fill
penup()
goto(180, 180)
pendown()
color("black")

begin_fill()
right(60)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(70, 180)
pendown()
color("black")


left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()



exitonclick()