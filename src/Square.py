from General import Figure


class Square(Figure):

    def __init__(self, a):
        super().__init__()
        self.a = a
        if (type(a) == float or type(a) == int) and (a > 0):
            pass
        else:
            raise ValueError

    def get_area(self):
        return self.a**2

    @property
    def perimetr(self):
        return self.a * 4
