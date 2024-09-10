with open("/Users/moes/Desktop/morina.txt", "w") as file:
    file.write("I am using the absolute path i.e . /Users/moes/Desktop/file.txt\n")

#open via relative path
with open("../../../morina.txt", "a") as file:
    file.write("I am editied via relative path i.e ../../../morina.txt")
