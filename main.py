from user import User
from admin import Admin

if __name__ == "__main__":
    bank = User()
    admin = Admin(bank)
   

    while True:
        print("1. User Menu")
        print("2. Admin Menu")
        print("3. Exit")


        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                print("1. Create Account")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Take Loan")
                print("6. Check Transaction History")
                print("7. Check Balance")
                print("8. Exit to Main Menu")

                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                   name = input("Enter your name: ")
                   initial_deposit = float(input("Enter initial deposit: "))
                   account = bank.create_account(name, initial_deposit)
                   print(f"Account created successfully. Account number: {account.account_number}")

                elif user_choice == 2:
                     account_number = int(input("Enter account number: "))
                     account = bank.get_account(account_number)
                     if account:
                        amount = float(input("Enter deposit amount: "))
                        account.deposit(amount)
                        print("Deposit successful.")
                     else:
                         print("Invalid account number.")

                elif user_choice == 3:
                      account_number = int(input("Enter account number: "))
                      account = bank.get_account(account_number)
                      if account:
                         amount = float(input("Enter withdrawal amount: "))
                         account.withdraw(amount)
                         print("Withdrawal successful.")
                      else:
                         print("Invalid account number.")
            
                elif user_choice == 4:
                     from_account_number = int(input("Enter source account number: "))
                     to_account_number = int(input("Enter target account number: "))
                     amount = float(input("Enter transfer amount: "))
                     bank.transfer(from_account_number, to_account_number, amount)

                elif user_choice == 5:
                     account_number = int(input("Enter account number: "))
                     bank.take_loan(account_number)

                elif user_choice == 6:
                    account_number = int(input("Enter account number: "))
                    bank.get_transaction_history(account_number)

                elif user_choice == 7:
                     account_number = int(input("Enter account number: "))
                     account = bank.get_account(account_number)
                     if account:
                        balance = account.get_balance()
                        print(f"Account balance: {balance}")
                     else:
                        print("Invalid account number.")

                elif user_choice == 8:
                     break

                else:
                   print("Invalid choice. Please try again.")

        elif choice == 2:
            while True:
                print("1. Create Account (Admin)")
                print("2. Check Total Available Balance (Admin)")
                print("3. Check Total Loan Amount (Admin)")
                print("4. Toggle Loan Feature (Admin)")
                print("5. Exit to Main Menu (Admin)")

                admin_choice = int(input("Enter your choice: "))

                if admin_choice == 1:
                    name = input("Enter user's name: ")
                    initial_deposit = float(input("Enter initial deposit: "))
                    admin.create_account(name, initial_deposit)

                elif admin_choice == 2:
                    admin.check_total_balance()

                elif admin_choice == 3:
                    admin.check_total_loan()

                elif admin_choice == 4:
                    enable_loan = input("Enter 'on' to enable or 'off' to disable the loan feature: ")
                    admin.toggle_loan_feature(enable_loan.lower() == "on")

                elif admin_choice == 5:
                    break

                else:
                    print("Invalid choice. Please try again.")

        elif choice == 3:
            break

        else:
            print("Invalid choice. Please try again.")
