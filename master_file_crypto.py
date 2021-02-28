#This is the master file for everything to be chucked in together

def menu():
    error = False
    start = True
    while start == True:
        while error == False:
            try:
                print("Would you like to Encrypt or Decrypt? (1 or 2)")
                print("1. Encrypt")                    
                print("2. Decrypt")
                print("3. Quit")
                print()
                choice = int(input("Choice:"))
                if choice == 1:
                    error = False
                elif choice == 2:
                    error = False
                elif choice == 3:
                    quit()
            except:
                error = True
                print("Please try again")
                menu()
menu()
