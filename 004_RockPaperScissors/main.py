rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

human = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
ai = random.randint(0,2)
hand = [rock, paper, scissors]

print(f"Human:\n{hand[human]}")
print(f"AI:\n{hand[ai]}")

#Remis
if human == ai:
    print("Remis")
elif human == 2 and ai == 0:
    print("You lose!")
elif human == 0 and ai == 2:
    print("You win!")
elif human > ai:
    print("You win!")
elif human < ai:
    print("You lose!")
elif human > 2 or human < 0:
    print("You typed an ivalid number, you lose!")