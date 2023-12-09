#Phase 1
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}/{self.y})"

    def __repr__(self):
        return self.__str__()

# Example usage:
p1 = Point(2.3, 43.14)
p2 = Point(5.53, 2.5)
p3 = Point(12.2, 28.7)

print(p1)
print([p1, p2, p3])

#Phase 2
class Shape(list[Point,...]):   #a shape class inherits from a list of points --> it has all the properties list of points has
    def __init__(self, *points):            # this would be inheritance
        self.points = list(points)

    def __str__(self):
        return f"Shape {self.points}"

# Example usage:
s1 = Shape(p1, p2, p3)
s2 = Shape(p2)
s3 = Shape()

print(s1)
print(s2)
print(s3)