import math
import sys

with open("input.txt", "rb") as fh:
    data = fh.read().split("\n")

total = 0
for line in data:
    if not line:
        continue
    try:
        mass = float(line)
        print("mass {}: {}".format(mass, math.floor(mass/3.0) - 2))
        total += math.floor(mass/3.0) - 2
    except:
        import traceback
        traceback.print_exc()
        print("Failed on \"{}\"".format(line))
print(total)
