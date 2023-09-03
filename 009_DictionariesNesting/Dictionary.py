# Dictionary v1.0.0
# -----------------------------------------------------
# Instructions
# -----------------------------------------------------

# -----------------------------------------------------
# {Key: Value}
# {"Bug": "An error in a program that prevents the program from running as expected.}

# Crating new dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
    }

# Retrieving items from dictionary.
print(programming_dictionary["Bug"])

# Adding new items to dictionary.
programming_dictionary["New"] = "New item in dictionary"

print(programming_dictionary)

# Create an empty dictionary.
empty_list = []
empty_dictionary = {}

# Wipe an existing dictionary.
programming_dictionary = {}
print(programming_dictionary)

# Crating new dictionary.
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again."
    }

# Edit an item in a dictionary.
programming_dictionary["Bug"] = "New definition"
print(programming_dictionary)

# Loop through a dictionary.
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])