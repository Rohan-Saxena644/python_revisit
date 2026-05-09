class Animal:
    name = "lion" #class attribute

    def __init__ (self,age):
        self.age =  age #instance attribute

        
    def show(self):
        print("name:",self.name)
        print("age:",self.age)    

    def eat(self):
        print("eating")

    @classmethod
    def sleep(cls):
        print("sleeping")

    @staticmethod
    def run():
        print("running")


obj = Animal(12)

obj.show()


# class Factory: #parent c;ass
#     a = "I am a Factory"

#     def hello(self):
#         print("Hello from factory")


# class Factory2(Factory):  #child class / sub class
#     pass

# obj = Factory()
# print(obj.a)

# obj2 = Factory2()
# print(obj2.a) #inheritance


# class Animal:
#     def __init__(self,name):
#         self.name = name    

#     def show(self):
#         print("name:",self.name)


# class Human(Animal):
#     def __init__(self,name,age):
#         super().__init__(name) #call the parent class constructor
#         self.age = age

#     def show(self):
#         print("name:",self.name)
#         print("age:",self.age) 

# person = Human("John",23)
# animal1 = Animal("lion")

# person.show()


# Exzample of multiple inheritance
# class Animal:
#     def __init__ (self,age):
#         self.age = age #instance attribute
#     name = "lion" #class attribute

# class Human:
#     def __init__(self,age,state):
#         self.age = age #instance attribute
#     name = "John" #class attribute

# class Robots(Animal,Human):
#     name = "Robo"


# obj = Robots(age=10)  # constructor of the first class inherited will be used
# print(obj.name) #name from Animal class       


# class Factory:
#     def __init__(self,material,zips):
#         self.material = material
#         self.zips = zips

# class Factory2(Factory):
#     def __init__(self,material,zips,color):
#         super().__init__(material,zips) #call the parent class constructor
#         self.color = color  


# class Factory3(Factory2):
#     def __init__(self,material,zips,color,size):
#         super().__init__(material,zips,color) #call the parent class constructor
#         self.size = size

# obj = Factory3("steel",100,"red","large")
# print(obj.material)                

#polymorphism
# class Animal:
#     def show(self):
#         print("I am an animal")

# class Human(Animal):
#     def show(self):
#         print("How are you")

# obj = Human()                
# obj.show()

# # Duck typing
# class Animal:
#     def show(self):
#         print("I am an animal")

# class Human:
#     def show(self):
#         print("How are you")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()


# class Factory:
#     __a = "pune"
    

#     def show(self):
#         print("I am a factory")
#         print(Factory.__a)

# # class Factory2(Factory):
# #     def show(self):
# #         print(super().a)        

# obj = Factory()
# # obj2 = Factory2()

# print(obj.show())


# ABSTRACTION
# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Rectangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width  



# DUNDER METHODS

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello how are you {self.name}"
    
    def __add__(self,other):
        sum = 0
        for i in other:
            sum += i.age
        return f"your sum of ages are {self.age + sum}"


obj = Animal("Lion",12)
obj2 = Animal("Tiger",10)
obj3 = Animal("Leopard",8)
print(obj + (obj2 , obj3))


#Decorator
# class Animal:
#     @property
#     def show(self):
#         print("Hello how are you")


# obj = Animal()

# obj.show

# Base of decorator

# def decorate(func):
#     def wrapper():
#         print("I will print myself before the function hello is called")
#         func()
#         print("I will print after the function hello is called")
#     return wrapper

# @decorate
# def hello():
#     print("Hello how are you")

# hello()


# def decorate(func):
#     def wrapper(a,b):
#         print("I will print myself before the function hello is called")
#         func(a,b)
#         print("I will print after the function hello is called")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(f"Your sum is {a+b}")

# addition(12,67)


# def addition(*args):
#     print(args)
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)

# def information(**kwargs):
#     print("Your information is:")
#     for i in kwargs:
#         print(i,":",kwargs[i])

# information(name="John",age=23,city="Pune")

# addition(12,67,23,56)    


# # Now in decorator

# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("I will print myself before the function hello is called")
#         func(*args,**kwargs)
#         print("I will print after the function hello is called")
#     return wrapper

# @decorate
# def addition(*args): 
#     sum = 0
#     for i in args:
#         sum += i
#     print(f"Your sum is {sum}")


# addition(12,67)    


# List Comphrension

# a = 12

# print("even number") if a % 2 == 0 else print("odd number")

# label = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
# # ['Even', 'Odd' , 'Even' , 'Odd' , 'Even']

# evens = {x: x*x for x in range(10) if x % 2 == 0}
# # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# unique_even_squares = {x*x for x in range(10) if x % 2 == 0}
# # {0, 4, 16, 36, 64}

# l = [i for i in range(1,21) if i % 2 == 0]
# # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(l)

# l = {i: i**2 for i in range(1,21) if i%2 == 0}
# # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100, 12: 144, 14: 196, 16: 256, 18: 324, 20: 400}


# # Lambda function 
# addition = lambda a,b : a+b
# print(addition(12,67))

# addition = lambda *args : sum(args)
# print(addition(12,67,23,56))

# addition = lambda a: "even" if a%2 == 0 else "odd"
# print(addition(12))

# # Map filter and zip
# l = [1,2,3,4,5]
# doubled = list(map(lambda x: x*2,l))

# l = [1,2,3,4,5]
# def double(x):
#     return x*2

# doubled = list(map(double,l))


# def is_even(x):
#     return x % 2 == 0

# a = [1,2,3,4,5]
# even_numbers = list(filter(is_even,a))

# a = [1,2,3,4,5]
# even_numbers = list(filter(lambda x: x%2 ==  0, a))

# a = [1,2,3,4,5]
# even = list(filter(lambda x: True if x%2 == 0 else False, a))


# Packages and Modules

from models import hello as h,maths as m 

print(m.addition(12,12))
h.hello()

import math as m
print(m.sqrt(16))

# if another folder inside models then we can import it like this
# from models.subfolder import module_name as alias_name