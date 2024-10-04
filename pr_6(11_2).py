# вариант 11 задание 2
from random import*
list_1=[randint (0,21) for i in range (10)]
list_2=[]
for i in range (len(list_1)):
    if list_1[i-1]%2==0 and list_1[i-1]<10:
        list_2.append(list_1[i-1])

if len(list_2)==0:
    print("Таких чисел нету")
else:
    list_2.sort()
    print(list_2)