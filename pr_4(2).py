#10
N=int(input("Количество чисел из ряда Фибоначчи: "))
K=int(input("Порядковый номер в ряду,с которого нужно начать суммировать: "))
s=[0,1]
sym=0
if K==1 or K==2:
    sym=1
for i in range(N-2):
    a=s[i]+s[i+1]
    s.append(a)
    if len(s)>=K:
        sym=sym+s[len(s)-1]
print(s)
print(sym)
    

