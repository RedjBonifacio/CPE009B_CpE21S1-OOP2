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
    def __init__(self, name, grades):
        self.__name = name
        self.__grades = grades

    def get_info(self):
        avg_grade = sum(self.__grades) / len(self.__grades)
        return f"Name: {self.__name}\nGrades: {self.__grades}\nAverage Grade: {avg_grade:.2f}\n"

students = [
    Person("Student 1", [85, 90, 78]),
    Person("Student 2", [88, 92, 80]),
    Person("Student 3", [90, 85, 88])
]

for student in students:
    print(student.get_info())

