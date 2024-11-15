# 11 вариант 1 задание
from random import*
def F(x):
    mn=100
    g=0
    for i in range(len(x)):
        s=x[i]
        min=100
        for j in range(len(s)):
            if x[i][j]<min:
                min=x[i][j]
        if min<mn:
            mn=min
            g=i
    sym=0
    for k in range(len(x[g])):
        sym=sym+x[g][k]
    return sym

num=int(input("Введите число строк в матрице: "))
matrix=[[randint (1,50) for i in range (num)] for j in range(num)]
print(matrix)
print(F(matrix))