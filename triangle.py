import math

def compute_triangle_area(a, b, c):
    s = (a + b + c) / 2
    
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    return area

a = 5
b = 6
c = 7
area = compute_triangle_area(a, b, c)
print("Area of the triangle:", area)