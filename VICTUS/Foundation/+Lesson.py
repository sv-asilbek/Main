# 1
# b = ('Bobur', 'Asadbek', 'Zafar', 'Murod', 'Asilbek', 'Shahriyor', 'Otabek')
# print(b)

# 2
# a = ([int(i) for i in input().split()])
# a.sort(reverse=True)
# print(a)
# b = {1, 2, 3, 4, 5, 'python'}
# print(type(b))


# a = [1, 2, 321, 34, 213, 21, 321, 3, 21, 3, 213, 213, 21, 321, 3, 213, 12, 3]
# print(set(a))
# for i in a:
#     print(i, end=" ")


# a = ['Bobur', 'Asadbek', 'Zafar', 'Murod', 'Muslima', 'Asilbek', 'Xurshid', 'Davron', 'Shahriyor', 'Otabek', 'Ali',
#      'Islom']
# b = ['Asilbek', 'Xurshid']
# c = ['Davron']
# d = ['Shahriyor', 'Otabek', 'Ali', 'Islom']
# e = set(a)
# f = set(b)
# g = set(c)
# h = set(d)
# p = {'Alimardon'}
# print(p.union(e, f, g, h))


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
#     a.remove(554)
# print(a)
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# a.pop()
# print(a)
# a.add(12)
# print(a)
# print(list(a))
# print(complex(a))
# b = str(a)
# print(type(b))
# print(b)

# a = {'name': 'Asilbek'}
# print(a.values())


# a = {213, 21, 43, 46, 7, 987565, 3, 542, 52, 64}
# for i in a:
#     print(i, end=" ")

# a = {12345, 7654, 7654, 54, 3524, 56, 54, 4, 5, 6, 7}
# b = {12, 56, 54, 5445, 4, 42356, 4, 4, 5, 6, 7, 34, 5}
# a.intersection_update(b)
# print(a)


#
# def son(**kwargs):
#     a = int(input())
#     b = int(input())
#     c = int(input())
#     d = int(input())
#     e = int(input())
#
#     print(a ** 2, b ** 2, c ** 2, d ** 2, e ** 2)
#     print(a ** 2 + b ** 2 + c ** 2 + d ** 2 + e ** 2)
#
#
# son()

# a = [i for i in input().split()]
# b = list(map(lambda v: v.upper(), a))
# print(b)

# a = [i for i in input().split()]
# b = list(filter(lambda v: v.isdigit(), a))
# print(b)


# def son(v):
#     number = list(map(lambda z: z.lower(), v))
#     return number
#
#
# g = ['UZUM', 'PAYME', 'CLICK']
#
# print(son(g))

# 1)

# print([int(i) for i in input().split()
# 2)

# a = int(input('son1: '))
# b = input('belgi: ')
# c = int(input('son2: '))
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
# elif b == '%':
#     print(a % c)

# 3)

# a = [i for i in input().split()]
# b = list(filter(lambda v: v.isalpha(), a))
# print(b)

# 4)

# a = [1, 3, 21, 45, 78, 89, 0, 87, 54, 4, 3, 22, -8]
# v = []
# b = []
# for i in a:
#     if i % 2 == 0:
#         v.append(i)
#     if i % 2 != 0:
#         b.append(i)
# print(v)
# print(b)

# 5)

# def son():
#     v = []
#     a = [i for i in input().split()]
#     for i in a:
#         if i.isalpha():
#             v.append(i)
#         print(v)
#
#
# print(son())

# ISYSTEM
# name = str(input('ismingizni kiriting: '))
# if name == 'Maxmud':
#     print('Mening ismim', name)
# else:
#     print('Notog\'ri ism kiritildi')
#
#
#
#
# a = int(input('son1 = '))
# b = int(input('son2 = '))
# if a > b:
#     print(a, katta-if')
#
#
# a = 5
# b = 5
# if a > b:
#     print(a)
# if a < b:
#     print(b)
# if a == b:
#     print('teng')
# if a >= b:
#     print('katta yoki teng')
# if a <= b:
#     print('kichik yoki teng')
# if a !=b:
#     print('teng emas')
# # and -- va(and ni ikkala tarafi ham True bolishi kerak)
# # or -- yoki(or ni yoki o'ng yoki chap tarafi True bolsa dastur ishlaydi)
#
# a = in
#
#
# a = 12
# if a > 0:
#     print('dan katta son')
#
# print(0dan katta bolsagina; ')
#
#
#
#
#
#
#
# a = N<0
#     if a % 2:
#     # # # print("12")
#     # # print(12)
#     # # print(type("12"))
#     # # print(type(12))
#     # '''Biz pythonnni o'rganishni boshladik'''
#     # print("Python")
#     # name = "Alimardon"
#     # print(name)
#     # a = 12
#     # b = 90
#     # print(a + b)
#     # a = 12
#     # b = 50
#     # c = a * b
#     # print(c)
#     # int n = 12
#     # a = 50
#     # print(a)
#     # a = "olma"
#     # print(a)
#
#     # a = 15
#     # b = 5
#     # print(a - b)
#     # a = 12
#     # b = 20
#     # c = a  # c = 12
#     # a = b  # a = 20
#     # b = c  # b = 12
#     #
#     # print("A =", a)  # 20
#     # print("B =", b)  # 12
#
#     # a = 12
#     # b = 20
#     # a = a + b  # a = 12 + 20 = 32
#     # b = a - b  # 32 - 20 = 12
#     # a = a - b  # 32 - 12 = 20
#     # print("A =", a)
#     # print("B =", b)
#
#     # my name = "Alimardon" mumkin emas
#     # my-name = "Alimardon" mumkin emas
#     # 1my_name = "Alimardon"  mumkin emas
#     # $name = "salom"  mumkin emas
#         my_name = "Alimardon"  # mumkin
#     myName = "Alimardon"  # mumkin
#     my_name12 = "Alimardon"  # mumkin
#     a = 12
#     print(my_name)
#     print(myName)
#     # print(1my_name)
#     print(my_name12)
#     print(a)
#
#
#
#
#
#
# print("Hello Python") # string

