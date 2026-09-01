num = int(input("Enter The Number As Your Wish: "))

if num < 0:
    print(f"The number {num} is a -ve Number.")
elif num > 0:
    print(f"The number {num} is a +ve number.")
else:
    print(f"You Input thing {num} is not a Valid number.")