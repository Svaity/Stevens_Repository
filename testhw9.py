from HW09 import University, Student, Instructor
import unittest


class HW9Test(unittest.TestCase):
	def test_stevensstud(self):
		"""test for student pt"""
		wdir = "/Users/Shrey/PycharmProjects/HW9"
		stevens = University(wdir, False)
		expect_students = [["10103", "Baldwin, C", "SFEN", ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']],
						["10115", "Wyatt, X", "SFEN", ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']],
						["10172", "Forbes, I", "SFEN", ['SSW 555', 'SSW 567']],
						["10175", "Erickson, D", "SFEN", ['SSW 564', 'SSW 567', 'SSW 687']],
						["10183", "Chapman, O", "SFEN", ['SSW 689']],
						["11399", "Cordova, I", "SYEN", ['SSW 540']],
						["11461", "Wright, U", "SYEN", ['SYS 611', 'SYS 750', 'SYS 800']],
						["11658", "Kelly, P", "SYEN", ['SSW 540']],
						["11714", "Morton, A", "SYEN", ['SYS 611', 'SYS 645']],
						["11788", "Fuller, E", "SYEN", ['SSW 540']]
						]
		students = [s.pt_row() for s in stevens._students.values()]
		self.assertEqual(students, expect_students)

	def test_stevensinstr(self):
		"""test for instructor pt"""
		wdir = "/Users/Shrey/PycharmProjects/HW9"
		stevens = University(wdir, False)
		expect_instructors = [["98765", "Einstein, A", "SFEN", "SSW 567", 4],
							["98765", "Einstein, A", "SFEN", "SSW 540", 3],
							["98764", "Feynman, R", "SFEN", "SSW 564", 3],
							["98764", "Feynman, R", "SFEN", "SSW 687", 3],
							["98764", "Feynman, R", "SFEN", "CS 501", 1],
							["98764", "Feynman, R", "SFEN", "CS 545", 1],
							["98763", "Newton, I", "SFEN", "SSW 555", 1],
							["98763", "Newton, I", "SFEN", "SSW 689", 1],
							["98760", "Darwin, C", "SYEN", "SYS 800", 1],
							["98760", "Darwin, C", "SYEN", "SYS 750", 1],
							["98760", "Darwin, C", "SYEN", "SYS 611", 2],
							["98760", "Darwin, C", "SYEN", "SYS 645", 1],
							]
		instructors = [row for instructor in stevens._instructors.values() for row in instructor.pt_row()]
		self.assertEqual(instructors, expect_instructors)


if __name__ == "__main__":
	unittest.main(exit=False, verbosity=2)