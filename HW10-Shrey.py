"""
Created on 8 November 8:00 pm 2018
@author: Shrey_Vaity
Title:  add new features to data repository you created last week.
One of the most popular features is knowing what classes have been completed when signing up for classes for next semester.
However, users point out that it would be nice if your system also the remaining required courses.

"""
import unittest
from collections import defaultdict
import os
from prettytable import PrettyTable
from other import pat as file_reader


class Instructor:
	"""Class for instructors"""
	pt_labels = ["CWID", "NAME", "DEPT", "COURSE", "STUDENTS"]

	def __init__(self, cwid, name, dept):
		self._cwid = cwid
		self._name = name
		self._dept = dept
		self._courses = defaultdict(int)

	def add_course(self, course):
		"""add course"""
		self._courses[course] += 1

	def pt_row(self):
		"""generator for info"""
		for course, students in self._courses.items():
			yield [self._cwid, self._name, self._dept, course, students]


class Student:
	"""class for student"""
	pt_labels = ["CWID", "NAME", "MAJOR", "Completed COURSES", "Rmn Reqd", "Rmn Elct"]

	def __init__(self, cwid, name, major, majors):
		self._cwid = cwid
		self._name = name
		self._major = major
		self._majors = majors
		self._courses = dict()

	def add_course(self, course, grade):
		"""add if passing grade """
		passing_grade = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C']
		if grade in passing_grade:
			self._courses[course] = grade  # add the grades to dict using course as the key

	def pt_row(self):
		"""generator for student"""
		completed_courses, rem_required, rem_electives = self._majors.grade_check(self._courses)
		return [self._cwid, self._name, self._major, completed_courses, rem_required, rem_electives]


class University:
	def __init__(self, wdir, ptables=True):
		self._wdir = wdir
		self._students = dict()
		self._instructors = dict()
		self._majors = dict()

		self.read_instructors(os.path.join(wdir, 'instructors.txt'))
		self.read_majors(os.path.join(wdir, 'majors.txt'))  # add read txt
		self.read_students(os.path.join(wdir, 'students.txt'))
		self.read_grades(os.path.join(wdir, 'grades.txt'))

		if ptables:

			print("\n Major Summary")
			self.majors_prettytable()

			print("\n Student Summary")
			self.student_prettytable()

			print("\n Instructor Summary")
			self.instructor_prettytable()

	def read_majors(self, path):
		"""read the majors from major.txt"""
		try:
			for major, flag, course in file_reader(path, 3, sep='\t', header=False):
				if major in self._majors:
					self._majors[major].add_course(flag, course)
				else:
					self._majors[major] = Major(major)
					self._majors[major].add_course(flag, course)
		except ValueError as err:
			print(err)

	def read_students(self, path):
		"""read the students.txt"""
		try:
			for cwid, name, major in file_reader(path, 3, sep="\t", header=False):
				if cwid in self._students:
					print(f"{cwid} is already there")
				else:
					self._students[cwid] = Student(cwid, name, major, self._majors[major])
		except ValueError as err:
			print(err)

	def read_instructors(self, path):
		"""read the file instructors.txt"""
		try:
			for cwid, name, dept in file_reader(path, 3, sep="\t", header=False):
				if cwid in self._instructors:
					print(f"already exists {cwid}")
				else:
					self._instructors[cwid] = Instructor(cwid, name, dept)
		except ValueError as err:
			print(err)

	def read_grades(self, path):
		"""read the file grades.txt"""
		try:
			for student_cwid, course, grade, instructor_cwid in file_reader(path, 4, sep='\t', header=False):
				if student_cwid in self._students:
					self._students[student_cwid].add_course(course, grade)  
				else:
					print(f"Warning: Student cwid {student_cwid} doesnt exist in students file")

				if instructor_cwid in self._instructors:
					self._instructors[instructor_cwid].add_course(course)  # using the instructor cwid as key
				else:
					print(f"Warning: instructor cwid {instructor_cwid} doesnt exist in instructor file")

		except ValueError as erf:
			print(erf)

	def majors_prettytable(self):
		"""Prettytable for majors"""
		pt = PrettyTable(field_names=["Major", "Required Course", "Electives"])
		for major in self._majors.values():
			pt.add_row(major.pt_row())
		print(pt)

	def student_prettytable(self):
		"""Make Pretty table for students"""
		pt = PrettyTable(field_names=Student.pt_labels)
		for student in self._students.values():
			pt.add_row(student.pt_row())
		print(pt)

	def instructor_prettytable(self):
		"""Make Pretty table for instructors"""
		pt = PrettyTable(field_names=Instructor.pt_labels)
		for instructor in self._instructors.values():
			for row in instructor.pt_row():
				pt.add_row(row)
		print(pt)


class Major:
	pt_labels = ["MAJOR", "REQUIRED", "ELECTIVES"]

	def __init__(self, name, passing=None):
		self._name = name
		self._required = set()
		self._electives = set()
		if passing is None:
			self._passing_grades = {'A', 'A-', 'B+', 'B-', 'C+', 'C-'}
		else:
			self._passing_grades = passing

	def add_course(self, flag, course):
		"""Check of the Subjects are required and electives"""
		if flag == 'E':
			self._electives.add(course)
		elif flag == 'R':
			self._required.add(course)
		else:
			raise ValueError("No such {} course occurs".format(flag))

	def grade_check(self, courses):
		"""check if the grades and conditions rae fulfilled"""
		completed_courses = {course for course, grade in courses.items() if grade in self._passing_grades}
		if completed_courses == "{}":
			return [completed_courses, self._required, self._electives]
		else:
			rem_required = self._required - completed_courses
			if self._electives.intersection(completed_courses):
				rem_electives = None
			else:
				rem_electives = self._electives

			return [completed_courses, rem_required, rem_electives]

	def pt_row(self):
		return [self._name, self._required, self._electives]


def main():
	University("/Users/Shrey/PycharmProjects/HW10")


if __name__ == "__main__":
	main()
