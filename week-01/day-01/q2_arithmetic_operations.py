"""
Take two numbers from the user and print their sum, difference, product, division, floor division, remainder, and the first number raised to the power of the second.
"""

num1=int(input("Enter num 1 : "))
num2=int(input("Enter num 2 : "))
sum_result=num1+num2
print(f"Sum of 2 numbers is : {sum_result}")
difference_result=num1-num2
print(f"Difference of 2 numbers is : {difference_result}")
product_result=num1*num2
print(f"Product of 2 numbers is : {product_result}")
if num2!=0:
    division_result=num1/num2
    print(f"Divison of num 1 by num 2 is : {division_result}")
    floor_division_result=num1//num2
    print(f"Floor division of num 1 and num 2 is : {floor_division_result}")
    remainder_result=num1%num2
elif num2==0:
    print("division by zero is not possible ")
power_result=num1**num2
print(f"Power of num 1 to num 2 is : {power_result}")