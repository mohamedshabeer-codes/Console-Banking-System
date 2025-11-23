class BankAccount:

    def __init__(self, balance=50000.0, pin=1234):
        # Initialize account with default balance and PIN
        self.balance = balance
        self.pin = pin

    def deposit(self):
        # PIN verification before transaction
        password = int(input("Enter your pin: "))
        if password != self.pin:
            print("Incorrect PIN!, Transaction Failed!")
            return

        try:
            # Accept deposit amount and update balance
            amount = float(input("Enter amount to deposit: "))
            self.balance += amount
            print(f"Deposit successful. Total balance: {self.balance} \nThank you for banking with us!")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def withdraw(self):
        # PIN verification before transaction
        password = int(input("Enter your pin: "))
        if password != self.pin:
            print("Incorrect PIN!, Transaction Failed!")
            return

        try:
            # Accept withdrawal amount and check balance
            amount = float(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawal successful. Total balance: {self.balance} \nThank you for banking with us!")
            else:
                print("Insufficient balance!")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def get_balance(self):
        # PIN verification before showing balance
        password = int(input("Enter your pin: "))
        if password != self.pin:
            print("Incorrect PIN!, Transaction Failed!")
            return
        print(f"Your balance is: {self.balance} \nThank you for banking with us!")

    def change_pin(self):
        # Verify existing PIN before changing it
        password = int(input("Enter your pin: "))
        if password != self.pin:
            print("Incorrect PIN!, Transaction Failed!")
            return

        try:
            # Update to new PIN
            new_pin = int(input("Enter new PIN: "))
            self.pin = new_pin
            print("PIN updated successfully! \nThank you for banking with us!")
        except ValueError:
            print("Invalid PIN format!")

    def menu(self):
        # Main menu loop
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Change PIN")
            print("5. Exit")

            try:
                # User menu selection
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid Input! Enter a number.")
                continue

            # Call respective functions based on choice
            if choice == 1:
                self.deposit()
            elif choice == 2:
                self.withdraw()
            elif choice == 3:
                self.get_balance()
            elif choice == 4:
                self.change_pin()
            elif choice == 5:
                print("Thank you for banking with us!")
                break
            else:
                print("Invalid choice!")

# Object creation and starting the menu
shabeer_acc = BankAccount()
shabeer_acc.menu()