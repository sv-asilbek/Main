# class Laptop:
#     def init(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#
#     def all_info(self):
#         return self.name, self.color, self.memory
#
#     def return_color(self):
#         return self.color
#
#
# class Phone:
#     def init(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#
#     def all_info(self):
#         return self.name, self.color, self.memory
#
#     def return_color(self):
#         return self.color
#
# #
# from abc import ABC, abstractmethod
#
# class Shakl(ABC):
#
#     @abstractmethod
#     def yuza(self):
#         pass
#
#     def perimetr(self):
#         pass
#
# class Tortburchak(Shakl):
#     def init(self, boyi, eni):
#         self.boyi = boyi
#         self.eni = eni
#
#     def yuza(self):
#         return self.eni * self.boyi
#
#     def perimetr(self):
#         return (self.eni + self.boyi) * 2
#
# class Kvadrat(Shakl):
#     def init(self, tomoni):
#         self.tomoni = tomoni
#
#     def yuza(self):
#         return self.tomoni * self.tomoni
#
#     def perimetr(self):
#         return self.tomoni * 4
#
# # obj1 = Shakl()
# obj2 = Tortburchak(12, 3)
# obj3 = Kvadrat(6)
# # print(obj1.yuza())
# print(obj2.yuza())
# print(obj3.yuza())
#
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
#
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
# # object = Students('aaa', 50, 4,3,2,)
# # print(object.name, object.get_avg())
# object1 = Students('www', 5,4,3,10)
# print(object1.get_all_score())
# # print(object1.get_avg())
#
#
# class Car:
#     def init(self, name, color, speed):
#         self.name = name
#         self.color = color
#         self.speed = speed
#
#     def all_info(self):
#         return self.name, self.color, self.speed
#
#     def return_color(self):
#         return self.color
#
#
# for i in Laptop, Phone, Car:
#     print()
#
# class Windows:
#     def __init__(self, name, model, color, memory):
#         self.name = name
#         self.model = model
#         self.color = color
#         self.memory = memory
#
#     def info(self):
#         return f'Ism: {self.name}\nModel: {self.model}\nColor: {self.color}\nMemory: {self.memory}'
#
#
# class Lenux(Windows):
#     def __init__(self, name, model, color, memory):
#         Windows.__init__(self, name, model, color, memory)
#
#
# obj = Lenux('hp', 'victus', 'black', 256)
# print(obj.info())
#
# class Avto:
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#
#     def info(self):
#         return f'name: {self.name}\ncolor: {self.color}\nprice: {self.price}\n'
#
#     def avto_name(self):
#         return f'name: {self.name}'
#
#
# obj1 = Avto('Bentley', 'grey', 100_000_000)
# print(obj1.info())
#
#
# class Car(Avto):
#     def mashina(self, name, color, price, engine):
#         Avto.__init__(self, name, color, price)
#         self.engine = engine
#
#
# obj2 = Avto('BMW', 'blue', 230_000_000)
# print(obj2.info())
#
#
# class ElectroCar(Avto):
#     def electro(self, name, color, price):
#         Avto.__init__(self, name, color, price)
#
#
# obj3 = ElectroCar('Mersedes', 'white', 120_000_000)
# print(obj3.info())
#
#
# class It:
#     def __init__(self, sound, color, type):
#         self.sound = sound
#         self.color = color
#         self.type = type
#
#     def infos(self):
#         return self.sound, self.color, self.type
#
#
# class Mushuk:
#     def __init__(self, sound, color, type):
#         self.sound = sound
#         self.color = color
#         self.type = type
#
#     def infos(self):
#         return self.sound, self.color, self.type
#
#
# class Sigir:
#     def __init__(self, sound, color, type):
#         self.sound = sound
#         self.color = color
#         self.type = type
#
#     def infos(self):
#         return self.sound, self.color, self.type
#
#
# animal1 = It('Wow', 'black', 'Apcharka')
# animal2 = Mushuk('Miyov', 'white', 'rich')
# animal3 = Sigir('Moo', 'Black', 'Galand')
#
# for i in animal1, animal2, animal3:
#     # print(i.color)
#     print(i.infos())
#
# class Number1:
#     def __init__(self, name, digit):
#         self.name = name
#         self.digit = digit
#
#     def infos(self):
#         return self.name, self.digit
#
#
# class Number2:
#     def __init__(self, name, digit):
#         self.name = name
#         self.digit = digit
#
#     def infos(self):
#         return self.name, self.digit
#
#
# class Number3:
#     def __init__(self, name, digit):
#         self.name = name
#         self.digit = digit
#
#     def infos(self):
#         return self.name, self.digit
#
#
# a = Number1('Number1', 1).infos()
# b = Number2('Number2', 5).infos()
# c = Number3('Number3', 3).infos()
#
# v = []
# v.append(a[1])
#
# n = []
# n.append(b[1])
#
# m = []
# m.append(c[1])
#
# total = (v[0] + n[0] + m[0]) // 3
# print(total)
#
#
# class Avtomobil:
#     def __init__(self, name, color, speed):
#         self.name = name
#         self.color = color
#         self.speed = speed
#
#     def infos(self):
#         return self.name, self.color, self.speed
#
#
# class Car(Avtomobil):
#     def __init__(self, name, color, speed):
#         Avtomobil.__init__(self, name, color, speed)
#
#     def infos(self):
#         return self.name, self.color, self.speed
#
#
# class Electrocar(Avtomobil):
#     def __init__(self, name, color, speed):
#         Avtomobil.__init__(self, name, color, speed)
#
#     def infos(self):
#         return self.name, self.color, self.speed
#
#
# avtomobil = Avtomobil('bentley', 'blue', 300)
# car = Avtomobil('BMW', 'black', 400)
# avto = Avtomobil('Mersedes', 'white', 360)
# for i in Avtomobil, Car, Electrocar:
#     print(i)
#
#
# from abc import ABC, abstractmethod
#
#
# class Car(ABC):
#     def __init__(self, name, color, speed):
#         self.name = name
#         self.color = color
#         self.speed = speed
#
#     def info(self):
#         return self.name, self.color, self.speed
#
#
# class Name(Car):
#     # @abstractmethod
#     def car_name(self):
#         return self.name
#
#
# class Avto(Name):
#     def __init__(self, name, color, speed):
#         Car.__init__(self, name, color, speed)
#
#
# obj = Avto('BMW', 'white', 400)
# print(obj.car_name())
#
# from abc import ABC, abstractmethod
#
#
# class Avto(ABC):
#     def __init__(self, name, price1, price2, price3):
#         self.name = name
#         self.price1 = price1
#         self.price2 = price2
#         self.price3 = price3
#
#     def info(self):
#         return self.name, self.price1, self.price2, self.price3
#
#
# class Car(Avto):
#     @abstractmethod
#     def max_price(self):
#         pass
#
#     @abstractmethod
#     def min_price(self):
#         pass
#
#     @abstractmethod
#     def name(self):
#         pass
#
#
# obj = Car('BMW', 4000, 5000, 6000)
# print(obj.info())
#
# 342, 21, 27
#
# class Article:
#     def init(self, name, image, author, description):
#         self.name = name
#         self.image = image
#         self.author = author
#         self.description = description
#
#     @property
#     def get_image(self):
#         return self.image
#
#     def get_info(self):
#         return f'Name{self.name}\nAuthor{self.author}\nDescription{self.description}\nImage: {self.get_image}'
#
#
# class Article_Detail(Article):
#     def init(self, name, image, author, description):
#         super().init(name, image, author, description)
#
#
# n = int(input())
# f = []
# for i in range(n):
#     object = Article_Detail(input('name: '), input('image_path: '), input('author: '), input('description: '))
#     f.append(object)
#
#
#
# a = [1, 2, 3, 5]
# search = int(input('search: '))
#
# import queue
# a = queue.Queue()
# a.put(34)
# a.put(37)
# a.put(30)
# a.put(12)
# while not a.empty():
#     b = a.get()
#     print(b)
#
#
# class Stack:
#     def init(self):
#         self.stack = []
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#
#     def peek(self):
#         if not self.is_empty():
#             return self.stack[-1]
#
#     def size(self):
#         return len(self.stack)
#
#
# # Stack obyektini yaratish
# stack = Stack()
#
# # Elementlarni qo'shish
# stack.push(10)
# stack.push(20)
# stack.push(30)
#
# # Elementlarni o'qish
# print(stack.peek())  # 30
# print(stack.pop())  # 30
#
# # Stackning hozirgi o'lchami
# print(stack.size())  # 2
#
#
# # Classwork
# # Leetcode: 859(easy), 155(medium), 70(easy)
#
# import queue
#
# a = queue.Queue()
# a.put(22)
# a.put(780)
# a.put(78)
# a.put(7)
# a.put(2)
#
# while not a.empty():
#     b = a.get()
#     print(b)
#
# import queue
# a = queue.Queue()
# a.put('Salom')
# a.put('hello')
# a.put('world')
# a.put('python')
#
# while not a.empty():
#     b = a.get()
#     print(b)
#
#
# import queue
#
# a = queue.Queue()
# a.put(33)
# a.put('sssssssss')
# a.put(22)
#
# while not a.empty():
#     b = a.get()
#     print(b)
#

