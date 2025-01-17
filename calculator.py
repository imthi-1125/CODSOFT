while True:
    num1=int(input("Enter a number 1:"))
    num2=int(input("Enter a number 2:"))
    add=num1+num2
    sub=num1-num2
    multi=num1*num2
    div=num1/num2 if num2!=0 else print("undefined by zero")
    operation=input("Enter your operation[add/sub/multi/div]:").lower()
    if (operation=="add"):
        print("addition of numbers:",add)
    elif(operation=="sub"):
        print("substraction of the numbers:",sub)
    elif(operation=="multi"):
        print("multipliation of the numbers:",multi)
    elif(operation=="div"):
        print("division of the numbers:",div)
    else:
        print("invalid operation")
    
    choice = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if choice!="yes":
       print("Exiting calculator...\nThank you for using calculator")
       break





    
        
    