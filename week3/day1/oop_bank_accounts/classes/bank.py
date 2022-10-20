from .account import Account
from .owner import Owner
import csv


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, **account_info):
        self.accounts.append(Account(**account_info))
        return self.accounts[-1]
    
    def add_saved_accounts(self):


        with open(f"./support/accounts.csv", "r") as csvfile:
            accounts_dict = csv.DictReader(csvfile, delimiter = ',', skipinitialspace=True)

            for account in accounts_dict:
                

                account['bank'] = self.name

                self.accounts.append(Account(**account))

    def remove_account(self, id):

        for account in self.accounts:
            if account.id == id:
                self.accounts.remove(account)

    def display_all_accounts(self):
        
        for account in self.accounts:
            print(account.id, account.balance)

