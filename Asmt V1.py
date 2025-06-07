#This is version 1 of my bank account simulator program

name = input("Enter your name: ")

while True:
    try:
        age = int(input("Please enter your age: "))
        if age < 12:
            print("You are too young. Come again when you have turned 12.")
            exit()
        else:
            print(f"Hello {name}, {age} years of age.")
            break #Program continues if the user is the appropriate age
    except ValueError:
        print("Invalid input. Please enter a valid integer age.")


print("This system allows you to withdraw or deposit money.")

#.strip and .lower allows any capitalization and spaces entered
ans = input("Would you like to use the system? (yes/no) : ").strip().lower()

if ans == "yes":
    while True:
        try:
            balance = float(input("Enter your starting balance: "))
            if balance < 0:
                print("Balance cannot be negative.")
            else:   
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        choice = input("Would you like to deposit or withdraw? ").strip().lower()
        if choice == "deposit":
            #While loop for deposits
            while True:
                try:
                    dep_amt = float(input("How much would you like to deposit? : "))
                    if dep_amt < 0:
                        print("You cannot enter a negative number.")
                    else:
                        balance += dep_amt #deposit amt is added to balance
                        print(f"Your new balance is ${balance:.2f}")#Rounds result to 2 decimal points
                        break
                except ValueError:
                    print("Please enter a valid number.")
            break

        elif choice == "withdraw":
            #While loop for withdrawals
            while True:
                try:
                    with_amt = float(input("How much would you like to withdraw? : "))
                    if with_amt < 0:
                        print("You cannot enter a negative number.")
                    elif with_amt > balance:
                        print("You cannot exceed your balance.")
                    else:
                        balance -= with_amt #withdrawal amt is subtracted from balance
                        print(f"Your new balance is ${balance:.2f}")
                        break
                except ValueError:
                    print("Please enter a valid number.")
            break

        else:
            print("Invalid choice. Please enter 'deposit' or 'withdraw'.")

else:
    print("Thank you. Goodbye!")#User enters something other than yes
