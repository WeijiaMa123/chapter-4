import turtle
wn=turtle.Screen()
tess = turtle.Turtle()
def draw_poly(t, n, sz):
    for i in range(n):
        tess.forward(sz)
        tess.left(360/n)
def draw_equitriangle(t,sz):
    draw_poly(t,3,sz)
draw_equitriangle(tess,100)