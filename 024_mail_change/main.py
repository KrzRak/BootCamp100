# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", mode="r") as invited_names:
    names = invited_names.readlines()

for names_id in range(0, len(names)):
    names[names_id] = names[names_id].strip()

    with open("Input/Letters/starting_letter.txt", mode="r") as starting_letter:
        starting_letter_read = starting_letter.read()
        starting_letter_read = starting_letter_read.replace("[name]", names[names_id])

    with open(f"Output/ReadyToSend/{names[names_id]}_letter.txt", mode="w") as name_letter:
        name_letter.write(starting_letter_read)
