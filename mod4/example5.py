# 5. Shipping cost calculation
order_total = float(input("Enter your order total: "))
if order_total < 50:
    total_cost = order_total + 5
else:
    total_cost = order_total
print(f"Your total cost is: ${total_cost:.2f}")
