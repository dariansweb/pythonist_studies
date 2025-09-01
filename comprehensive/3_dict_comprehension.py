# dictionary comprehension syntax template
# squared = {key_expression: value_expression for temp_var in original_iterable}

# for loop - Create a new dictionary that contains integers 1-10 and their squared values
squared_1 = {}
for num in range(1, 11):
    squared_1[num] = num**2

squared_2 = {num: num**2 for num in range(1, 11)}

# for loop - Create a new dictionary that contains the AUD calculated from the USD
products_usd = {"butter": 5.5, "garlic": 3.5, "parsley": 1.2}
products_aud = {}
usd_to_aud = 1.49
for product, price in products_usd.items():
    products_aud[product] = price * usd_to_aud

products_add2 = {
    product: price * usd_to_aud for product, price in products_usd.items() if price < 5
}
# print statements

print(squared_1)
print(squared_2)
print(products_aud)
print(products_add2)
