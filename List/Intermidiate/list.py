list = [10, 20, 30, 40, 50, 30, 10, 70, 55, 21]

largest = None
second_largest = None

for i in list:
    if largest is None or i > largest:
        second_largest = largest
        largest = i
    elif i != largest and (second_largest is None or i > second_largest):
        second_largest = i

print("Largest: ", largest)
print("Second Largest: ", second_largest)

print("====================SECOND SMALLEST=====================")

smallest = None
second_smallest = None

for i in list:
    if smallest is None or i < smallest:
        second_smallest = smallest
        smallest = i
    elif i != smallest and (second_smallest is None or i < second_smallest):
        second_smallest = i

print("Smallest: ", smallest)
print("Second Smallest: ", second_smallest)

print("========================REMOVE DUPLICATE========================")

UNIQUE_NUMBER = []

for i in list:
    if i not in UNIQUE_NUMBER:
        UNIQUE_NUMBER.append(i)

print("Original List: ", list)
print("List After Removing Duplicates: ", UNIQUE_NUMBER)   

print("========================COUNT FREQUENCY========================")

FREQUENCY = {}

for i in list:
    if i in FREQUENCY:
        FREQUENCY[i] += 1
    else:
        FREQUENCY[i] = 1

print("Element Frequency: ",FREQUENCY)

print("================= DUPLICATE ELEMENTS =================")

unique = []
duplicates = []

for i in list:
    if i not in unique:
        unique.append(i)
    elif i not in duplicates:
        duplicates.append(i)

print("Original List: ", list)
print("Duplicate Elements: ", duplicates)

print("================= EVEN/ODD ELEMENTS LIST =================")

even = []
odd = []

for i in list:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("The even list is: ", even)
print("The odd list is: ", odd)

print("================= SQUARE ELEMENTS LIST =================")

square = []

for i in list:
    square.append(i ** 2)

print("Original List: ", list)
print("Square List: ", square)

print("================= FILTER ELEMENTS =================")

given_number = 20
result = []

for i in list:
    if i > given_number:
        result.append(i)

print("The original list: ", list)
print("The given number: ", given_number)
print("Filtered list: ", result)

print("================= MERGE LIST =================")

new_list = [20, 30, 82, 45, 56]

merged_list = []

for i in list:
    merged_list.append(i)
for i in new_list:
    merged_list.append(i)

print("List-1: ", list)
print("List-2: ", new_list)
print("Merged List: ", merged_list)


print("================= COMMON ELEMENTS =================")


common = []

for i in list:
    if i in new_list:
        common.append(i)

print("First List: ", list)
print("Second List: ", new_list)
print("Merged List: ", common)

print("================= FIRST ELEMENTS PRESENT IN FIRST NOT IN SECOND =================")


fresh = []

for i in list:
    if i not in new_list:
        fresh.append(i)

print("New List is:", fresh)


print("================= ASCENDING ORDER =================")

LIST = [20, 10, 5, 82, 5, 30]

N = len(LIST)

for i in range(N):
    for j in range(0, N - i - 1):
        if LIST[j] > LIST[j + 1]:
            temp = LIST[j]
            LIST[j] = LIST[j + 1]
            LIST[j + 1] = temp

print("Sorted list: ", LIST)

print("================= DESCENDING ORDER =================")

N = len(LIST)

for i in range(N):
    for j in range(0, N - i - 1):
        if LIST[j] < LIST[j + 1]:
            temp = LIST[j]
            LIST[j] = LIST[j + 1]
            LIST[j + 1] = temp

print("Sorted list: ", LIST)

print("================= MOVE ZEROS TO END =================")

LIST1 = [10, 0, 20, 30, 0, 50, 0]

RESULT = []

for i in LIST1:
    if i != 0:
        RESULT.append(i)

for i in LIST1:
    if i == 0:
        RESULT.append(i)

print("Original List: ", LIST1)
print("Updated List: ", RESULT)

print("================= LEFT ROTATION =================")

k = 3

n = len(LIST1)
k = k % n

for i in range(k):
    first = LIST1[0]

    for j in range(n - 1):
        LIST1[j] = LIST1[j + 1]

    LIST1[n -1] = first

print("Roated List: ", LIST1)