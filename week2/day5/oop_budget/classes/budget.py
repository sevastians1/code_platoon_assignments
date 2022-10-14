from . import user

class Budget:

    all_transactions = {}

    def __init__(self, category, balance):
        self.category = category
        self.balance = balance
        self.transaction_history = {}