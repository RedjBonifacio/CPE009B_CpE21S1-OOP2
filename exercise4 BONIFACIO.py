##EXAMPLE 1:
class foo:
    def __init__(self, a ,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
foo_object = foo(3,4)
foo_object.add()

##EXAMPLE 2:
class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1
        
    def value(self):
        return self.current

    def reset(self):
        self.current = 0

counter = Counter()

counter.increment()
counter.increment()
counter.increment()

print("Example 2\n",counter.value())

##EXAMPLE 3:
class RegularPolygon:
    def __init__(self, side):
        self.side = side

class Square(RegularPolygon):
    def area(self):
        return self.side * self.side

class EquilateralTriangle(RegularPolygon):
    def area(self):
        return self.side * self.side * 0.433

obj1 = Square(4)
obj2 = EquilateralTriangle(4)

# Print the areas
print("\n(Example 3):")
print("Area of the square:", obj1.area())
print("Area of the equilateral triangle:", obj2.area())


##Application 1
class Person:
    def __init__(self, name, pre, mid, fin):
        self.__name = name
        self.__pre = pre
        self.__mid = mid
        self.__fin = fin

    def Grade(self):
        return (self.__pre + self.__mid + self.__fin) / 3

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Average Grade: {self.Grade():.2f}")

student1 = Person("Student 1", 85, 90, 88)
student2 = Person("Student 2", 78, 82, 80)
student3 = Person("Student 3", 92, 94, 96)

student1.display_info()
student2.display_info()
student3.display_info()

