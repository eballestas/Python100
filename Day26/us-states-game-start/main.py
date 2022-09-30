import turtle

import pandas

screen = turtle.Screen()
screen.setup(730, 500)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("50_states.csv")
states_list = df.state.to_list()

writer = turtle.Turtle()
writer.hideturtle()
guesses = []
game_on = True

while game_on:
    answer_state = screen.textinput(title=f"{len(guesses)}/50 States correct", prompt="whats your state name")
    answer_state = answer_state.title()

    #guesses.append(new_item for item in list if condition else )
    # if answer_state == "Exit":
    #     break
    # else:
    #     for _ in df.state:
    #         if _ == answer_state:
    #             guesses.append(_)
    #             writer.penup()
    #             x_cor = int(df[df["state"] == _].x.values)
    #             y_cor = int(df[df["state"] == _].y.values)
    #             writer.goto(x_cor, y_cor)
    #             writer.write(_)

response = list(set(states_list).difference(guesses))
response.sort()
new_data = pandas.DataFrame(response)
new_data.to_csv("states_to_learn.csv")
# with open("states_to_learn.txt", mode="w") as f:
#     for x in response:
#         f.write(f"{x}\n")


