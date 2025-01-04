# 4) Boss level:
# ააგეთ 4 კვადრატი ისე, როგორც მე გავაკეთე, ანუ სამივე მიდგომით

# 2)პირველი მიდგომა
from turtle import *

# first
penup()
goto(100, 100)
pendown()

for i in range(4):
    forward(200)
    left(90)

# second
penup()
goto(-300, 100)
pendown()

for i in range(4):
    forward(200)
    left(90)

# third
penup()
goto(-300, -300)
pendown()

for i in range(4):
    forward(200)
    left(90)

# fourth
penup()
goto(100, -300)
pendown()

for i in range(4):
    forward(200)
    left(90)

exitonclick()
