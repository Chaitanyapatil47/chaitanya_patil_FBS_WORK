# 7. Roots of a quadratic equation

import math

a = 2
b = -14
c = 20

d = b*b - 4*a*c

root1 = (-b + math.sqrt(d)) / (2*a)
root2 = (-b - math.sqrt(d)) / (2*a)

print("Root 1 =", root1)
print("Root 2 =", root2)
