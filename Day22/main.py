import time
from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Ping Pong Game")
screen.tracer(0)

l_paddle = Paddle((350, 0))
r_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

screen.onkey(r_paddle.go_up, "w")
screen.onkey(r_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    print(f"distance {ball.distance(r_paddle)}")
    print(f"xcor{ball.xcor()}")

    #if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
    #    print("contact")


screen.exitonclick()
