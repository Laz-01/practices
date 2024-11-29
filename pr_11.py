from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.ttk import Combobox
import tkinter as tk

def clicked_menu():
    file=filedialog.askopenfilename(filetypes=(("Text files","*.txt"),("all files","*.*")))
    if file:
        try:
            with open(file, "r", encoding="utf-8") as f:
                text_new = f.read()
                text.delete("1.0", tk.END)
                text.insert(tk.END, text_new)
        except Exception:
            messagebox.showerror("Ошибка","Ошибка при загрузке файла")

def calculator():
    try:
        number_1=float(number1.get())
        number_2=float(number2.get())
        action=combo.get()
        if action=="+":
            result=number_1+number_2
        elif action=="-":
            result=number_1-number_2
        elif action=="*":
            result=number_1*number_2
        else:
            result=number_1/number_2
        text4.config(text=f"Результат: {result}")

    except ZeroDivisionError:
        text4.config(text="Деление на ноль невозможно!")
    except ValueError:
        text4.config(text="Ошибка ввода")
        
def clicked():
    list=[]
    if check_var1.get():
        list.append("Первый")
    if check_var2.get():
        list.append("Второй")
    if check_var3.get():
        list.append("Третий")
    if len(list)!=0:
        messagebox.showinfo("Заголовок","Вы выбрали "+ str(",".join(list))+ " вариант")
    else:
        messagebox.showinfo("Заголовок","Вы ничего не выбрали")

window=Tk()
window.title("Лазаренко Мария Владимировна")
window.geometry("400x250")

menu=Menu(window)
new_item=Menu(menu)
new_item.add_command(label="Загрузить файл",command=clicked_menu)
menu.add_cascade(label="Файл",menu=new_item)
window.config(menu=menu)

tab_control=ttk.Notebook(window)
tab1=ttk.Frame(tab_control)
tab2=ttk.Frame(tab_control)
tab3=ttk.Frame(tab_control)
tab_control.add(tab1,text="Калькулятор")
tab_control.add(tab2,text="Чекбоксы")
tab_control.add(tab3,text="Работа с файлом")
lbl1=Label(tab1,padx=5,pady=5)
lbl1.pack()
lbl2=Label(tab2,padx=25,pady=25)
lbl2.pack()
lbl3=Label(tab3,padx=45,pady=45)
lbl3.pack()
tab_control.pack(expand=1,fill="both")

number1=Entry(lbl1,width=7)
number1.pack(pady=5)
combo=Combobox(lbl1,width=3)
combo['values']=("+","-","*","/")
combo.current(0)
combo.pack(pady=5)
number2=Entry(lbl1,width=7)
number2.pack(pady=5) 
btn1=Button(lbl1,text="Вычислить",command=calculator)
btn1.pack(pady=5)
text4 = Label(lbl1)
text4.pack(pady=5)

selected=IntVar()
check_var1 = BooleanVar()
check_var2 = BooleanVar()
check_var3 = BooleanVar()
check1 = Checkbutton(lbl2, text="Первый", variable=check_var1)
check1.pack(pady=5)
check2 = Checkbutton(lbl2, text="Второй", variable=check_var2)
check2.pack(pady=5)
check3 = Checkbutton(lbl2, text="Третий", variable=check_var3)
check3.pack(pady=5)
btn2=Button(lbl2,text="Выбрать",command=clicked)
btn2.pack(pady=5)

text=Text(lbl3,height=200,width=200,bg="white",fg="blue",wrap=WORD)
text.pack()
window.mainloop()
