n=int(input("Enter the number : "))
sum=0

while(n>0):
    reminder=n%10
    sum=sum+reminder
    n=n//10

print("Sum of the digits of given number : ",sum)