year=int(input("Enter a year to check it is leap year or not : "))
if ((year%4==0 and year%100!=0) or year%400==0):
    print(f"The Year {year} is a leap year ")
else:
    print(f"The Year {year} is not a leap year")
