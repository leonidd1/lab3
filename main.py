import psycopg2
from tkinter import messagebox


class Repository:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                host="195.19.32.74",
                port=5432,
                user="student",
                password="bmstu",
                database="fn1133_2022"
            )
        except Exception as ex:
            messagebox.showerror('Ошибка', 'Подключение к серверу не установлено. Пожалуйста проверте подключение к интеренету')

    def insert_into_users(self, nick_name, first_name, last_name, password_user):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    INSERT INTO users 
                    VALUES (%s, %s, %s, %s); """,
                           (nick_name, first_name, last_name, password_user))
            self.connection.commit()

    def user_verification(self, nick_name, password_user):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT 1 FROM users WHERE nick_name = %s AND  password_user = %s""",
                           (nick_name, password_user))
            return cursor.fetchone()

    def checking_uniqueness(self, nick_name):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT 1 FROM users WHERE nick_name = '{0}'""".format(nick_name))
            return cursor.fetchone()

    def count_investors(self, nick_name):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                       SELECT COUNT(DISTINCT name_startup) FROM investors WHERE investor = '{0}'""".format(nick_name))
            return cursor.fetchone()

    def name_startup(self, nick_name):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                       SELECT DISTINCT name_startup FROM investors WHERE investor = '{0}'""".format(nick_name))
            return cursor.fetchall()

    def my_startups(self, name_startup, nick_name, data):  # ВАЖНО Дата в формате: год-месяц-01
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT name_startup, nick_name_owner, planned_cost, percent,
       (SELECT SUM(monthly_income) FROM data_all WHERE data_all.name_startup = '{0}'),
       (SELECT monthly_income FROM data_all WHERE month_all = '{2}' AND data_all.name_startup = '{0}'),
       (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}' AND investor = '{1}'),
       (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}')
FROM startups WHERE name_startup = '{0}'"""
                           .format(name_startup, nick_name, data))
            return cursor.fetchone()

    def investor_income(self, name_startup, nick_name):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT month_all,monthly_income, monthly_income * (SELECT percent FROM startups WHERE startups.name_startup = '{0}') / 100
* (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}' AND investor = '{1}' AND investors.month_all <= data_all.month_all)
/ (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}' AND investors.month_all<= data_all.month_all)
       FROM data_all WHERE name_startup = '{0}' ORDER BY month_all""".format(name_startup, nick_name))
            return cursor.fetchall()

    def sum_investor_income(self, name_startup, nick_name):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT SUM(monthly_income * (SELECT percent FROM startups WHERE startups.name_startup = '{0}') / 100
* (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}' AND investor = '{1}' AND investors.month_all<= data_all.month_all)
/ (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}' AND investors.month_all<= data_all.month_all))
       FROM data_all WHERE name_startup = '{0}'""".format(name_startup, nick_name))
            return cursor.fetchone()

    def income(self, name_startup):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT month_all,monthly_income FROM data_all WHERE name_startup = '{0}' ORDER BY month_all"""
                           .format(name_startup))
            return cursor.fetchall()
    def all_startups(self, name_startup, data):  # ВАЖНО Дата в формате: год-месяц-01
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT name_startup, nick_name_owner, planned_cost, percent,
       (SELECT SUM(monthly_income) FROM data_all WHERE data_all.name_startup = '{0}'),
       (SELECT monthly_income FROM data_all WHERE month_all = '{1}' AND data_all.name_startup = '{0}'),
       (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}')
FROM startups WHERE name_startup = '{0}'"""
                           .format(name_startup, data))
            return cursor.fetchone()

    def count_all(self):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                       SELECT name_startup FROM startups""")
            return cursor.fetchall()

    def count_startups(self):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                       SELECT COUNT(*) FROM startups""")
            return cursor.fetchone()

    def insert_into_investors(self, investor, month_all, name_startup, sum_investor):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    INSERT INTO investors VALUES ('{0}', '{1}', '{2}', '{3}') """
                           .format(investor, month_all, name_startup, sum_investor))
            self.connection.commit()

    def checking_into_investors(self, nick_name, month_all, name_startup):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT 1 FROM investors WHERE investor = '{0}' AND month_all = '{1}' AND
                     name_startup = '{2}'""".format(nick_name, month_all, name_startup))
            return cursor.fetchone()

    def name_startup_nick(self, nick_name_owner):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                       SELECT DISTINCT name_startup FROM startups WHERE nick_name_owner = '{0}'""".format(nick_name_owner))
            return cursor.fetchall()

    def count_name_startup(self, nick_name_owner):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                       SELECT COUNT(DISTINCT name_startup) FROM startups WHERE nick_name_owner = '{0}'""".format(nick_name_owner))
            return cursor.fetchone()

    def my_startups_no_invest(self, name_startup, data):  # ВАЖНО Дата в формате: год-месяц-01
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT name_startup, nick_name_owner, planned_cost, percent,
           (SELECT SUM(monthly_income) FROM data_all WHERE data_all.name_startup = '{0}'),
           (SELECT monthly_income FROM data_all WHERE month_all = '{1}' AND data_all.name_startup = '{0}'),
           (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}')
    FROM startups WHERE name_startup = '{0}'"""
                            .format(name_startup, data))
            return cursor.fetchone()


    def startaper_income(self, name_startup):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT month_all, monthly_income, monthly_income - monthly_income * (SELECT percent FROM startups WHERE startups.name_startup = '{0}') / 100
       FROM data_all WHERE name_startup = '{0}' ORDER BY month_all""".format(name_startup))
            return cursor.fetchall()

    def sum_startaper_income(self, name_startup):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT SUM(monthly_income - monthly_income * (SELECT percent FROM startups WHERE startups.name_startup = '{0}') / 100)
       FROM data_all WHERE name_startup = '{0}'""".format(name_startup))
            return cursor.fetchone()

    def insert_into_startups(self, name_startup, nick_name_owner, planned_cost, percent):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    INSERT INTO startups VALUES ('{0}', '{1}', '{2}', '{3}') """
                           .format(name_startup, nick_name_owner, planned_cost, percent))
            self.connection.commit()

    def checking_name_startaps(self, name_startup):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT 1 FROM startups WHERE name_startup = '{0}'""".format(name_startup))
            return cursor.fetchone()

    def insert_into_data(self, month_all, name_startup, monthly_income):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    INSERT INTO data_all VALUES ('{0}', '{1}', '{2}') """
                           .format(month_all, name_startup, monthly_income))
            self.connection.commit()

    def update_data(self, monthly_income, month_all, name_startup):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    UPDATE data_all SET monthly_income = '{0}' WHERE month_all = '{1}' AND name_startup = '{2}'"""
                           .format(monthly_income, month_all, name_startup))
            self.connection.commit()

    def startup_ch(self, name_startup):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
           SELECT (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}')
    FROM startups WHERE name_startup = '{0}'"""
                            .format(name_startup))
            return cursor.fetchone()

    def sum_startaper_income_else(self, name_startup):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                    SELECT SUM(monthly_income)
       FROM data_all WHERE name_startup = '{0}'""".format(name_startup))
            return cursor.fetchone()