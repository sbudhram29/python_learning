class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def draw(self):
        print("draw")


point = Point(1, 2)
print(point.x)
print(point.y)
point.draw()

new_point = Point()
print(new_point.x)
print(new_point.y)
new_point.draw()

