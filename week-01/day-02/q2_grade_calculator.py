"""
Take marks from 0 to 100 and print a grade: 90 and above is A, 75 to 89 is B, 50 to 74 is C, below 50 is Fail. If the marks are outside 0 to 100, print “Invalid marks”.
"""

marks=int(input("Enter marks (0-100) to check grade : "))
if marks < 0 or marks > 100:
    print("Invalid Marks.")
elif marks >= 90:
    print("Grade A")
elif marks >=75:
    print("Grade B")
elif marks >=50:
    print("Grade C")
else:
    print("FAIL")
