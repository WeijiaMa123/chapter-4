import turtle
wn = turtle.Screen()
tess=turtle.Turtle()
wn.bgcolor("lightgreen")
tess.color("hotpink")
tess.pensize(3)
def draw_poly(t, n, sz):
    for i in range(n):
        tess.forward(sz)
        tess.left(360/n)

draw_poly(tess,8,50)
    