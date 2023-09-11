
class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, initial_deposit):
        account = self.bank.create_account(name, initial_deposit)
        print(f"Account created successfully. Account number: {account.account_number}")

    def check_total_balance(self):
        total_balance = sum(account.get_balance() for account in self.bank.accounts)
        print(f"Total available balance in the bank: {total_balance}")

    def check_total_loan(self):
        total_loan = sum(account.get_balance() for account in self.bank.accounts if account.balance < 0)
        print(f"Total loan amount in the bank: {abs(total_loan)}")

    def toggle_loan_feature(self, enable):
        self.bank.loan_feature_enabled = enable
        status = "enabled" if enable else "disabled"
        print(f"Loan feature is now {status}.")