'''
课后作业：自己写一个面向对象的例子
使用 yaml 来管理实例的属性
'''
import yaml

'''
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
'''


class Animal():
    '''定义一个Animal的类'''

    def __init__(self, name, color, age, sex):
        '''初始化属性name,color,age和sex'''
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def call(self):
        """模拟动物叫"""
        print(f"{self.name} is now calling")

    def run(self):
        # print(self.name.title() + "is now running")
        print(f"{self.name} is now running")


'''
创建子类【猫】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=短毛，
- 添加一个新的方法， 会捉老鼠，
- 复写父类的‘【会叫】的方法，改成【喵喵叫】
'''


class Cat(Animal):
    def __init__(self, name, color, age, sex, hair):
        '''
        初始化父类的属性
        :param name:
        :param color:
        :param age:
        :param sex:
        '''
        super(Cat, self).__init__(name, color, age, sex)
        self.hair = hair
        # self.skill = ""

    def hair(self):
        print(f"{self.name} has short hair")

    def skill(self):
        print(f"{self.name} 捉到了老鼠")

    def call(self):
        print("This cat can't run. It can meow")


'''
创建子类【狗】，继承【动物类】，
- 复写父类的__init__方法，继承父类的属性，
- 添加一个新的属性，毛发=长毛，
- 添加一个新的方法， 会看家，
- 复写父类的【会叫】的方法，改成【汪汪叫】
'''


class Dog(Animal):
    def __init__(self, name, color, age, sex, hair):
        super(Dog, self).__init__(name, color, age, sex)
        self.hair = hair

    def hair(self):
        print(f"{self.name} has long hair")

    def skill(self):
        print(f"{self.name} 会看家")

    def call(self):
        print(f"{self.name} 汪汪叫")


if __name__ == '__main__':
    with open("animal_data.yml") as f:
        data = yaml.safe_load(f)

    print(data)
'''
创建一个猫猫实例
- 调用捉老鼠的方法
- 打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
'''
# if __name__ == "__main__":
#     my_animal_cat = Cat('Lucy','black',2,'female','short')
#
#
# print("这只猫叫"f'{my_animal_cat.name}, {my_animal_cat.color}色, {my_animal_cat.age}岁了,是{my_animal_cat.sex}猫,{my_animal_cat.hair}发!')
# my_animal_cat.skill()

'''
创建一个狗狗实例
- 调用【会看家】的方法
- 打印【狗狗的姓名，颜色，年龄，性别，毛发】。
'''
# dog = Dog('Anne', 'yellow', 5, 'male', 'long')
# print("这只狗叫"f'{dog.name}, {dog.color}色, 今年快{dog.age}岁了,{dog.sex} dog,{dog.hair}发!')
# dog.call()
# dog.skill()
