"""
Take a number and print whether it is positive, negative, or zero.
"""

num=int(input("Enter a number to check positive,negative or zero : "))
if num<0:
    print("Negative Number.")
elif num>0:
    print("Positive Number.")
elif num==0:
    print("It is zero.")
