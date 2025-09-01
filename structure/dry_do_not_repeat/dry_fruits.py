fruits = [
    {"name": "grapes", "price": "2.50"},
    {"name": "oranges", "price": "1.50"},
    {"name": "apples", "price": "2.75"},
]

vegetables = [
    {"name": "carrots", "price": "2.25"},
    {"name": "celery", "price": "1.75"},
    {"name": "red peppers", "price": "3.00"},
]

def convert_price(list):
    for item in list:
        item["price"] = float(item["price"])

def add_location(list):
    for item in list:
        item["location"] = "Produce Section"

convert_price(fruits)
convert_price(vegetables)
add_location(fruits)
add_location(vegetables)

print(fruits)
print(vegetables)
