import time
from ball import Ball
from turtle import Screen
from paddle import Paddle
from field import Field
from scoreboard import Scoreboard

L_PADDLE_INITIAL = (-370, 0)
R_PADDLE_INITIAL = (370, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Ping Pong Game")
screen.tracer(0)


screen.listen()
field = Field()
ball = Ball()
scoreboard = Scoreboard()
l_paddle = Paddle(L_PADDLE_INITIAL)
r_paddle = Paddle(R_PADDLE_INITIAL)


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move("r")

    if ball.distance(r_paddle) > 10 and ball.xcor() > 390:
        ball.goto(0, 0)
        r_paddle.goto(R_PADDLE_INITIAL)
        ball.y_move *= -1
        scoreboard.r_point()
        ball.move("r")

    if ball.distance(l_paddle) > 10 and ball.xcor() < -390:
        ball.goto(0, 0)
        l_paddle.goto(L_PADDLE_INITIAL)
        ball.y_move *= -1
        scoreboard.l_point()
        ball.move("l")

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 40 and ball.xcor() > 355 or ball.distance(l_paddle) < 40 and ball.xcor() > -355:
        ball.bounce_x()

screen.exitonclick()
