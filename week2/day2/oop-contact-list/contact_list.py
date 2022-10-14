from operator import itemgetter


class ContactList:

    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.contact_list = []

    def add_contact(self, new_name, new_phone_number, category):
        self.contact_list.append({'name':new_name, 'phone_number':new_phone_number, 'category':category})
        
    def remove_contact(self, name):
        for contact in self.contact_list:
            if contact['name'] == name:
                self.contact_list.remove(contact)
    
    def find_shared_contact(self, list1):
        shared_contact = []
        for contact in self.contact_list:
            for other_contact in list1.contact_list:
                if contact['name'] == other_contact['name'] and contact['phone_number'] == other_contact['phone_number']:
                    shared_contact.append(contact)

        return shared_contact

    def sorted_contacts(self):
        return sorted(self.contact_list, key=itemgetter('name'))
            


sam = ContactList('sam', 123123132)
dan = ContactList('dan', 1931992)
tim = ContactList('tim', 1039291)

sam.add_contact('tan', 13131313, 'friend')
sam.add_contact('dan', 13131313, 'friend')
sam.add_contact('kan', 13131313, 'friend')
sam.add_contact('ban', 13131313, 'friend')
sam.add_contact('oan', 13131313, 'friend')
dan.add_contact('kan', 13131313, 'friend')


print(sam.find_shared_contact(dan))
# print(dan.friend_list)

# print(ContactList.find_shared_contact(sam.contact_list, dan.contact_list))