x = int(input("Enter the first side : "))
y = int(input("Enter the second side : "))
z = int(input("Enter the third side : "))

s = (x+y+z)/2
area_of_triangle = (s*(s-x)*(s-y)*(s-z))**0.5

print("The semi perimeter is : ", s)
print("The area of triangle is : ",area_of_triangle)