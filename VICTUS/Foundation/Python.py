# a = [123, 5, 436, 34, 43576, 42, 54, 678]
# a.remove(a[1])
# print(a)

# a = [123, 5, 436, 34, 43576, 42, 54, 678]
# a.sort()
# print(a)

# a = [123, 5, 436, 34, 43576, 42, 54, 678]
# a.pop(1)
# print(a)

# a = [123, 5, 436, 34, 43576, 42, 54, 678]
# a.extend([1])
# print(a)

# a = [123, 5, 436, 34, 43576, 42, 54, 678]
# a.append('python')
# print(a)

# a = {'name': 'Asilbek'}
# print(a.values())

# a = {'name': 'Asilbek'}
# print(a.keys())

# a = {'name': 'python'}
# print(a.values())

# a = {'name': 'python'}
# print(a.keys())

# a = {1, 2, 3, 4, 12, 31}
# b = {1, 2, 3, 4, 12, 31}
# print(a.symmetric_difference(b))
# print(a)

# a = {'banan', 'cherry', 'apple', 'asil'}
# b = {'asil', 'python', 'glass', 'apple'}
# print(a.symmetric_difference(b))
# a.symmetric_difference_update(b)
# print(a)

# a = {1, 2, 4}
# b = {7, 8, 4}
# a.update()
# print(a)

# a = {1234, 5654, 3234, 554, 56, 3243}
# if 3234 in a:
#     a.remove(3234)
# print(a)

# a = {12345, 7654, 7654, 54, 3524, 56, 54, 4, 5, 6, 7}
# b = {12, 56, 54, 5445, 4, 42356, 4, 4, 5, 6, 7, 34, 5}
# a.intersection_update(b)
# print(a)

# import random
# a = [234, 432, 54, 65, 7, 5665]
# d = random.choice(a)
# print(a)
# print(d)

# import random
# print(random.randint(1, 10))

# import random
# a = ["apple", "banana", "cherry"]
# random.shuffle(a)


# import random
# a = [234, 432, 54, 65, 7, 5665]
# d = random.sample(a, k=5)
# # print(a)
# print(d)

# import random
# a = [234, 432, 54, 65, 7, 5665]
# d = random.choices(a, k=3)
# print(a)
# print(d)

# a = input()
# print(a[2])
# print(a[-2])
# print(a[0:5])
# print(a[:-2])
# print(a[::2])
# print(a[1::2])
# print(a[::-1])
# print(a[::-2])
# print(len(a))
# import random


#
# a = input()
# print(a[3:] + a[:3])


# a = input()
# if " " in a:
# print()


# a = input()
# print(a[(len(a)+1) // 2:] + a[:(len(a)+1 // 2])
# b = a[(len(a)+1) // 2:]
# c = a[:(len(a)+1) // 2]
# print(b+c)


# a = input()
# print(a[(len(a)+1) // 2:] + a[:(len(a)+1) // 2])
# b = a[(len(a)+1) // 2:]
# c = a[:(len(a)+1) // 2]
# print(b+c)


# a = int(input())
# one = 1
# if one in a:
#     print(one)


# a = input()
# if a.count('f') == 1:
#     print(-1)
# elif a.count('f') < 1:
#     print(-2)
# else:
#     print(a.find('f', a.find('f') + 1))

# s = input()
# a = s[:s.find('h')]
# b = s[s.find('h'):s.rfind('h')+1]
# c = s[s.rfind('h')+1:]
# s = a + b[::-1] + c
# print(s)


# from random import randint
# a = [234, 432, 54, 65, 7, 5665]
# d = random.choice(a)
# # print(a)
# print(d)
# print(random.choice(a))
# print(random.randint(1, 10))
# print(d)


# a = ['vbnhjk', 'hjk', 'fdgh']
# print(random.shuffle(a[]))


# import random
# def total():
#     a = ["apple", "banana", "cherry"]
#     random.shuffle(a)
#
#     print(a)


# total()

# def aaa():
#     b = int(input())
#     one = 1
#     if one in b:
#         print(one)


# a = ['vbnhjk', 'hjk', 'fdgh']
# random.shuffle(a)
# print(a)

#
from abc import ABC, abstractmethod

class Shakl(ABC):

    @abstractmethod
    def yuza(self):
        pass

    def perimetr(self):
        pass

class Tortburchak(Shakl):
    def init(self, boyi, eni):
        self.boyi = boyi
        self.eni = eni

    def yuza(self):
        return self.eni * self.boyi

    def perimetr(self):
        return (self.eni + self.boyi) * 2

class Kvadrat(Shakl):
    def init(self, tomoni):
        self.tomoni = tomoni

    def yuza(self):
        return self.tomoni * self.tomoni

    def perimetr(self):
        return self.tomoni * 4

obj1 = Shakl()
obj2 = Tortburchak(12, 3)
obj3 = Kvadrat(6)
print(obj1.yuza())
print(obj2.yuza())
print(obj3.yuza())

#
# import uuid
#
#
# class Student:
#     def init(self, name, age, surname, hobby):
#         self.name = name
#         self.age = age
#         self._surname = surname
#         self.hobby = hobby
#         self.__password = uuid.uuid4()
#
#     def return_info(self):
#         return f"{self.name} - {self.hobby}"
#
#     def get_password(self):
#         return self.__password
#
#     def __get_age(self):
#         return self.__age
#
#     def get_surname(self):
#         return self._surname
#
#
# obj = Student('Dishoda', '16', 'Xolmatova', 'running in the morning')
#
# print(obj.name)
# print(obj.get_surname())
# print(obj.get_password())
# # print(obj.get_age())
# # print(obj.__get_age())
#


# from abc import ABC, abstractmethod
#
#
# class Body(ABC):
#
#     @abstractmethod
#     def get_avg(self):
#         pass
#
#     @abstractmethod
#     def get_all_score(self):
#         pass
#
#
# class Students(Body):
#     def __init(self, name, x, y, a, b):
#         self.x = x
#         self.y = y
#         self.a = a
#         self.b = b
#         self.name = name
#
#     # def get_avg(self):
#     #     return (self.x + self.y + self.a + self.b) / 4
#
#     def get_all_score(self):
#         return self.x + self.y + self.a + self.b
#
#
# # object = Students('Bobur', 50, 4,3,2,)
# # print(object.name, object.get_avg())
# object1 = Students('Zafar', 5,4,3,10)
# print(object1.get_all_score())
# # print(object1.get_avg())
