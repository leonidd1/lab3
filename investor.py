from main import *
import customtkinter
from tkinter import messagebox
from dateutil.relativedelta import relativedelta
import datetime
from datetime import date

ip = Repository()


def investor_log(login, per):
    # ------- от сюда ------
    def more_info(name):
        def delete_more_info():
            frame4.grid_forget()
        def month_stat(name):
            def delete_freme():
                frame5.grid_forget()
            list = ip.investor_income(name, login)
            frame5 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
            frame5.grid(row=1, column=2)
            lbl = customtkinter.CTkLabel(master=frame5, text='Дата')
            lbl.grid(row=0, column=0, padx=15)
            lbl2 = customtkinter.CTkLabel(master=frame5, text='Доход стартапа')
            lbl2.grid(row=0, column=1, padx=15)
            lbl3 = customtkinter.CTkLabel(master=frame5, text='Мой доход по стартапу')
            lbl3.grid(row=0, column=2, padx=15)
            today = datetime.date.today()
            today2 = datetime.date.today()
            today2 -= relativedelta(months=12)

            today2 = str(today2)[:-3] + '-01'
            today2 = datetime.datetime.strptime(today2, "%Y-%m-%d").date()
            delta = relativedelta(today, today2)
            res_months = delta.months + (delta.years * 12) + 1
            for i in range(res_months):
                start = customtkinter.CTkLabel(master=frame5, text=f'{list[i][0]}')
                start.grid(row=i + 1, column=0, padx=30)
                start2 = customtkinter.CTkLabel(master=frame5, text=f'{list[i][1]}')
                start2.grid(row=i + 1, column=1, padx=30)
                if list[i][2] == None:
                    start3 = customtkinter.CTkLabel(master=frame5, text='0')
                else:
                    start3 = customtkinter.CTkLabel(master=frame5, text=f'{list[i][2]}')
                start3.grid(row=i + 1, column=2, padx=15)
            if ip.sum_investor_income(name, login)[0] == None:
                start4 = customtkinter.CTkLabel(master=frame5,
                                                text='Мой суммарный доход по стартапу: 0')
            else:
                start4 = customtkinter.CTkLabel(master=frame5,
                                                text=f'Мой суммарный доход по стартапу: {ip.sum_investor_income(name, login)[0]}')
            start4.grid(row=res_months + 2, column=2, padx=15)
            button7 = customtkinter.CTkButton(master=frame5, text='Закрыть окно', cursor='hand2', width=10,
                                              height=10,
                                              command= delete_freme)
            button7.grid(row=res_months + 2, column=0, pady=15, padx=15)

        frame4 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame4.grid(row=1, column=1)
        today = datetime.date.today()
        data = str(today)[:-3] + '-01'
        info = ip.my_startups(name, login, data)
        label1 = customtkinter.CTkLabel(master=frame4, text=f'Название - {info[0]}')
        label1.grid(row=0, column=0, padx=10, pady=5)
        label2 = customtkinter.CTkLabel(master=frame4, text=f'Владелец - {info[1]}')
        label2.grid(row=1, column=0, padx=10, pady=5)
        label3 = customtkinter.CTkLabel(master=frame4, text=f'Планируемая стоимость - {info[2]}')
        label3.grid(row=2, column=0, padx=10, pady=5)
        label4 = customtkinter.CTkLabel(master=frame4, text=f'Процент - {info[3]}')
        label4.grid(row=3, column=0, padx=10, pady=5)
        label5 = customtkinter.CTkLabel(master=frame4, text=f'Общая прибыль - {info[4]}')
        label5.grid(row=4, column=0, padx=10, pady=5)
        if info[5] == None:
            label6 = customtkinter.CTkLabel(master=frame4, text=f'Месячная приибыль - Нет данных')
        else:
            label6 = customtkinter.CTkLabel(master=frame4, text=f'Месячная приибыль - {info[5]}')
        label6.grid(row=5, column=0, padx=10, pady=5)
        label7 = customtkinter.CTkLabel(master=frame4, text=f'Моя инвестиция - {info[6]}')
        label7.grid(row=6, column=0, padx=10, pady=5)
        if info[7] == None:
            label8 = customtkinter.CTkLabel(master=frame4, text=f'Текущая стоимость - Нет инвесторов')
        else:
            label8 = customtkinter.CTkLabel(master=frame4, text=f'Текущая стоимость - {info[7]}')
        label8.grid(row=6, column=0, padx=10, pady=5)
        button4 = customtkinter.CTkButton(master=frame4, text='Статистика по месяцам', cursor='hand2', width=10,
                                          height=10,
                                          command=lambda name=name: month_stat(name))
        button4.grid(row=8, column=0, pady=10, padx=10)
        button6 = customtkinter.CTkButton(master=frame4, text='Закрыть', cursor='hand2', width=10,
                                          height=10,
                                          command=delete_more_info)
        button6.grid(row=9, column=0, pady=10, padx=10)
