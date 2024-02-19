#动物类
class Ainimal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def call(self):
        print("动物发出的叫声:")

#狗类
class Dog(Ainimal):  #继承动物类

    def call(self):  #重写动物类的call方法
        if self.name == 'Jack':
            print("汪汪汪")

#猫类
class Cat(Ainimal):  #继承动物类

    def call(self):  #重写动物类的call方法
        if self.name == 'Tom':
            print("喵喵喵")

#鸟类
class Bird(Ainimal):  #继承动物类

    def call(self):   #重写动物类的call方法
        if self.name == 'Nancy':
            print("叽叽叽")

#房间类
class House:
    def knock_door(self,Ainimal): # Ainimal 作为基类
        Ainimal.call()

if __name__ == "__main__":
    name = input()
    age = input()
    ainimal = Ainimal(name,age)
    dog = Dog(name,age)
    cat = Cat(name,age)
    bird = Bird(name,age)
    house = House()
    house.knock_door(ainimal)
    house.knock_door(dog)
    house.knock_door(cat)
    house.knock_door(bird)
