from classes.account import Account
from classes.bank import Bank
from classes.owner import Owner



Owner.add_reserved_owners()

new_bank = Bank('new_bank')

print(new_bank.name)

new_owner_info = {
    'owner_id': 10,
    'last_name': 'Son',
    'first_name': 'Samuel',
    'address': 'some address',
    'city': 'some city',
    'state': 'some state',
}

new_account_info = {
    'id': 1,
    'balance': 10322,
    'open_date': 'July',
    'bank': new_bank.name,
}

new_bank.add_account(**new_account_info)

# print(new_bank.accounts[-1].owner.first_name)


new_bank.add_saved_accounts()

print(new_bank.accounts[-1].owner)

# for contact in new_bank.accounts:
#     print(contact.owner)


# Account.withdraw(new_bank.accounts, 1, 1000)
# Account.get_account_by_id(new_bank.accounts, 1)
# Account.deposit(new_bank.accounts, 1, 2000)
# Account.get_account_by_id(new_bank.accounts, 1)

# new_bank.remove_account(1)

# new_bank.display_all_accounts()