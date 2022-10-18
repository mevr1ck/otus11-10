from General import Figure


class Circle(Figure):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        if (type(radius) == float or type(radius) == int) and (radius > 0):
            pass
        else:
            raise ValueError

    def get_area(self):
        return 3.14 * self.radius ** 2

    @property
    def length(self):
        l = 2 * 3.14 * self.radius
        return l


circle = Circle(radius=5)
print(circle.length)
print(circle.get_area())
