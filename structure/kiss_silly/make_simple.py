import random

# Too many comments make it less KISS
# Here's a variable holding the number 5  (REMOVE)
number = 5

# This function checks to see  (REMOVE)
# if a number is greater then 10 (REMOVE)
# if it is it will return true (REMOVE)
# if it isn't it will return false (REMOVE)

# Rename function to describe 
# check_greater_than_10(num)
def ten(num):
    # check if number is greater than 10 (REMOVE)
    if num > 10:
        return True
    # if the number is less than 10  (REMOVE)
    else:
        return False
    
    # return num > 10 is all the code needed and NO IF STATEMENT



# calling the check function and (REMOVE)
# passing in a number to check (REMOVE)
# then printing out the result (REMOVE)
print(ten(number))


# a function called go to movies (REMOVE)
# it randomly chooses a movie
# it picks some snacks for you
# then prints out a message with
# your movie and snacks

# REMOVE ALL COMMENTS
def go_to_movies(money):
    # list of movies
    movies = [
        "Parasite",
        "Green Book",
        "The Shape of Water",
        "Moonlight",
        "Spotlight",
        "Birdman",
        "12 Years a Slave",
        "Argo",
        "The Artist",
        "The Kings Speech",
    ]
    # randomly choose a movie
    movie_choice = random.choice(movies)

    # dictionary of snacks and amounts
    purchased_snacks = {"popcorn": 0, "soda": 0, "candy": 0}
    # make sure you have money first
    if money > 0:
        # while money is greater then zero
        # keep buying snacks
        while money > 0:
            # if money is greater than 3
            # purchase popcorn
            if money >= 3:
                purchased_snacks["popcorn"] = purchased_snacks["popcorn"] + 1
                money = money - 3
            # if money is greater than 2
            # purchase soda
            if money >= 2:
                purchased_snacks["soda"] = purchased_snacks["soda"] + 1
                money = money - 2
            # if money is greater than 1
            # purchase candy
            if money >= 1:
                purchased_snacks["candy"] = purchased_snacks["candy"] + 1
                money = money - 1
    return f"You went to see {movie_choice} and had {purchased_snacks}."


# calling the go to movie function
# and printing the result
print(go_to_movies(10))

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
    # loop through each dictionary
    for attribute in pet.items():
        # print out the attributes for each pet
        print(attribute)
