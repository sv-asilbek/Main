# a = int(input())
# g = []
# while a > 0:
#     g.append(a)
#     a = int(input())
#
# print(g)

# a = [13, 4, 12, 5, 67, 84, 980, 56, 43, -46, 9, 0, 1212]
# g = []
# for i in a:
#     if i % 2 == 0:
#         g.append(i)
# print(g)

#  KALKULYATOR

# a = int(input('1-son'))
# b = str(input('operator'))
# c = int(input('2-son'))
# if b == '+':
#     print(a + c)
# elif b == '-':
#     print(a - c)
# elif b == '*':
#     print(a * c)
# elif b == '/':
#     print(a / c)
# elif b == '//':
#     print(a // c)

# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1

# a = int(input())
# b = int(input())
# c = int(input())
#
# a1 = int(input())
# b1 = int(input())
# c1 = int(input())
#
# strike, ball = 0, 0
#
# if a == a1 and b == b1 and c == c1:
#     strike += 3
# elif a == a1 and b == b1 or a == a1 and c == c1:
#     strike += 2
# elif a == a1 or b == b1 or c == c1:
#     strike += 1
#
# if a == b1 or a == c1:
#     ball += 1
# if b == a1 or b == c1:
#     ball += 1
# if c == a1 or c == b1:
#     ball += 1
#
# print(strike, 'S', ball, 'B')

# def summa2():
#     a = int(input())
#     summa = 0
#     for i in range(a+1):
#         summa += i
#     return summa
#
# print(summa2())


# def hello(ism, familiya, yosh):
#     print("Ism: " + ism, "\nFamiliya: " + familiya, "\nYosh:", yosh)
#
#
# f_name = input()
# l_name = input()
# age = int(input())
#
# hello(f_name, l_name, age)
#
#
# def person(*args):
#     for i in args:
#         print(i, end=" ")
#
#
# person('python', 'world')
#
#
# def sum_args(*args):
#     summa = 0
#     for i in args:
#         summa += i
#     return summa
#
# print(sum_args(1,2,3,4,5,6,7,8,9))

# def sum_args(*args):
#     for i in args:
#         if i % 3 == 0:
#             print(i, end=" ")
# sum_args(1,2,3,4,5,6,7,8,9,10)

# from random import randint
# a = [234, 432, 54, 65, 7, 5665]
# d = random.choice(a)
# # print(a)
# print(d)
# print(random.choice(a))
# print(random.randint(1, 10))
# print(d)
# a = ["olma", "banan", "tarvuz"]
# random.shuffle(a)
#
# print(a)


# calendar
# import calendar
#
# print(calendar.calendar(1))
# print(calendar.month(2023, 10))
# print(calendar.month_name[3])
# print(calendar.day_name[6])
# print(calendar.weekday(2023, 10, 9))
# print(calendar.isleap(2016))
#
# # datetime
# import datetime
#
# print(datetime.datetime.now())
# print(datetime.datetime.today())
# print(datetime.time.min)


# def son(b):
#     v = []
#     a = int(b) + 1
#     c = ' '.join(int(i) for i in v)
#     v.append(a)
#     print(a, c, a)
#
#
# a = input('son: ')
# son(a)


# import random
# def son(list):
#     b = random.sample(list, k=5)
#     print(b)

# import Python
# print(Python.sonlar())

# import random
#
# a = random.randint(1, 10)
# b = int(input())
# if b == a:
#     print('Correct', b, a)
# else:
#     b = int(input())

# g = ' '.join(str(i) for i in a)
# print(g)

# for i in range(1, 1000):
#     if i % 2 == 0:
#         v = []
#         a = i ** 2
#         b = i // 2
#         print(a, b)
#         c = a + b
#         v.append(c)
#         print(sum(v))

# import random
# def son(list):
#     b = random.sample(list, k=5)
#     print(b)
#
#
# a = [int(i) for i in input().split()]
#
# son(a)

# import calendar
#
# print(calendar.calendar(2023))
#
# import datetime
#
# print(datetime.datetime.now())
# print(datetime.datetime.today())

