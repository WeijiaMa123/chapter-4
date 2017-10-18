import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
frank = turtle.Turtle()
frank.speed(10)
frank.color("blue")
def draw_spiral(turt,sz,space):
    turt.right(90)
    for i in range(98):
        turt.forward(sz)
        sz = sz+space
        turt.right(90)
        
    
    
draw_spiral(frank,10,2)