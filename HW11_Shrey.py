import os
from prettytable import PrettyTable
import sqlite3


path = "C:/Users/Sandeep/Desktop/810/Assignment/s_startup.db"
query = "select Instructor_CWID, Name, Dept, Course,Count(Student_CWID) from HW11_grades g join HW11_instructors i  on i.I_CWID = g.Instructor_CWID group by (Course)"
connect = sqlite3.connect(path)
pt_labels = ["CWID", "NAME", "DEPT", "COURSE", "STUDENTS"]
pt = PrettyTable(field_names=pt_labels)
for i in connect.execute(query):
    pt.add_row(i)

print(pt)





