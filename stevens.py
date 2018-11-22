from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

DB_FILE = "/Users/shrey/Desktop/new/shrey2.db"

@app.route("/")
def hello():
	return render_template("hello.html")

@app.route("/students")
def students_summary():
	students = [
		{
			"cwid": "1234",
			"name": "Kelly, P",
			"major": "SYEN",
			"taken": ["SSW 540"],
			"remaining": ["SSW 612", "SYS 671", "SYS 672", "SYS 673", "SYS 888"]
		},
		{
			"cwid": "4321",
			"name": "Mortan, A",
			"major": "SYEN",
			"taken": ["SYS 611, SYS 645"],
			"remaining": ["SSW 612", "SYS 671", "SYS 672", "SYS 673", "SYS 888"]
		}
	]
	return render_template("students_table.html",
							title="Stevens repository",
							table_title="Student summary",
							students=students)

@app.route("/student_courses")
def student_courses():

	query = "select s.cwid, s.name, s.major, count(g.Course) as complete from HW11_students s join HW11_grades g on s.cwid=g.Student_CWID group by s.cwid, s.name, s.major"
	db = sqlite3.connect(DB_FILE)
	results = db.execute(query)

	data = [{"cwid": cwid, "name": name, "major": major, "complete": complete}
			for cwid, name, major, complete in results]

	db.close()
	return render_template('student_courses.html',
							title= "Stevens_repository",
							table_title= "Number of completed " ,
							students= data)

@app.route("/choose_student")
def choose_student():
	query = "select cwid, name from HW11_students group by cwid, name"
	db = sqlite3.connect(DB_FILE)
	results = db.execute(query)
	students = [{"cwid": cwid, "name": name} for cwid, name in results ]
	db.close()
	return render_template("students.html", students=students)

@app.route("/show_student", methods=['POST'])
def show_students():
	"""user chose a student from the form and want the info"""
	if request.method == 'POST':
		cwid = request.form['cwid']
		query = "select course, grade from HW11_grades where student_cwid=?"
		args = (cwid,)
		table_title = "Course/Grades for CWID {}".format(cwid)

		db = sqlite3.connect(DB_FILE)
		results = db.execute(query, args)

		rows = [{'course': course, 'grade': grade} for course, grade in results]
		db.close()

		return render_template('display_student_grades.html', title="Student Repository",
							table_title=table_title, rows=rows)

app.run(debug=True)