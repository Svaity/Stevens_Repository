from collections import defaultdict
import os
from prettytable import PrettyTable
from other import pat as file_reader


class Student:
	pt_labels = ["CWID", "NAME", "MAJOR", "COURSES"]

	def __init__(self, cwid, name, major):
		self._cwid = cwid
		self._name = name
		self._major = major
		self._courses = dict()

	def add_course(self, course, grade):
		self._courses[course] = grade  # add the grades to dict using course as the key

	def pt_row(self):
		return [self._cwid, self._name, self._major, sorted(self._courses.keys())]


class Instructor:
	pt_labels = ["CWID", "NAME", "DEPT", "COURSE", "STUDENTS"]

	def __init__(self, cwid, name, dept):
		self._cwid = cwid
		self._name = name
		self._dept = dept
		self._courses = defaultdict(int)

	def add_course(self, course):
		self._courses[course] += 1

	def pt_row(self):
		for course, students in self._courses.items():
			yield [self._cwid, self._name, self._dept, course, students]


class University:
	def __init__(self, wdir, ptables=True):
		self._wdir = wdir
		self._students = dict()
		self._instructors = dict()

		self.read_students(os.path.join(wdir, 'students.txt'))
		self.read_instructors(os.path.join(wdir, 'instructors.txt'))
		self.read_grades(os.path.join(wdir, 'grades.txt'))

		if ptables:
			print("\n Student Summary")
			self.student_prettytable()

			print("\n Instructor Summary")
			self.instructor_prettytable()

	def read_students(self, path):
		try:
			for cwid, name, major in file_reader(path, 3, sep="\t", header=False):
				if cwid in self._students:
					print(f"ALready exists {cwid}")
				else:
					self._students[cwid] = Student(cwid, name, major)
		except ValueError as err:
			print(err)

	def read_instructors(self, path):
		try:
			for cwid, name, dept in file_reader(path, 3, sep="\t", header=False):
				if cwid in self._instructors:
					print(f"already exists {cwid}")
				else:
					self._instructors[cwid] = Instructor(cwid, name, dept)
		except ValueError as err:
			print(err)

	def read_grades(self, path):
		try:
			for student_cwid, course, grade, instructor_cwid in file_reader(path, 4, sep='\t', header=False):
				if student_cwid in self._students:
					self._students[student_cwid].add_course(course, grade)  # using the student cwid as key
				else:
					print(f"Warning: Student cwid {student_cwid} doesnt exist in students file")

				if instructor_cwid in self._instructors:
					self._instructors[instructor_cwid].add_course(course)  # using the instructor cwid as key
				else:
					print(f"Warning: instructor cwid {instructor_cwid} doesnt exist in instructor file")

		except ValueError as erf:
			print(erf)

	def student_prettytable(self):
		"""Make Pretty table"""
		pt = PrettyTable(field_names=Student.pt_labels)
		for student in self._students.values():
			pt.add_row(student.pt_row())
		print(pt)

	def instructor_prettytable(self):
		"""Make Pretty table"""
		pt = PrettyTable(field_names=Instructor.pt_labels)
		for instructor in self._instructors.values():
			for row in instructor.pt_row():
				pt.add_row(row)
		print(pt)


def main():
	University("/Users/Shrey/PycharmProjects/HW9")


if __name__ == "__main__":
	main()