#-----------------до сюда------- это первое окно


    def invest(name):


        def cancel():
            frame5.grid_forget()
        def go_in(name, inv):
            data = str(today)[:-3] + '-01'
            if ip.checking_into_investors(login, data, name):
                messagebox.showerror('Ошибка', 'Нельзя инвестировать несколько раз в месяц в один стартап')
            else:
                try:
                    ip.insert_into_investors(login, data, name, int(inv.get()))
                    messagebox.showerror('Успех', 'Операция совершина')
                    frame5.grid_forget()
                except ValueError:
                    messagebox.showerror('Ошибка', 'Необходимо ввести числовое значение')

        frame5 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame5.grid(row=1, column=2)
        lbl = customtkinter.CTkLabel(master=frame5, text='Сколько вы хотите инвестировать')
        lbl.grid(row=1, column=0, padx=10, pady=10)
        inv = customtkinter.CTkEntry(master=frame5,
                                            placeholder_text="Сумма",
                                            width=120,
                                            height=25,
                                            border_width=2,
                                            corner_radius=10, )
        inv.grid(row=1, column=1, padx=5, pady=10)
        button4 = customtkinter.CTkButton(master=frame5, text='Подтверждение', cursor='hand2', width=10,
                                          height=10,
                                          command=lambda name=name: go_in(name,inv))
        button4.grid(row=7, column=0, pady=15, padx=20)
        button6 = customtkinter.CTkButton(master=frame5, text='Отмена', cursor='hand2', width=10,
                                          height=10,
                                          command= cancel)
        button6.grid(row=7, column=1, pady=15, padx=20)

