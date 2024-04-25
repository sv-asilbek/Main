# a = int(input('son1 = '))
# b = int(input('son2 = '))
# c = int(input('son3 = '))
# d = int(input('son4 = '))
# m = min(a, b, c, d)
# x = max(a, b, c, d)
# summa = 0
# for i in range(m, x + 1):
#     summa += i
# print(summa)
#
# a = [13, 4, 12, 5, 67, 84, 980, 56, 43, -46, 9, 0, 1212]
# g = []
# for i in a:
#     if i % 2 == 0:
#         g.append(i)
# print(g)
#
# def son(x):
#
#     a = []
#     for i in range(x):
#         if i % 2 != 0:
#             a.append(i)
#     print(a)
# b = int(input())
# son(b)
#
#
# a = (1, 2, 3, 4, 12, 6, 7, 8, 9)
# print(a[1]+a[3]+a[4]+a[5]+a[7])
import asyncio.windows_events
# a = int(input('son1 = '))
# b = int(input('son2 = '))
# c = int(input('son3 = '))
# print(a * a + b * b + c * c)
# print(a  2 + b  2 + c  2)
# print(pow(a, 2) + pow(b, 2) + pow(c, 2))
import timeit


# a = int(input('son = '))
# if a % 2 != 0 and a > 9 and a < 100:
#     print(a)
# else:
#     print('None')
# if a >= -99 and a <= -10 or a >= 10 and a <= 99:
#     if a % 2 != 0:
#         print(a)
#     else:
#         print('None')
# else:
#     print('None')

# a = int(input('son1 = '))
# v = int(input('son2 = '))
# m = min(a, v)
# summa = 0
# while m <= max(a, v):
#     summa += m
#     m += 1
# print(summa)
# m = min(a, v)
# summa = 0
# for i in range(m, max(a, v)+1):
#     summa += i
#
# print(summa)

# a = int(input('son1 = '))
# b = int(input('son2 = '))
# c = int(input('son3 = '))
# d = int(input('son4 = '))
# minimum = min(a, b, c, d)
# maximum = max(a, b, c, d)
# total = 0
# # for i in range(minimum, maximum+1):
# #     total += i
# # print(total)
# while minimum <= maximum:
#     total += minimum
#     minimum += 1
# print(total)

# a = [1, 5, 8, 12, 9, -4, 212]
# f = []
# # for i in a:
# #     f.append(i*i)
# #     # print(i * i, end=' ')
# # print(f)
# i = 0
# g = len(a)
# while i < g:
#     f.append(a[i]  2)
#     i += 1
# print(f)
# a = int(input('son: '))
# m = []
# while a > 0:
#     m.append(a)
#     a = int(input('son: '))
# print(m)
# n = []
# while True:
#     a = int(input('son = '))
#     if a > 0:
#         n.append(a)
#     else:
#         break
# print(n)

# a =[13, 4, 12, 5, 67, 84, 980, 56, 43, -46, 9, 0, 1212]
# g = []
# for i in a:
#     if i % 2 == 0:
#         g.append(i)
# print(g)
#
# def sonlar(x):
#     a = []
#     for i in range(1, x + 1):
#         a.append(i)
#     return a
#
#
# a = int(input())
# print(sonlar(a))
# def son(a):
#     m = []
#     for i in range(1, a + 1):
#         if i % 2 == 0:
#             m.append(i)
#     return m
#
#
# a = int(input())
# print(son(a))

# Pythonda tuplelar
# a = [1]
# b = (1,)
# print(type(a), a)
# print(type(b), b)
# a = [212, 43, 2, 3]
# a[1] = 'Salom'
# print(a)
# b = (212, 43, 2, 3)
# b[1] = 'Salom'
# print(b)
# a = (1, 2, 3, 4, 12, 6, 7, 8, 9)
# print(a[1])
# print(a[1:8])
# print(a[::2])
# print(a[::-1])
# k = a[0] + a[8]
# print(k)

# d = a[1] + a[3] + a[4] + a[5] + a[7]
# print(d)
# summa = 0
# for i in a:
#     if i % 2 == 0:
#         summa += i
# print(summa)
# n = input()
# a = (1, 2, 3, 4, 5, 6425, 2, 32, 31)
# a = ('apple', 'orange', 'python')
# if n in a:
#     print('yes')
# else:
#     print('no')
# a = (1, 2, 312, 3, 124, 124, 12, 3, 21, 312, 3, 123, 12, 312,21,3,12,231,2,21,12,1,21,2,1,2,1,2,1312,3,1,2,21,2,124)
# print(a.count(312))
# print(a.count(3))
# print(a.count(2))
# print(a.count(100))
# print(a.index(124))
# print(len(a))
# b = (1, 2, 3)
# c = tuple(b)
# print(b)
# print(c)
# a = list(b)
# a.append('tuple')
# b = tuple(a)
# print(b)
# a = [1,2,3,4]
# b = (1,2,3,4)
# import sys
# import timeit
# print(sys.getsizeof(a), "bytes")
# print(sys.getsizeof(b), "bytes")
#
# print(timeit.timeit(stmt="[0,1,2,3,4,5,6]", number=1000000))
# print(timeit.timeit(stmt="(0,1,2,3,4,5,6)", number=1000000))


# a = int(input())
# b = int(input())
#
# print(a ** 3)
# print(b ** 3)
# print(a ** 3 + b ** 3)

# a = int(input())
# b = int(input())
#
# print(a ** 3 +b ** 3)

# for i in range(1, 11):
#     print(i ** 2, end=" ")

# def Hello_world():
#     a = int(input('hello world'))
#     print(a)
#
#
# Hello_world()
# g = []
# for i in range(1, 30 + 1):
#     if i % 3 == 0:
#         g.append(i)
# print(g)


# def summa():
#     g = []
#     for i in range(1, 101):
#         if i % 7 == 0 and i % 8 == 0:
#             g.append(i)
#             print(g)
#
#
# summa()


# def summa():
#
#
#     a = [1, 2, 7, 9, 11, 134, 12, 49]
#     b = int(input())
#     print(a.index(b))
#     if b in a:
#         print()
#     else:
#         print('-1')
#
#
# summa()


# a = input()
# v = []
# h = []
# for i in a:
#     if i.upper():
#         v.isappend(i)
#     if i.islower():
#         h.append(i)
# print(v)
# print(h)


# a = input()
# for i in a:
#     if i.islower():
#         print(i, end="")


# print([int(i) for i in input().split()])


# print(input().count(' ') + 1)


# a = [int(i) for i in input().split()]

# def max_son():
#     g = []
#     a = [int(i) for i in input().split()]
#     for i in a:
#         if g.isupper(i):
#             print(i, end=" ")
#
#
# max_son()


# g = []
# for i in range(1, 201):
#     if i % 3 == 0 and i % 5 == 0:
#         g.append(i)
# print(g)
# print(g[::-1])

# a.sort(reverse=True)


# def stri_inte(st):
#     a = int(st) + 1
#     d = str(a)
#     if a > 9 and a < 100:
#         print(a, ' ', a)
#
#
# m = '123'

























