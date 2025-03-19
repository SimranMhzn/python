"""
#functions -> def  
def printName():
  print("Hello, World!")
printName()
printName()
printName()

def returnName():
  return "Hello, World! from returnName" 
print(returnName())
print(returnName())
print(returnName())

#using pass keyword
def passName():
  pass #pass is used to avoid error when no code is written
print("Hello World below pass")

#parameters in function
def abc(a,b): #parameters
  print(a+b)
abc(10,20) #arguments

#function types
def abcd(a):
  print(a)
print(abcd(1))

#1. print even no. between two numbers
def even(a,b):
  for i in range(a,b):
    if i%2==0:
      print(i)
even(1,10)

#2. print odd no. between two numbers
def odd(a,b):
  for i in range(a,b):
    if(i%2!=0):
      print(i)
odd(1,10)

#function types 
#function with no parameters
def printName():
  print("Hello, World!")  

#function with parameters and no return type
def abc(a): 
  print(a)

#function with return type but no parameter
def returnName():
  return "Hello, World!"
print(returnName())

#function with parameter and also have return type
def abc(a): 
  return(a)
print(abc(10))

#parameter types
#default
#named
# *args
# **kwargs
#positional arguments -> give  value to the arg as you write in parameter
def abc(name,age):
  print(f"name={name} and age={age}")
abc("simran",27) 

#named parameter
def abc(name,age):
  print(f"name={name} and age={age}")
abc(age=27,name="simran") 

#default parameter value
def abc(name,age="20"):
  print(f"name={name} and age={age}")
abc("simran") 
abc("simran",28) 

#args -> truple data format ma kaam garcha
def abc(*name):
  for i in name:
    print(i)
abc("ram","hari") ##multiple arg haru lina ko  lagi param ma * symbol  use garnu parcha

#kwargs
def abc(**name):
  for keys, values in name.items():
    print(keys,values)
abc(name="ram",age="19",address="naxal") 

#revison of functions
def abc():
  print("Hello World")
  return "returning with no parameter"
abc()
def cde(a,b):
    print(a+b)
    return "returning from inside function with parameter"
cde(10,20)

def abcd():
  print("hello")
  return "hi"
  print("heyy") #cant be printed  
print(abcd())

# 3. prime or not
def primeNum(temp):
  count=0
  for i in range(2, temp): 
    if temp % i == 0:
      count+=1
  if count>1:
    print("It is not a prime number.")
  else:
    print("It is a prime number.")
num = int(input("Enter the number: "))
primeNum(num)

#lambda function -> anonymous function
let =lambda x: x+1 #one value given
print(let(3))

let =lambda x,y: x+y #two value given
print(let(3,4))
"""
# 4. mul of 5
def mul(a):
  for i in range(0,11):
    print(f"5 * {i} = {i*5}")
mul(5)