# import os
# a = open('newww.py', 'x')
# print(os.getcwd())

import os

# print(os.getcwd())
# a = 'C:/Users/NoutKomp/PycharmProjects/VICTUS/newww.py'
# try:
#     b = os.rmdir(a)
#     print(f'{b} deleted')
# except Exception as af:
#     print(af)


# v = [int(i) for i in input().split()]
# for i in v:
#     print(i ** 3, end=" ")

# 3

# v = [int(i) for i in input().split()]
# z = list(filter(lambda i: i % 2 == 0 and i > 9 and i < 100, a))
# print(v)

# 1
# def son():
#     a = [int(i) for i in input().split()]
#     v = 0
#     for i in a:
#         if i % 2 != 0:
#             v += 1
#     if v == len(a):
#         print(True)
#     else:
#         print(False)
#
#
# son()

# a = [int(i) for i in input().split()]
# for i in a:
#     d = 0
#     for j in a:
#         if i == j:
#             d += 1
# if d == 1:
#     print('Takrorlanish mavjud emas ')
# else:
#     print('Takrorlanish bor')


# a = [int(i)for i in input().split()]
# d = 0
# for i in a:
#     if a.count(i) > 1:
#         d += 1
# if d > 0:
#     print('Takrorlanish bor')
# else:
#     print('Takrorlanish mavjud emas')

# import os
# print(os.makedirs('C:/Users/NoutKomp/OneDrive/Рабочий стол/papka/papka1/papka2'))
# file = 'C:/Users/NoutKomp/OneDrive/Рабочий стол/papka/papka1/papka2'
# if os.path.exists(file):
#     os.rmdir(file)
#     print('Deleted')
# else:
#     print('Bunday fayl yoq')
# file1 = 'C:/Users/NoutKomp/OneDrive/Рабочий стол/papka/papka1'
# if os.path.exists(file1):
#     os.rmdir(file1)
#     print('Deleted')
# else:
#     print('Bunday fayl yoq')
# file2 = 'C:/Users/NoutKomp/OneDrive/Рабочий стол/papka'
# if os.path.exists(file2):
#     os.rmdir(file2)
#     print('Deleted')
# else:
#     print('Bunday fayl yoq')

# a = open('File.txt', 'w')
# a.write('def savol():\n'
# summa = 0\n'
# total = 1\n'
# for i in range(100):\n'
#   if i % 7 == 0 or i % 4 == 0:\n'
#       summa += i\n'
#       total *= i\n'
# print(summa, total))')
# a.write(f'')
#
# a.close()
#
# b = open('New.txt', 'a')
# b.write('Python')
# b.close()
# c = open('New.txt', 'a')
# c.write('\nPycharm')
# c.close()

# import requests
# file = 'https://chrome.com'
# print(requests.get(file))

# import json
# a = {'name': 'Asilbek',
#      'age': 15,
#      'hobby': None}
# b = json.dumps(a)
# print(b)
#
# import json
#
# a = {'name': 'Asilbek',
#      'age': 15,
#      'hobby': None}
# b = json.dumps(a, indent=4)
# print(b)
#
# import json
#
# a = {'name': 'Python',
#      'age': 77,
#      'hobby': 'Chess'}
# b = json.dumps(a, indent=4, separators=(':', ' = '))
# print(b)
#

# a = input('name: ')
# b = input('answer_name: ')
# age = input('age: ')
# hobby = input('hobby: ')
# my_json = f'{a}'':'f'{b}' \
#           f'{age}'':''15' \
#           f'{hobby}'':' 'Chess'
# print(my_json)

# b = json.dumps(my_json, indent=4)
# v = str(b)
# print(b)
# print(v)

# class Person:
#     def __init__(self, ism, age, familiya):
#         self.name = ism
#         self.familiya = familiya
#         self.Yosh = age
#
#     def all_info(self):
#         return f'Ism: {self.name}\nFamiliya: {self.familiya}'
#
#
# Odam = Person('Asilbek', 15, 'Suyunov')
#
# print(Odam.all_info())
# #
# class Car:
#     def __init__(self, name, model, color, speed):
#         self.nomi = name
#         self.marka = model
#         self.rangi = color
#         self.tezligi = speed
#
#     def Completely(self):
#         return f"Ism: {self.nomi}"


