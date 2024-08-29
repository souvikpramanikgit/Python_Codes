m=input("Enter any input : ")

if (m>='A' and m<='Z') or (m>='a' and m<='z'):
    print("You entered a alphabet.")
elif (m>='0') and (m<='9'):
    print("You entered a number.")
else:
    print("You entered a special character.")
