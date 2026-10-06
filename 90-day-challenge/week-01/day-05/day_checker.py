day=int(input("Enter a day number which u want to check (1-7): "))
if day<=7:
    if day == 1:
        print("Sunday")
    elif day == 2:
        print("Monday")
    elif day == 3:
        print("Tuesday")
    elif day == 4:
        print("Wednesday")
    elif day == 5:
        print("Thursday")
    elif day == 6:
        print("Friday")
    elif day == 7:
        print("Saturday")
else:
    print("Enter a value from 1 to 7 to check the day")
