list = [1, 2, 3, 4, 5, 6, 8, 10]

print(f"First lement of the given list {list}: ", list[0])
print(f"Last lement of the given list {list}: ", list[7])

count = 0

for i in list:
    count += 1
    print("The element of the given list: ", i)
print("The length of the list: ", count)

print("=================USING WHILE LOOP===============")

i = 0
sum = 0

while i < len(list):
    print(list[i])
    sum = sum + i
    i += 1

print("Sum of all the elements os this list: ", sum)

print("=================LARGET ELEMENT==================")

largest = list[0]

for i in list:
    if i > largest:
        largest = i
print("The largest element is: ", largest)

print("=================SMALLEST ELEMENT==================")

SMALLEST = list[0]

for i in list:
    if i < SMALLEST:
        SMALLEST = i

print("The smallest element is: ", SMALLEST)

print("=================EVEN/ODD ELEMENT==================")

count_even = 0
count_odd = 0

for i in list:
    if i % 2 == 0:
        count_even += 1
        print("The Even Elements is: ", i)
    else:
        count_odd += 1
        print("The Odd Elements is: ", i)

print("The Total Even Elements: ", count_even)
print("The Total Odd Elements: ", count_odd)

print("=================REVERSE ELEMENT===============")

LEFT =0
RIGHT = len(list) - 1

while LEFT < RIGHT:
    temp = list[LEFT]
    list[LEFT] = list[RIGHT]
    list[RIGHT] = temp

    LEFT += 1
    RIGHT ++ 1

print("Reserved List: ", list)