# Find the side C of a Triangle

import math

a = float(input("\n\nEnter the side A of a triangle: "))
b = float(input("Enter the side B of a triangle: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"\n\nSide C of the triangle is: {round(c, 2)}")