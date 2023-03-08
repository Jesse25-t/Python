# # a function that accepts input
# # again = True
# # while True:
#
# # user_province = input("What is your province? ")
#
# tax_rate_option = {
#     "AB": 1,
#     "BC": 2
# }
#
#
# def get_province_tax():
#     user_province = input("What is your province? ").upper().strip()
#     tax = tax_rate_option.get(user_province)
#     if tax is None:
#         return 3
#     return tax, user_province
#
#
# tax_prov = get_province_tax()
# print(f"your province is {tax_prov[1]} \n "
#       f"and your tax rate is {tax_prov[0]}")
#
# # ahead = input("Do you want to go ahead? ").lower
# # if ahead == "Yes":
# #     again = True
# #     continue
# # else:
# #     again = False
# #     break
#

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days_of_the_week:
    print(day)
    if day == "Friday":
        break

listed = ["a", "b", "c"]
for i in listed:
    print(i)
    if i == "b":
        break



