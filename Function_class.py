#     if user_time_period == 0:
#         break

#     user_selected_day = input("Enter a specific day [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]")
#     if user_time_period in time_period:
#         user_quantity = int(input("enter the quantity: "))
#         total_profit += float(time_period[user_time_period]) *user_quantity
#     else:
#         break
#
# print(f"Total profit for the {day} is: ${total_profit}")
# if total_price < achieved_profit:
#         print("We didn’t reach our goal for this period. More work is needed")
# else:
#     print("You did well this period! Keep up the great work!")
# break
# first_list = ["Jesse", "Patricia", "mommy", "daddy"]
# first_dictionary = {1: first_list, 2: "Mommy"}
# print(first_dictionary[1][3])
#
# total_price = 0
# days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# time_periods = {1: days_of_the_week, 2: "Week", 3: "Business days", 4: "Weekend"}
# product_prices = {"1": 120.45, "2": 99.50, "3": 75.69, "4": 65.73, "5": 51.49}
#
# while True:
#     for day in days_of_the_week:
#         # for time in range(len(day)):
#         print(f"for {day}")
#         while True:
#             user_product_number = str(input("Enter product number 1-5, or enter 0 to stop:\n "))
#             if user_product_number in product_prices:
#                 user_quantity = int(input("Enter quantity sold:\n "))
#                 total_price += user_quantity * product_prices.get(user_product_number)
#
#             elif user_product_number == "0":
#                 print(f"Your profit for today is {round(total_price, 2)}")
#                 break
#             else:
#                 print("you have not specified between the numbers 1-5. Please specify.")

# days = ["Happy", "Birthday", "To", "This", "Person"]
#
# # time = days.get()
#
# print(days[2])
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_periods = {1: days_of_the_week, 2: "Week", 3: "Business days", 4: "Weekend"}
if time_periods in range(1, 3):
 print(range(1, 3))
