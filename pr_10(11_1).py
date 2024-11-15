# 11 вариант 1 задание
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
with open("Лазаренко М.В._УБ-41_vvod(1).txt", 'r') as file_vvod:
        number = int(file_vvod.readline())
        list = []
        for i in range(number):
            row = [int(x) for x in file_vvod.readline().split()]
            list.append(row)
    
with open("Лазаренко М.В._УБ-41_vivod(1).txt","w") as file_vivod:
     file_vivod.write(f"Сумма элементов строки, в которой расположен элемент с наименьшим значением, равна {F(list)}")
     file_vivod.close() 
