# 1.
def format_string(number, char):
    return "The number is {} and the character is '{}'".format(number, char)

result = format_string(145, 'o')
print(result)



# 2.
radius = 84
pi = 3.14
# Calculate the area of the pond
area = pi * (radius ** 2)
print("Area of the pond:", area)
# Bonus: Calculate the total amount of water in the pond
water_per_square_meter = 1.4
total_water = area * water_per_square_meter
print("Total amount of water in the pond (without decimal):", int(total_water))


# 3.
distance = 490
time_minutes = 7
time_seconds = time_minutes * 60  # convert minutes to seconds
# Calculate speed
speed = distance / time_seconds
print("Speed in meters per second (without decimal):", int(speed))