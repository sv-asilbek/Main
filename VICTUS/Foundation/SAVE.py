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

# os
# a = open('File.txt', 'w')
# a.write('def savol():\n'
#         '    summa = 0\n'
#         '    total = 1\n'
#         '    for i in range(100):\n'
#         '       if i % 7 == 0 or i % 4 == 0:\n'
#         '           summa += i\n'
#         '           total *= i\n'
#         '    print(summa, total))')
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
import os

# import qrcode
#
# # QR kod yaratish uchun ma'lumot
# data = "https://www.instagram.com/alimardon_boqijonov/"
#
# # QR kod obyektini yaratish
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=15,
#     border=4,
# )
#
# # Ma'lumotni QR kodga qo'shish
# qr.add_data(data)
# qr.make(fit=True)
#
# # QR kodni rasmga o'rnatish
# img = qr.make_image(fill_color="black", back_color="white")
#
# # Rasmni sahifaga saqlash
# # img.save("insta.png")


# import os
# print(os.cpu_count())

#
# a = os.getcwd()
# print(a)

# b = os.listdir('C:/Users/NoutKomp/PycharmProjects\VICTUS')
# print(b)

# import os
#
# v = os.getcwd()
# print(v)
# a = 'C:/Users/NoutKomp/OneDrive/Рабочий стол/Pythonospath'
# try:
#     b = os.rmdir(a)
#     print(f'{b} ochirildi')
# except Exception as af:
#     print(af)

# def password():
#     password1 = int(input('PIN1: '))
#     password2 = int(input('PIN2: '))
#     if password1 == password2:
#         print('Correct')
#     else:
#         print('Error')
#         return password()
#
#
# password()

# def plusOne(digits):
#     v = []
#     a = ''.join(str(i) for i in digits)
#     a = str(int(a) + 1)
#     for i in a:
#         v.append(i)
#     return v
#
#
# y = int(input('Son: '))
# print(plusOne(y))
import collections
import math


# def plusOne(digits):
#     a = int(digits) + 1
#     d = str(a)
#     j = []
#     for i in d:
#         j.append(int(i))
#     return j
#
#
# m = int(input('Son: '))
# print(son(m))
# print(type(m))


# def lanlastWord(s):
#     b = s[-1]
#     print(len(b))
#
#
# a = input().split()
# lanlastWord(a)


# def son(nums, target):
# while target in nums:
#     v = nums.index(target)
#     print(v)
# else:
#     print('-1')

# target = int(input('Son: '))
# nums = [4, 5, 6, 7, 0, 1, 2]
# if target in nums:
#     v = nums.index(target)
#     print(v)
# else:
#     print('-1')


# def like():
#     def wrapper():
#         v = input('YouTube: ')
#         if v == 'like':
#             print('Accaunt kiriting')
#         else:
#             print('Ok')
#         return wrapper()
#
#
#
#
#
# def account(email):
#     def wrapper():
#         print(' Accaunt kiriting')
#         email()
#
#     return wrapper
#
#
# @like
# @account
# def register(func):
#     def wrapper(*args, **kwargs):
#         a = input('Ismingizni kiriting: ')
#         b = input('Parolni kiriting: ')
#         if a and b:
#             print('Royxatdan otdingiz')
#         func()
#
#     return wrapper
#
#
# register()


# def forma(func):
#     def wrapper():
#         v = []
#         a = input()
#         v.append(a)
#         print(v)
#         func()
#     return wrapper()
#
#
# @forma
# def sss(fun):
#     for i in range(10 + 1):
#         a = input('Ism: ')
#         b = input('Familya: ')
#         c = input('Tel: ')
#
#         print(a, b, c)
#         fun()
#
# sss()


# storage = []
#
#
# def post():  # create
#     data = input().split()
#     for i in data:
#         storage.append(i)
#     return data
#
#
# def get_objects_all():  # read
#     return storage
#
#
# def get_object():
#     id = int(input())
#     return storage[id]
#
#
# def put():  # update
#     id = int(input())
#     new_data = input()
#     storage[id] = new_data
#     return storage
#
#
# def delete():  # delete
#     id = int(input())
#     storage.pop(id)
#     return storage
#
#
# print(f"Post: {post()}")
# print(f'Get_all: {get_objects_all()}')
# print(f'Get: {get_object()}')
# print(f'Put:  {put()}')
# print(f'Delete: {delete()}')


# def total(x, y):
#     summa = 0
#     j = min(x, y)
#     l = max(x, y)
#     for c in range(j, l):
#         summa += c
#     return summa
#
#
# n = int(input('Son1: '))
# m = int(input('Son2: '))
# print(total(n, m))

# def son():
#     a = int(input('a: '))
#     b = int(input('b: '))
#     summa = 0
#     for i in range(a + 1):
#         summa += i
#     print(summa)
#     if a == b:
#         print('=')
#     else:
#         print('null')
#
# son()

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

# from abc import ABC, abstractmethod


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
# def liner_search(objects, target):
#     for i in range(len(objects)):
#         if objects[i].name == target:
#             return objects[i].get_info()
#
#
#
# target = input('search... ')
# print(liner_search(f, target))

