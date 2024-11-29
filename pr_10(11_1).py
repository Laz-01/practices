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

with open("Лазаренко М.В._УБ-41_vvod(1).txt", 'r') as file_vvod:
        number = int(file_vvod.readline())
        list = []
        for i in range(number):
            row = [int(x) for x in file_vvod.readline().split()]
            list.append(row)
    
with open("Лазаренко М.В._УБ-41_vivod(1).txt","w") as file_vivod:
     file_vivod.write(f"Сумма элементов строки, в которой расположен элемент с наименьшим значением, равна {F(list)}")
     file_vivod.close() 
