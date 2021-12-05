import math


class SquareException(ValueError):
    pass


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        if a < 0:
            raise SquareException
        else:
            self.a = a

    def get_area_square(self):

        return self.a ** 2


class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return self.r ** 2 * math.pi


def main():
    rect_1 = Rectangle(3, 4)
    rect_2 = Rectangle(12, 5)
#    print(F"{rect_1.get_area()}, {rect_2.get_area()}")

    square_1 = Square(5)
    square_2 = Square(10)
#    print(F"{square_1.get_area_square()}, {square_2.get_area_square()}")

    circle_1 = Circle(4)
    circle_2 = Circle(8)
#    print(F"{circle_1.get_area()}, {circle_2.get_area()}")

    figures = [rect_1, rect_2, square_1, square_2, circle_1, circle_2]

    for i in figures:
        if isinstance(i, Rectangle):
            print(i.get_area())
        elif isinstance(i, Square):
            print(i.get_area_square())
        else:
            print(i.get_area())


if __name__ == '__main__':
    main()
