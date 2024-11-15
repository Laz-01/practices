#Блок В задание 3
def function():
    a=int(input("Введите число: "))
    number=1
    while a!=0:
        if number%2==1:
            print(a)
        a=int(input("Введите число: "))
        number+=1
function()
