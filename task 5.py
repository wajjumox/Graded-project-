
def check_stock_level(stock_level, threshold=35):


    if stock_level < threshold:
        print("Reorder Now")
    else:
        print("Stock is sufficient")



try:
    stock_level = int(input("Enter current stock level: "))
    check_stock_level(stock_level)
except ValueError:
    print("Invalid input. Please enter an integer value.")
