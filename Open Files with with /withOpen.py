## Old method of opening and closing files
from doctest import testfile

# file = open("testFile.txt")
# file_content = file.read()
# print(file_content)
# file.close()

##opening and closing files via wth open method
##this will automatically close the file for us

#read mode
with open("testFile.txt") as file:
    file_content = file.read()
print(file_content)

#write mode, this will erase what is in the file and add what we wanna add
print("\n")
with open("testFile.txt", "w") as file:
    file.write("My name is Morina Singh, I love animals😍")

#reopening the file and printing the contents
with open("testFile.txt") as file:
    updated_file_contents = file.read()
print(updated_file_contents)
print("\n")
#opening the file in append mode
with open("testFile.txt", "a") as file:
    file.write("\nMy favourite animal is cats and small dogs")

with open("testFile.txt") as file:
    appended_file_contents = file.read()
print(appended_file_contents)

