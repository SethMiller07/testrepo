with open("hiking_log.txt", "a") as file:
    while True:
        hike_name = input("Enter hike name (or 0 to stop): ")
        if hike_name == "0":
            break
        distance = input("Enter distance in miles: ")
        file.write(f"{hike_name} - {distance} miles\n")

# Read and display the log
print("\nYour Hiking Log:")
with open("hiking_log.txt", "r") as file:
    for line in file:
        print(line.strip())
