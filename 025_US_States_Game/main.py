# Import
from re import S
import turtle
import pandas

# Screen configuration
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Parameters init
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# missing_states = data.state.to_list()
guessed_states = []

# main
while len(guessed_states) < 50:
    # Popup with question and answer
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name").title()

    if answer_state == "Exit":
        missing_states_sol = []
        for state in all_states:
            if state not in guessed_states:
                missing_states_sol.append(state)
        # neww = pandas.DataFrame(missing_states)
        # neww.to_csv("new_data.csv")
        new_data = pandas.DataFrame(missing_states_sol)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        # missing_states.remove(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Arial", 10, "bold"))
        #t.write(state_data.state.item(), align="center", font=("Arial", 10, "bold"))


###---------------------------------------###
# # Take coordinates from picture
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

###---------------------------------------###
# Close screen on click
#screen.exitonclick()
###---------------------------------------###
# states_lower = []
# for string in states_list:
#     states_lower.append(string.lower())

