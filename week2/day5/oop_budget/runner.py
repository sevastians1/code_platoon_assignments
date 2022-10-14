# After you write all your classes, use this file to call them all together and run your program
from classes.user import User
from classes.budget import Budget

def run_budget(run=True):

    user_info = create_new_user()

    while run == True:
        
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


def front_page():
    print(f"Please select from the following option:\n")
    front_page_option = input("1. View your budget balance\n2. View your transaction history\n3. Create a new budget\n4. Make a transaction\n5. Percentage spent in each category\n6. Post your monthly income\n7. View your total remaining monthly balance\n8. Quit\n")

    if front_page_option == '1':
        Budget.get_budget_list()
        # front_page()

    elif front_page_option == '2':
        Budget.get_transaction_history()

    elif front_page_option == '3':
        Budget.create_budget()
        # front_page()

    elif front_page_option == '4':
        Budget.post_transaction()

    elif front_page_option == '5':
        Budget.calculate_expense_percentage()

    elif front_page_option == '6':
        Budget.post_income()

    elif front_page_option == '7':
        Budget.get_remaining_total_balance()

    elif front_page_option == '8':
        return False





run_budget()