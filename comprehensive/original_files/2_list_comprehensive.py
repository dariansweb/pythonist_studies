# for loop - Capitalize all names in the nametags list
old_nametags = ["laura", "dustin", "rachel"]
new_nametags = []
for nametag in old_nametags:
    new_nametags.append(nametag.capitalize())

# list comprehension syntax template
# new_nametags = [expression for temporary_variable in original_iterable]

########

# for loop - make the 'welcome' string all caps
old_banner = "welcome"
new_banner = ""
for letter in old_banner:
    new_banner += letter.upper()

# list comprehension syntax template
# new_banner = [expression for temporary_variable in original_iterable]

########

# print statements
# print(new_nametags)
# print(new_banner)
