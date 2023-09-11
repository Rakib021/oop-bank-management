from account import Account

class User:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, initial_deposit):
        account_number = len(self.accounts) + 1
        account = Account(account_number, name, initial_deposit)
        self.accounts.append(account)
        return account

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)

        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                from_account.add_transaction(f"Transfer to account {to_account_number}", amount)
                to_account.add_transaction(f"Transfer from account {from_account_number}", amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds in the source account.")
        else:
            print("Invalid account number.")
            
    def take_loan(self, account_number):
        account = self.get_account(account_number)
        if account:
            loan_amount = account.balance * 2
            account.deposit(loan_amount)
            account.add_transaction("Loan", loan_amount)
            print(f"Loan of {loan_amount} successfully added to Account {account_number}.")
        else:
            print("Invalid account number.")

    def get_transaction_history(self, account_number):
        account = self.get_account(account_number)
        if account:
            account.display_transaction_history()
        else:
            print("Invalid account number.")