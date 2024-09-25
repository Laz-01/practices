#10
N=int(input("Количество чисел из ряда Фибоначчи: "))
K=int(input("Порядковый номер в ряду,с которого нужно начать суммировать: "))
num_elements=2
a=0
b=1
sym=0
print(0,1)
if K==1 or K==2:
    sym=1
for i in range(N-2):
    a,b=b,a+b
    num_elements+=1
    if num_elements>=K:
        sym=sym+b

print(f"Сумма элементов c {K} элемента последовательности равна {sym}")
    

