# множественное наследование
# venv

# инкапсуляцию абстракция

# скрытые детали, класс
# 3 публичный,_привытный-защищенный,__скрытый
# _Class__object
# object class - Super klass

class Дед:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print('sleep')

ded=Дед('Бекболот',20)
ded.sleep()
class Отец(Дед):
    def work(self):
        print(self.name, 'working')

name=Отец('мирлан',17)
name.work()

class Отчим:
    def __init__(self,name2):
        self.name=name2

    def starwars(self):
        print(self.name,"я твой отец")

name2=Отчим('Нурлан')


class Son(Отец,Отчим):...


#
# # MRO-порядок наследования методов
# son=Son('люк',17)
# son.starwars()
# venv

import math
# import импортирует целый модуль
print(math.e)


from math import pi
print(pi)
# модули 3 встроенные собвственные и внешние