# def mergeTwoLists(list1, list2):
#     f = []
#     b = list1 + list2
#     b.sort()
#     f.append(b)
#     f.sort()
#     return f
#
#
# a = [1, 2, 3, 748, 4]
# b = [1, 5, 3, 798, 3, 34]
# print(mergeTwoLists(a, b))


# def son(st):
#     goal = st.reverse
#     return goal
#
#
# a = 'ab'
# print(son(a))

# def isPowerOfFour(n):
#     if n % 4 == 0:
#         return True
#     elif n == 1:
#         return True
#
#     else:
#         return False
#
#
# a = int(input('Son: '))
# print(isPowerOfFour(a))

#
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
# f = []
# for i in range(n):
#     obj = Telefon(input('name: '), input('color: '), int(input('memory: ')))
#     f.append(obj)
#
#
# def liner_search(objects, target):
#     for j in range(objects):
#         if target == obj.name:
#             return j
#
#
#
# print(liner_search())

# 342, 21, 27

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
# def liner_search(objects, target):
#     for i in range(len(objects)):
#         if objects[i].name == target:
#             return objects[i].get_info()
#
#
#
# target = input('search... ')
# print(liner_search(f, target))

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
#
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


# def searchInsert(nums, target):
#     total = 0
#     uzunligi = len(nums)
#
#     while total < uzunligi:
#         indeks = (total + uzunligi) // 2
#         if nums[indeks] == target:
#             return indeks
#         if nums[indeks] < target:
#             total = indeks + 1
#         else:
#             uzunligi = indeks
#     return total
#
#
# a = [1, 2, 3, 5]
# search = int(input('search: '))
# print(searchInsert(a, search))


# import queue
# pq = queue.Queue()
# pq.put(0)
# pq.put(7)
# pq.put(5)
# pq.put(3)
# pq.put(1)
# while not pq.empty():
#     a = pq.get()
#     print(a)

# def runningSum(nums):
#     for i in nums:
#         return i + [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1]
#
#
# a = [1, 2, 3, 4]
# print(runningSum(a))

# import queue
#
#
# class Queue:
#     def __init__(self, input0):
#         self.a = queue.Queue()
#         self.a.put(input0)
#
#     def reverse(self):
#         while not self.a.empty():
#             c = self.a
#             return c
#
#
# b = [int(i) for i in input().split()]
# obj = Queue(b)
# print(obj.reverse())

# import queue
#
# a = queue.Queue()
# a.put('hello')
# a.put('salom')
# a.put('world')
# a.put('python')
# while not a.empty():
#     b = a.get()
#     print(b)
#
# pq = queue.LifoQueue()
# pq.put(1)
# pq.put(2)
# pq.put(3)
# pq.put(4)
# while not pq.empty():
#     w = pq.get()
#     print(w)
#
#
# class Queue:
#     def __init__(self):
#         self.queue = []
#
#     def is_empty(self):
#         return len(self.queue) == 0
#
#     def enqueue(self, element):
#         self.queue.insert(0, element)
#
#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.pop()
#
#
# obj = Queue()
# obj.enqueue(1)
# obj.enqueue(12)
# obj.enqueue(188)
# print(obj.queue)
# print(obj.dequeue())
# print(obj.dequeue())
# obj.enqueue('hello')
# print(obj.dequeue())
# print(obj.queue)

# LinkedList
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#     def printlist(self):
#         x = self.head
#         while x:
#             print(x.data)
#             x = x.next


# llist = LinkedList()
# llist.head = Node(1)
# llist.head.next = Node(2)
# llist.head.next.next = Node(3)
#
# print(llist.head.data)

# obj = LinkedList()
# obj.head = Node('Yakshanba')
# week2 = Node('Dushanba')
# week3 = Node('Seshanba')
# week4 = Node('Chorshanba')
# print(week2.data)
#
# obj.head.next = week2
# week2.next = week3
# week3.next = week4
# week4.next = obj.head
# print(obj.head.data)
# print(obj.printlist())

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#
# node1 = LinkedList()
# node1.head = Node('Monday')
# node2 = Node('Tuesday')
# node3 = Node('wednesday')
# node4 = Node('thursday')
# node5 = Node('friday')
# node6 = Node('saturday')
# node7 = Node('Sunday')
#
# node1.head.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6
#
# print(node2.next.data)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.last = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#
# node5 = LinkedList()
# node5.head = Node(5)
# node4 = Node(4)
# node3 = Node(3)
# node2 = Node(2)
# node1 = Node(1)
#
# node5.head.last = node4
# node4.last = node3
# node3.last = node2
# node2.last = node1
#
#
# print(node5.head.last.data)

