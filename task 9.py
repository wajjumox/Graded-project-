
products = [
    {'name': 'Product A', 'price': 150},
    {'name': 'Product B', 'price': 250},
    {'name': 'Product C', 'price': 80},
    {'name': 'Product D', 'price': 200},
    {'name': 'Product E', 'price': 120}
]
threshold = 250

eligible_products = [product for product in products if product['price'] >= threshold]
print("Eligible products for the discount campaign:")
for product in eligible_products:
    print(f"{product['name']} - rs{product['price']}")
