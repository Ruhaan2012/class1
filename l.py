import math
def calculate_area(radius):
    area = math.pi * radius ** 2
    return area

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

radius = float(input("Enter the radius of the circle: "))

area = calculate_area(radius)
circumference = calculate_circumference(radius)

print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")