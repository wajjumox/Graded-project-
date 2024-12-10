# List of customer spending amounts
spending = [36000, 2500, 1200, 9000, 49000, 2200, 23000]
for amount in spending:
    if amount < 25000:
        category = "Low"
    elif 25000 <= amount < 28000:
        category = "Medium"
    else:
        category = "High"
    print(f"Customer spending Rs{amount} is categorized as: {category}")
