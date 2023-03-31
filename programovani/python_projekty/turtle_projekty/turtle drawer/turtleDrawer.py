import turtle

t = turtle.Turtle()

#FUNCTIONS

#move

def forward(lenght):
    t.fd(lenght)

def backward(lenght):
    t.bk(lenght)

def left(degrees):
    t.lt(degrees)

def right(degrees):
    t.rt(degrees)

#shapes

def square(size):
    for x in range(0,4):
        t.fd(size)
        t.lt(90)

def triangle(size):
    for x in range(0,2):
        t.fd(size)
        t.lt(120)
    t.fd(size)

def circle(size):
    t.circle(size)

#polygon

def polygon(size, sides):
    for x in range(0, sides):
        t.fd(size)
        t.lt(360/sides)