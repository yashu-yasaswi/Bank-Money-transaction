# bank.py
import os

class Bank:
    def __init__(self, initial_amount=0.00, transaction_file="transaction.txt"):
        self.balance = initial_amount
        self.transaction_file = transaction_file
        self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.transaction_file):
            with open(self.transaction_file, "r") as file:
                lines = file.readlines()
                if lines:
                    # Get the last balance from the last line
                    last_transaction = lines[-1].strip().split()
                    self.balance = float(last_transaction[-1])

    def log_transaction_details(self, details):
        with open(self.transaction_file, "a") as file:
            file.write(f"{details:<20} balance: {self.balance:.1f}\n")

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount and self.balance >= amount:
            self.balance -= amount
            self.log_transaction_details(f"Withdrew: {amount}")
            return True, self.balance
        else:
            return False, "Insufficient funds"

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance += amount
            self.log_transaction_details(f"Deposited: {amount}")
            return True, self.balance
        return False, "Invalid amount"
