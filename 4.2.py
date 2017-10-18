import turtle
wn=turtle.Screen()
wn.bgcolor("lightgreen")
frank=turtle.Turtle()
frank.color("hotpink")
frank.pensize(3)
def draw_bigger_squares(frank,size):
    for i in range(4):
        frank.forward(size)
        frank.left(90)
    frank.penup()
    frank.backward(10)
    frank.left(90)
    frank.backward(10)
    frank.right(90)
    frank.pendown()
   
       
 
square=20
for i in range(5):
    draw_bigger_squares(frank,square)
    square=square+20
    
        
    
    