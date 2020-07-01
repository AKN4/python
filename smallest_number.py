number1=int(input("number1: "))
number2=int(input("number2: "))
number3=int(input("number3: "))
if number1<number2 and number1<number3:
    print("number 1 is the smallest")
elif number2<number1 and number2<number3:
    print("number 2 is the smallest")
else:
    print("number 3 is the smallest")