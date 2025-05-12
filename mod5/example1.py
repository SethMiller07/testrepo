# 1. Sum from 1 to n using while loop
n = int(input("Enter a positive integer: "))
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum from 1 to", n, "is:", total)
print("\n" + "-"*30 + "\n")
