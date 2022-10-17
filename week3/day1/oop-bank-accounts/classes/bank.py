class Bank:
    def __init__(self, name):
        self.name = name
        self.account = self.Account()

    class Account:
        def __init__(self, balance):
            self.balance = balance
            self.owner = self.Owner()


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

        class Owner:
            def __init__(self, name, address, phone_number, password):
                self.name = name
                self.address = address
                self.phone_number = phone_number
                self.password = password

            