#crypto project v1

def menu():
    error = False
    start = True
    while start == True:
        while error == False:
            try:
                print("Would you like to Encrypt or Decrypt? (1 or 2)")
                print("1. Encrypt")                    
                print("2. Decrypt")
                print()
                choice = int(input("Choice:"))
                if choice == 1:
                    error = False
                elif choice == 2:
                    error = False
            except:
                error = True
                print("Please try again")
                menu()
menu()
