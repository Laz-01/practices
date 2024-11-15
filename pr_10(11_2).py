# 11 вариант 2 задание
with open("Лазаренко М.В._УБ-41_vvod(2).txt", 'r') as file_vvod:
        number = int(file_vvod.readline())
        list = []
        for i in range(number):
            row = [int(x) for x in file_vvod.readline().split()]
            list.append(row)
file_vivod=open("Лазаренко М.В._УБ-41_vivod(2).txt","a")
e=[]
for i in range(len(list[0])):
    number=0
    pr=1
    for j in range(len(list)):
       if -10<=list[j][i]<=10:
            pr=pr*list[j][i]
            number+=1
    if number==len(list):
       e.append([i,pr])        
if len(e)!=0:
    mn=1000000000
    num_column=0
    for w in range(len(e)):
        if e[w][1]<mn:
            mn=e[w][1]
            num_column=w
    file_vivod.write(f"Минимальное произведение всех элементов столбца, который по модулю не больше 10, равно {mn}")
    if num_column!=(len(list[0])-1):
        for x in range(len(list)-1):
            list[x][num_column],list[x][num_column+1]=list[x][num_column+1],list[x][num_column]
    else:
        for o in range(len(list)-1):
            list[o][num_column],list[o][num_column-1]=list[o][num_column+1],list[o][num_column]
    file_vivod.write(f"\nПолучившиеся матрица: {list}")
else:
    file_vivod.write("Столбцов с элементами, которые по модулю не больше 10, не существует в этой матрице")