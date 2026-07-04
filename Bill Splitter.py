#Bill Splitter

running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 24.29

running_total += appetizers + main_courses + desserts + drinks
print("Total bill so far:",running_total)

tip = running_total * 0.25
print("Tip amount:",tip)

running_total += tip
print("Total bill with tip:",running_total)

final_bill = running_total / num_of_friends
print("Bill per person:",final_bill)

each_pays=round(final_bill,2)
print("Each person pays:",each_pays)
