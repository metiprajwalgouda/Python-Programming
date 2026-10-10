"""Simple calculator: take two numbers and an operator (+, -, *, /, %, **) and print the result. Handle division by zero without crashing."""
num1=int(input("Enter num 1 : "))
num2=int(input("Enter num 2 : "))
operator=input("Enter any operation which you want to perform on 2 numbers (eg: +,-,*,/,%,** ) please enter any one :")
if (operator == "+"):
    print(f"The sum of 2 numbers : {num1 + num2}")
elif(operator == "-"):
    print(f"The difference between num1 and num 2 is : {num1 - num2}")
elif(operator == "*"):
    print(f"The product of 2 numbers is : {num1 * num2}")
elif(operator == "%"):
    if num2 ==0:
        print("Modulo by zero is not possible")
    else:
        print(f"The modulo of 2 num is : {num1 % num2}")
elif(operator == "**"):
    print(f"The exponential power of num1 to num2 is : {num1 ** num2}")
elif(operator == "/"):
    if num2 == 0:
        print("division by zero is not possible")
    else:
        print(f"The division of 2 numbers is : {num1 / num2}")
else:
    print("Enter a valid numbers")