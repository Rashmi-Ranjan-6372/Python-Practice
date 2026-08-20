name = input("Enter your name: ")

print("Hello, " + name + "! Welcome to the program.")

search = input("Enter a character to search in your name: ")

if search in name:
    print(f"The character '{search}' is present in your name. In the name '{name}', the character '{search}' is present at index {name.index(search)}.")
else:
    print(f"The character '{search}' is not present in your name.")
