from art import tprint
tprint('go')
import random
print(random.randint(1,8))

class A: ...  # родительский супер класс


class B(A): ...  # дочерний класс


# super()...


# инкапсуляция... абстракция
# git clone
# наследование полиморфизм


# 2

class Bank(object):
    def __init__(self, name, age, key, money):
        self.name = name
        self.age = age
        self.__key = key
        self._money = money

    def tprint(self):
        print(self.name, self._money)

    def keys2(self):
        self.__keys()

    def __keys(self):
        print(self.__key)


# 1 публичный, 2 приватный _, 3 скрытый __

beka = Bank('beka', 20, '123edftrewer', 1_000)
beka.tprint()
beka._money = 1_000_000
beka.tprint()

mirlan = Bank('mirlan', 17, '123456789', 1_000)
beka.__key = '123456789'
beka.age2 = 12
# print(beka.__key)
beka.keys2()
print(B.mro())

print(dir(beka))
beka._Bank__key = 'qweqweqwe'