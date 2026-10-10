"""
3. Max of Three: Write a function find_max(a, b, c) that accepts three numbers and returns the largest one without using Python's built-in max() function.
"""

def find_max(a,b,c):
    if a>b and a>c:
        print(f"a is greater")
    elif b>c and b>a:
        print(f"b is greater")
    elif c>b and c>a:
        print(f"c is greater")
find_max(2,4,5)
