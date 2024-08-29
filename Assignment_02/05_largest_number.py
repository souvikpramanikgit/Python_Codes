a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
c=int(input("Enter the third number : "))

if a>b and a>c:
    print("Largest Number : ",a)
elif b>a and b>c:
    print("Largest Number : ",b)
else:
    print("Largest Number : ",c)
