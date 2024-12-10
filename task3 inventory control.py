prices = [10.52 ,7.99 , 63.90 , 60.97 , 75.99 , 50.39 , 35.62 ]
#prices = [kia sonet , karens , kia ev 60, basemodel imt 2.2]
#all are the car prices of a car manufacturing retail  company kia
highest_price = max(prices)
lowest_price = min(prices)
mid_range_prices = [price for price in prices if price != highest_price and price != lowest_price]
premium_price = 79.83  #adding
updated_prices = mid_range_prices + [premium_price]
print(f"Highest price: rs{highest_price}")
print(f"Lowest price: rs{lowest_price}")
print(f"Mid-range prices: {mid_range_prices}")
print(f"Updated prices (with premium): {updated_prices}")
