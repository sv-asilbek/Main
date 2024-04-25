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
#


