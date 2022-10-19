
from .owner import Owner
import csv


class Account:
    accounts_list = []

    def __init__(self, id, balance, open_date, bank):
        self.id = id
        self.balance = balance
        self.open_date = open_date
        self.bank = bank

        for owner in Owner.owner_list:
            print(self.id)
            print(owner.id)
            if self.id == owner.id:
                self.owner_account = owner
            else:
                self.owner_account = None

        Account.accounts_list.append(self)


    def all_accounts(bank):
        with open(f"./support/accounts.csv", "r") as csvfile:
            accounts_dict = csv.DictReader(csvfile, delimiter = ',', skipinitialspace=True)

            for account in accounts_dict:
                account['bank'] = bank
                Account(**account)


    def withdraw(id, amount):
        for account in Account.accounts_list:
            if account.id == id:
                if account.balance - amount < 0:
                    return 'Cannot withdraw more than what is remaining in your bank balance'
                else:
                    account.balance -= amount
                    return f"Amount of {amount} has been withdrawn from your account.\nRemaining balance is {account.balance - amount}"


    def get_account(id):
        for account in Account.accounts_list:
            if account.id == id:
                return account


    def deposit(self, id, amount):
        for account in Account.accounts_list:
            if account.id == id:
                self.balance += amount
