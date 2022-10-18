class Account:
    def __init__(self, balance):
        self.balance = balance


    def withdraw(self, amount):
        if self.balance - amount < 0:
            return 'CANT'
        else:
            self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def all_accounts():
        pass
    
    def find_account():
        pass