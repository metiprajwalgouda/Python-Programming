"""
2. Area Calculator: Write a function area_of_rectangle(width, length) that returns the area of a rectangle. Provide a default argument of 1 for the length if it isn't specified.

"""

def area_calculator(width,length=1):
    area=length*width
    print(f"Area : {area}")
area_calculator(2,3)