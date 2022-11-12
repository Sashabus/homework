class Vector:
    pen_width = 12
    pen_colour = "green"

    def __init__(self):
        self.x1, self.y1 = self.set_first_point()
        self.x2, self.y2 = self.set_second_point()

    def get_cords(self):
        return self.x2 - self.x1, self.y2 - self.y1

    def get_length(self):
        length = (self.get_cords()[0] ** 2 + self.get_cords()[1] ** 2) ** 0.5
        return length

    def all_info(self):
        return {"coordinates": self.get_cords(),
                "length:": self.get_length()}

    def draw(self):
        pass

    @staticmethod
    def set_first_point():
        x1 = int(input("x1:"))
        y1 = int(input("y1:"))
        return x1, y1

    @staticmethod
    def set_second_point():
        x2 = int(input("x2:"))
        y2 = int(input("y2:"))
        return x2, y2

    @classmethod
    def change_width(cls, width):
        cls.pen_width = width

    @classmethod
    def change_colour(cls, colour):
        cls.pen_colour = colour


vector1 = Vector()
print("coordinates:", vector1.get_cords())
print("length:", vector1.get_length())
print(vector1.all_info())