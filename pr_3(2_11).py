#2 задание вариант 11
y=int(input("Введите число y "))
x=int(input("Введите число x "))
if y<2 and x==4:
    q=x+x*y
elif x<y:
    q=y**2+1
else:
    q=y**2+4

print(q)