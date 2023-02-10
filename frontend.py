import tkinter as tk
from tkinter import *

from config import host, user, password, db_name, port
from architecture import *
from main import *


ip = Repository()
def clicked():
    res1 = txt1.get()
    # res2 = txt2.get()
    print(type(ip.test2(res1)))
    list = ip.test2(res1)
    if not ip.test2(res1):
        print(ip.test2(res1))
        print('Список пустой шо')
    else:
        print(list[1])
        print(list[1][1])
        print('Список не пустой :)')
    for i in list:
        for j in i:
            print(j)

    # if ip.test(res1) != None:
    #     print('Такой никнейм уже занят попробуйте другой')
    # else:
    #     print('Продолжайте регистрацию')

    # tuple = ip.test(res1)
    # for i in tuple:
    #     print(i)
    # print(tuple[1])

    # if ip.checking_uniqueness(res1):
    #     tuple = ip.checking_uniqueness(res1)
    #     print('Такой никнейм уже занят попробуйте другой')
    #     print(tuple[0])
    # else:
    #     print('Продолжайте регистрацию')

window = tk.Tk()
window.columnconfigure(1,weight=1, minsize=50)
window.rowconfigure(1,weight=1, minsize=50)
frm = tk.Frame()

lbl = Label(master = frm, text="Имя: ")
lbl.grid(column=0, row=0)


txt1 = Entry(window,width=10)
txt1.grid(column=1, row=0)

# lbl = Label(master = frm, text="Ник нейм: ")
# lbl.grid(column=0, row=1)
#
# txt2 = Entry(window,width=10)
# txt2.grid(column=1, row=1)

btn = Button(master = frm, text="Продолжить", command=clicked)
btn.grid(column=0, row=2)

frm.grid()


window.mainloop()
