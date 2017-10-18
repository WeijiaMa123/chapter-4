import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.pensize(3)
tess.color("blue")
def draw_pattern(tess,number):
    for j in range(number):
        for i in range(4):
            tess.forward(70)
            tess.left(90)
        tess.left(15)
tess.speed(10)
draw_pattern(tess,26)
        
        
    