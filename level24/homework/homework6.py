# 4) Boss level:
# ააგეთ 4 კვადრატი ისე, როგორც მე გავაკეთე, ანუ სამივე მიდგომით

# 3)პირველი მიდგომა
from turtle import *

def draw_square(x_coordinate, y_coordinate):

  penup()
  goto(x_coordinate, y_coordinate)
  pendown()

  for i in range(4):
    forward(200)
    left(90)

draw_square(100, 100)
draw_square(-300, 100)
draw_square(-300, -300)
draw_square(100, -300)
