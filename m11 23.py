import unittest
import sqlite3
from datetime import datetime

now = datetime.now()

conn = sqlite3.connect("база даных.sqlite")
curs = conn.cursor()

# после первого запуска за коментировать до строки 35 !!!!
# curs.execute("CREATE TABLE Students(id int PRIMARY KEY, name varchar(32),surname varchar(32), age int,city varchar(32))")

# curs.execute("CREATE TABLE Courses(id int PRIMARY KEY,name varchar(32), time_start int,time_end int)")

# curs.execute("CREATE TABLE Student_courses(student_id int, course_id int)")



# добывление курса
def App_courses(name,time_start,time_end):
    curs.execute("SELECT id FROM Courses ")
    curs.executemany("INSERT INTO Courses  VALUES (?,?, ?, ?)",[(curs.fetchall()[-1][0]+1,name,time_start,time_end)])


# добавление студентов
def App_Srudent(name,surname,age,city):
    curs.execute("SELECT id FROM Students ")
    curs.executemany("INSERT INTO Students VALUES (?,?, ?, ?, ?)",[(curs.fetchall()[-1][0]+1,name,surname,age,city)])


# добавление Student_courses
def App_Student_courses(name_courses, name,surname):
    curs.execute("SELECT id FROM Courses WHERE name = ?",(name_courses,))
    coursesf = curs.fetchall()[0][0]
    curs.execute("SELECT id FROM Students WHERE name = ? AND surname = ? ", (name,surname))
    studentsf = curs.fetchall()[0][0]
    curs.executemany("INSERT INTO Student_courses VALUES (?, ?)", [(studentsf, coursesf)])


def Delete_student(name,surname):
    curs.execute("SELECT  id  FROM Students WHERE  name = ? AND surname = ? ", (name,surname) )
    h = curs.fetchall()
    Delete_course(h)
    curs.execute("DELETE FROM Students WHERE name = ? AND surname = ? ", (name,surname))


def Delete_course(ids):
    print(ids[0])
    curs.execute("DELETE FROM Student_courses WHERE student_id = ? ",(ids[0]))


class students_and_courses(unittest.TestCase):

    def test_App_courses(self):
        a = ("C#",now.strftime('13.07.21'), now.strftime('16.08.21'))
        self.assertEqual(App_courses(a))
        prin("Hello")



unittest.main()
conn.commit()
conn.close()