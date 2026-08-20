num1 = input("Enter The Number: ")

last_digit = int(num1) % 10
print("The last digit of the number is: ", last_digit)
print("After removing the last digit of the number is: ", int(num1) // 10)