# class Matem:
#     def __init__(self, input_1):
#         self.input_1 = input_1
#
#     def all_info(self):
#         return self.input_1
#
#
# class Algebra(Matem):
#     def __init__(self, input_1):
#         Matem.__init__(self, input_1)
#
#
# class Matematika(Matem):
#     def __init__(self, input_1):
#         Matem.__init__(self, input_1)
#
#
# a = [int(i) for i in input().split()]
# b = [int(i) for i in input().split()]
# c = [int(i) for i in input().split()]
# h = a.sort()
# j = a.sort()
# h = a.sort()
# obj1 = Matem(h)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def insert(root, data):
#     if root is None:
#         return Node(data)
#     else:
#         if data < root.data:
#             root.left = insert(root.left, data)
#         else:
#             root.right = insert(root.right, data)
#
#     return root
#
#
# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.data)
#         inorder_traversal(root.right)
#
#
# root = None
# root = insert(root, 5)
# root = insert(root, 3)
# root = insert(root, 8)
# root = insert(root, 1)
# root = insert(root, 4)
#
# inorder_traversal(root)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def preorder_traversal(root):
#     if root:
#         print(root.data)
#         preorder_traversal(root.left)
#         preorder_traversal(root.right)
#
#
# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.data)
#         inorder_traversal(root.right)
#
#
# def postorder_traversal(root):
#     if root:
#         postorder_traversal(root.left)
#         postorder_traversal(root.right)
#         print(root.data)
#
#
# root = Node(5)
# root.left = Node(3)
# root.right = Node(8)
# root.left.left = Node(1)
# root.left.right = Node(4)
# print('Preorder traversal:')
# postorder_traversal(root)
# print('Inorder traversal:')
# inorder_traversal(root)
# print('Postorder traversal:')
# postorder_traversal(root)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def preorder_traversal(root):
#     if root:
#         print(root.data)
#         preorder_traversal(root.left)
#         preorder_traversal(root.right)
#
#
# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.data)
#         inorder_traversal(root.right)
#
#
# def postorder_traversal(root):
#     if root:
#         postorder_traversal(root.left)
#         postorder_traversal(root.right)
#         print(root.data)
#
#
# # Daraxtni yaratish
# root = Node(8)
# root.left = Node(3)
# root.right = Node(4)
# root.left.left = Node(12)
# root.left.right = Node(23)
# root.left.right.left = Node(26)
# root.left.right.right = Node(18)
# root.right.right = Node(7)
#
# # Daraxtni tarqatishlar
# print("Preorder traversal:")
# preorder_traversal(root)
#
# print("Inorder traversal:")
# inorder_traversal(root)
#
# print("Postorder traversal:")
# postorder_traversal(root)

# Preorder traversal:
# 5
# 3
# 1
# 4
# 8
# Inorder traversal:
# 1
# 3
# 4
# 5
# 8
# Postorder traversal:
# 1
# 4
# 3
# 8
# 5

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def insert(root, data):
#     if root is None:
#         return Node(data)
#     else:
#         if data < root.data:
#             root.left = insert(root.left, data)
#         else:
#             root.right = insert(root.right, data)
#
#     return root
#
#
# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.data)
#         inorder_traversal(root.right)
#
#
# root = None
# root = insert(root, 5)
# root = insert(root, 3)
# root = insert(root, 8)
# root = insert(root, 1)
# root = insert(root, 4)
#
# inorder_traversal(root)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def preorder_traversal(root):
#     if root:
#         print(root.data)
#         preorder_traversal(root.left)
#         preorder_traversal(root.right)
#
#
# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.data)
#         inorder_traversal(root.right)
#
#
# def postorder_traversal(root):
#     if root:
#         postorder_traversal(root.left)
#         postorder_traversal(root.right)
#         print(root.data)
#
#
# root = Node(5)
# root.left = Node(3)
# root.right = Node(8)
# root.left.left = Node(1)
# root.left.right = Node(4)
# print('Preorder traversal:')
# postorder_traversal(root)
# print('Inorder traversal:')
# inorder_traversal(root)
# print('Postorder traversal:')
# postorder_traversal(root)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# def preorder_traversal(root):
#     if root:
#         print(root.data)
#         preorder_traversal(root.left)
#         preorder_traversal(root.right)
#
#
# def inorder_traversal(root):
#     if root:
#         inorder_traversal(root.left)
#         print(root.data)
#         inorder_traversal(root.right)
#
#
# def postorder_traversal(root):
#     if root:
#         postorder_traversal(root.left)
#         postorder_traversal(root.right)
#         print(root.data)
#
#
# # Daraxtni yaratish
# root = Node(8)
# root.left = Node(3)
# root.right = Node(4)
# root.left.left = Node(12)
# root.left.right = Node(23)
# root.left.right.left = Node(26)
# root.left.right.right = Node(18)
# root.right.right = Node(7)
#
# # Daraxtni tarqatishlar
# print("Preorder traversal:")
# preorder_traversal(root)
#
# print("Inorder traversal:")
# inorder_traversal(root)
#
# print("Postorder traversal:")
# postorder_traversal(root)

# Preorder traversal:
# 5
# 3
# 1
# 4
# 8
# Inorder traversal:
# 1
# 3
# 4
# 5
# 8
# Postorder traversal:
# 1
# 4
# 3
# 8
# 5

# import json
#
# a = ('world', 'python', None)
# b = json.dumps(a)
# print(type(b))
# print(b)
#
# n = json.loads(b)
# print(type(n))
# print(n)

