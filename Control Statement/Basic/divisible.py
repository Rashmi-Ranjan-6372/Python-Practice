num = int(input("Enter a number to check whether the number is divisible by 5: "))

if num % 5 == 0 or num % 10 == 0:
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 5")