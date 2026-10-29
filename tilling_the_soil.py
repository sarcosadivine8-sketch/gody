import math

# Read 8 inputs: width and length for front, rear, left, right (in that order)
dimensions = []
for _ in range(8):
    try:
        value = int(input())
    except Exception:
        value = 0
    dimensions.append(value)

# Calculate total area
area = 0
for i in range(0, 8, 2):
    width = dimensions[i]
    length = dimensions[i + 1]
    area += width * length

