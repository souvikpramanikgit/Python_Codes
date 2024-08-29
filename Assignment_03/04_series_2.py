n=int(input("Enter the number : "))
sum=0
for i in range(1,n+1):
    sum=sum+(1/(i**2))
print("Sum of series is : ",round(sum,2))