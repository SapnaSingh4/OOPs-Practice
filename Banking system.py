#OOPs Practice
#Creating BankAccount
class BankAccount:
    def __init__(self):
        self.acc_holder_name = "Sapna"
        self.acc_num = "234598764567"
        self.pin = "2345"
        self.balance = 0

    def menu(self):
        while True:
            user_input = input("""
            Hi! How can I help you?
            1. Check your account details
            2. Deposit money
            3. Withdraw money
            4. Check your balance
            5. Exit
            Enter your choice: """)
            
            if user_input == '1':
                self.acc_detail()
            elif user_input == '2':
                self.deposit()
            elif user_input == '3':
                self.withdraw()
            elif user_input == '4':
                self.check_balance()
            elif user_input == '5':
                print("Thank you for using our service. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def acc_detail(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            print(f"""
            Account Holder Name: {self.acc_holder_name}
            Account Number: {self.acc_num}
            """)
        else:
            print("Invalid PIN! Please try again.")

    def deposit(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            try:
                dep_amount = float(input("Enter the amount to deposit: "))
                if dep_amount > 0:
                    self.balance += dep_amount
                    print(f"You have successfully deposited ₹{dep_amount:.2f}.")
                else:
                    print("Deposit amount must be positive.")
            except ValueError:
                print("Invalid amount entered. Please try again.")
        else:
            print("Invalid PIN! Please try again.")

    def withdraw(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            try:
                with_amount = float(input("Enter the amount to withdraw: "))
                if with_amount > 0:
                    if with_amount <= self.balance:
                        self.balance -= with_amount
                        print(f"You have successfully withdrawn ₹{with_amount:.2f}.")
                    else:
                        print("Insufficient balance.")
                else:
                    print("Withdrawal amount must be positive.")
            except ValueError:
                print("Invalid amount entered. Please try again.")
        else:
            print("Invalid PIN! Please try again.")

    def check_balance(self):
        user_pin = input("Enter your PIN: ")
        if user_pin == self.pin:
            print(f"Your current balance is: ₹{self.balance:.2f}")
        else:
            print("Invalid PIN! Please try again.")


account = BankAccount()
account.menu()
