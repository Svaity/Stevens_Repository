import sqlite3

file = "/Users/shrey/Desktop/new/shrey2.db"
query = "select s.cwid, s.name, s.major, count(g.Course) as complete from HW11_students s join HW11_grades g on s.cwid=g.Student_CWID group by s.cwid, s.name, s.major"
args = ('10103',)
db = sqlite3.connect(file)
rows = db.execute(query)

# convert the query of results to a list of dictionaries
data = [{"CWID": cwid,"name": name,"major": major}
		for cwid, name, major in rows]

db.close()