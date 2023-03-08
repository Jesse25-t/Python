# Authors: Leon, Mako, Jesse
# Assignment 2 Group 4
# Programme that calculates
# Dictionary contains number and quantity
product_prices = {"1": 120.45, "2": 99.50, "3": 75.69, "4": 65.73, "5": 51.49}

print("Welcome to Circle phones' profit calculator.")
total_price = 0

# When loop is FALSE, it breaks and prints out the total
loop = True
while loop:
    user_product_number = str(input("Enter product number 1-5, or enter 0 to stop:\n "))
    if user_product_number in product_prices:
        user_quantity = int(input("Enter quantity sold:\n "))
        total_price += user_quantity * product_prices.get(user_product_number)
        loop = True
    elif user_product_number == "0":
        loop = False
        print(f"Your profit for today is {round(total_price, 2)}")
    else:
        print("you have not specified between the numbers 1-5. Please specify.")
        loop = True

