import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
frank=turtle.Turtle()
frank.penup()
frank.backward(200)
frank.pendown()
frank.color("pink")
frank.pensize(5)
def drawsquares(frank,length):
    for i in range(5):
        for i in range(4):
            frank.forward(length)
            frank.right(90)
        frank.penup()
        frank.forward(80)
        frank.pendown()

drawsquares(frank,60)
frank.right(90)
frank.penup()
frank.forward(60)
frank.left(90)
frank.forward(20)
frank.pendown()

    