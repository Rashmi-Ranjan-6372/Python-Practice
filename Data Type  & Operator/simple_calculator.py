num1 =  input("Enter The First Number: ")
num2 =  input("Enter The Second Number: ")

operator = input("Enter The Operator (+, -, *, /): ")

if operator == "+":
    print("Sum of the 2 numbers is: ", int(num1) + int(num2))
elif operator == "-":
    print("Substraction of 2 numbers is: ", int(num1) - int(num2))
elif operator == "*":
    print("Multiplication of 2 numbers is: ", int(num1) * int(num2))
elif operator == "/":
    print("Division of 2 numbers is: ", int(num1) / int(num2))