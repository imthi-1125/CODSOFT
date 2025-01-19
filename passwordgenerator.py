import random

def generate_password(length):
        char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
        password=''.join(random.choice(char)
        for _ in range(length))
        return password

def main():
        print("WELCOME TO THE PASSWORD GENERATOR!")
        while True:
            try:
                length=int(input("Enter the length of your password(0 to exit):"))
                if length == 0:
                    print("Exiting password generator...\nThank you!")
                    break
                elif length < 2:
                    print("Error:Password length must be atleast 2")
                    continue
                print("here's your generated password:",generate_password(length))
            except ValueError:
                print("Error:Enter a valid number")
if __name__=="__main__":
        main()

    
        
            
            
    