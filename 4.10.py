import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
frank = turtle. Turtle ()
frank.color("hotpink")
frank.pensize(3)
def draw_astar(frank,length):
    for j in range(5):
        for i in range (5):
            frank.forward(length)
            frank. right(144)
        frank.penup()
        frank.forward(350)
        frank.right(144)
        frank.pendown()
        
frank.penup()
frank.backward(200)
frank.pendown()
draw_astar(frank,100)