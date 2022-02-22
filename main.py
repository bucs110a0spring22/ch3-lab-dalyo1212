import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('pink')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


## 5. your code goes here
calls = (10)
for i in range(calls):
  x = random.randrange(1,10)
  for s in range(x):
    michelangelo.forward(x)
    leonardo.forward(x)
# Part B - complete part B here
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

michelangelo.down()
shapes = [3,4,6,9,12]
list_size = len(shapes)
side_length = 20
go_forward = 40

for i in range (list_size):
    for s in range(shapes[i]):
      angle = 360/shapes[i]
      michelangelo.down()
      michelangelo.right(angle)
      michelangelo.forward(side_length)
    michelangelo.up()
    michelangelo.forward(go_forward)


window.exitonclick()
