#1 example
import math

degree = float(input("Enter degree: "))
radian = degree * math.pi / 180  
print(f"Radian: {radian:.6f}")
#2example
height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = (base1 + base2) * height / 2
print(f"Area of trapezoid: {area}")
#3example
import math

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))
print(f"The area of the polygon is: {area}")
#4example
base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print(f"Area of parallelogram: {area}")