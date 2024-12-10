# Dloyalty points
def calculate_loyalty_points(total_purchase):
    if total_purchase >= 1000:
        multiplier = 5  # High tier
    elif total_purchase >= 500:
        multiplier = 3  # Midrange tier
    elif total_purchase >= 100:
        multiplier = 2  # Lowest tier
    else:
        multiplier = 1  # Basic tier
#retuen loyalty points calculator
    return total_purchase * multiplier
# customer list
customers = [
    {"name": "raviteja ", "purchase": 1200},
    {"name": "sindu", "purchase": 600},
    {"name": "ayesha", "purchase": 450},
    {"name": "heena", "purchase": 50}
]
# printing the loyalty points of the customers
print("Customer Loyalty Points:")
for customer in customers:
    points = calculate_loyalty_points(customer["purchase"])
    print(f"{customer['name']}: {points} points")
