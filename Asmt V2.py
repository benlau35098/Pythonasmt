#This is version 2 of my bank simulator program. Various functions and new features have been added.

#Function to get the user's name and age
def user_info():
    while True:
        name = input("Enter your name: ")
        print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
        if name == "":
            print("You must enter a name. ")
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
        elif not name.isalpha():
            print("Name can only contain letters")
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
        else:
            break

    while True:
        try:
            age = int(input("\nEnter your age: "))
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")

            if age < 0:

                print("\nAge cannot be negative.")
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")

            #No trivial ages can be entered
            elif age > 120:

                print("\nPlease enter your real age. ")
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            #Age limit for program is 12   
            elif age < 12:

                print("\nYou are too young. Come again when you have turned 12.")
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
                exit()
            
            else:

                print(f"\nWelcome, {name}, {age} years of age.")
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
                return name #makes name an accessible variable for other functions

        except ValueError:

            print("\nInvalid input. Please enter a valid integer age.")
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")


#Function for the user's initial balance
def start_bal(): 
    while True:
        try:
            balance = float(input("\nEnter your starting balance: "))
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            if balance < 0:
                print("\nBalance cannot be negative.")
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            else:
                return balance #allows balance to be accesible to other functions 
        except ValueError:
            print("\nInvalid input. Please enter a number.")
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")


#Function for when the user wants to deposit into their account
def deposit(balance): #putting balance as a parameter allows dep function to access it
    while True:
        try:
            amount = float(input("\nHow much would you like to deposit? "))
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            if amount < 0:
                print("\nYou cannot deposit a negative amount.")
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            else:
                balance += amount #adds to balance if deposit occurs
                print(f"\nDeposit successful. Your new balance is ${balance:.2f}")
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
                return balance
        except ValueError:
            print("\nPlease enter a valid number.")
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")


#Function for when the user wants to withdraw from their account
def withdraw(balance): 

    while True:

        try:
            amount = float(input("\nHow much would you like to withdraw? "))
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")

            if amount < 0:
                print("\nYou cannot withdraw a negative amount.")
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")

            elif amount > balance:
                print("\nYour withdrawal cannot exceed your current balance.") #Withdrawal cannot go over balance
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")

            else:
                balance -= amount #subtracts from balance if withdrawal occurs
                print(f"\nWithdrawal successful. Your new balance is ${balance:.2f}")
                print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
                return balance

        except ValueError:
            print("\nPlease enter a valid number.")
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")

def main():

    name = user_info()#Gives main function access to the name variable defined 

    while True:
        
        ans = input("\nThis system allows you to withdraw and/or deposit money.\n\nWould you like to use the system? (yes/no): ").strip().lower()
        print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
        if ans in ("yes", "no"): #Ensures that the user can only type yes or no
            break
        else:
            print("\nPlease enter 'yes' or 'no' only.")
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")

    if ans == "no":
        print("\nNo worries. Goodbye!")
        print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
        return

    balance = start_bal()

    while True: #using a while loop which encapsulates these functions allow the user to infinitely withdraw and deposit.

        choice = input("\nWould you like to deposit, withdraw, or quit? ").strip().lower()

        if choice == "deposit":
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            balance = deposit(balance) #calling the functions based on what the user chooses to do

        elif choice == "withdraw":
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            balance = withdraw(balance)

        elif choice == "quit":
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            print(f"\nThank you, {name}. Your final balance is ${balance:.2f}. Goodbye!")#using :.2f gives balance at 2dp
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")
            break

        else:
            print("\nInvalid choice. Please enter 'deposit', 'withdraw', or 'quit'.")
            print("\n*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*.*")

#Run the program
main()
