####=====================================================###no. 234
# # List Comperhension structure
# from operator import truediv
# new_list = [1, 2, 3]
# new_numbers = [n+1 for n in new_list]

# name = "Angela"
# letters_list = [letter for letter in name]

# numbers = range(1,5)
# double = [n*2 for n in range(1,5)]

# names = ["Ales", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [n for n in names if len(n) < 5]
# uppernames = [n.upper() for n in names if len(n) > 4]

# test = [1 for n in names if len(n) > 4]
####=====================================================###no.235

# # List Comperhension structure
# from operator import truediv

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# squared = [n**2 for n in numbers if n > 0]

# print(squared)
# true = 1

####=====================================================###no.236

# # List Comperhension structure
# from operator import truediv

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# result = [n for n in numbers if n % 2 == 0]

# true = 1

####=====================================================###no.237

# List Comperhension structure
from operator import truediv

with open("026_List_Comperhension/file1.txt") as file1:
    file_1_data = file1.readlines()

with open("026_List_Comperhension/file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(n) for n in file_1_data if n in file_2_data]

print(result)