#rust
from tkinter import*
from tkinter import messagebox
from zipfile import ZipFile
import requests
import json

def clicked():
    try:
        repo = txt.get()
        url = f"https://api.github.com/users/{repo}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        company=data.get('company',None)
        created_at = data.get('created_at',None)
        email=data.get('email',None)
        id=data.get('id',None)
        name = data.get('name',None)
        meaning_url=data.get('url',None)

        info={'company': company,
              'created_at': created_at,
              'email': email,'id': id,
              'name': name,
              'meaning_url': meaning_url}
   
        with open("Information.json","w") as file:
              json.dump(info,file,indent=4)
              file.close()

        messagebox.showinfo("Результат"," В фаил 'Information.json' были сохранены извлечённые данные")

    except requests.exceptions.RequestException:
        messagebox.showerror("Ошибка","Ошибка при отправке HTTP-запроса")
    except json.JSONDecodeError:
        messagebox.showerror("Ошибка","Ошибка при работе с JSON")

         

window=Tk()
window.title("Извлечение данных из репозитория")
window.geometry("400x250")
text=Label(window,text="Введите название репозитория")
text.pack(pady=5)
txt=Entry(window,width=10)
txt.pack(pady=5)
btn=Button(window,text="Получить информацию",command=clicked)
btn.pack(pady=5)

window.mainloop()