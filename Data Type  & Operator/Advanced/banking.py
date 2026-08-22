initial = float(input("Enter your initial amount: "))
deposit = float(input("Enter your deposit amount: "))
withdrawal = float(input("Enter your withdrawal amount: "))
interest_rate = float(input("Enter your interest rate (in %): "))

total_amount = initial + deposit

if withdrawal > total_amount:
    print("Insufficient funds for withdrawal.")
else:
    total_amount -= withdrawal
    interest = total_amount * (interest_rate / 100)
    total_amount += interest

    print("Total interest earned:", interest)
    print("Total amount after deposit, withdrawal, and interest:", total_amount)
