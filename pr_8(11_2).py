# 11 вариант 2 задание
from random import*
list_1=int(input("Введете число строк для матрицы: "))
list_2=int(input("Введите колическтво элементо в строке матрицы: "))
list=[[randint (-12,12) for i in range(list_2)] for j in range(list_1)]
print("Полученная матрича",list)
my_list=[]
for i in range(list_2):
    number=0
    product=1
    for j in range(list_1):
        if -10<=list[j][i]<=10:
            product=product*list[j][i]
            number+=1
    if number==list_1:
        my_list.append([i,product])      
print("номер столбца,в котором все числа по модулю не больше 10, и его произведение",my_list)  
if len(my_list)!=0:
    mn=1000000000
    num_column=0
    for w in range(len(my_list)):
        if my_list[w][1]<mn:
            mn=my_list[w][1]
            num_column=w
    print("Минимальное произведение всех элементов столбца, который по модулю не больше 10, равно ",mn)
    if num_column!=(list_2-1):
        for x in range(list_1-1):
            list[x][num_column],list[x][num_column+1]=list[x][num_column+1],list[x][num_column]
    else:
        for o in range(list_1-1):
            list[o][num_column],list[o][num_column-1]=list[o][num_column+1],list[o][num_column]
    print("Получившиеся матрица",list)

else:
    print("Столбцов с элементами, которые по модулю не больше 10, не существует в этой матрице")