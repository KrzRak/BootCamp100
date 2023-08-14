#  v1.0
# -----------------------------------------------------
# Instructions
# -----------------------------------------------------
# You are going to write a program that will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]
# This is a bit hard to work with. So on lines 6 and 23, we've used this line of code print(f"{row1}\n{row2}\n{row3}" to format the 3 lists to be printed as a 3 by 3 square, each on a new line. 
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# Now it looks a bit more like the coordinates of a real map:
# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit in the input will specify the column (the position on the horizontal axis).
# The second digit in the input will specify the row number (the position on the vertical axis). 
# So an input of 23 should place an X at the position shown below:

# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit in the input will specify the column (the position on the horizontal axis).
# The second digit in the input will specify the row number (the position on the vertical axis). 
# So an input of 23 should place an X at the position shown below:

# Remember that Lists start at index 0!
# map is just a variable that contains a nested list. It's not related to the map function in Python.
# Remember that nested lists are accessed from out to in. So if list=[[A,B,C],[E,F,G]] then E = list[1][0]
# Check that you haven't accidentally added extra spaces and the X is a capital X with a single quote around it.

# -----------------------------------------------------

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


map[int(position[1])-1][int(position[0])-1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")