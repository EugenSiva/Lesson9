name = input("Zadaj nazov suboru: ")
fileHandler = open(name, "w")
print(fileHandler.read())
