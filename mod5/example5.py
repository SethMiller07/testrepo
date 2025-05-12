# 5. Keep asking for numbers until 0 is entered
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Exiting...")
        break
    else:
        print("You entered", num)
