import math

while True:
    try:
        num1=int(input("Enter a number 1:"))
        num2=int(input("Enter a number 2:"))
    
        operation=input("Enter your operation[add/sub/multi/div/sqrt/power]:").lower()
    
        add=num1+num2
        sub=num1-num2
        multi=num1*num2
        div = "undefined by zero" if num2 == 0 else num1 / num2
        sqrt=math.sqrt
        power=math.pow

    
        if (operation=="add"):
            print("Addition of the numbers:", add)
        elif(operation=="sub"):
            print("Substraction of the numbers:",sub)
        elif(operation=="multi"):
            print("Multipliation of the numbers:",multi)
        elif(operation=="div"): 
            print(f"Division of the numbers:",div)
        elif(operation=="sqrt"):
            sqrt=math.sqrt(num1)
            sqrt1=math.sqrt(num2)
            print("square root of the given numbers:",sqrt ,sqrt1)
        elif (operation=="power"):
            power=math.pow(num1,num2)
            print(f"{num1} raised to the power of {num2} is: {power}")
        else:
            print("invalid operation,Please enter a valid operation[add/sub/multi/div/sqrt/power]")
    except ValueError:
        print("Invalid input! Please enter numbers only.")
    choice = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if choice!="yes":
       print("Exiting calculator...\nThank you for using calculator")
       break
