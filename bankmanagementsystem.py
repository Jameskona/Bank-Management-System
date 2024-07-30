
#BANK MANAGEMENT SYSTEM
"""The program ensures input validation and provides appropriate feedback to the user.
When you run this program, it allows you to simulate a basic bank management system by creating accounts, 
depositing money, withdrawing money, and checking balances. It uses the Bank class to manage accounts and account operations."""
class Account:
    def __init__(self, account_number, password, balance=0):
        self.account_number = account_number
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

    def verify_password(self, password):
        return self.password == password

class SavingsAccount(Account):
    pass

class CheckingAccount(Account):
    def __init__(self, account_number, password, balance=0, overdraft_limit=100):
        super().__init__(account_number, password, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance ")

def main():
    accounts = {}
    while True:
        print("***WELCOME TO BANK MANAGEMENT SYSTEM***")
        print("\n1: Create Account\n2: Login and Deposit\n3: Login and Withdraw\n4: Login and Check Balance\n5: Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            acc_type = input("Enter account type (savings/checking): ")
            acc_holder =input("Enter account holders name: ")
            acc_number = input("Enter account number: ").lower()
            password = input("Enter password: ")
            if acc_type == 'savings':
                accounts[acc_number] = SavingsAccount(acc_number, password)
            elif acc_type == 'checking':
                accounts[acc_number] = CheckingAccount(acc_number, password)
            print(f"Hi {acc_holder} your Account is created successfully!")
        elif choice in ['2', '3', '4']:
            acc_number = input("Enter account number: ")
            password = input("Enter password: ")
            if acc_number in accounts and accounts[acc_number].verify_password(password):
                if choice == '2':
                    amount = float(input("Enter amount to deposit: "))
                    accounts[acc_number].deposit(amount)
                elif choice == '3':
                    amount = float(input("Enter amount to withdraw: "))
                    accounts[acc_number].withdraw(amount)
                elif choice == '4':
                    print(f"your Balance is: {accounts[acc_number].get_balance()}")
            else:
                print("Account not found or incorrect password.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


"""***WELCOME TO BANK MANAGEMENT SYSTEM***

1: Create Account
2: Login and Deposit
3: Login and Withdraw
4: Login and Check Balance
5: Exit
Enter your choice: 1
Enter account type (savings/checking): savings
Enter account holders name: sriya
Enter account number: 123
Enter password: 1234
Hi sriya your Account is created successfully!
***WELCOME TO BANK MANAGEMENT SYSTEM***

1: Create Account
2: Login and Deposit
3: Login and Withdraw
4: Login and Check Balance
5: Exit
Enter your choice: 2
Enter account number: 123
Enter password: 1234
Enter amount to deposit: 500
Deposited: 500.0
***WELCOME TO BANK MANAGEMENT SYSTEM***

1: Create Account
2: Login and Deposit
3: Login and Withdraw
4: Login and Check Balance
5: Exit
Enter your choice: 4
Enter account number: 123
Enter password: 1234
your Balance is: 500.0
***WELCOME TO BANK MANAGEMENT SYSTEM***

1: Create Account
2: Login and Deposit
3: Login and Withdraw
4: Login and Check Balance
5: Exit
Enter your choice: 3
Enter account number: 200
Enter password: 1234
Account not found or incorrect password.
***WELCOME TO BANK MANAGEMENT SYSTEM***

1: Create Account
2: Login and Deposit
3: Login and Withdraw
4: Login and Check Balance
5: Exit
Enter your choice: 3
Enter account number: 123
Enter password: 1234
Enter amount to withdraw: 200
Withdrew: 200.0
***WELCOME TO BANK MANAGEMENT SYSTEM***

1: Create Account
2: Login and Deposit
3: Login and Withdraw
4: Login and Check Balance
5: Exit
Enter your choice: 4
Enter account number: 123
Enter password: 1234
your Balance is: 300.0
***WELCOME TO BANK MANAGEMENT SYSTEM***

1: Create Account
2: Login and Deposit
3: Login and Withdraw
4: Login and Check Balance
5: Exit
Enter your choice: 5"""