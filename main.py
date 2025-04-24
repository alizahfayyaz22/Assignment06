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
