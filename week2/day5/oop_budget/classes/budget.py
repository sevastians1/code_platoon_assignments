

class Budget:
    budget_list = []
    transaction_history = []
    income = 0

    def __init__(self):
        pass

    def post_income():
        new_income = int(input("Enter your monthly income: "))
        Budget.income = new_income
        return print(f"You have posted your monthly income of ${new_income}")            


    def create_budget():
        new_budget_category = input("Enter a new category: ")
        new_budget_budget = int(input("Enter a budget limit: "))

        for budget in Budget.budget_list:
            if budget['category'] == new_budget_category:
                return print('This budget category already exists.\nReturning to main menu.')
        
        Budget.budget_list.append({'category':new_budget_category, 'budget':new_budget_budget})
        return print(f"Budget category '{new_budget_category}' has been created.")


    def post_transaction():
        new_transaction_name = input("Enter the transaction name: ")
        new_transaction_amount = int(input("Enter the transaction amount: "))
        new_transaction_category = input("Enter the transaction category: ")

        for budget in Budget.budget_list:
            if budget['category'] == new_transaction_category:
                Budget.transaction_history.append({'name':new_transaction_name, 'amount':new_transaction_amount, 'category':new_transaction_category})
                budget['budget'] -= new_transaction_amount
                return print(f"Transaction amount of {new_transaction_amount} has been posted to {new_transaction_category}.\nBudget category {new_transaction_category} has a remaining balance of {budget['budget']}.\n")

            else:
                return print('The budget for this category is not created.\nCreate a new budget with the category listed in order to post the new transaction.')


    def get_budget_list():
        print("\n***BUDGET LIST***")

        for budget in Budget.budget_list:
            print(f"Budget category {budget['category']} has a remaining balance of {budget['budget']}.")

        return print("***END OF BUDGET LSIT***")

    
    def get_transaction_history():
        print("\n***TRANSACTION HISTORY***")

        for transaction in Budget.transaction_history:
            print(f"Transaction of amount {transaction['amount']} has been posted to {transaction['category']}.")

        return print("**END OF TRANSACTION HISTORY")


    def get_remaining_total_balance():

        if len(Budget.transaction_history) > 0:
            total_transaction_amount = 0
            for transaction in Budget.transaction_history:
                total_transaction_amount += transaction['amount']

            Budget.income -= total_transaction_amount
        return print(f"Remaining total monthly balance is ${Budget.income}.")


    def calculate_expense_percentage():

        if len(Budget.transaction_history) > 0:
            total_transaction_amount = 0
            for transaction in Budget.transaction_history:
                total_transaction_amount += transaction['amount']

            print(f"Enter the name of the category from this list:\n")
            for budget in Budget.budget_list:
                print(budget['category'])

            category_selection = input('')

            category_total_amount = 0
            for transaction in Budget.transaction_history:
                if transaction['category'] == category_selection:
                    category_total_amount += transaction['amount']

            percentage = float(category_total_amount / total_transaction_amount)
            return print(f"{percentage} of your transactions is spent on {category_selection}")

        else:
            return print("No transactions have been made.")