#Гдето тут нужно сделать проврку что ввели не пустое число и ввели впринципе число



    def month_stat1(name):
        def delete_month_stat1():
            frame5.grid_forget()
        list = ip.income(name)
        frame5 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame5.grid(row=1, column=2)
        lbl = customtkinter.CTkLabel(master=frame5, text = 'Дата')
        lbl.grid(row=0, column=0, padx=20)
        lbl2 = customtkinter.CTkLabel(master=frame5, text='Доход стартапа')
        lbl2.grid(row=0, column=1, padx=20)
        today = datetime.date.today()
        today4 = datetime.date.today()
        today4 -= relativedelta(months=12)

        today4 = str(today4)[:-3] + '-01'
        today4 = datetime.datetime.strptime(today4, "%Y-%m-%d").date()
        delta = relativedelta(today, today4)
        res_months = delta.months + (delta.years * 12) + 1
        for i in range(res_months):
            start = customtkinter.CTkLabel(master=frame5, text=f'{list[i][0]}')
            start.grid(row=i+1, column=0, padx=20)
            start2 = customtkinter.CTkLabel(master=frame5, text=f'{list[i][1]}')
            start2.grid(row=i + 1, column=1, padx=20)
        button6 = customtkinter.CTkButton(master=frame5, text='Закрыть', cursor='hand2', width=10,
                                          height=10,
                                          command=delete_month_stat1)
        button6.grid(row=res_months + 2, column=1, pady=15, padx=20)

    def more_info1(name):
        def delete_more_info1():
            frame4.grid_forget()
        frame4 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame4.grid(row=1, column=1)
        today = datetime.date.today()
        data = str(today)[:-3] + '-01'
        info = ip.all_startups(name, data)
        label1 = customtkinter.CTkLabel(master=frame4, text=f'Название - {info[0]}')
        label1.grid(row=0, column=0, padx=10, pady=5)
        label2 = customtkinter.CTkLabel(master=frame4, text=f'Владелец - {info[1]}')
        label2.grid(row=1, column=0, padx=10, pady=5)
        label3 = customtkinter.CTkLabel(master=frame4, text=f'Планируемая стоимость - {info[2]}')
        label3.grid(row=2, column=0, padx=10, pady=5)
        label4 = customtkinter.CTkLabel(master=frame4, text=f'Процент - {info[3]}')
        label4.grid(row=3, column=0, padx=10, pady=5)
        label5 = customtkinter.CTkLabel(master=frame4, text=f'Общая прибыль - {info[4]}')
        label5.grid(row=4, column=0, padx=10, pady=5)
        if info[5] == None:
            label6 = customtkinter.CTkLabel(master=frame4, text=f'Месячная приибыль - Нет данных')
        else:
            label6 = customtkinter.CTkLabel(master=frame4, text=f'Месячная приибыль - {info[5]}')
        label6.grid(row=5, column=0, padx=10, pady=5)
        if info[6] == None:
            label8 = customtkinter.CTkLabel(master=frame4, text=f'Текущая стоимость - Нет инвесторов')
        else:
            label8 = customtkinter.CTkLabel(master=frame4, text=f'Текущая стоимость - {info[6]}')
        label8.grid(row=6, column=0, padx=10, pady=5)
        button4 = customtkinter.CTkButton(master=frame4, text='Статистика по месяцам', cursor='hand2', width=10,
                                          height=10,
                                          command=lambda name=name: month_stat1(name))
        button4.grid(row=7, column=0, pady=10, padx=10)
        button5 = customtkinter.CTkButton(master=frame4, text='Инвестировать', cursor='hand2', width=10,
                                          height=10,
                                          command=lambda name=name: invest(name))
        button5.grid(row=8, column=0, pady=10, padx=10)
        button11 = customtkinter.CTkButton(master=frame4, text='Закрыть', cursor='hand2', width=10,
                                          height=10,
                                          command=delete_more_info1)
        button11.grid(row=9, column=0, pady=10, padx=15)
    # -----------------до сюда------- это последнее окно


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
        if ip.count_investors(login)[0] == 0:
            no_startups = customtkinter.CTkLabel(master=frame3, text='Всего заработано: 0. У вас еще нет стартапов')
            no_startups.grid(row=0, column=0, padx=15, pady=15)
        else:
            lbl = customtkinter.CTkLabel(master=frame3, text='Дата')
            lbl.grid(row=1, column=0, padx=15)
            lbl2 = customtkinter.CTkLabel(master=frame3, text='Весь доход за месяц')
            lbl2.grid(row=1, column=1, padx=15)
            today = datetime.date.today()
            today1 = datetime.date.today()
            today1 -= relativedelta(months=12)

            today1 = str(today1)[:-3] + '-01'
            today1 = datetime.datetime.strptime(today1, "%Y-%m-%d").date()
            delta = relativedelta(today, today1)
            res_months = delta.months + (delta.years * 12) + 1
            my_sum = 0
            for i in range(res_months):
                start1 = customtkinter.CTkLabel(master=frame3, text=f'{today1}')
                start1.grid(row=i + 2, column=0, padx=15)
                today1 += relativedelta(months=1)
            arr = [0] * res_months
            for i in range(ip.count_investors(login)[0]):
                m=0
                name = ip.name_startup(login)[i][0]
                for j in range(res_months):
                    if ip.investor_income(name, login)[j][2] != None:
                        arr[m] += ip.investor_income(name, login)[j][2]
                    m +=1
                if ip.sum_investor_income(name,login)[0] != None:
                    my_sum += ip.sum_investor_income(name,login)[0]
            startups = customtkinter.CTkLabel(master=frame3, text=f'Всего заработано: {my_sum} ')
            startups.grid(row=0, column=0, padx=15)
            for i in  range(len(arr)):
                start2 = customtkinter.CTkLabel(master=frame3, text=f'{arr[i]}')
                start2.grid(row=i + 2, column=1, padx=15)

    if per == 2:
        frame3 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame3.grid(row=1, column=0, padx=30, sticky='w')
        if ip.count_investors(login)[0] == 0:
            no_startups = customtkinter.CTkLabel(master=frame3, text='У вас еще нет стартапов')
            no_startups.grid(row=0, column=0, padx=15, pady=15)
        else:
            for i in range(ip.count_investors(login)[0]):
                name = ip.name_startup(login)[i][0]
                startup = customtkinter.CTkLabel(master=frame3, text=f'{i + 1} Стартап - {name}')
                startup.grid(row=i, column=0, padx=15)
                button = customtkinter.CTkButton(master=frame3, text='...', cursor='hand2', width=10, height=10,
                                                 command=lambda name=name: more_info(name))
                button.grid(row=i, column=1, padx=10)

    if per == 3:
        frame3 = customtkinter.CTkFrame(investor_window, fg_color='#158f58', corner_radius=10)
        frame3.grid(row=1, column=0, padx=30, sticky='w')
        for i in range(ip.count_startups()[0]):
            name = ip.count_all()[i][0]
            startup = customtkinter.CTkLabel(master=frame3, text=f'{i + 1} Стартап - {name}')
            startup.grid(row=i, column=0, padx=15)
            button = customtkinter.CTkButton(master=frame3, text='...', cursor='hand2', width=10, height=10,
                                                 command=lambda name=name: more_info1(name))
            button.grid(row=i, column=1, padx=10)



    button1 = customtkinter.CTkButton(master=frame1, text='Портфель', cursor='hand2', command=portfolio)
    button1.grid(row=0, column=0, pady=15, padx=20)

    button2 = customtkinter.CTkButton(master=frame1, text='Мои стартапы', cursor='hand2', command=startups_button)
    button2.grid(row=0, column=1, pady=15, padx=20)

    button3 = customtkinter.CTkButton(master=frame1, text='Все стартапы', cursor='hand2', command=all_startups)
    button3.grid(row=0, column=2, pady=15, padx=20)

    frame2 = customtkinter.CTkFrame(investor_window, fg_color='#1f7850', corner_radius=10)
    frame2.grid(row=0, column=2, padx=30, pady=30,  sticky='e')

    logout = customtkinter.CTkButton(master=frame2, text="Выйти из аккаунта ", font=('Century Gothic', 15),
                                     cursor='hand2', command=logout)
    logout.grid(row=0, column=0, padx=10, pady=10)
    def refresh():
        investor_window.destroy()
        investor_log(login, 0)

    button30 = customtkinter.CTkButton(master=frame2, text='Обновить страницу', cursor='hand2', command=refresh)
    button30.grid(row=0, column=1, pady=10, padx=10)

    today = date.today()
    label2 = customtkinter.CTkLabel(master=frame2, text='Сегодняшняя дата')
    label2.grid(row=1, column=0, padx=10, pady=10)
    label = customtkinter.CTkLabel(master=frame2, text=str(today))
    label.grid(row=1, column=1, padx=10, pady=10)

    investor_window.columnconfigure(2, weight=1)
    investor_window.rowconfigure(1, weight=1)


    investor_window.mainloop()

# investor_log(1, 0)
