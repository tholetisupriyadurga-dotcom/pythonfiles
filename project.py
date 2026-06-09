name = input("Enter Account Holder Name: ")
pin = input("Set a 4-digit PIN: ")

balance = 100000

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    entered_pin = input("Enter PIN: ")

    if entered_pin != pin:
        print("Incorrect PIN!")
        continue

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(name, balance, "₹{balance}")

    elif choice == "2":
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print("Deposit Successful!")
        print("Updated Balance: ₹", balance)

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance: ₹", balance)
        else:
            print("Insufficient Balance!")

    elif choice == "4":
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid Choice! Please try again.")        
          
