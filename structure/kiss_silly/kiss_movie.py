import random


def random_movie():
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
    return random.choice(movies)

def buy_snacks(money):
    purchased_snacks = {"popcorn": 0, "soda": 0, "candy": 0}

    if money > 0:
        while money > 0:
            if money >= 3:
                purchased_snacks["popcorn"] = purchased_snacks["popcorn"] + 1
                money = money - 3
            if money >= 2:
                purchased_snacks["soda"] = purchased_snacks["soda"] + 1
                money = money - 2
            if money >= 1:
                purchased_snacks["candy"] = purchased_snacks["candy"] + 1
                money = money - 1

    return purchased_snacks

# REMOVE ALL COMMENTS
def go_to_movies(money):
    movie_choice = random_movie()
    purchased_snacks = buy_snacks(money)

    return f"You went to see {movie_choice} and had {purchased_snacks}."

# EXAMPLE USAGE
print(go_to_movies(89))
