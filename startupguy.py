from main import *
import customtkinter
from tkinter import messagebox
from dateutil.relativedelta import relativedelta
import datetime
from datetime import date

ip = Repository()


def startup_log(login,per):

    def new_sturtap1():
        def register_button(name_startup, planned_cost, percent):
            if ip.checking_name_startaps(name_startup.get()):
                messagebox.showerror('Ошибка', 'Стартап с таким именем уже существует. Пожалуйста придумайте другой')
            else:

                try:
                    ip.insert_into_startups(name_startup.get(), login, int(planned_cost.get()), int(percent.get()))
                    messagebox.showerror('Успех', 'Стартап создан успешно. Пожалуйста обновите страницу')
                    data_1 = date(2025, 1, 1)
                    date_const = date(2022, 2, 1)
                    while data_1 != date_const:
                        ip.insert_into_data(date_const, name_startup.get(), 0)
                        date_const += relativedelta(months=1)
                        frame6.grid_forget()
                except ValueError:
                    messagebox.showerror('Ошибка', 'Необходимо ввести числовое значение')


        def delete_new_sturtap1():
            frame6.grid_forget()
        frame6 = customtkinter.CTkFrame(investor_window, fg_color='#1f7850', corner_radius=10)
        frame6.grid(row=1, column=1)

        name_startup = customtkinter.CTkEntry(master=frame6,
                                            placeholder_text="Название",
                                            width=120,
                                            height=25,
                                            border_width=2,
                                            corner_radius=10, )
        name_startup.grid(row=1, column=0, padx=5, pady=10)
        planned_cost = customtkinter.CTkEntry(master=frame6,
                                           placeholder_text="Планируемая стоймость",
                                           width=120,
                                           height=25,
                                           border_width=2,
                                           corner_radius=10, )
        planned_cost.grid(row=2, column=0, padx=5, pady=10)

        percent = customtkinter.CTkEntry(master=frame6,
                                       placeholder_text="Процент",
                                       width=120,
                                       height=25,
                                       border_width=2,
                                       corner_radius=10, )
        percent.grid(row=3, column=0, padx=5, pady=10)

        button2 = customtkinter.CTkButton(master=frame6, text='Создать', cursor='hand2',
                                          command=lambda name_startup=name_startup: register_button(name_startup, planned_cost, percent))
        button2.grid(row=4, column=0, pady=10)
        button8 = customtkinter.CTkButton(master=frame6, text='Отмена', cursor='hand2',
                                          command=delete_new_sturtap1)
        button8.grid(row=5, column=0, pady=10)
    def month_stat(name):
        def delete_month_stat():
            frame5.grid_forget()
        list = ip.startaper_income(name)
        frame5 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame5.grid(row=1, column=2)
        lbl = customtkinter.CTkLabel(master=frame5, text = 'Дата')
        lbl.grid(row=0, column=0, padx=15)
        lbl2 = customtkinter.CTkLabel(master=frame5, text='Доход стартапа')
        lbl2.grid(row=0, column=1, padx=15)
        lbl3 = customtkinter.CTkLabel(master=frame5, text='Мой доход по стартапу')
        lbl3.grid(row=0, column=2, padx=15)
        today = datetime.date.today()
        today4 = datetime.date.today()
        today4 -= relativedelta(months=12)

        today4 = str(today4)[:-3] + '-01'
        today4 = datetime.datetime.strptime(today4, "%Y-%m-%d").date()

        delta = relativedelta(today, today4)
        res_months = delta.months + (delta.years * 12) + 1
        for i in range(res_months):
            start = customtkinter.CTkLabel(master=frame5, text=f'{list[i][0]}')
            start.grid(row=i+1, column=0, padx=15)
            start2 = customtkinter.CTkLabel(master=frame5, text=f'{list[i][1]}')
            start2.grid(row=i + 1, column=1, padx=15)
            start3 = customtkinter.CTkLabel(master=frame5, text=f'{list[i][2]}')
            start3.grid(row=i + 1, column=2, padx=15)
        start3 = customtkinter.CTkLabel(master=frame5, text=f'Мой суммарный доход по стартапу: {ip.sum_startaper_income(name)[0]}')
        start3.grid(row=res_months + 1, column=2, padx=15)
        button4 = customtkinter.CTkButton(master=frame5, text='Закрыть', cursor='hand2', width=10,
                                          height=10,
                                          command=delete_month_stat)
        button4.grid(row=res_months + 1, column=0, pady=15, padx=15)


    def more_info(name):
        def delete_more_info():
            frame4.grid_forget()
        frame4 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame4.grid(row=1, column=1)
        today = datetime.date.today()
        data = str(today)[:-3] + '-01'
        info = ip.my_startups_no_invest(name, data)
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
        if info[6] == None:
            label8 = customtkinter.CTkLabel(master=frame4, text=f'Текущая стоимость - Нет инвесторов')
        else:
            label8 = customtkinter.CTkLabel(master=frame4, text=f'Текущая стоимость - {info[6]}')
        label8.grid(row=6, column=0, padx=10, pady=10)
        button4 = customtkinter.CTkButton(master=frame4, text='Статистика по месяцам', cursor='hand2', width=10,
                                          height=10,
                                          command=lambda name=name: month_stat(name))
        button4.grid(row=7, column=0, pady=15, padx=20)
        button5= customtkinter.CTkButton(master=frame4, text='Закрыть', cursor='hand2', width=10,
                                          height=10,
                                          command=delete_more_info)
        button5.grid(row=8, column=0, pady=15, padx=20)



    def update_info(name_startup):
        def update_button(name_startup, monthly_income):
            today = datetime.date.today()
            data = str(today)[:-3] + '-01'
            try:
                ip.update_data(int(monthly_income.get()), data, name_startup)
                messagebox.showerror('Успех', 'Операция совершина')
                frame8.grid_forget()
            except ValueError:
                messagebox.showerror('Ошибка', 'Необходимо ввести числовое значение')

        def delete_update_info():
            frame8.grid_forget()
        frame8 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame8.grid(row=1, column=1)
        label1 = customtkinter.CTkLabel(master=frame8, text=f'Обновите информацию о доходе данного стартапа за текущий месяц')
        label1.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        monthly_income = customtkinter.CTkEntry(master=frame8,
                                              placeholder_text="Доход за месяц",
                                              width=120,
                                              height=25,
                                              border_width=2,
                                              corner_radius=10, )
        monthly_income.grid(row=1, column=0, padx=5, pady=10)
        button2 = customtkinter.CTkButton(master=frame8, text='Подтвердить', cursor='hand2',
                                          command=lambda name_startup=name_startup: update_button(name_startup, monthly_income))
        button2.grid(row=2, column=0, pady=10)
        button7 = customtkinter.CTkButton(master=frame8, text='Отмена', cursor='hand2',
                                          command=delete_update_info)
        button7.grid(row=2, column=1, pady=10)
    def logout():
        investor_window.destroy()
        import signin

    def portfolio():
        per1 = 1
        investor_window.destroy()
        startup_log(login, per1)

    def startups_button():
        per2 = 2
        investor_window.destroy()
        startup_log(login, per2)


    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    investor_window = customtkinter.CTk()
    width = investor_window.winfo_screenwidth()
    height = investor_window.winfo_screenheight()
    investor_window.geometry("%dx%d-9+0" % (width, height))
    investor_window.title('Investor page')

    frame1 = customtkinter.CTkFrame(investor_window, fg_color='#1f7850', corner_radius=10)
    frame1.grid(row=0, column=0, padx=30, pady=30, columnspan=2, rowspan = 2, sticky='nw')

    if per == 1:
        frame3 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame3.grid(row=1, column=0, padx=30, sticky='w')
        if ip.count_name_startup(login)[0] == 0:
            no_startups = customtkinter.CTkLabel(master=frame3, text='Всего заработано: 0. У вас еще нет стартапов')
            no_startups.grid(row=0, column=0, padx=15, pady=15)
        else:
            lbl = customtkinter.CTkLabel(master=frame3, text='Дата')
            lbl.grid(row=1, column=0, padx=15)
            lbl2 = customtkinter.CTkLabel(master=frame3, text='Весь доход за месяц')
            lbl2.grid(row=1, column=1, padx=15)
            today = datetime.date.today()
            today5 = datetime.date.today()
            today5 -= relativedelta(months=12)

            today5 = str(today5)[:-3] + '-01'
            today5 = datetime.datetime.strptime(today5, "%Y-%m-%d").date()

            delta = relativedelta(today, today5)
            res_months = delta.months + (delta.years * 12) + 1
            my_sum = 0
            for i in range(res_months):
                start1 = customtkinter.CTkLabel(master=frame3, text=f'{today5}')
                start1.grid(row=i + 2, column=0, padx=15)
                today5 += relativedelta(months=1)
            arr = [0] * res_months
            for i in range(ip.count_name_startup(login)[0]):
                m = 0
                name = ip.name_startup_nick(login)[i][0]
                for j in range(res_months):
                    if ip.startaper_income(name)[j][2] != None:
                        arr[m] += ip.startaper_income(name)[j][2]
                    m += 1
                if ip.sum_startaper_income(name)[0] != None:
                    my_sum += ip.sum_startaper_income(name)[0]
            startups = customtkinter.CTkLabel(master=frame3, text=f'Всего заработано: {my_sum} ')
            startups.grid(row=0, column=0, padx=15)
            for i in range(len(arr)):
                start2 = customtkinter.CTkLabel(master=frame3, text=f'{arr[i]}')
                start2.grid(row=i + 2, column=1, padx=15)

    if per == 2:
        frame3 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame3.grid(row=1, column=0, padx=30, sticky='w')
        if ip.count_name_startup(login)[0] == 0:
            no_startups = customtkinter.CTkLabel(master=frame3, text='У вас еще нет стартапов')
            no_startups.grid(row=0, column=0, padx=30, pady=30)
        else:
            for i in range(ip.count_name_startup(login)[0]):
                name = ip.name_startup_nick(login)[i][0]
                startup = customtkinter.CTkLabel(master=frame3, text=f'{i + 1} Стартап - {name}')
                startup.grid(row=i, column=0, padx=30)
                button = customtkinter.CTkButton(master=frame3, text='...', cursor='hand2', width=10, height=10,
                                                 command=lambda name=name: more_info(name))
                button.grid(row=i, column=1, padx=10)
                button2 = customtkinter.CTkButton(master=frame3, text='Обновить', cursor='hand2', width=10, height=10,
                                                 command=lambda name=name: update_info(name))
                button2.grid(row=i, column=2, padx=10)
        button5 = customtkinter.CTkButton(master=frame3, text='Создать', cursor='hand2', width=10,
                                              height=10,
                                              command=new_sturtap1)
        button5.grid(row=ip.count_name_startup(login)[0]+1, column=1, padx=10)


    button1 = customtkinter.CTkButton(master=frame1, text='Портфель', cursor='hand2', command=portfolio)
    button1.grid(row=0, column=0, pady=15, padx=20)

    button2 = customtkinter.CTkButton(master=frame1, text='Мои стартапы', cursor='hand2', command=startups_button)
    button2.grid(row=0, column=1, pady=15, padx=20)

    frame2 = customtkinter.CTkFrame(investor_window, fg_color='#1f7850', corner_radius=10)
    frame2.grid(row=0, column=2, padx=30, pady=30,  sticky='e')

    def refresh():
        investor_window.destroy()
        startup_log(login, 0)

    button30 = customtkinter.CTkButton(master=frame2, text='Обновить страницу', cursor='hand2', command=refresh)
    button30.grid(row=0, column=1, pady=10, padx=10)

    logout = customtkinter.CTkButton(master=frame2, text="Выйти из аккаунта ", font=('Century Gothic', 15),
                                     cursor='hand2', command=logout)
    logout.grid(row=0, column=0, padx=10, pady=10)

    today = date.today()
    label2 = customtkinter.CTkLabel(master=frame2, text='Сегодняшняя дата')
    label2.grid(row=1, column=0, padx=10, pady=10)
    label = customtkinter.CTkLabel(master=frame2, text=str(today))
    label.grid(row=1, column=1, padx=10, pady=10)

    investor_window.columnconfigure(2, weight=1)
    investor_window.rowconfigure(1, weight=1)

    investor_window.mainloop()

