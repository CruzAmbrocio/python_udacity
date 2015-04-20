import turtle
def draw_square(some_turtles):
    for x in range(1,5):
        some_turtles.forward(100)
        some_turtles.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor ("black")
    brad=turtle.Turtle()
    brad.shape('turtle')
    brad.color('sky blue')
    brad.speed(1)
    for x in range(1,37):
        draw_square(brad)
        brad.right(10)
    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("pink")
    #angie.circle(100)
    window.exitonclick()
draw_art()