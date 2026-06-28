pin = 1234
balance = 50000

user_pin = int(input("Enter your PIN: "))

if user_pin == pin:

    print("Welcome Kashan Bank ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))

        if amount > 0:
            balance = balance + amount
            print("New balance is:", balance)
        else:
            print("Invalid amount")

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient Balance")
        else:
            balance = balance - amount
            print("Remaining balance is:", balance)

    else:
        print("Invalid Choice")

else:
    print("Access Blocked")