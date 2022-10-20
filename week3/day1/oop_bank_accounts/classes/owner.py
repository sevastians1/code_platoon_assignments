import csv

class Owner:

    owners_list = []

    def __init__(self, owner_id, last_name, first_name, address, city, state):
        self.id = owner_id
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.city = city
        self.state = state

    # @classmethod
    def add_reserved_owners():

        with open(f"./support/owners.csv", "r") as csvfile:
            owners_dict = csv.DictReader(csvfile, delimiter = ',', skipinitialspace=True)
            
            for owner in owners_dict:
                Owner.owners_list.append(owner)


    def get_owner_info(account_id):
        
        with open("./support/account_owners.csv", "r") as another_csvfile:
            account_owner_dict = csv.DictReader(another_csvfile, delimiter= ',', skipinitialspace=True)

            for account_owner in account_owner_dict:
                if account_owner['account_id'] == account_id:
                    # print('works')
                    owner_id = account_owner['owner_id']
                    # print(owner_id)

                    for owner in Owner.owners_list:
                        # print(owner['id'])
                        if owner['owner_id'] == owner_id:
                            # print(owner)
                            return owner

            # return None