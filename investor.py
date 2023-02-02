from main import *
import customtkinter
import datetime
from datetime import date

ip = Repository()


def investor_log(login, per):
    def month_stat():
        print(ip.investor_income(name, login))

    def more_info(name):
        frame4 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame4.grid(row=0, column=1, padx=30, pady=30, sticky='w')
        today = datetime.date.today()
        data = str(today)[:-3] + '-01'
        info = ip.my_startups(name, login, data)
        print(info)
        label1 = customtkinter.CTkLabel(master=frame4, text=f'Название - {info[0]}')
        label1.grid(row=0, column=0, padx=10, pady=10)
        label2 = customtkinter.CTkLabel(master=frame4, text=f'Владелец - {info[1]}')
        label2.grid(row=1, column=0, padx=10, pady=10)
        label3 = customtkinter.CTkLabel(master=frame4, text=f'Планируемая стоимость - {info[2]}')
        label3.grid(row=2, column=0, padx=10, pady=10)
        label4 = customtkinter.CTkLabel(master=frame4, text=f'Процент - {info[3]}')
        label4.grid(row=3, column=0, padx=10, pady=10)
        label5 = customtkinter.CTkLabel(master=frame4, text=f'Общая прибыль - {info[4]}')
        label5.grid(row=4, column=0, padx=10, pady=10)
        if info[5] == None:
            label6 = customtkinter.CTkLabel(master=frame4, text=f'Месячная приибыль - Нет данных')
        else:
            label6 = customtkinter.CTkLabel(master=frame4, text=f'Месячная приибыль - {info[5]}')
        label6.grid(row=5, column=0, padx=10, pady=10)
        label7 = customtkinter.CTkLabel(master=frame4, text=f'Моя инвестиция - {info[6]}')
        label7.grid(row=6, column=0, padx=10, pady=10)
        label8 = customtkinter.CTkLabel(master=frame4, text=f'Текущая стоимость - {info[7]}')
        label8.grid(row=7, column=0, padx=10, pady=10)
        button4 = customtkinter.CTkButton(master=frame4, text='Статистика по месяцам', cursor='hand2', width=10,
                                          height=10,
                                          command=month_stat)
        button4.grid(row=8, column=0, pady=15, padx=20)

    def logout():
        investor_window.destroy()
        import signin

    def portfolio():
        per1 = 1
        investor_window.destroy()
        investor_log(login, per1)

    def startups_button():
        per2 = 2
        investor_window.destroy()
        investor_log(login, per2)

    def all_startups():
        per3 = 3
        investor_window.destroy()
        investor_log(login, per3)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    investor_window = customtkinter.CTk()  # создание окна
    investor_window.geometry('850x600+450+100')
    investor_window.title('Investor page')

    frame1 = customtkinter.CTkFrame(investor_window, fg_color='#1f7850', corner_radius=10)
    frame1.grid(row=0, column=0, padx=30, pady=30, sticky='nw')
    if per == 1:
        frame3 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame3.grid(row=0, column=0, padx=30, pady=30, sticky='sw')

    if per == 2:
        frame3 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame3.grid(row=0, column=0, padx=30, pady=30, sticky='w')
        if ip.count_investors(login)[0] == 0:
            no_startups = customtkinter.CTkLabel(master=frame3, text='У вас еще нет стартапов')
            no_startups.grid(row=0, column=0, padx=30, pady=30)
        else:
            for i in range(ip.count_investors(login)[0]):
                name = ip.name_startup(login)[i][0]
                startup = customtkinter.CTkLabel(master=frame3, text=f'{i + 1} Стартап - {name}')
                startup.grid(row=i, column=0, padx=30)
                button = customtkinter.CTkButton(master=frame3, text='...', cursor='hand2', width=10, height=10,
                                                 command=lambda name=name: more_info(name))
                button.grid(row=i, column=1, padx=10)

    if per == 3:
        frame3 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame3.grid(row=0, column=0, padx=30, pady=30, sticky='n')
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
    label = customtkinter.CTkLabel(master=frame2, text=str(today))
    label.grid(row=1, column=0, padx=10, pady=10)

    investor_window.columnconfigure(0, weight=1)
    investor_window.rowconfigure(0, weight=1)

    frame1.rowconfigure(0, weight=1)
    frame1.columnconfigure(0, weight=1)

    investor_window.mainloop()

# investor_log(1, 0)
