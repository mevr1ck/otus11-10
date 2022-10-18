from General import Figure


class Triangle(Figure):

    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        if (type(a) == float or type(a) == int) and (type(b) == float or type(b) == int) and (
                type(c) == float or type(c) == int):
            pass
        else:
            raise ValueError

        if (a + b > c) and (a + c > b) and (b + c > a) and (a > 0) and (c > 0) and (b > 0):
            pass
        else:
            raise ValueError

    def get_area(self):
        polu_perimetr = (self.a + self.b + self.c) / 2
        s = (polu_perimetr * (polu_perimetr - self.a) * (polu_perimetr - self.b) * (polu_perimetr - self.c)) ** 0.5
        return s

    @property
    def perimetr(self):
        p = self.a + self.b + self.c
        return p


triangle = Triangle(a=4, b=3, c=5)
print(triangle.get_area())
print(triangle.perimetr)
