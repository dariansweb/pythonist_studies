# Practice Emulating Built-ins
# 1) Add a dunder str method to Dog that returns the Pet's name
# 2) Add a dunder eq method to Dog that check if two dog's names are the same
# 3) Add a dunder iter method to Shelter to iterate through the animals list

class Dog:
    def __init__(self, name="Maddie"):
        self.name = name

    # 1) str: when you print() or str() a Dog, return its name
    def __str__(self):
        return self.name

    # 2) eq: check if two Dog objects have the same name
    def __eq__(self, other):
        if isinstance(other, Dog):
            return self.name == other.name
        return False


class Shelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, pet):
        self.animals.append(pet)

    # 3) iter: allow Shelter to be looped over
    def __iter__(self):
        return iter(self.animals)


maddie = Dog()
jethro = Dog("Jethro")
luna = Dog("Luna")

kc_pet_project = Shelter()
kc_pet_project.add_animal(maddie)
kc_pet_project.add_animal(jethro)
kc_pet_project.add_animal(luna)


for pet in kc_pet_project:
    if pet == maddie:
        print("equal")
        print(pet)
    else:
        print("not equal")
        print(pet)

