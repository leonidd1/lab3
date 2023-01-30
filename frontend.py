from tkinter import *
from architecture import *
# Это я, Илья
print
def clicked():
    res = f"Привет {txt.get()}"
    lbl.configure(text=res)
    window.destroy()
    window2 = Tk()
    window2.title("Добро пожаловать в приложение PythonRu")
    window2.geometry('1920x1080')




window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('1920x1080')
lbl = Label(window, text="Привет", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
txt = Entry(window, width=10)
txt.focus()
txt.grid(column=1, row=0)
btn = Button(window, text="Не нажимать!", command=clicked)
btn.grid(column=2, row=0)


window.mainloop()
