import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('green')
    #create the turtle Brad - Draws as a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("red")
    brad.speed(4)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #create the turtle Angie - Draws as a circle
    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('white')
    angie.circle(100)

    window.exitonclick()
draw_art()

print("Wedad Saleh :-) Thank you")
