#1
class student:
    def __init__(self,name,marks):
       self.name=name
       self.marks=marks
    def display(self):
      print(f"student's name:{self.name} and student's marks is:{self.marks}" )
result=student("alizah",90)
result.display()   
    #   2
class Counter:
    count = 0  

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Counter.count += 1  

    @classmethod
    def show(cls):
        print(f"Total count = {cls.count}")
a = Counter("Alizah", 17)
b = Counter("Ayesha", 16)
Counter.show()
# 3

class car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
            print(f"{self.brand} engine started.")
brand_car=car("toyota")
# accesing public variable
print(brand_car.brand)
# accessing public method
brand_car.start()            

# 4
class Bank:
    bank_name = "Pak Islamic Bank"   # Class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder  # Instance variable

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name  # Change shared data

    def display(self):
        print(f"{self.account_holder} - {Bank.bank_name}")
a1 = Bank("Alizah")
a2 = Bank("Ayesha")

a1.display()   
a2.display()   

Bank.change_bank_name("New Islamic Bank")

a1.display()   
a2.display()   
# 5
class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
print(MathUtils.add(2,5))    


# 6. Constructors and Destructors
class Logger:
    def __init__(self):
        print("Logger object created")

    def __del__(self):
        print("Logger object destroyed")


# 7. Access Modifiers
class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # public
        self._salary = salary  # protected
        self.__ssn = ssn  # private


# 8. The super() Function
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


# 9. Abstract Classes and Methods
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# 10. Instance Methods
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"


# 11. Class Methods
class Book:
    total_books = 0

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


# 12. Static Methods
class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


# 13. Composition
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start_engine(self):
        return self.engine.start()


# 14. Aggregation
class Department:
    def __init__(self, employee):
        self.employee = employee

class EmployeeAggregation:
    def __init__(self, name):
        self.name = name


# 15. MRO and Diamond Inheritance
class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return "B"

class C(A):
    def show(self):
        return "C"

class D(B, C):
    pass


# 16. Function Decorators
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    return "Hello!"


# 17. Class Decorators
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class PersonDecorated:
    pass


# 18. Property Decorators
class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price


# 19. callable() and __call__()
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor


# 20. Custom Exception
class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    return "Age is valid."


# 21. Custom Iterable
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value









