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

fruits[0]["price"] = float(fruits[0]["price"])
fruits[1]["price"] = float(fruits[1]["price"])
fruits[2]["price"] = float(fruits[2]["price"])

vegetables[0]["price"] = float(vegetables[0]["price"])
vegetables[1]["price"] = float(vegetables[1]["price"])
vegetables[2]["price"] = float(vegetables[2]["price"])

fruits[0]["location"] = "produce section"
fruits[1]["location"] = "produce section"
fruits[2]["location"] = "produce section"

vegetables[0]["location"] = "produce section"
vegetables[1]["location"] = "produce section"
vegetables[2]["location"] = "produce section"


print(fruits)
print(vegetables)