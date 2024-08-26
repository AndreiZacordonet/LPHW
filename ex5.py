name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_in_cm = height * 2.54
weight = 180 # lbs
weight_in_kg = weight / 2.205
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height_in_cm} cm tall.")
print(f"He's {weight_in_kg} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teech are usually {teeth} depending on the coffee.")

# this line is tricky, try to get ti exactly right
total = age + height_in_cm + weight_in_kg
print(f"If I add {age}, {height_in_cm} and {weight_in_kg} I get {total}.")
