with open('sales_log.txt', 'w') as file:
    file.write("Daily Sales Summary - 10th December 2024\n")
    file.write("Total Sales: rs5000, Number of Transactions: 35\n")
with open('sales_log.txt', 'r') as file:
    content = file.read()
    print("Sales Log File Content:")
    print(content)
