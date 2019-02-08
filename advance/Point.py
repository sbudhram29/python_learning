class Point:
    """Represents a point in 2-D space."""

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{__class__.__name__}({self.x}, {self.y})"


class Rectangle:
    """
        Represents a rectangle, with corner that is point
        attributes: width, height, corner
    """

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"{__class__.__name__}({self.width}, {self.height})"

    def area(self):
        return self.width * self.height

    def find_center(self):
        x = self.corner.x + self.width/2
        y = self.corner.y + self.height/2

        return Point(x, y)


class Circle:
    """
        Represents a circle
        attributes: center, radius
    """

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"{__class__.__name__}({self.center}, {self.radius})"

    def point_in_circle(self, location: Point):

        if (location.x > self.center.x + self.radius
                or location.x < self.center.x - self.radius):
            return False

        if (location.y > self.center.y + self.radius
                or location.y < self.center.y - self.radius):
            return False

        return True

    def area(self):
        return 2 * 3.14 * self.raduis * self.raduis


def main():
    box = Rectangle(100.0, 200.0)
    box.corner = Point(0.0, 0.0)

    center = box.find_center()
    print(center.x)
    print(center.y)

    circle = Circle(Point(150, 100), 75)

    print(circle.point_in_circle(Point(226, 176)))
    print(circle.point_in_circle(Point(206, 176)))
    print(circle.point_in_circle(Point(226, 116)))
    print(circle.point_in_circle(Point(200, 100)))
    print(circle)
    print(box)


if __name__ == '__main__':
    main()
