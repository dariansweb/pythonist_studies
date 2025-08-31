# Example of comprehensive coding
# new_var = [expression for tem_var in iterable]
# View file original_files/loops.py and list_comprehensive.py

name_tags = ["laura", "dustin", "rachel"]
old_banner = "welcome"

# A name_tags.append() isn't needed because of brackets
# Brackets will always produce a list
new_name_tag = ", ".join([name.capitalize() for name in name_tags])
new_banner = "".join([letter.upper() for letter in old_banner])

print(new_name_tag)
print(new_banner)
# for loop - Capitalize all names in the nametags list
