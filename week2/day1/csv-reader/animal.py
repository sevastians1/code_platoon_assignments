class Animal:
    def __init__(self, id, name, age, breed):
        self.id = id
        self.name = name
        self.age = age
        self.breed = breed

    def display(self):
        return {'id': self.id, 'name':self.name, 'age':self.age, 'breed':self.breed}