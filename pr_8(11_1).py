# 11 вариант 1 задание
from random import*
def F(x):
    min_matrix=100
    num_line=0
    for i in range(len(x)):
        line=x[i]
        min_line=100
        for j in range(len(line)):
            if x[i][j]<min_line:
                min_line=x[i][j]
        if min_line<min_matrix:
            min_matrix=min_line
            num_line=i
    sym=0
    for k in range(len(x[num_line])):
        sym=sym+x[num_line][k]
    return sym

num=int(input("Введите число строк для квадратной матрице: "))
matrix=[[randint (1,50) for i in range (num)] for j in range(num)]
print(matrix)
print(F(matrix))