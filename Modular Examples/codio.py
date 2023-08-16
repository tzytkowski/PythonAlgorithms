import turtle

t = turtle.Turtle()

def roof():
  """Draw a triangle to represent a roof"""
  for i in range(3):
    t.lt(120)
    t.forward(100)


def house():
  """Draw a rectangle to represent a house"""
  for i in range(4):
    t.rt(90)
    t.forward(100)

def door():
  t.rt(90)
  t.forward(100)
  t.rt(90)
  t.forward(25)
  for i in range(4):
    t.forward(50)
    t.rt(90)

roof()
house()
door()

turtle.mainloop()