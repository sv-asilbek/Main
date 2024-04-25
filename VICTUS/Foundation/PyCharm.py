# 1
# my_dict = {'A': 10, 'B': 5, 'C': 8}
# m = my_dict.values()
# print(max(m))
# 2
# my_dict = {'A': 10, 'B': 5, 'C': 8}
# m = my_dict.values()
# print(min(m))
# 3
# my_dict = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
# a = my_dict.values()
# print(max(a))
# 4
# my_tuple = (1, 2, 3, 4, 5)
# a = ''.join(str(i) for i in my_tuple)
# print(a)
# 5
# my_tuple = ('A', 'B', 'C', 'D', 'E')
# print(my_tuple[::-1])
# 6
# my_set = {1, 2, 3, 4, 5}
# a = ''.join(str(i) for i in my_set)
# print(a)
# 7
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# print(set1.union(set2))
# 8
# import os
#
#
# print(os.getcwd())
# 9
# import os
#
#
# file_path = "file.txt"
# if os.path.exists("file.txt"):
#     os.remove('file.txt')
#     print('Deleted')
# else:
#     print('Bunday file yo\'q')

# 10
# import requests
#
#
# url_path = 'https://realpython.com/tutorials/advanced/'
# data = requests.get(url_path)
# print(data.status_code)
# print(data.text)
# 11
# import requests
#
#
# def son():
#     url_path = 'https://realpython.com/tutorials/advanced/'
#     data = requests.post(url_path)
#     print(data.status_code)
#     print(data.text)
#
#
# son()

# 13
# import random
#
#
# z = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'x', 'X', 'y', 'Y', 'z', 'Z', 'w', 'W', '@', '!', '#', '$', '&', '*', '?', '.', '..', ' ']
# v = random.sample(z, k=50)
# print(''.join(str(i) for i in v))

# 14
# a = open('yangi.txt', 'x')
# a.write('Biz Python FOundationni tamomlayapmiz, Biz kuchli dasturchi bo\'lamiz')
# a.close()
# 15
# b = open('yangi.txt', 'r')
# print(b.read())
# b.close()
# 16
# v = open('yangi.txt', 'a')
# v.write('Sabr+Harakat+Ishonch=Muvaffaqqiyat\n')
# v.close()
# 17
# import os
# if os.path.exists('yangi.txt'):
#     os.remove('yangi.txt')
#     print('deleted')
# else:
#     print('Bunday file mavjud emas !')

# def name():
#     ism = input('Name: ')
#     password1 = int(input('PIN1: '))
#     password2 = int(input('PIN2: '))
#     if password1 == password2:
#         print(password1, password2, ism)
#         print(ism, 'Muvaffaqiyatli otdingiz')
#     else:
#         print('Error')
#         return name()
#
#
# name()
#
# password1 = int(input('PIN1: '))
# password2 = int(input('PIN2: '))
# Ism = input()
# name(password1, password2, Ism)
# import os
#
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
#
#
# import json
# data = '{"name": "Asilbek", "age": 22}'
# result = json.dumps(data)
# print(result)
#
#
# data = {
#     'name': 'John',
#     'age': 35,
#     'child': {
#         'name': 'Bob',
#         'age': 12,
#         'name2': 'Lucy',
#         'age2': 15,
#     },
#     'profession': {
#         'job': 'developer',
#         'work_place': 'LosAngels',
#         'salary': 120_000_000,
#         'boss': None,
#     }
# }
#
# a = data.get('profession')
# b = a.get('salary')
# print(b)
#
# a = data.get('child')
# b = a.get('name2')
# print(b)
# #
# a = data.get('profession')
# b = a.items()
# h = list(b)
# print(h[3])
#
#
# a = int(input('Oquvchilar_soni_1: '))
# b = int(input('Oquvchilar_soni_2: '))
# c = int(input('Oquvchilar_soni_3: '))
# for i in a, b, c:
#     f = int(i / 2)
#     if i % 2 != 0:
#         b = i + 1
#         l = b / 2
#         v = f + l
#         print(v)
#
#
# def son(func):
#     def world():
#         a = int(input('Son: '))
#         print(a ** 2)
#
#     func()
#     return world()
#
#
# @son
# def org():
#     a = input('___: ')
#     if a == 'Salom':
#         print(a)
#     else:
#         print('Error')


# class Student:
#     def __init__(self, name, ball1, ball2, ball3):
#         self.name = name
#         self.ball1 = ball1
#         self.ball2 = ball2
#         self.ball3 = ball3
#
#         self.total = (self.ball1 + self.ball2 + self.ball3) // 3
#
#     def info(self):
#         return f"Name: {self.name} - Total: {self.total}"
#
#     def all_info(self):
#         return max(self.ball1, )
#
#
# n = int(input('SON: '))
# l = []
# for i in range(n):
#     obj = Student(input('Name: '), int(input('Ball-1: ')), int(input('Ball-2: ')), int(input('Ball-3: ')))
#     l.append(obj)
#
# for i in l:
#     print(i.info())

# class Car:
#     def __init__(self, name, color, speed):
#         self.name = name
#         self.color = color
#         self.speed = speed
#
#     def info(self):
#         return f'Ism: {self.name}\nColor: {self.color}\nSpeed: {self.speed}'
#
#
# class Electrocar(Car):
#     def __init__(self, name, color, speed):
#         Car.__init__(self, name, color, speed)
#
#
# obj = Electrocar(input('name: '), input('color: '), int(input('speed: ')))
# print(obj.info())


# class Car:
#     def __init__(self, name, color, speed):
#         self.name = name
#         self.color = color
#         self.speed = speed
#
#     def info(self):
#         return f"name: {self.name}, color: {self.color}, speed: {self.speed}"
#
#
# obj = Car('BMW', 'black', 360)
# obj2 = Car('Audi', 'white', 280)
# print(obj.info())
# print(obj2.info())

# class Car:
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#
#     def all_info(self):
#         print(f"name: {self.name}\nColor: {self.color}\nPrice: {self.price}")
#
#
# n = int(input('Objectlar soni: '))
# f = []
# g = []
# for i in range(n):
#     objects = Car(input('name: '), input('color: '), int(input('price: ')))
#     f.append(objects)
#     g.append(objects.color)
#
# maxx = f[-1]
# for i in f:
#     if maxx.price > i.price:
#         maxx = i
# maxx.all_info()
