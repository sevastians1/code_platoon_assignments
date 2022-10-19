from classes.account import Account
from classes.bank import Bank
from classes.owner import Owner



new_bank = Bank('Chase')
# new_bank.account_list.('1', 13312, 'open date')
new_owner = Owner('1','soo','saam','some address','cit name','statekfkf','5')

new_account = Account(1,120,'some date', new_bank)

# print(new_account.balance)

Account.all_accounts(new_bank)
# print(Account.accounts_list)


# for account in Account.accounts_list:
#     print(account.__str__())
# print(new_account.id)


print(Account.get_account(1).bank.name)
print(Account.get_account(1).balance)
print(Account.withdraw(1, 50))
print(Account.get_account(1).balance)


# def make_withdrawal(id):
new_owner = Owner.all_owner()
# print(Owner.owner_list)
print(Account.get_account(1).owner_account)

for account in Account.accounts_list:
    print(account.id)