# import networkx as nx
# import matplotlib.pyplot as plt
#
# G = nx.Graph()
#
# G.add_node("Murodbek")
# G.add_node("Bobur")
# G.add_node("Davron")
# G.add_node("Xurshid")
# G.add_node("Asilbek")
# G.add_node("Shaxzod")
# G.add_node("Asadbek")
# G.add_node("Firdavs")
# G.add_node("Zafar")
# G.add_node("Islombek")
# G.add_node("Begzod")
# G.add_node("Ali")
#
# G.add_edge("Murodbek", "Bobur")
# G.add_edge("Bobur", "Davron")
# G.add_edge("Davron", "Xurshid")
# G.add_edge("Xurshid", "Asilbek")
# G.add_edge("Asilbek", "Shaxzod")
# G.add_edge("Shaxzod", "Asadbek")
# G.add_edge("Asadbek", "Firdavs")
# G.add_edge("Firdavs", "Zafar")
# G.add_edge("Zafar", "Islombek")
# G.add_edge("Islombek", "Begzod")
# G.add_edge("Begzod", "Ali")
#
# nx.draw(G, with_labels=True)
# plt.show()


# a = [132, 321, 321132, 213, 3212, 132, 132, 2, 31232, 123, 1322]
# a.sort()
# print(a[0])
# a.sort(reverse=True)
# print(a[0])

# b = [int(i) for i in input().split()]
# b.sort()
# print(b[0])
# b.sort(reverse=True)
# print(b[0])

# a = [int(i) for i in input().split()]
# summa = a[0]
# total = a[0]
# data = {'category': [
#     'cat_id',
#     'cat_name'
# ],
#     'product': [
#         'samsung', 1000,
#         'apple', 5000,
#         'category', 'phone'
#
#     ]}
# summa = int(input('summa: '))
# total = int(input('total: '))
# category = input('category: ')
# for i in range(1, 2):
#     a = open('mainn.txt', 'a')
#     a.write(data[summa],['total'],['category'])
#     a.close()


# for i in range(len(a)):
#     if summa < a[i]:
#         summa = a[i]
#
# print(summa)
# del summa
# for i in range(len(a)):
#     if total < a[i]:
#         total = a[i]
#         print(total)
