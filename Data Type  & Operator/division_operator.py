num1 = input("Enter The First Number: ")
num2 = input("Enter The Second Number: ")

operator = input("Enter The Operator (/, //, %): ")

if operator == "/":
    print("Division of 2 numbers is: ", int(num1) / int(num2))
elif operator == "//":
    print("Floor Division of 2 numbers is: ", int(num1) // int(num2))
elif operator == "%":
    print("Modulus of 2 numbers is: ", int(num1) % int(num2))