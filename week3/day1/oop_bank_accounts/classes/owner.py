import csv

class Owner:

    owner_list = []

    def __init__(self, id, last_name, first_name, address, city, state, account_id):
        self.id = id
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.city = city
        self.state = state
        self.account_id = account_id
        Owner.owner_list.append(self)

    def all_owner():

        owner_dict_lists = []

        with open(f"./support/owners.csv", "r") as csvfile:
            owner_dict = csv.DictReader(csvfile, delimiter = ',', skipinitialspace=True)

            for owner in owner_dict:
                owner_dict_lists.append(owner)
            
        # print(owner_dict_lists)

        account_owner_dict_list = []
        
        with open("./support/account_owners.csv", "r") as another_csvfile:
            account_owner_dict = csv.DictReader(another_csvfile, delimiter= ',', skipinitialspace=True)

            for account_owner in account_owner_dict:
                account_owner_dict_list.append(account_owner)

        # print(account_owner_dict_list)

        for owner in owner_dict_lists:
            for account_owner in account_owner_dict_list:
                if owner['id'] == account_owner['owner_id']:
                    owner['account_id'] = account_owner['account_id']
                    Owner(**owner)


    def find_owner(id):

        for owner in Owner.owner_list:
            if owner['id'] == id:
                return owner

    def del_owner(id):

        for owner in Owner.owner_list:
            if owner['id'] == id:
                pass
                