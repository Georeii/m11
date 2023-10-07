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
    for i in ids:
            curs.execute("DELETE FROM Student_courses WHERE student_id = ? ",(i))


class students_and_courses(unittest.TestCase):
    def test_App_courses(self):
        a = ("C#",now.strftime('13.07.21'), now.strftime('16.08.21'))
        App_courses(a[0],a[1],a[2])
        h = curs.execute("SELECT name,time_start,time_end FROM Courses WHERE name = ? AND time_start = ? AND time_end = ? ",a)
        self.assertEqual(a,curs.fetchall()[0])

    def test_App_Srudent(self):
    
        a = ( 'Kate', 'Brooks', 34, 'Spb')
        App_Srudent(a[0],a[1],a[2],a[3],)
        h = curs.execute("SELECT name,surname,age,city FROM Students WHERE name = ? AND surname = ? AND age = ? AND city = ?",a)
        self.assertEqual(a,curs.fetchall()[0])

    def test_delet_student(self):
        a = ( 'Kate', 'Brooks', 34, 'Spb')
        Delete_student(a[0],a[1],)
        self.assertTrue(examination_delet_student(a))


    def test_delet_student_and_courses(self):
        a = ( 'Max', 'Brooks', 24, 'Spb')
        curs.execute("SELECT id FROM Students WHERE name = ? AND surname = ? AND age = ? AND city = ?",a)
        ids = curs.fetchall()
        Delete_student(a[0],a[1],)
        self.assertTrue(examination_delet_student_courses(a,ids))

def examination_delet_student(student):
    curs.execute("SELECT * FROM Students WHERE name = ? AND surname = ? AND age = ? AND city = ?",student)
    h = curs.fetchall()
    if h == []:
        return(True)
    else:
        return(False)

def examination_delet_student_courses(student,ids):
    curs.execute("SELECT * FROM Students WHERE name = ? AND surname = ? AND age = ? AND city = ?",student)
    h = curs.fetchall()
    curs.execute("SELECT * FROM Student_courses WHERE student_id == ?",ids[0])
    g = curs.fetchall()
    if h == [] and g == []:
        return(True)
    else:
        return(False)


    

# App_Srudent('Kate', 'Brooks', 34, 'Spb')
# App_Student_courses('python','Max', 'Brooks')


# Delete_student('Kate', 'Brooks')
unittest.main()
conn.commit()
conn.close()