print("Enter Your Marks To Check You are Pass or Fail !!!!!!!!!!!!!")
print("============================================================")

sub1 = float(input("Enter your Secured Mark Of Odia: "))
sub2 = float(input("Enter your Secured Mark Of English: "))
sub3 = float(input("Enter your Secured Mark Of Hindi: "))
sub4 = float(input("Enter your Secured Mark Of Mathmetics: "))
sub5 = float(input("Enter your Secured Mark Of General Science: "))
sub6 = float(input("Enter your Secured Mark Of Social Science: "))

print("============================================================")

total_mark = sub1 + sub2 + sub3 + sub4 + sub5
total_per = total_mark / 600 * 100

print("Your Total Mark is: ", total_mark)
print("Your Secured percentage(%) is: ", total_per)

if total_per < 33:
    print("You are fail")
else:
    print("Congratulations You Are Passed In Exam !")