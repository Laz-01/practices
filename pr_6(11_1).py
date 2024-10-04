#11 вариант 1 задание
from random import*
list=[randint(0,101) for t in range (10)]
mx=0
for i in range(len(list)):
    if list[i-1]%2==0:
        mx=max(mx,list[i-1])
print(list)
print(mx)

