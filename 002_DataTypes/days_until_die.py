# Calculating how much time do you have if you will live till 90s

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

month = (90-int(age))*12
weeks = (90-int(age))*52
days = (90-int(age))*365

print(f"You have {days} days, {weeks} weeks, and {month} months left.")
