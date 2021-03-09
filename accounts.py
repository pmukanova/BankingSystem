import pandas as pd
import exception
import connection as cn


class BalanceError(Exception):
    pass


class BankAccounts():
    def __init__(self, account_number, balance, account_type, date_created):
        self.account_number, self.account_type = account_number, account_type
        self.balance, self.date_created = balance,  date_created
        if balance < 0:
            raise ValueError("Invalid balance!")
        self._balance = balance

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self):
        self.created_at = pd.to_datetime('today').date()

    def deposit(amount, account_number):
        balance = cn.pull_balance(account_number)
        balance += float(amount)
        print("\n Amount deposited: $", float(amount), "\nYour balance now: $", balance)

    def withdraw(amount, account_number):
        balance = cn.pull_balance(account_number)
        if balance < float(amount):
            raise BalanceError("Insufficient balance. Please, enter different amount. ")
        else:
            balance -= float(amount)
            print("\n Amount withdrawn: $", float(amount), "\nYour balance now: $", balance)

    def check_balance(account_number):
        balance = cn.pull_balance(account_number)
        print("\n Your Balance is $", balance)

    def create_account(customer_id, acc_type):
        balance = float(
            input("Please, enter initial deposit for the {} account: \n".format(acc_type)))
        created_at = pd.to_datetime('today').date()
        account_type = acc_type
        cn.push_account(customer_id, account_type, balance, created_at)
        acc_data = cn.pull_account(customer_id)
        account_number = acc_data[0][0]
        print("Success! Your {} account number is: ".format(account_type),
              account_number, "\nBalance: ${}".format(acc_data[0][3]))


class CheckingAccount(BankAccounts):

    def __init__(self, account_number, balance, account_type, date_created, limit):
        super.__init__(self, account_number, balance, account_type)
        self.limit = limit
        self.account_type = "Checking"

    def withdraw(self, amount, account_number, fee=0):
        if fee <= self.limit:
            BankAccounts.withdraw(self, amount - fee)
        else:
            BankAccounts.withdraw(self, amount - self.limit)


class SavingsAccount(BankAccounts):
    def __init__(self, account_number, balance, account_type, date_created, interest_rate):
        super.__init__(self, account_number, balance, account_type,
                       date_created)
        self.interest_rate = interest_rate
        account_type = "Savings"

    def compute_interest(self, n_periods=1):
        return self.balance * ((1 + self.interest_rate) ** n_periods - 1)
