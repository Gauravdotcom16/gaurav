import moduleee
print(moduleee.add(12,54))
print(moduleee.prod(32,99))
from moduleee import*
print(add(3,5))
import math
print(math.pi)
print(math.inf)
print(-math.inf)
print(math.fabs(-56))
print(math.factorial(5))
print(math.ceil(1.4))#round of to highesh number
print(math.floor(1.4))#round of to lowest number
print(math.fmod(20,3))#gives remaninder
print(math.fsum([1,2,3,3,4,5,5,5,5,5,]))#tuple,lists,range,dict.set
print(math.prod([1,2,8,4]))#multiply the numbers
print(math.pow(10,2))
print(math.sqrt(49))
print(math.trunc(1.4))#removes the number after point
from random import *
for i in range(5):
    print(randint(1,10))
for i in range(2):
    print(random())
for i in range(2):
    print(randrange(10))
for i in range(3):
    print(uniform(5,10))
list=[1,2,3,3,4,4,4,5,5,5,]
for i in range(10):
    print(choice(list),end=" ")
import random
random.shuffle(list)
print("\n",list)