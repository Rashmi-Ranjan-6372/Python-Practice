age = int(input("Enter your age: "))

if age >= 1 and age <= 18:
    print("You are a child.")
elif age >= 19 and age <= 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(a < b and b > 15)
print(a > b or b > 15)
print(a == b)
print(a != b)