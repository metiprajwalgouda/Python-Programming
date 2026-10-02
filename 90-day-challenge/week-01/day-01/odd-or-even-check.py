user_input=input("Enter a number to check even or odd : ")
if user_input.isdigit():
    num=int(user_input)
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Please Enter a Valid Number ")
