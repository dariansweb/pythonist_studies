### Challenge 1 - List the leapyears between 1901 and 2000. Use `range()` to generate a list of years to work with.
# Expected output
# [1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000]

leap_years = """write your comprehension here"""

print("Challenge 1 - Leap years between 1900 and 2000:")
print(leap_years)

########

### Challenge 2 - List only the Simpsons and add “Simpson” to the name
# Expected output
# ['Homer Simpson', 'Marge Simpson', 'Bart Simpson', 'Lisa Simpson', 'Maggie Simpson']

simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
characters = [
    "Homer",
    "Apu",
    "Bob",
    "Marge",
    "Milhouse",
    "Edna",
    "Krusty",
    "Bart",
    "Moe",
    "Lisa",
    "Ned",
    "Lenny",
    "Ralph",
    "Maggie",
    "Nelson",
    "Barney",
]

the_simpsons = """write your comprehension here"""

print("\nChallenge 2 - The Simpsons are: ")
print(the_simpsons)

########

### Challenge 3 - Given a list of words, create a dictionary that maps each word to its length, but only if the word has 5 or more letters.
# Expected output
# {'apple': 5, 'banana': 6, 'cherry': 6}
words = ["apple", "banana", "cherry", "kiwi", "pear"]
word_lengths = """write your comprehension here"""

print(
    "\nChallenge 3 - Dictionary mapping word to length, but only if the word has 5+ letters:"
)
print(word_lengths)

########

### Challenge 4 - Add 1 to each person's age except for 'Danny' since he was born on a leap year
# Expected output
# {'Ally': 34, 'Benny': 29, 'Caddy': 24, 'Danny': 22, 'Ely': 19, 'Franky': 18, 'Georgey': 14}
ages = {
    "Ally": 33,
    "Benny": 28,
    "Caddy": 23,
    "Danny": 22,
    "Ely": 18,
    "Franky": 17,
    "Georgey": 13,
}
ages_next_year = """write your comprehension here"""

print("\nChallenge 4 - Everyone's age next year:")
print(ages_next_year)

########

### Challenge 5 - Generate a set of vowels, displayed in lowercase, from a given string
# Expected output
# {'e', 'i', 'o'}
statement = "Oh, I loooooove Python!"
vowels = """write your comprehension here"""

print("\nChallenge 5 - Vowels in 'Oh, I loooooove Python':")
print(vowels)

########

### Challenge 6 - From 2 lists of fruits & vegetables, create a set that contains the common elements of both
# Expected output
# {'Tomato', 'Cucumber'}
fruits = ["Tomato", "Pomegranate", "Mango", "Cucumber", "Strawberry", "Blackberry"]
vegetables = ["Broccoli", "Cucumber", "Carrot", "Zucchini", "Tomato", "Beetroot"]

overlap = """write your comprehension here"""

print("\nChallenge 6 - Foods that are both a vegetable and a fruit:")
print(overlap)

########

### Challenge 7 - Professor or Doctor? Take a list of dictionaries and return a list of graduate last names with their new honorific. If they scored 90+, they receive the Professor honorific. Otherwise, they receive the Doctor honorific. If they scored below 70
# You will need to know how to access dictionary values using keys. You may also need to use the `split()` method.
# This one can get quite lengthy! Feel free to write a helper function for this challenge
# Expected output:
# ['Doctor McLarry', 'Professor Candy', 'Doctor Penny', 'Doctor Dolly', 'Professor Cherry']
phd_candidates = [
    {"name": "Barry McLarry", "score": 84},
    {"name": "Randy Candy", "score": 92},
    {"name": "Benny Penny", "score": 87},
    {"name": "Polly Dolly", "score": 89},
    {"name": "Jerry Cherry", "score": 98},
    {"name": "Oopsie Daisy", "score": 60},
]

graduates = """write your comprehension here"""

print("\nChallenge 7 - Our new graduates:")
print(graduates)
