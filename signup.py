import tkinter
from main import *
from tkinter import messagebox
import customtkinter
from config import host, user, password, db_name

# from PIL import ImageTk, Image

ip = Repository()


def clear_login():
    login.delete(0, len(login.get()) + 1)


def login_page():
    signup_window.destroy()
    import signin


def register_button():
    if login.get() == '' or password.get() == '':
        messagebox.showerror('Ошибка', 'Не все поля заполнены')
    elif ip.checking_uniqueness(login.get()):
        messagebox.showerror('Ошибка', 'Такой логин уже существует')
        clear_login()
    else:
        ip.insert_into_users(login.get(), first_name.get(), last_name.get(), password.get())
        messagebox.showinfo('Успех', 'Регистрация прошла успешно')
        signup_window.withdraw()
        import signin


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

signup_window = customtkinter.CTk()  # создание окна
signup_window.geometry('450x400+700+200')
signup_window.title('Register page')

frame1 = customtkinter.CTkFrame(signup_window, fg_color='#1f7850', corner_radius=10)
frame1.grid(row=0, column=0, padx=20, pady=20)

l1 = customtkinter.CTkLabel(master=frame1, text="Регистрация в системе  ", font=('Century Gothic', 15))
l1.grid(row=0, column=0, sticky='e', padx=20, pady=10)

first_name = customtkinter.CTkEntry(master=frame1,
                                    placeholder_text="Имя",
                                    width=120,
                                    height=25,
                                    border_width=2,
                                    corner_radius=10, )
first_name.grid(row=1, column=0, padx=5, pady=10)
last_name = customtkinter.CTkEntry(master=frame1,
                                   placeholder_text="Фамилия",
                                   width=120,
                                   height=25,
                                   border_width=2,
                                   corner_radius=10, )
last_name.grid(row=2, column=0, padx=5, pady=10)

login = customtkinter.CTkEntry(master=frame1,
                               placeholder_text="Логин",
                               width=120,
                               height=25,
                               border_width=2,
                               corner_radius=10, )
login.grid(row=3, column=0, padx=5, pady=10)

password = customtkinter.CTkEntry(master=frame1,
                                  placeholder_text="Пароль",
                                  width=120,
                                  height=25,
                                  border_width=2,
                                  corner_radius=10, )
password.grid(row=4, column=0, padx=5, pady=10)

button2 = customtkinter.CTkButton(master=frame1, text='Зарегистрироваться', cursor='hand2', command=register_button)
button2.grid(row=5, column=0, pady=10)

arleadyaccount = customtkinter.CTkLabel(master=frame1, text='Уже есть аккаунт?')
arleadyaccount.grid(row=6, column=0)

loginButton = customtkinter.CTkButton(master=frame1, text='Войти', command=login_page)
loginButton.grid(row=7, column=0, pady=10)

signup_window.columnconfigure(0, weight=1)
signup_window.rowconfigure(0, weight=1)

frame1.rowconfigure(0, weight=1)
frame1.columnconfigure(0, weight=1)

signup_window.mainloop()
