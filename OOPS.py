class employee():
    def __init__(self,name,age,id,salary):
        self.name=name
        self.age=age
        self.salary=salary
        self.id=id
def earn(self):
    pass

class childemployee1(employee):
    def earn(self):#Run-time polymorphism
        print("Hello")

class childemployee2(employee):
    def earn(self):
        print("Hello there")

a=childemployee1
a.earn(employee)
b=childemployee2
b.earn(employee)