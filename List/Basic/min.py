list = [20, 0, 30, 40, 100]

smallest = list[0]

for n in list:
    if n < smallest:
        smallest = n
print("Smallest number is: ", smallest)