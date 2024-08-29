n=int(input("Enter the number : "))
sum=0
for i in range(1,n+1):
    sum=sum+((i**2)/i)
print("Sum of series is : ",round(sum,2))