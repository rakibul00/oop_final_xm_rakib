class User:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact
        self.account_balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.account_balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            self.transaction_history.append(f"Withdrawal: -{amount}")
        else:
            print("Insufficient funds.")

    def transfer(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            recipient.account_balance += amount
            self.transaction_history.append(f"Transfer: -{amount} to {recipient.name}")
            recipient.transaction_history.append(f"Transfer: +{amount} from {self.name}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.account_balance

    def get_transaction_history(self):
        return self.transaction_history


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, address, contact):
        user = User(name, address, contact)
        self.bank.users.append(user)
        return user

    def check_total_balance(self):
        total_balance = sum(user.get_balance() for user in self.bank.users)
        return total_balance

    def check_total_loan_amount(self):
        total_loan_amount = sum(user.get_balance() for user in self.bank.users if user.get_balance() > 0)
        return total_loan_amount

    def toggle_loan_feature(self, enabled):
        self.bank.loan_feature_enabled = enabled


class Bank:
    def __init__(self):
        self.users = []
        self.loan_feature_enabled = True

    def is_bankrupt(self):
        return sum(user.get_balance() for user in self.users) < 0


# Usage example:
bank = Bank()
admin = Admin(bank)

# Create accounts
user1 = admin.create_account("rakib", "123 Main ra", "rakib@example.com")
user2 = admin.create_account("rakib khan", "456 Elm ra", "rakib@.com")

# Deposit money
user1.deposit(500)
user2.deposit(1000)

# Withdraw money
user1.withdraw(200)

# Transfer money
user1.transfer(100, user2)

# Check balance
balance = user1.get_balance()
print(f"User1 balance: {balance}")

# Check transaction history
history = user1.get_transaction_history()
print("User1 transaction history:")
for transaction in history:
    print(transaction)

# Take a loan
if bank.loan_feature_enabled:
    user1.deposit(user1.get_balance())
    balance = user1.get_balance()
    print(f"User1 balance after loan: {balance}")
else:
    print("Loan feature is currently disabled.")

# Check total bank balance
total_balance = admin.check_total_balance()
print(f"Total bank balance: {total_balance}")

# Check total loan amount
total_loan_amount = admin.check_total_loan_amount()
print(f"Total loan amount: {total_loan_amount}")

# Toggle loan feature
admin.toggle_loan_feature(False)
if bank.is_bankrupt():
    print("The bank is bankrupt.")
else:
    print("The bank is still operational.")
