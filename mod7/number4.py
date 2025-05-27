def ferry_fare(age, vehicle):
    if age <= 18:
        return 0
    elif 19 <= age <= 64:
        return 20 if vehicle else 10
    elif age >= 65:
        return 15 if vehicle else 5
