class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.add_transaction("Deposit", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.add_transaction("Withdrawal", amount)
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.balance

    def add_transaction(self, description, amount):
        self.transactions.append({"description": description, "amount": amount})

    def display_transaction_history(self):
        print(f"Transaction history for Account {self.account_number}:")
        for transaction in self.transactions:
            print(f"{transaction['description']}: {transaction['amount']}")

