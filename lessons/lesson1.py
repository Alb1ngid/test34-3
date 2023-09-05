# ООП,алгоритмы,базы данных, GIT

# Class: методы свойства экземпляры

# lambda

# def a(b,c):
#     print(b+c)
#
# a(6,9)


class Human:
    body = True # свойства


    # магические методы
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self): #принт
        return f"name is: {self.name}\n" \
               f"age is: {self.age}\n"

    def __len__(self):
        return f"{len(self.name)}"

    def run(self): # методы
        print('run',self.name)

human = Human('beka',20) # экземпляры
human1 = Human('mirlan',17)

print(len(human1))

print(human1)
human.run()
#
# a = 1, 7.9, 'str', True, [], {}, ()
#
# print(type(a))
