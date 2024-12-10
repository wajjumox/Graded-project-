#storing product details
product = {
    "product_name": "speakers",
    "SKU": "6598we",
    "price": 12000,
    "category": "Electronics"
}

#query by customer executive 
def query_product_details(product_dict):
    product_name = product_dict.get("product_name", "Unknown")
    sku = product_dict.get("SKU", "Unknown")
    print(f"Product Name: {product_name}")
    print(f"SKU: {sku}")
query_product_details(product)
