# List Comperhension structure
from operator import truediv

new_list = [1, 2, 3]
new_numbers = [n+1 for n in new_list]

name = "Angela"
letters_list = [letter for letter in name]

numbers = range(1,5)
double = [n*2 for n in range(1,5)]

names = ["Ales", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [n for n in names if len(n) < 5]
uppernames = [n.upper() for n in names if len(n) > 4]

test = [1 for n in names if len(n) > 4]

true = 1
