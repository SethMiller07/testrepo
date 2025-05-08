4. Movie age restriction
age = int(input("Enter your age: "))
if age < 13:
    print("You can watch G-rated movies.")
elif 13 <= age <= 17:
    print("You can watch PG-13-rated movies.")
else:
    print("You can watch R-rated movies.")
