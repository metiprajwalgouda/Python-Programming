a=int(input("Side 1 : "))
b=int(input("Side 2 : "))
c=int(input("Side 3 : "))

if a<=0 and b<=0 and c<=0:
    print("Triangles Sides Must be Positive")
elif a+b>c and b+c>a and a+c>b:
    if a==b and b==c:
        print("All 3 Sides are equal so it is Equilateral Triangle.")
    elif a==b or b==c or a==c:
        print("It is Isosceles Triangle.")
    else:
        print("Scalene")
else:
    print("Not a triangle.")