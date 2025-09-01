# list of dictionaries containing some treehouse pets
pets = [
    {"name": "Jethro", "animal": "dog", "breed": "Australian Shepherd"},
    {"name": "Harley", "animal": "dog", "breed": "Unkown"},
    {"name": "Booger", "animal": "cat", "breed": "Unkown"},
    {"name": "Argo", "animal": "cat", "breed": "Unkown"},
    {"name": "Ace", "animal": "cat", "breed": "Unkown"},
]

# loop through each pet in the list
for pet in pets:
    print(pet["name"])
    print(pet["animal"])
    print(pet["breed"])
