# 2. Headlights sensor
sensor_value = int(input("Enter the daylight sensor value: "))
if sensor_value < 8:
    print("Headlights On")
else:
    print("Headlights Off")
