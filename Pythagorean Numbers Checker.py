while True:
    Number1 = float(input("Enter the first number: "))
    Number2 = float(input("Enter the second number: "))
    Number3 = float(input("Enter the third number: "))
    
    Numbers = [Number1, Number2, Number3]
    Numbers.sort()
    
    if Numbers[2]**2 == Numbers[1]**2 + Numbers[0]**2:
        print("Yes")
    else:
        print("No")
