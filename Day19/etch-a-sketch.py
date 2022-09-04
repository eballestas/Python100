from turtle import Turtle, Screen

tim = Turtle()
tim.speed("fastest")
screen = Screen()


def forward_move():
    tim.forward(10)


def backwards_move():
    tim.backward(10)


def counter_clock():
    #tim.right(5.0)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clockwise():
    tim.left(5.0)


def clear():
    screen.resetscreen()


screen.listen()
screen.onkey(fun=forward_move, key="w")
screen.onkey(fun=backwards_move, key="s")
screen.onkey(fun=counter_clock, key="a")
screen.onkey(fun=clockwise, key="d")
screen.onkey(fun=clear, key="c")

screen.exitonclick()
