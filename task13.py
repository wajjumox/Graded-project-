
def calculate_discounted_price(original_price, discount_percentage):
    discount_amount = (original_price * discount_percentage) / 100
    final_price = original_price - discount_amount
    return round(final_price, 2)
products = [
    {"name": "Product A", "original_price": 5000, "discount_percentage": 10},
    {"name": "Product B", "original_price": 2600, "discount_percentage": 20},
    {"name": "Product C", "original_price": 6200, "discount_percentage": 15},
    {"name": "Product D", "original_price": 8500, "discount_percentage": 5}
]
print("Discounted Prices for Products:")
for product in products:
    final_price = calculate_discounted_price(product["original_price"], product["discount_percentage"])
    print(f"{product['name']}: rs{final_price}")
