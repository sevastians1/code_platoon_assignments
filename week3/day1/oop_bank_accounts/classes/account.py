from .owner import Owner
import csv

class Account:

    def __init__(self, id, balance, open_date, bank):
        self.id = id
        self.balance = balance
        self.open_date = open_date
        self.bank = bank
        self.owner = Owner.get_owner_info(id)


    @staticmethod
    def get_account_by_id(accounts, id):
        for account in accounts:
            if account.id == id:
                print(account.id, account.balance, account.open_date, account.bank)
                return account
            else:
                return f"There is no account by the id {id}"

    @staticmethod
    def withdraw(accounts, id, amount):
        for account in accounts:
            if id == account.id:
                account.balance -= amount
                print(account.balance)

    @staticmethod
    def deposit(accounts, id, amount):
        for account in accounts:
            if id == account.id:
                account.balance += amount
                print(account.balance)
    
