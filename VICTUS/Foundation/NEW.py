# Suyunov Asilbek
#       N1
# OOP ning 4 ta ustuni bor:
# 1) Abstraction,
# 2) Inheritance,
# 3) Polymorphism,
# 4) Encapsulation.

#       N2
# class Fruits:
#     def __init__(self, name, color, weight):
#         self.name = name
#         self.color = color
#         self.weight = weight
#
#     def all_info(self):
#         return self.name, self.color, self.weight
#
#     def get_color(self):
#         return self.color
#
#
# n = int(input('Kiritiladigan son: '))
# world = []
# a = []
# for i in range(n):
#     obj = Fruits(input('name: '), input('color: '), int(input('weight: ')))
#     world.append(obj.name)
#     a.append(obj)
#
# search = input('search: ')
# index = world.index(search)
# total = a[index]
# Finish = []
# Finish.append(total.all_info())
# print(Finish)

#       N3
# class Oquv_Markaz:
#     def __init__(self, name, courses, teachers_count, students_count):
#         self.name = name
#         self.courses = courses
#         self.teachers_count = teachers_count
#         self.students_count = students_count
#
#     def all_info(self):
#         return self.name, self.courses, self.teachers_count, self.students_count
#
#
# obj1 = Oquv_Markaz(input('name: '), input('course: '), int(input('teachers_count: ')), input('students_count: '))
# print(obj1.all_info())
#
#
# class Isystem(Oquv_Markaz):
#     def __init__(self, name, courses, teachers_count, students_count):
#         Oquv_Markaz.__init__(self, name, courses, teachers_count, students_count)
#
#     def add_Student(self):
#         return self.students_count + self.students_count
#
#     def add_course(self):
#         return self.courses + self.courses
#
#
# obj2 = Isystem('Asadbek', 'uzb', 30, 40)
# print(obj2.add_Student())
# print(obj2.add_course())
#
#
# class Pdp(Oquv_Markaz):
#     def __init__(self, name, courses, teachers_count, students_count):
#         Oquv_Markaz.__init__(self, name, courses, teachers_count, students_count)
#
#     def add_Student(self):
#         return self.students_count + self.students_count
#
#     def add_course(self):
#         return self.courses + self.courses
#
#
# obj3 = Isystem('Bobur', 'rus', 90, 400)
# print(obj2.add_Student())
# print(obj2.add_course())
#
#
# class Najottalim(Oquv_Markaz):
#     def __init__(self, name, courses, teachers_count, students_count):
#         Oquv_Markaz.__init__(self, name, courses, teachers_count, students_count)
#
#     def add_Student(self):
#         return self.students_count + self.students_count
#
#     def add_course(self):
#         return self.courses + self.courses
#
#
# obj2 = Isystem('Muhammad', 'eng', 300, 420)
# print(obj2.add_Student())
# print(obj2.add_course())

#       N4
# from abc import ABC, abstractmethod
#
#
# class Shakl(ABC):
#
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#
# class Kvadrat(Shakl):
#     def __init__(self, tomoni):
#         self.tomoni = tomoni
#
#     def perimetr(self):
#         return self.tomoni * 4
#
#
# obj = Kvadrat(2)
# print(obj.perimetr())
#       N5
# import uuid
#
#
# class Student:
#     def __init__(self, name, age, surname):
#         self.name = name
#         self.age = age
#         self._surname = surname
#         self.__password = uuid.uuid4()
#
#     def return_info(self):
#         return f"{self.name}"
#
#     def get_password(self):
#         return self.__password
#
#     def get_surname(self):
#         return self._surname
#
#
# obj = Student('Asilbek', '15', 'Suyunov')
#
# print(obj.name)
# print(obj.get_surname())
# print(obj.get_password())
#       N7
# a = [str(i) for i in input().split()]
# a.sort()
# print(a)
# print(a[0])
#       N8
# class Cars:
#     def __init__(self, name1, name2):
#         self.name1 = name1
#         self.name2 = name2
#
#     def sort_name(self):
#         v = []
#         v.append(self.name1)
#         v.append(self.name2)
#         v.sort()
#         return v
#
#
# obj = Cars(input('name1: '), input('name2: '))
# print(obj.sort_name())

# from World import PinCar
# print(PinCar.get_Pin())
