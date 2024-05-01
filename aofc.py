import math

def circle_area(radius):

  math.pi=3.14
  area = math.pi * (radius ** 2)
  return area


radius = float(input("Enter the radius of the circle: "))

circle_area_value = circle_area(radius)

print("The area of the circle with radius", radius, "is:", circle_area_value)
