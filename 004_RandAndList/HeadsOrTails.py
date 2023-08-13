# HeadsOrTails v1.0
# -----------------------------------------------------
# Instructions
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
# e.g. 1 means Heads 0 means Tails
# Example Output
# Heads
# or
# Tails
# When you're happy with your code, click submit.
# -----------------------------------------------------

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random

coin = random.randint(0, 1)

if coin == 0:
    print("Tails")
elif coin == 1:
    print("Heads")
