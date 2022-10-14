# After you write all your classes, use this file to call them all together and run your program
from classes.user import User
from classes.budget import Budget

def run_budget(run=True):
    while run == True:
        user_info = create_new_user()
        
        # print(front_page())

        if front_page() == False:
            run = False
        





def create_new_user():
    new_user_name = input("Enter your name: ")
    new_user_username = input("Enter a new username: ")
    new_user_password = input("Enter a password: ")

    user_info = {
        'name':new_user_name,
        'username':new_user_username,
        'password':new_user_password,
    }

    new_user_name = User.create_user(**user_info)

    print(f"Username has been successfully created.\nWelcome to your budget page {new_user_name.name}!")

    return user_info

def create_new_budget():
    new_budget_cat = input("Enter a new budget category: ")
    new_budget_balance = input("Enter the budget limit: ")

    new_budget_info = {
        'category': new_budget_cat,
        'balance': new_budget_balance
    }

    new_budget = Budget(**new_budget_info)
    print(vars(new_budget))

    return new_budget


def front_page():
    print(f"Please select from the following option:\n")
    front_page_option = input("1. View your budget balance\n2. View your transaction history\n3. Create a new budget\n4. Make a transaction\n5. Quit\n")

    if front_page_option == '1':
        budget_page()

    elif front_page_option == '2':
        pass

    elif front_page_option == '3':
        create_new_budget()
        front_page()

    elif front_page_option == '4':
        pass

    elif front_page_option == '5':
        return False


def budget_page():
    print("Welcome to your budget list!\nPlease select the following option to view your remaining budget in each category.")
    budget_option = input("1. Rent\n2. Utilities\n3. Food\n4. Transportation\n5. Entertainment\6. Return to main menu")

    if budget_option == '1':
        pass
    elif budget_option == '2':
        pass
    elif budget_option == '3':
        pass
    elif budget_option == '4':
        pass
    elif budget_option == '5':
        pass
    elif budget_option == '6':
        front_page()



run_budget()