# conditional list syntax template
# new_nametags = [expression for temporary_variable in original_iterable if condition]

name_tags = ["laura", "dustin", "rachel"]
old_banner = "welcome"

# Using conditional list syntax to create a list with only the names with 6+ letters
new_nametags = [
    nametag.capitalize() if len(nametag) >= 6 else nametag for nametag in name_tags
]

# for loop - make only the vowels uppercase
new_banner = "".join(
    [letter.upper() if letter in "aeiou" else letter for letter in old_banner]
)


print(new_nametags)
print((new_banner))
