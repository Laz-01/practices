#11 вариант 2 задание
from random import*
def maximum(s): 
    max_=0
    for i in range(len(s)):
        t=s[i]
        p=0
        for j in range(len(t)):
            if s[i][j]>=p:
                p=max(p,s[i][j])
        max_=max(max_,p)
    return max_

def measure(s_1,s_2):
    max_s1=maximum(s_1)
    max_s2=maximum(s_2)
    for i in range(len(s_1)):
        e=s_1[i]
        for j in range(len(e)):
            if s_1[i][j]==max_s1:
                s_1[i][j]=max_s2

    for r in range(len(s_2)):
        t=s_2[r]
        for y in range(len(t)):
            if s_2[r][y]==max_s2:
                s_2[r][y]=max_s1
                
    return s_1,s_2

A_1=int(input("Введите количество строк для А матрице: "))
A_2=int(input("Количество переменных в одной строке для матрице А: "))
B_1=int(input("Введите количество строк для В матрице: "))
B_2=int(input("Количество переменных в одной строке для матрице B: "))

A=[[randint(1,20) for i in range(A_2)]for j in range (A_1)]
B=[[randint(1,20) for i in range(B_2)] for j in range(B_1)]

print(f"Матрица А: {A}")
print(f"Матрица В: {B}")
print(f"Максимальный элемент матрицы А равен {maximum(A)}")
print(f"Максимальный элемент матрицы B равен {maximum(B)}")

print(measure(A,B))


