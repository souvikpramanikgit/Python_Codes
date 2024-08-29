# a=int(input("Enter the number : "))
# flag=0

for num in range(900,1001):
    if num>1:
      for i in range(2,num):
        if(num%i)==0:
            break
        else:
            print(num)