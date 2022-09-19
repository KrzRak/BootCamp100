# Libraries
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
states_correct = 0
guessed_list = []
states = pandas.read_csv("50_states.csv")
states_list = states.state.to_list()

# main
while states_correct < 51:
    # Popup with question and answer
    title_text = f"{states_correct}/50 States Correct"
    prompt_text = "What's another state's name"
    answer_state = screen.textinput(title_text, prompt_text)
    
    #state,x,y
    if answer_state.title() in states_list:
        turtle.goto(160,150)
        turtle.write(answer_state.title(), align="center", font=("Arial", 10, "bold")) 
        states_correct += 1


# Stay with screen all time
if states_correct > 50:
    screen.exitonclick()
else:
    turtle.mainloop()



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

