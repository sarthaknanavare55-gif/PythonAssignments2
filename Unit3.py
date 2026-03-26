#Experiment 1
import shapes
print("Choose a shape:")
print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    r = float(input("Enter radius: "))
    area = shapes.circle_area(r)
    print("Area of Circle =", area)

elif choice == 2:
    l = float(input("Enter length: "))
    w = float(input("Enter width: "))
    area = shapes.rectangle_area(l, w)
    print("Area of Rectangle =", area)

elif choice == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = shapes.triangle_area(b, h)
    print("Area of Triangle =", area)

else:
    print("Invalid choice")

#Shapes.py
import math

def circle_area(radius):
    return math.pi * radius * radius

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

