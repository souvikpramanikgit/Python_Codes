n=int(input("Enter the number : "))
sum=0
i=0
while(i<=n):
    sum=sum+i
    i=i+1
avg = sum/n

print("The sum of", n, "numbers is : ",sum)
print("The average of", n, "numbers is : ",avg)