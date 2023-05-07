import math
def sides(a, b, c):
    sides_of_triangle = [a, b, c]
    result = math.prod(sides_of_triangle)
    return result

print(sides(1, 10, 5))


