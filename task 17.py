# product and stock levels
products = {
    "Product A": 15,
    "Product B": 5,
    "Product C": 12,
    "Product D": 3,
    "Product E": 20
}
#threhold  replenishment
threshold = 10
# products that need replenishment
replenishment_list = [product for product, stock in products.items() if stock < threshold]
# printing products that have to be ordered
if replenishment_list:
    print("Products that need replenishment:")
    for product in replenishment_list:
        print(f"- {product}")
else:
    print("All products are sufficiently stocked.")
