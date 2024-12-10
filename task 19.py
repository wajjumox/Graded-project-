# sales data
last_3_months_sales = [35000, 75000, 35600]

# next 3 month sales
def forecast_sales(sales):
    # avg of last 3 months
    average_sales = sum(sales) / len(sales)
    return average_sales

# next monthly saLES
next_month_sales_forecast = forecast_sales(last_3_months_sales)

# Print the forecasted sales figure
print(f"Forecasted sales for next month: rs{next_month_sales_forecast:.2f}")
