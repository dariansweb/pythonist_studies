# for loop - Return a list with only the names with 6+ letters
old_nametags = ["laura", "dustin", "rachel"]
new_nametags = []
for nametag in old_nametags:
    if len(nametag) >= 6:
        new_nametags.append(nametag)

# conditional list syntax template
# new_nametags = [expression for temporary_variable in original_iterable if condition]


# for loop - return a string with only the vowels
old_banner = "welcome"
new_banner = ""
for letter in old_banner:
    if letter in "aeiou":
        new_banner += letter

# conditional list syntax template
# new_banner = [expression for temporary_variable in original_iterable if condition]


# Print statements
print(new_nametags)
print(new_banner)
