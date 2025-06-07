'''
This is the third and final version of my bank simulator program.
The program will now be based in easygui for better appearance,
user interface and efficiency. Some other issues will also
be fixed.
'''

#Importing easygui for better user interface and experience
from easygui import*




#function to get the user's name and age
def user_info():
    while True:
        name = enterbox("Enter your name:")  
        if name is None:
            exit() #This means if the user presses X or cancel, the program will exit.
        elif name == "":
            msgbox("You must enter a name.")  # Ensures the user doesn't leave it blank
        elif not name.isalpha():
            msgbox("Name can only contain letters")  #Prevents numbers or special characters
        else:
            break

    while True:
        age = enterbox("Enter your age:")  #Prompts for age
        if age is None:
            exit()  #Allows the user to cancel and exit
        try:
            age = int(age)  #Converts input to integer
            if age < 0:
                msgbox("Age cannot be negative.")  #Prevents negative input
            elif age > 100:
                msgbox("Please enter your real age.")  #Prevents unrealistic ages
            elif age < 12:
                msgbox(f"You are too young. Come again when you have turned {MIN_AGE}.")  # Age restriction for system use
                exit()
            else:
                msgbox(f"Welcome, {name}, {age} years of age.")  # Confirmation message
                return name  #Makes name an accessible variable for other functions
        except ValueError:
            msgbox("Invalid input. Please enter a valid integer age.")  # Handles non-numeric input


# Function for the user's initial balance
def start_bal(): 
    while True:
        start = enterbox("Enter your starting balance:")  
        if start is None:
            exit()
        try:
            balance = float(start)  # Converts to float
            if balance < 0:
                msgbox("Balance cannot be negative.")  # Prevents negative starting balance
            else:
                return balance  # Allows balance to be accessible to other functions
        except ValueError:
            msgbox("Invalid input. Please enter a number.")  # Handles invalid entries


# Function for when the user wants to deposit into their account
def deposit(balance):  #Putting balance as a parameter allows deposit function to access it
    while True:
        amt = enterbox("How much would you like to deposit?")
        if amt is None:
            return balance  #amt remains unchanged if user cancels
        try:
            amount = float(amt)
            if amount < 0:
                msgbox("You cannot deposit a negative amount.")  #Negative deposit not allowed
            else:
                balance += amount  #Adds to balance if deposit occurs
                msgbox(f"Deposit successful. Your new balance is ${balance:.2f}") 
                return balance
        except ValueError:
            msgbox("Please enter a valid number.")  #Ensures the user enters a number


#Function for when the user wants to withdraw from their account
def withdraw(balance): 
    while True:
        amt = enterbox("How much would you like to withdraw?")
        if amt is None:
            return balance  # Return unchanged if user cancels
        try:
            amount = float(amt)
            if amount < 0:
                msgbox("You cannot withdraw a negative amount.")  
            elif amount > balance:
                msgbox("Your withdrawal cannot exceed your current balance.")  #Preventing overdraft
            else:
                balance -= amount  #Subtracts from balance if withdrawal occurs
                msgbox(f"Withdrawal successful. Your new balance is ${balance:.2f}")  # Confirmation message
                return balance
        except ValueError:
            msgbox("Please enter a valid number.")  





# Main function to run the program
def main():
    name = user_info()  #Gives main function access to the name variable defined

    #User decides if they want to use the program
    choice = buttonbox("Would you like to use the banking system?", choices=["Yes", "No"])
    if choice == "No":
        msgbox("No worries. Goodbye!")  
        return #exits
    elif choice is None:
        exit()

    balance = start_bal()  #Get starting balance
  

    while True:  #using a while loop allows the user to continue depositing or withdrawing
        action = buttonbox("What would you like to do?", choices=["Deposit", "Withdraw", "Quit"])
        if action == "Deposit":
            balance = deposit(balance)  #Calling deposit function
            
        elif action == "Withdraw":
            balance = withdraw(balance)  #Calling withdraw function
            
        elif action == "Quit":
            msgbox(f"Thank you, {name}. Your final balance is ${balance:.2f}. Goodbye!")  # Exit message
            
            break
        elif action is None:
            msgbox("You have exited the program. Goodbye!")
            exit()


#Run the program by calling main function
main()
