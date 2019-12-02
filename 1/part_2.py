import math
import sys

with open("input.txt", "rb") as fh:
    data = fh.read().split("\n")

def calculate_fuel_for_mass(mass):
    return math.floor(mass/3.0) - 2

def calculate_fuel_for_fuel(fuel_mass):
    total = 0.0
    while fuel_mass:
        fuel_mass = calculate_fuel_for_mass(fuel_mass)
        if fuel_mass <= 0:
            break
        total += fuel_mass
    return total

def calculate_fuel_for_mass_and_fuel(mass):
    fuel_needed = calculate_fuel_for_mass(mass)
    return fuel_needed + calculate_fuel_for_fuel(fuel_needed)


total = 0
for line in data:
    if not line:
        continue
    try:
        mass = float(line)
        fuel_needed = calculate_fuel_for_mass_and_fuel(mass)
        print("mass {}: {}".format(mass, fuel_needed))
        total += fuel_needed
    except:
        import traceback
        traceback.print_exc()
        print("Failed on \"{}\"".format(line))
print(total)