# class Noutbook:
#     def __init__(self, ism, marka, xotira):
#         self.name = ism
#         self.model = marka
#         self.memory = xotira
#
#     def end(self):
#         return f"ism: {self.name}\n" \
#                f"model: {self.model}\n" \
#                f"memory: {self.memory}"
#
#
# kompname = Noutbook(input('ism: '), input('model: '), input('memory: '))
# print(kompname.end())
#
#
# def laptop():
#     victus = Noutbook(input('ism: '), input('model'), input('memory: '))
#     for i in range(10):
#         return victus.end()
#
#
# print(laptop())


# class Noutbook:
#     def __init__(self, name, price, color, memory, ram):
#         self.name = name
#         self.price = price
#         self.color = color
#         self.memory = memory
#         self.ram = ram
#     def add_memory(self, x):
#         new_memory = self.memory + x
#         return new_memory
#
#     def all_info(self):
#         return f'nomi: {self.name}\nNarxi: {self.price}\nRangi: {self.color}\nXotirasi: {self.memory}ram: {self.ram}'
#
#
# a = int(input('Kiritiladigan son: '))
# v = []
# for i in range(a):
#     obj = Noutbook(input('name: '), int(input('price: ')), input('color: '), int(input('memory: ')), input('ram: '))
#     v.append(obj)
#
# for i in v:
#     print(i.all_info)
#     l = input('NAME: ')
#     p = i.name
#     if p == l:
#         print('Mavjud')
#     else:
#         print('Mavjud emas')


# class Person:
#     def __init__(self, ism, familiya, yosh, prof):
#         self.name = ism
#         self.surname = familiya
#         self.age = yosh
#         self.prof = prof
#
#     def all_info(self):
#         return f'Ism: {self.name}\nFamiliya: {self.surname}\nYosh: {self.age}\nProfessiya: {self.prof}'
#
#
# a = int(input('Kiritiladigan son: '))
# v = []
# for i in range(a):
#     obj = Person(input('name: '), input('Familiya: '), int(input('Yosh: ')), input('Professiya: '))
#     v.append(obj)
#
# i = 0
# for i in v:
#     print(i.all_info)
# s = int(input('SON: '))
# w = i.age
# if w == s:
#     print('Mavjud')
# else:
#     print('Xato')


# class Student:
#     def __init__(self, name, ball1, ball2, ball3):
#         self.ism = name
#         self.ball1 = ball1
#         self.ball2 = ball2
#         self.ball3 = ball3
#         self.avg = (self.ball1 + self.ball2 + self.ball3) // 3
#         self.maximum = max(ball1, ball2, ball3)
#
#     def all_info(self):
#         return f'Ism: {self.ism},Avarage score: {self.avg}, Maximum: {self.maximum}'
#
#
# n = int(input('SON: '))
# for i in range(n):
#     obj = Student(input('name: '), int(input('Ball-1: ')), int(input('Ball-2: ')), int(input('Ball-3: ')))
#     v = obj.all_info()
#     print(v)
# a = [213, 12, 3, 213, 21, 31, 243, 25, 25, 324, 21, 4, 213]
# for i in a:
#     print(i, end=' ')
# # v = []
# summa = 0
# i = 0
# j = 0
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] > j:
#             j += 1
#             summa += 1
#             print(summa)

# a = [213, 12, 3, 213, 21, 31, 243, 25, 25, 324, 21, 4, 213]
# for i in a:
#     print(max(a))


# a = [213, 12, 3, 213, 21, 31, 243, 25, 25, 324, 21, 4, 213]
# a.sort(reverse=True)
# print(a[0])

# a = [213, 12, 3, 213, 21, 31, 243, 25, 25, 324, 21, 4, 213]
# max = a[0]
# for i in range(1, len(a)):
#     if max < a[i]:
#         # max = a[i]
#         print(a[i])


