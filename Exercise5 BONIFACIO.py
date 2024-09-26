#polymorphism

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
#inherits the attribute of a person
class Student(Person):
    def traits(self):
        return f'studying, playing, dancing, singing'
        
class Teacher(Person):
    def traits(self):
        return f'teaching, socializing, participating'
        
student = Student("Ana", 20)
teacher = Teacher("Maam Sayo", 41)
    
print("As a student, I do", student.traits())
print("As a teacher, I do", teacher.traits())
print("\n")

#EXERCISE 5
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Japanese(Car):
    traits = 'reliable, fast, balanced, easy to maintain, and long lasting'

class American(Car):
    traits = 'fast, powerful, unreliable, all-around, and has rare parts'

print("Most Japanese cars are", Japanese.traits)
print("Most American cars are", American.traits)


