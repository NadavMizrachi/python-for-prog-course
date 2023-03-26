class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __gt__(self, other):
        return self.x**2 + self.y**2 > other.x**2 + other.y**2


p1 = Point(1,2)
p2 = Point(2,2)

print(f"p1 > p2 {p1 > p2}")
