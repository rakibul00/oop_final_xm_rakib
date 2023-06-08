class Bank:
    def __init__(self):
        self.users = {}
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def creact_account(self, user_id):
        if user_id in self.users:
            return "Account already exists."
        self.users[user_id] = {
            'balance': 0,
            'transactions': []
        }
        return "Account created successfully."

    def deposit(self, user_id, amount):
        if user_id not in self.users:
            return "Account does not exist."
        self.users[user_id]['balance'] += amount
        self.total_balance += amount
        self.users[user_id]['transactions'].append(f"Deposited: {amount}")
        return "Amount deposited successfully."

    def withdraw(self, user_id, amount):
        if user_id not in self.users:
            return "Account does not exist."
        if user_id in self.users and self.users[user_id]['balance'] >= amount:
            self.users[user_id]['balance'] -= amount
            self.total_balance -= amount
            self.users[user_id]['transactions'].append(f"Withdrawn: {amount}")
            return "Amount withdrawn successfully."
        else:
            return "Insufficient balance."

    def check_balance(self, user_id):
        if user_id not in self.users:
            return "Account does not exist."
        return f"Available balance: {self.users[user_id]['balance']}"

    def transfer(self, sender_id, receiver_id, amount):
        if sender_id not in self.users:
            return "Sender account does not exist."
        if receiver_id not in self.users:
            return "Receiver account does not exist."
        if self.users[sender_id]['balance'] >= amount:
            self.users[sender_id]['balance'] -= amount
            self.users[receiver_id]['balance'] += amount
            self.users[sender_id]['transactions'].append(f"Transferred: {amount} to {receiver_id}")
            self.users[receiver_id]['transactions'].append(f"Received: {amount} from {sender_id}")
            return "Amount transferred successfully."
        else:
            return "Insufficient balance."

    def check_transaction_history(self, user_id):
        if user_id not in self.users:
            return "Account does not exist."
        return self.users[user_id]['transactions']

    def take_loan(self, user_id):
        if user_id not in self.users:
            return "Account does not exist."
        if self.loan_feature_enabled:
            total_amount = self.users[user_id]['balance'] * 2
            self.users[user_id]['balance'] += total_amount
            self.total_loan_amount += total_amount
            self.users[user_id]['transactions'].append(f"Loan taken: {total_amount}")
            return f"Loan of {total_amount} granted."
        else:
            return "Loan feature is currently disabled."

    def admin_check_total_balance(self):
        return f"Total available balance of the bank: {self.total_balance}"

    def admin_check_total_loan_amount(self):
        return f"Total loan amount of the bank: {self.total_loan_amount}"

    def admin_enable_loan_feature(self):
        self.loan_feature_enabled = True
        return "Loan feature enabled."

    def admin_disable_loan_feature(self):
        self.loan_feature_enabled = False
        return "Loan feature disabled."


# Example usage:
bank = Bank()

# User operations
print(bank.creact_account("user1"))
print(bank.deposit("user1", 1000))
print(bank.withdraw("user1", 500))
print(bank.check_balance("user1"))
print(bank.transfer("user1", "user2", 200))
print(bank.check_transaction_history("user1"))
print(bank.take_loan("user1"))

# Admin operations
print(bank.admin_check_total_balance())
print(bank.admin_check_total_loan_amount())
print(bank.admin_disable_loan_feature())
