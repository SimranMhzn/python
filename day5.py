#oop in python
#it is a programming paradism (real lide example lai class & obj ma convert garne)
#properties, class, object, methods, self-> this, 4 pillars(enc, inherit, poly, abs)
#dunder methods, class meta, abstract classes

#class-> it is a blueprint
#colony->
#house number

#object-> instance of class
"""
class colony:
  #properties->variable, fields 
  rooms= 50
  name="Naxal"

house=colony()
print(f'The total number of rooms available are {house.rooms}.')
print(f"The name of colony is {house.name}.")

house2=colony()
house2.rooms=70
print(f'The total number of rooms available are {house2.rooms}.')
print(f"The name of colony is {house2.name}.")

class kist:
  add="Kamalpokhari"
  name="Simran"
  age=20
  course="BIT"
obj=kist()
print(f"Kist is in {obj.add}.")
print(f"The name of student is {obj.name}.")
print(f"The age of student is {obj.age}.")
print(f"The course taken is {obj.course}.")

#using constructor (self compulsorily lekhna parcha)
class kist:
  def __init__(self,batch,name):
    self.name=name
    self.batch=batch
    print(f"{name,batch}")
obj=kist("2025","Simran")

#constructor-> calls itself when object is created
#self -> this ->
class kist:
  def __init__(self):
    print("Called itself")
  def abc(self):
    print("hello from the method")
obj=kist()
obj.abc()

class add:
  def __init__(self,a,b):
    self.a=a
    self.b=b
  def addNum(self,c):
    print(self.a+self.b+c)
obj=add(10,25)
obj.addNum(10)

#wap in oop about the class  name Students with the following options
#need to make a constructor with the value of name, age, gender, and batch
#need to make 3 methods which will add two number a,b
#print name and age and last one print  gender and batch
class Students:
  def __init__(self,name,age,gender,batch):
    self.name=name
    self.age=age
    self.gender=gender
    self.batch=batch
  def add(self,a,b):
    print(a+b)
  def printNameAge(self):
    print(self.name,self.age)
  def printGenderBatch(self):
    print(self.gender,self.batch)
obj=Students("Simran",20,"Female",2022)
obj.add(10,20)
obj.printNameAge()
obj.printGenderBatch()

#static class and static method (object banairakhnu pardaina)
class One:
  @staticmethod
  def abc(a,b):
    return a+b
print(One.abc(20,10))

class mul:
  @staticmethod
  def abc(a,b):
    return a*b
print(mul.abc(10,20))

#compare two number usinng static method
class Compare:
  @staticmethod
  def compare(a,b):
    if a>b:
      return f"{a} is greater than {b}."
    else:
      return f"{b} is greater than {a}."
print(Compare.compare(10,2))

class Two:
  a=20
  b=30
  @classmethod
  def cde(cls,bc):
    cls.b=bc
    print(cls.b+bc)
Two.cde(30)
"""
class Age:
  @staticmethod

  def age(agE):
    if agE>18:
      print("Can drive")
    else:
      print("Can't drive")
Age.age(20)
Age.age(15)

#dundar method, 4 pillars