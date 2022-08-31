from turtle import Screen, Turtle as t


timmy = t()

timmy.speed('fastest')

counter = 0
while counter < 360:
# for x in range(100):
    timmy.circle(100)
    current_heading = timmy.heading()
    timmy.setheading(current_heading+10)
    counter +10









screen = Screen()
screen.exitonclick()
