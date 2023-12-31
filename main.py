#Phase 1
import math
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}/{self.y})"

    def __repr__(self):
        return self.__str__()

    def distance_from_origin(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

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

    def __repr__(self):
        return self.__str__()

    def centroid(self) -> Point:
        if not self.points:
            raise ValueError("Cannot calculate centroid for an empty shape")

        n = len(self.points)
        avg_x = sum(point.x for point in self.points) / n
        avg_y = sum(point.y for point in self.points) / n

        return Point(avg_x, avg_y)

    def __eq__(self, other):
        return self.centroid().distance_from_origin() == other.centroid().distance_from_origin()

    def __lt__(self, other):
        return self.centroid().distance_from_origin() < other.centroid().distance_from_origin()

    # The __str__ method is used to print a single object.
# The __repr__ method is used to print a collection of objects (like when using print([p1, p2, p3]) in the example).
    def centroid(self) -> Point:
        if not self.points:
            raise ValueError("Cannot calculate centroid for an empty shape")

        n = len(self.points)
        avg_x = sum(point.x for point in self.points) / n
        avg_y = sum(point.y for point in self.points) / n

        return Point(avg_x, avg_y)
# Example usage:
s1 = Shape(p1, p2, p3)
s2 = Shape(p2)
s3 = Shape()

s4 = Shape(Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0))
s5 = Shape(Point(0, 0.5), Point(0.5, 1), Point(1, 0.5), Point(0.5, 0))
s6 = Shape(Point(0.25, 0.25), Point(0.25, 0.75), Point(0.75, 0.75), Point(0.75, 0.25))

print(s4.centroid())  # Output: (0.5/0.5)
print(s5.centroid())  # Output: (0.5/0.5)
print(s6.centroid())  # Output: (0.5/0.5)

print(s1)
print(s2)
print(s3)

# Example usage
p4 = Point(1, 1)
p5 = Point(5, 5)
p6 = Point(10, 10)

print(p4.distance_from_origin())  # Output: 1.4142135623730951
print(p5.distance_from_origin())  # Output: 7.0710678118654755
print(p6.distance_from_origin())  # Output: 14.142135623730951

print(s4 == s5)  # Output: True
s5 = Shape(Point(5, 5), Point(5, 6), Point(6, 6), Point(6, 5))
print(s4 < s5)   # Output: True
s6 = Shape(Point(10, 10), Point(10, 11), Point(11, 11), Point(11, 10))
shapes = [s6,s4, s5]
print(shapes)    # Output: [Shape [(10/10), (10/11), (11/11), (11/10)], Shape [(0/0), (0/1), (1/1), (1/0)], Shape [(5/5), (5/6), (6/6), (6/5)]]
print(sorted(shapes))  # Output: [Shape [(0/0), (0/1), (1/1), (1/0)], Shape [(5/5), (5/6), (6/6), (6/5)], Shape [(10/10), (10/11), (11/11), (11/10)]]
