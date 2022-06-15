class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, x):
        self.width = x

    def set_height(self, x):
        self.height = x

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        pic = ""
        for i in range(self.height):
            pic = pic + "*" * self.width + "\n"
        return pic

    def get_amount_inside(self, shape):
        x = self.width / shape.width
        y = self.height / shape.height
        return str(int(x) * int(y)) + " times"

    def __repr__(self):
        return self.name


class Square(Rectangle):

    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side




rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))