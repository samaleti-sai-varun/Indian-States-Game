import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "india2gif.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("30_india_states.csv")
all_states = data.state.to_list()
guessed_states=[]

while len(guessed_states) < 30:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/30 States Correct",
                                    prompt="What's another state name").title()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data=pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