# class Father:
#     def init(self, name, age, car):
#         self.name = name
#         self.age = age
#         self.car = car
#
#     def malumot(self):
#         return f'Ism: {self.name}, Age: {self.age}, Car_name: {self.car}'
#
#
# class Child1(Father):
#     def init(self, name, age, car, course):
#         # Father.init(self, name, age, car)
#         super().init(name, age, car)
#         self.kurs = course
#
#     def malumot(self):
#         return f'Ism: {self.name}\nYosh: {self.age}\nCar: {self.car}\nKurs: {self.kurs}'
#
#
# class SubChild(Child1):
#     def init(self, name, age, car, course):
#         Child1.init(self, name, age, car, course)
#
#
#
#
#
#
# obj2 = Child1('Usmonali', 24, 'Audi R8', 'Python')
# print(obj2.malumot())
#
# # obj3 = SubChild('Sulton', 'Pytyhon')
# #
# # print(obj3.malumot())
#
#
# # obj1 = Father('Jaloldin', 56, 'BMW')
# # # print(obj1.malumot())
# # print(obj1.name)

# from abc import ABC, abstractmethod
#
#
# class Abstraction(ABC):
#     @abstractmethod
#     def all_info(self):
#         pass
#
#
# class Car(Abstraction):
#     def __init__(self, name, color, speed):
#         self.name = name
#         self.color = color
#         self.speed = speed
#
#     def all_info(self):
#         return self.name, self.color, self.speed
#
#
# class Avto(Car):
#     def __init__(self, name, color, speed):
#         Car.__init__(self, name, color, speed)
#
#     def get_name(self):
#         return self.name
#
#
# class Avtomobil(Car):
#     def __init__(self, name, color, speed):
#         Car.__init__(self, name, color, speed)
#
#     def get_name(self):
#         return self.name
#
#
# class PinCar(Car):
#     def __init__(self, name, color, speed, Pin):
#         Car.__init__(self, name, color, speed)
#         self.__pin = Pin
#
#     def get_Pin(self):
#         return self.__pin
#
#
# obj1 = Car('BMW', 'black', 360)
# obj2 = Car('Mersedes', 'blue', 300)
# obj3 = Car('Bentley', 'white', 280)
# obj4 = PinCar('Gentra', 'black', 220, 2008)
# for i in obj1, obj2, obj3, obj4:
#     print(i.name)
#
# print(obj4.get_Pin())


# from abc import ABC, abstractmethod
#
#
# class New(ABC):
#     @abstractmethod
#     def all_info(self):
#         pass
#
#
# class Laptop(New):
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#
#     def all_info(self):
#         return self.name, self.color, self.memory
#
#
# class Noutbook(Laptop):
#     def __init__(self, name, color, memory, rtx):
#         super().__init__(name, color, memory)
#         self.rtx = rtx
#
#     def infos(self):
#         return self.name, self.color, self.memory, self.rtx
#
#
# class PIN(Noutbook):
#     def __init__(self, name, color, memory, rtx, password):
#         super().__init__(name, color, memory, rtx)
#         self.__password = password
#
#     def passwordPin(self):
#         return self.__password
#
#
# obj1 = Noutbook('VICTUS', 'black', 256, 30_50)
# obj2 = PIN('Lenovo', 'grey', 256, 30_50, 2008)
# print(obj2.passwordPin())


# class Phone:
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#
#     def all_info(self):
#         return self.name, self.color, self.memory
#
#
# class Telefon(Phone):
#     def __init__(self, name, color, memory):
#         Phone.__init__(self, name, color, memory)
#
#
# n = int(input('Kiritiladigan son: '))
# world = []
# a = []
# for i in range(n):
#     obj = Telefon(input('name: '), input('color: '), int(input('memory: ')))
#     world.append(obj.name)
#     a.append(obj)
#
# search = input('search: ')
# index = world.index(search)
# total = a[index]
# Finish = []
# Finish.append(total.all_info())
# print(Finish)

