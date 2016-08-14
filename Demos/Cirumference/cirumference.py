# calculate the area and circumference of a circle from its radius
# Step 1: prompt for a radius
# Step 2: apply for area formula
# Step 3: Print out the results

import math

radiusString = raw_input("Enter the radius fof your circle: ")
radiusInteger = int(radiusString)

circumference = 2 * math.pi * radiusInteger
area = math.pi * math.pow(radiusInteger, 2)

print('The circumference: %s, the area : %s' % (circumference, area))
