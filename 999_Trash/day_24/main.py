# file = open("my_file.txt")
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")




# file.close()
