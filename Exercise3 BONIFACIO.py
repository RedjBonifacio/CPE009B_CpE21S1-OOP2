
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

rectL= float(input("Rectangle length: "))
rectH = float(input("Rectangle height: "))

my_rect = Rectangle(rectL, rectH)

print("Perimeter of the rectangle:", my_rect.Perimeter())

print("Area of the rectangle:", my_rect.Area())
