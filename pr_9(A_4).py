#Блок А задание 4
def amount(num):
    sym=0
    if num>9:
        sym=num%10+amount(num//10)
    else:
        sym=sym+num
    return sym


N=int(input("Введите число: "))
print(f"Сумма цифр числа {N} равна {amount(N)}")