a=int(input("Enter the number : "))
flag=0

if a>1:
    for i in range(1,a+1):
        if(a%i==0):
            flag=flag+1
if flag==2:
    print(a,"is a prime number")
else:
    print(a,"is not a prime number")