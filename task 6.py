products_sold = ["carens", "sonet", "sonet htk", "sonet htk o", "seltos gravity"]

print("Using for loop:")
for product in products_sold:
    print(product.upper())

print("\nUsing while loop:")
index = 0
while index < len(products_sold):
    print(products_sold[index].upper())
    index += 1
