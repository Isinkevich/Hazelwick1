cost = 0
item = int(input("How many items would you like to buy?"))
for i in range(item):
    single = float(input("Enter the cost of a single item: "))
    cost = cost + single
if cost > 20:
    cost = cost * 0.8
print("Your total cost is", cost)