a=int(input("Enter marks : "))

if a>=90 and a<=100:
    print("Your Grade is 'O'")
elif a>=80 and a<=89:
    print("Your Grade is 'E'")
elif a>=70 and a<=79:
    print("Your Grade is 'A'")
elif a>=60 and a<=69:
    print("Your Grade is 'B'")
elif a>=50 and a<=59:
    print("Your Grade is 'Poor'")
elif a>=40 and a<=49:
    print("Your Grade is 'Very Poor'")
elif a<40:
    print("Your Grade is 'F'")