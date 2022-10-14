import csv


def parse_data():

    try:
        animal_list = []

        user_input = input('Enter a type of animal: ')

        with open(f"./data/{user_input}.csv", "r") as csvfile:
            animal_dict = csv.DictReader(csvfile, delimiter = ',', skipinitialspace=True)

            for animal in animal_dict:
                animal_list.append(animal)

        for animal in animal_list:
            print(f"{animal['name']} is a {animal['age']} year old {animal['breed']}")

        return animal_list

    except:
        return f"Sorry, we dont' have any {user_input} here."


print(parse_data())