# a = ['python', 'english', 'program', 11, 23, 45, 768]
# import random
# from Programming import total
#
# total()
#
# print(random.randint(1, 8))
# import random


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

# def ismlar():
#     a = [int(i) for i in input().split()]
#     print(a)
#
#
# ismlar()


# def name(a):
#     return a
#
#
# a = [str(i) for i in input().split()]
# print(name(a))

# a = ['python', 'english', 'program', 11, 23, 45, 768]
# import random
# from Programming import total
#
# total()
#
# print(random.randint(1, 8))

# from Programming import aaa
# aaa()

# a = ['vbnhjk', 'hjk', 'fdgh']
# random.shuffle(a)
# print(a)

# a = random.randint(1, 9999)
# print(a)


# a = ['vbnhjk', 'hjk', 'fdgh']
# print(random.shuffle(a[]))


# a = [21, 3, 24, 5, 678, 53]
# print(random.choice(a))


# def name(a):
#     return a
#
#
# a = [str(i) for i in input().split()]
# print(name(a))


# a = [21, 3, 24, 5, 678, 53]
# print(random.sample(a, 1))
# print(a)

# a = [21, 3, 24, 5, 678, 53]
# random.shuffle(a)
# print(a)

# a = [21, 3, 24, 5, 678, 53]
# print(random.choice(a))

# a = [21, 3, 24, 5, 678, 53]
# print(random.randint(1,10))
# print(a)

# a = random.randint(1, 9999)
# print(a)


# a = ['vbnhjk', 'hjk', 'fdgh']
# print(random.shuffle(a[]))


# a = [21, 3, 24, 5, 678, 53]
# print(random.choice(a))

# def total():
#     Parol = int(input('PIN: '))
#     b = random.randint(999, 9999)
#     for i in range(b):
#         if i == Parol:
#             print(Parol, 'Sizning Parolingiz')
#
#
# Parol = int(input('PIN: '))
# total()


# a = {21345, 5432, 5, 789, 9, 8, 7896, 78, 97, 5543, 45, 8, 34, 56, 3, 564}
# b = {34, 56, 75, 2, 3457, 86, 564, 3, 456, 889, 98, 7, 6, 3, 34, 58, 12}
# ikkala setdan oxshash raqamlarni topib, toqlarini ochiring va ularning yigindisini toping

# a = input()
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
# print(calendar.calendar(2023))


# def vzlom(a):
#     b = ['1', '2', '3', '4', '5',  '6', '7', '8', '9', '0', 'a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'x', 'X', 'y', 'Y', 'z', 'Z', 'w', 'W', '@', '!', '#', '$', '&', '*', '?', '.', '..', ' ']
#     f = []
#     for i in a:
#         if i in b:
#             f.append(i)
#         print('searching...')
#     d = ''.join(str(i) for i in f)
#     print('Your PIN:', d)
#
#
# a = input('PIN: ')
# vzlom(a)


import random

# def sonlar():
#     a = [int(i) for i in input().split()]
#     b = random.sample(a, k=6)
#     print(b)
#
#
# sonlar()


# from rembg import remove
# from PIL import Image
#
# rasm = "m.jpg"
# natija = "natija.png"
# rasm_path = Image.open(rasm)
# natija_path = remove(rasm_path)
# natija_path.save(natija)

# def aaa():
#     a = {}
#     v = [int(i) for i in input().split()]
#     for i in range(len(v)):
#         if i % 3 == 0:
#             a.add(v[i])
#     return a
#
#
# print(aaa())

# n = int(input())
# i = 1
# while i <= n:
#     if n % i == 0:
#         print(i, end=" ")
#         i += 1
#
# n = int(input('javob: '))
# # k = int(input('tahmin:'))
# while n != k:
#     print("corek")
# while n > k:
#     print("up")
# while n < k:
#     print("daun")
import random

# #
# # # 2 misol
# n = int(input('javob: '))
# k = int(input('tahmin:'))
# while n != k:
#     if k > n:
#         print(k, '>')
#         k = int(input('tahmin'))
#     elif k < n:
#         print(k, '<')
#     else:
#         print('toptingiz', k, '==', n)
# else:
#     print('toptingiz', k, '==', n)

# j=0
# m=int(input())
# # while j < m:
#
# i=1
# while
#
# print("bobur")
#
# a=int(input('son1'))
# b=int(input('son2'))
# s=(a*b//2)
# print(s)
#
# a=int(input("hozirgi yil"))
# b=int(input("tug'ilgan yilimgiz"))
# s=(a-b)
# print(s, "yoshdasiz")
# print(12)

# def ismlar():
#     return a
#
# a = [str(i) for i in input().split()]
# print(ismlar())

import random

#
# def sonni_top():
#     a = random.randint(1, 10)
#     b = int(input('son'))
#     while True:
#         if a == b:
#             print('toptingiz son', b)
#             break
#         elif a > b:x
#             print('katta son kriting')
#             b = int(input())
#         elif a < b:
#             print('kichik son kriting')
#
#

# array = [3, 4, 52, 5, 7, 4, 6, 78, 5, 9]
# max = array[0]
# for i in range(len(array)):
#     if array[i] > max:
#         max = array[i]
# print(max)













