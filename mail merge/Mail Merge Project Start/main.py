#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#Successfully obitaned the list of names
with open("./Input/Names/invited_names.txt") as names:
    name_lst = names.read()

invitees = name_lst.split("\n")

#obitaining stating letter
with open("./Input/Letters/starting_letter.txt") as letter_body:
    letter = letter_body.read()

#generating output
for name in  invitees:

    with open("./Output/letter_for_" + name, "w" ) as file:
        letter_body = letter.replace("[name]", name)
        file.write(letter_body)



