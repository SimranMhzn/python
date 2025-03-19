#conditions and loops
"""if True:
  print("The condition is true.")
else:
  print("The condition is false.")

condition=True
if(condition):
  print("Condition is true.")
else:
  print("Condition is false.")

#WAP to check if user is above 18
age1=19
age2=17
if age1>18:
  print("He/She is above 18.")
elif age1 ==18: 
  print("He/She is 18.")
elif age1 <=18: 
  print("Cannot count.")
else: 
  print("He/She is below 18.")"


#switch python v10 bhanda muni ko ma chaldaina
num = int(input("Enter a number: "))

def choice(ab):
  match(num):
    case 1:
      print("The number was 1.")
    case 2:
      print("The number was 2.")"

#QUESTIONS   
#wap to check if the given character is vowel or not
char=input("Enter any character: ")
if char in ('a', 'e', 'i', 'o', 'u'):
    print("The character is a vowel.")
else:
    print("The character is not a vowel.")

#even or odd
num = int(input("Enter a number: "))
if num%2==0:
  print("The number is even.")
else:
  print("The number is odd.")

#what day is today using match
print("The list of days in week are: \n 1.Sunday \n 2.Monday \n 3.Tuesday \n 4.Wednesday \n 5.Thurssday \n 6.Friday \n 7.Saturday")
num = int(input("What day is today?"))
match(num):
   case 1:
      print("Today is Sunday")
   case 2:
      print("Today is Monday")
   case 3:
      print("Today is Tuesday")
   case 4:
      print("Today is Wednesday")
   case 5:
      print("Today is Thursday")
   case 6:
      print("Today is Friday")
   case 7:
      print("Today is Saturday")

#leap year or not
# divisible by 4 and not divisible by 100, or it is also divisible by 400
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#prime or not
num = int(input("Enter a number: "))
count=0
for i in range(2, num): 
  if num % i == 0:
    count+=1
if count>1:
  print("It is not a prime number.")
else:
  print("It is a prime number.")

#what month is today
print("The list of months are: \n 1.January \n 2.February \n 3.March \n 4.April \n 5.May \n 6.June \n 7.July \n 8.August \n 9.September \n 10.October \n 11.November \n 12.December")
month = int(input("What is the month now?"))
match(month):
   case 1:
      print("Today is January")
   case 2:
      print("Today is February")
   case 3:
      print("Today is March")
   case 4:
      print("Today is April")
   case 5:
      print("Today is May")
   case 6:
      print("Today is June")
   case 7:
      print("Today is July")
   case 8:
      print("Today is August")
   case 9:
      print("Today is September")
   case 10:
      print("Today is October")
   case 11:
      print("Today is November")
   case 12:
      print("Today is December")

#positive or negatiive
num=int(input("Enter a number: "))
if num>0:
   print(f"{num} is positive.")
elif num<0:
   print(f"{num} is negative.")
else:
   print(f"{num} is equals to 0 so it is neither positive or negative.")"

#CODE
#for loop
for i in range(0,11,2):
  if(i%2==0):
    print(i)

#while loop
ab=0
while(ab<=10):
  print(ab)
  ab+=1


#breaking statement -> break,continue,pass
print("break example")
for i in range(0,11):
  print(i)
  if i==5:
    break

print("continue example")
for i in range(0,11):
  if i==5:
    continue
  print(i)

print("pass example")
for i in range(0,11):
  pass

print("hello pass")

#QUESTIONS
#wap to print the numbers from 1 to 10
for i in range(1,11):
  print(i)
  i+=1

#all even number between 2 value a and b
num1=int(input("Enter number one: "))
num2=int(input("Enter number two: "))
print("The even numbers are ")
for i in range(num1,num2):
  if i%2==0:
    print(f"{i}")

#all odd number between 2 value a and b
num1=int(input("Enter number one: "))
num2=int(input("Enter number two: "))
print("The odd numbers are: ")
for i in range(num1,num2):
  if i%2!=0:
    print(f"{i}")
    
#print all value betn 0 to 100 but not 50
for i in range(0,100):
  if i==50:
    continue
  else:
    print(i)

#mul table of 5
for i in range (1,11):
  mul=5*i
  print(f"{mul}")

#mul table of 0 to 10 using nested loop
for  i  in range (0,10):
  print(f"Table of {i}")
  for j in range (1,11):
    mul=i*j
    print(f"{mul}")

#sum of all no between 1 to 100
sum=0
for i in range (1,100):
  sum+=i
  i+=1

print(sum)
"""
#wap if the number is light or fire or water is num divisible by 2=light, 3=water, 5=fire
num=int(input("Enter a number: "))
while(num%2>0):
  num=num/2;
  print("The number is light.")
  break;
while(num%3==0):
  print("The number is water.")
  break;
while(num%5==0):
  print("The number is fire.")
  break;


