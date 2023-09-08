# принципы ооп

# класс: свойства методы атрибуты экземпляры и магич.методы

#
# def init(a,b):
#     print(a+b)
#
# init(7,9)


class A:
    a = 'beka'

    # конструктор класса
    def __init__(self, b, c):
        self.b = b
        self.c = c

    def s(self):
        print('свойство этой переменной равна', self.a)

    def __str__(self): ...


a = A('b', 'c')
c = A('c', 'b')
a.s()


# 3 +1 наследование полиморфизм инкапсуляция + абстракция

class Cat:  # Супер класс или родительский класс
    sleep = True

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def runnig(self):
        print(f'{self.name} run')


cat1 = Cat(20, 'beka')
cat1.runnig()


class Cat2(Cat):  # дочерний класс
    def __init__(self, age, name, name_human):
        super().__init__(age, name)
        # Cat.__init__(self,age,name)
        self.human = name_human

    sleep = False

    def ff(self):
        print(f'{self.name} умеет прыгать')

    def runnig(self):
        if self.sleep == True:
            print(self.name, 'оно спит')
        else:
            super().runnig()


cat2 = Cat2(21, 'арсик', 'Beka')
cat2.runnig()
cat2.ff()
