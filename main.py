import psycopg2



class Repository:
    def __init__(self):
        # set connection
        self.connection = psycopg2.connect(
            host="195.19.32.74",
            port=5432,
            user="student",
            password="bmstu",
            database="fn1133_2022"
        )

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
                       SELECT COUNT(*) FROM investors WHERE investor = '{0}'""".format(nick_name))
            return cursor.fetchone()

    def name_startup(self, nick_name):
        with self.connection.cursor() as cursor:
            cursor.execute(""" 
                       SELECT name_startup FROM investors WHERE investor = '{0}'""".format(nick_name))
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
                    SELECT month_all, monthly_income * (SELECT percent FROM startups WHERE startups.name_startup = '{0}') / 100
* (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}' AND investor = '{1}')
/ (SELECT SUM(sum_investor) FROM investors WHERE investors.name_startup ='{0}')
       FROM data_all WHERE name_startup = '{0}'""".format(name_startup, nick_name))
            return cursor.fetchall()