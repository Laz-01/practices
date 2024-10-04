# 11 вариант 1 задание
def F(n):
    list=[]
    for i in range(n,2*n+1):
        for j in range(i, 2*n+1):
            if i-j==-2:
                list.append([i,j])
    return list
    
            
a=int(input("Введите число n, которое больше двух : "))
if a>2:
    print(F(a))
else:
    print("Попробуйте занова")