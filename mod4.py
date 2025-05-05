# 1. Truth Table for (A AND B) OR (NOT B)
# |   A   |   B   | (A AND B) | (NOT B) | (A AND B) OR (NOT B) |
# |-------|-------|-----------|---------|---------------------|
# | True  | True  |   True     |  False  |        True          |
# | True  | False |   False    |  True   |        True          |
# | False | True  |   False    |  False  |        False         |
# | False | False |   False    |  True   |        True          |

sensor_value = int(input("Enter daylight sensor reading: "))
if sensor_value < 8:
    print("Headlights On")
else:
    print("Headlights Off")
balance = float(input("Enter your bank balance: $"))
print(balance < 100)
age = int(input("Enter your age: "))
if age < 13:
    print("You can see G-rated movies.")
elif 13 <= age <= 17:
    print("You can see PG-13 movies.")
else:
    print("You can see R-rated movies.")
order_total = float(input("Enter your order total: $"))
if order_total < 50:
    total_with_shipping = order_total + 5
else:
    total_with_shipping = order_total
print(f"Your total cost is: ${total_with_shipping:.2f}")
