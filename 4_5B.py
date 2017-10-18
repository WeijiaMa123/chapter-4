import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
frank = turtle.Turtle()
frank.speed(20)
frank.color("blue")
frank.pensize(2)
def draw_spiral(turt,sz,space,angle):
    turt.right(90)
    for i in range(120):
        turt.forward(sz)
        sz = sz+space
        turt.right(90+angle)
        
    
    
draw_spiral(frank,3,2,1)