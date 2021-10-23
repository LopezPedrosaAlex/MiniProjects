#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[Name]"


with open('./Input/Names/invited_names.txt', 'r') as names_file:
    names = names_file.readlines()


with open('./Input/Letters/starting_letter.txt', 'r') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", 'w') as letter_to_send:
            letter_to_send.write(new_letter)

