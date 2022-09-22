# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Letters/starting_letter.txt", mode="r") as letter_template:
    letter_template = letter_template.read()
    letter = letter_template.split("\n")

with open("./Input/Names/invited_names.txt", mode="r") as names:
    names = names.read()
    names = names.split("\n")

for x in names:
    new_letter = letter
    new_letter[0] = letter[0].replace("Dear [name],", f"Dear {x},")
    with open(f"Output/ReadyToSend/{x}", mode='w') as l:
        for y in new_letter:
            l.write(f"{y}\n")
    new_letter[0] = letter[0].replace(f"Dear {x},", "Dear [name],")
