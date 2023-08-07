class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount} units. New balance: {self.balance}")

    def get_balance(self):
        return self.balance
def main():
    account_number = input("Enter account number: ")
    account = BankAccount(account_number)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            amount = float(input("Enter the deposit amount: "))
            account.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter the withdrawal amount: "))
            account.withdraw(amount)
        elif choice == 3:
            print("Current balance:", account.get_balance())
        elif choice == 4:
            print("Exiting the Bank Account Management System.")
            break
        else:
            print("Invalid choice. Try again.")
main()