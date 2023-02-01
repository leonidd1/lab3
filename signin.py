import tkinter
from main import *
from tkinter import messagebox
import customtkinter
from investor import investor_log
# from PIL import ImageTk, Image

ip = Repository()


def login_button():
    if login.get() == '' or password.get() == '':
        messagebox.showerror('Ошибка', 'Не все поля заполнены')
    elif ip.user_verification(login.get(), password.get()):
        if combobox.get() == 'Инвестор':
            signin_window.withdraw()
            investor_log(login.get())
        if combobox.get() == 'Стартапер':
            signin_window.withdraw()
            import startupguy
    else:
        messagebox.showerror('Ошибка', 'Неверный логин или пароль')


def register_page():
    signin_window.withdraw()
    import signup


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

signin_window = customtkinter.CTk()  # создание окна
signin_window.geometry('450x400+700+200')
signin_window.title('Login page')


frame1 = customtkinter.CTkFrame(signin_window, fg_color='#1f7850', corner_radius=10)
frame1.grid(row=0, column=0, padx=20, pady=20)
# frame1.geometry()

l1 = customtkinter.CTkLabel(master=frame1, text="Войдите в свой аккаунт как ", font=('Century Gothic', 15))
l1.grid(row=0, column=0, padx=10)

optionmenu_var = customtkinter.StringVar(value="Стартапер")  # set initial value
combobox = customtkinter.CTkOptionMenu(master=frame1,
                                       values=["Стартапер", "Инвестор"],
                                       variable=optionmenu_var)
combobox.grid(row=0, column=1, columnspan=2, padx=5, pady=10, sticky="nsew")
login = customtkinter.CTkEntry(master=frame1,
                               placeholder_text="Логин",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10, )
login.grid(row=1, column=0)

password = customtkinter.CTkEntry(master=frame1,
                                  placeholder_text="Пароль",
                                  width=120,
                                  height=25,
                                  border_width=2,
                                  corner_radius=10, )
password.grid(row=2, column=0, pady=10)

button1 = customtkinter.CTkButton(master=frame1, text='Войти', cursor='hand2', command=login_button)
button1.grid(row=3, column=0, pady=10)

button2 = customtkinter.CTkButton(master=frame1, text='Зарегистрироваться', cursor='hand2', command=register_page)
button2.grid(row=3, column=1, pady=10)

signin_window.columnconfigure(0, weight=1)
signin_window.rowconfigure(0, weight=1)

frame1.rowconfigure(0, weight=1)
frame1.columnconfigure(0, weight=1)

signin_window.mainloop()
