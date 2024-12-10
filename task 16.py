# sales figure for month
daily_sales = [
    200, 250, 250, 400, 150, 500, 600, 961, 450, 378,
    350, 126, 200, 956, 450, 395, 600, 700, 340, 750,
    670, 256, 480, 782, 550, 600, 700, 985, 900, 800
]
# total and average sales calculating
total_sales = sum(daily_sales)
average_sales = total_sales / len(daily_sales)
# sales report
report_content = f"""Monthly Sales Report
---------------------
Total Sales: ${total_sales}
Average Daily Sales: ${average_sales:.2f}
"""
# text file
with open("monthly_report.txt", "w") as file:
    file.write(report_content)

print("Monthly sales report has been generated and saved as 'monthly_report.txt'.")
