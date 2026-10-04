marks=int(input("Enter the marks to know your grade : "))
if (marks>0 and marks<100):
    if marks>=90:
        print("Grade A")
    elif marks<=89 and marks>=75:
        print("Grade B")
    elif marks<=74 and marks>=60:
        print("Grade C")
    elif marks<=59 and marks>=40:
        print("Grade D")
    elif marks<40:
        print("Fail")

else:
    print("Enter a valid marks")