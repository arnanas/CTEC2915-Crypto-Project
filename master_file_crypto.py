#This is the master file for everything to be chucked in together

#Creating a procedure to hold the main menu procedure
def menu():
    error = False  #creating  two empty boolean values for while loops
    start = True #those while loops are used for robustness
    while start == True:
        while error == False:
            try: #different options users can select from
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
            except: #if coice isnt one of the options 
                error = True #loop whacks the user to the beggining
                print("Please try again")
                menu()
menu()
