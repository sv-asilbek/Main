# a = [int(i)for i in input().split()]
# d = 0
# for i in a:
#     if a.count(i) > 1:
#         d += 1
# if d > 0:
#     print('Takrorlanish bor')
# else:
#     print('Takrorlanish mavjud emas')

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


# 1
# def son(x):
#     b = list(map(lambda z: z ** 2, x))
#     return b
#
#
# a = [int(i) for i in input().split()]
# print(son(a))

# 2
# a = str(input())
# for i in a:
#     if i.isalpha():
#         print(i, end=" ")

# 3
# import random
#
# a = random.randint(10, 20)
# while True:
#     v = int(input("Taxmin son: "))
#     if v == a:
#         print("Tog\'ri")
#         break
#     elif v < a:
#         print("Kattaroq son kiriting")
#     elif v > a:
#         print("Kichikroq son kiriting")

# c = 'Mevalar == 15.000'
# v = 'Sabzavotlar == 20.000'
# b = 'shirinliklar == 40.000'
# a = open('MAkro.txt', 'x')
# f = input('kassir: ')
# a.write('-------📙--Havas--📙--------\n'
#         'Kassir:\n'
#         'Produktalar: 2x5.000 = 10.000\n'
#         'Mevalar:\n'
#         '--------------------------\n'
#         'QQS: 15%  = 145\n'
#         'Total price: 10.145\n'
#         'Kassir'.format(f))
# a.close()

# a = open("secret.png", "rb")
# print(a.read())
# a.close()

























