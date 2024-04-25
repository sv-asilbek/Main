# N1
# a = int(input('1-raqam: '))
# b = int(input('2-raqam: '))
# i = 1
# while i <= min(a, b):
#     if a % i == 0 and b % i == 0:
#         Ekub = i
#     i += 1
# if Ekub == (a + b) // 2:
#     print('1')
# elif Ekub != (a + b) // 2:
#     print('0')


# N6
# a = [1, 2, 31, 12, 42, 56, 89, -98, 0, -56]
# b = int(input('Son Kiriting: '))
# if b in a:
#     print('1')
# else:
#     print('0')

# N7
# a = {'smartphones':
#          {'brends':
#               {'apple':
#                    {'name': 'python',
#                     'price': '1800$',
#                     'color': 'Silver',
#                     },
#                'samsung':
#                    {'name': 'samsung',
#                     'price': '1500$',
#                     'color': 'black',
#                     }
#                }
#           }
#      }
#
# print(a['smartphones']['brends']['apple']['name'], a['smartphones']['brends']['apple']['price'],
#       a['smartphones']['brends']['apple']['color'])
# print(a['smartphones']['brends']['samsung']['name'], a['smartphones']['brends']['samsung']['price'])

# N4
# a = (1, 2, 3, 44, 9, True, 0, 2, 9, False)
# b = set(a)
# print(b)

# N3
# a = ('world', True)
# print(a)
# print(type(a))
#
# b = tuple('world')
# print(b)
# print(type(b))

# N2
# a = [int(i) for i in input('raqam: ').split()]
# total = 0
# for i in range(len(a)):
#     b = (a[i] ** 2)
#     total += b
# print('Summa:', total)
# print('O\'rta arifmetik:', sum(a) / len(a))
# print('uzunligi:', len(a))

# N5
# a = [float(i) for i in input('numbers: ').split()]
# b = a[0]
# for o in range(len(a)):
#     if b > a[o]:
#         b = b
#     elif b < a[o]:
#         b = a[o]
# e = a[0]
# for f in range(len(a)):
#     if e < a[f]:
#         e = e
#     elif e > a[f]:
#         e = a[f]
# a.remove(b)
# c = a[0]
# for k in range(len(a)):
#     if c > a[k]:
#         c = c
#     elif c < a[k]:
#         c = a[k]
# print('max1:', b)
# print('max2:', c)
# print('minus:', e)

# N9
# Text = 'Sa1l0omP9^ayt54h*on@89da8&stur12ch1i7la12r'
#
# a = []
# b = []
# c = []
#
# for i in Text:
#     if i.isalpha():
#         a.append(i)
#     elif i.isdigit():
#         b.append(i)
#     else:
#         c.append(i)
#
# print("letter:", a)
# print("number:", b)
# print("character:", c)

# # N8
# a = input('Input: ')
# for i in a:
#     if not i.isalpha() and not i.isnumeric():
#         print(i, end=' ')

