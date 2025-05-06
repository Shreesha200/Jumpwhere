quantity = int(input("Enter the quantity: "))
unit_price = 100
total_cost = quantity * unit_price

if total_cost > 1000:
    discount = total_cost * 0.10
    total_cost -= discount

print("Total cost:", total_cost)