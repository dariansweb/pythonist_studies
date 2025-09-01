# Take a string and replace a character
# then print out the changed string.
# Given: string, index to replace, character to replace with

# WHEN IN DOUBT PRINT IT OUT

import random

string = "piccolo"
index = random.choice(range(len(string)))
character = "t"


def replace_character(string, index, character):
    # use print statements to help follow the results as you go
    print(index)
    # print out the letter of piccolo at that index
    print(string[index])
    # strings are immutable so this would be an error
    # string[index] = character
    # instead we need to create a new string
    split_string = list(string)
    print(split_string)
    
    split_string[index] = character
    print(split_string)

    word = "".join(split_string)
    print(word)


    new_string = string[:index] + character + string[index + 1 :]
    print(new_string)


replace_character(string, index, character)
