import turtle
import pandas

TOTAL_STATE = 50
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < TOTAL_STATE:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the State", prompt="Hazard a guess").title()

    if answer_state == "Exit":
        missing_states = []

        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        final_data = pandas.DataFrame(missing_states)
        final_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state in guessed_states:
            continue
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
