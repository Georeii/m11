import sqlite3
from datetime import datetime

now = datetime.now()

conn = sqlite3.connect("база даных.sqlite")
curs = conn.cursor()

# # после первого запуска за коментировать до строки 35 !!!!
# # добавление таблиц
curs.execute("CREATE TABLE Students(id INTEGER PRIMARY KEY, name varchar(32),surname varchar(32), age int,city varchar(32))")

curs.execute("CREATE TABLE Courses(id INTEGER PRIMARY KEY,name varchar(32), time_start int,time_end int)")

curs.execute("CREATE TABLE Student_courses(student_id int, course_id int)")



# добывление курса
def App_courses(name,time_start,time_end):
    curs.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)",[name,time_start,time_end])

# добавление студентов
def App_Srudent(name,surname,age,city):
    curs.executemany("INSERT INTO Students VALUES (?, ?, ?, ?)",[(name,surname,age,city)])

# добавление Student_courses
def App_Student_courses(id_studens, id_coursers):
    curs.executemany("INSERT INTO Student_courses VALUES (?, ?)", [(id_studens, id_coursers)])

def Delete_student(name,surname):
    curs.execute(f"DELETE FROM Students WHERE name and surname LIKE {name} and {surname}")


def Delete_course():
    pass


# # # до этого момента
# # -----------------------------------------------
# curs.execute("SELECT * FROM Students WHERE age >= 30")
# print(curs.fetchall())
# # -----------------------------------------------
# curs.execute("SELECT student_id  FROM Student_courses WHERE course_id == 1")
# h = curs.fetchall()
# for i in h:
#     curs.execute("SELECT * FROM Students WHERE id == (?)", [i[0]])
#     print("студенты по пайтон", curs.fetchall())
# # ---------------------------------------------
# for i in h:
#     curs.execute("SELECT * FROM Students WHERE city == 'Spb' and id == (?)", [i[0]])
#     student = curs.fetchall()
#     if student != []:
#         print("студенты из города Spd по пайтон", student)
# # -----------------------------------------------

conn.commit()
conn.close()


# (1, 'python', now.strftime('21.07.21'), now.strftime('21.08.21')),
                  # (2, 'java', now.strftime('13.07.21'), now.strftime('16.08.21'))
# ТЕСТЫ
