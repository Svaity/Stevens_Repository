from HW10 import University, Student, Instructor, Major, main
import unittest


class HW10Test(unittest.TestCase):
	def test_stevens(self):
		wdir = '/Users/Shrey/PycharmProjects/HW10'
		stevens = University(wdir, False)
		"""Test for Student table """
		expect_student = [['10103','Baldwin, C','SFEN',{'SSW 567', 'SSW 564'},{'SSW 540', 'SSW 555'},{'CS 501', 'CS 513', 'CS 545'}],
					['10115','Wyatt, X','SFEN',{'SSW 567', 'SSW 564', 'CS 545', 'SSW 687'},{'SSW 540', 'SSW 555'},None],
					['10172','Forbes, I','SFEN',{'SSW 567', 'SSW 555'},{'SSW 564', 'SSW 540'},{'CS 501', 'CS 513', 'CS 545'}],
					['10175','Erickson, D','SFEN',{'SSW 567', 'SSW 564', 'SSW 687'},{'SSW 540', 'SSW 555'},{'CS 501', 'CS 513', 'CS 545'}],
					['10183','Chapman, O','SFEN',{'SSW 689'},{'SSW 567', 'SSW 564', 'SSW 540', 'SSW 555'},{'CS 501', 'CS 513', 'CS 545'}],
					['11399','Cordova, I','SYEN',set(),{'SYS 612', 'SYS 671', 'SYS 800'},{'SSW 565', 'SSW 540', 'SSW 810'}],
					['11461','Wright, U','SYEN',{'SYS 750', 'SYS 611', 'SYS 800'},{'SYS 612', 'SYS 671'},{'SSW 565', 'SSW 540', 'SSW 810'}],
					['11658','Kelly, P','SYEN',set(),{'SYS 612', 'SYS 671', 'SYS 800'},{'SSW 565', 'SSW 540', 'SSW 810'}],
					['11714','Morton, A','SYEN',{'SYS 611'},{'SYS 612', 'SYS 671', 'SYS 800'},{'SSW 565', 'SSW 540', 'SSW 810'}],
					['11788','Fuller, E','SYEN',{'SSW 540'},{'SYS 612', 'SYS 671', 'SYS 800'},None]]
		"""Test for Instructor table"""
		expect_instructor = [["98765", "Einstein, A", "SFEN", "SSW 567", 4],
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
					["98760", "Darwin, C", "SYEN", "SYS 645", 1]]

		"""Test for expected major"""
		expect_major = [["SFEN", {'SSW 540', 'SSW 564', 'SSW 567', 'SSW 555'}, {'CS 545', 'CS 501', 'CS 513'}], ["SYEN", {'SYS 612', 'SYS 800', 'SYS 671'}, {'SSW 810', 'SSW 565', 'SSW 540'}]]

		ptstudent = [s.pt_row() for s in stevens._students.values()]
		ptinstructor = [row for Instructor in stevens._instructors.values() for row in Instructor.pt_row()]
		ptmajor = [m.pt_row() for m in stevens._majors.values()]

		self.assertEqual(ptmajor, expect_major)
		self.assertEqual(ptstudent, expect_student)
		self.assertEqual(ptinstructor, expect_instructor)

if __name__ == '__main__':
	unittest.main(exit=False, verbosity=2)