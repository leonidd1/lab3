from main import *
import customtkinter
from datetime import date

ip = Repository()

# global frame3
# global frame4
# global frame5


def investor_log(login):
    def logout():
        investor_window.destroy()

    def portfolio():
        # frame3.grid_forget()
        frame3 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame3.grid(row=0, column=0, padx=30, pady=30, sticky='nw')


    def startups_button():
        print(2)

    def all_startups():
        print(2)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    investor_window = customtkinter.CTk()  # создание окна
    investor_window.geometry('850x600+450+100')
    investor_window.title('Investor page')

    frame1 = customtkinter.CTkFrame(investor_window, fg_color='#1f7850', corner_radius=10)
    frame1.grid(row=0, column=0, padx=30, pady=30, sticky='nw')

    button1 = customtkinter.CTkButton(master=frame1, text='Портфель', cursor='hand2', command=portfolio)
    button1.grid(row=0, column=0, pady=15, padx=20)

    button2 = customtkinter.CTkButton(master=frame1, text='Мои стартапы', cursor='hand2', command=startups_button)
    button2.grid(row=0, column=1, pady=15, padx=20)

    button3 = customtkinter.CTkButton(master=frame1, text='Все стартапы', cursor='hand2', command=all_startups)
    button3.grid(row=0, column=2, pady=15, padx=20)

    frame2 = customtkinter.CTkFrame(investor_window, fg_color='#1f7850', corner_radius=10)
    frame2.grid(row=0, column=1, padx=30, pady=30, sticky='ne')

    logout = customtkinter.CTkButton(master=frame2, text="Выйти из аккаунта ", font=('Century Gothic', 15),
                                     cursor='hand2', command=logout)
    logout.grid(row=0, column=0, padx=10, pady=10)

    today = date.today()
    month1 = today.strftime('%m')
    label = customtkinter.CTkLabel(master=frame2, text=str(today))
    label.grid(row=1, column=0, padx=10, pady=10)

    frame3 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
    frame3.grid(row=0, column=0, padx=30, pady=30, sticky='nw')
    # frame3.grid_forget()

    investor_window.columnconfigure(0, weight=1)
    investor_window.rowconfigure(0, weight=1)

    frame1.rowconfigure(0, weight=1)
    frame1.columnconfigure(0, weight=1)

    investor_window.mainloop()


investor_log('test')
