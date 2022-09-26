import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_input = screen.textinput(title="Guest the state", prompt="What's another state's name ")
answer_input = answer_input.title()

data = pandas.read_csv("50_states.csv")
states_list = data.state
data["location"] = list(zip(data.x.values, data.y.values))
state = turtle.Turtle()

game_on = True
while game_on:
    state.color("blue")
    if answer_input.title() in data["state"]:
        state.goto(data[data["location"] == answer_input].location)
        state.write(answer_input)

turtle.exitonclick()
