"""
Take two numbers from the user and print their sum, difference, product, division, floor division, remainder, and the first number raised to the power of the second.
"""

num1=int(input("Enter num 1 : "))
num2=int(input("Enter num 2 : "))
sum=num1+num2
difference=num1-num2
product=num1*num2
division=num1/num2
floor_division=num1//num2
remainder=num1%num2
power=num1**num2
print(f"Sum of 2 numbers is : {sum}")
print(f"Difference of 2 numbers is : {difference}")
print(f"Product of 2 numbers is : {product}")
print(f"Divison of num 1 by num 2 is : {division}")
print(f"Floor division of num 1 and num 2 is : {floor_division}")
print(f"Remainder of num 1 divided by num 2 is : {remainder}")
print(f"Power of num 1 to num 2 is : {power}")