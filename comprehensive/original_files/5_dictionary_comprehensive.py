# for loop - Create a new dictionary that contains integers 1-10 and their squared values
squared = {}
for num in range(1, 11):
    squared[num] = num**2

# dictionary comprehension syntax template
# squared = {key_expression: value_expression for temporary_variable(s) in original_iterable}

# for loop - Create a new dictionary that contains the AUD calculated from the USD
products_usd = {"butter": 5.5, "garlic": 3.5, "parsley": 1.2}
products_aud = {}
usd_to_aud = 1.49
for product, price in products_usd.items():
    products_aud[product] = price * usd_to_aud

# dictionary comprehension syntax template
# products_aud = {key_expression: value_expression for (key, value) in original_iterable}

# print statements
print(squared)
print(products_aud)
