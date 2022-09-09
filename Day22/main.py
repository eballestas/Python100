from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Ping Pong Game")
screen.tracer(0)

l_paddle = Paddle(350)
r_paddle = Paddle(-350)


screen.listen()
screen.onkey(Paddle.go_up, "Up")
screen.onkey(Paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
