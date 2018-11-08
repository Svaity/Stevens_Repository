
import unittest
import datetime
import os
from prettytable import PrettyTable


def date_time(a, b, num_days):
	"""Using time date module find days between after and before days"""

	dt1 = datetime.datetime.strptime(a, "%d %b %Y")
	dt2 = datetime.datetime.strptime(b, "%d %b %Y")

	# time between 2 dates
	days_btwn = abs(dt2 - dt1).days
	d = ("{} days between {} and {}".format(days_btwn, dt1.strftime("%m/%d/%Y"), dt2.strftime("%m/%d/%Y")))

	# how many days before
	days_aft = dt1 - datetime.timedelta(days=num_days)
	e = ("{} days before {} is {}".format(num_days, dt1.strftime("%m/%d/%Y"), days_aft.strftime("%m/%d/%Y")))

	# how many days before
	days_bfr = dt1 + datetime.timedelta(days=num_days)
	f = ("{} days after {} is {}".format(num_days, dt1.strftime("%m/%d/%Y"), days_bfr.strftime("%m/%d/%Y")))

	return d, e, f


def sep_file_read(i):
	"""Read the file and return line by line"""
	file_name = i
	try:
		fp = open(file_name, "r")
	except FileNotFoundError:
		print("No such file present")
		exit()
	else:
		with fp:
			for line in fp:
				yield line


def pat(pt, num_fields, sep, header):
	"""CHeck and returns the user given fields"""
	file_name = pt
	if file_name in pt:
		fp = open(file_name, "r")
	else:
		raise FileNotFoundError
	with fp:
		for line_num, line in enumerate(fp, 1):
			line = line.strip()
			line = line.strip("\n")
			elements = line.split(sep)
			if len(elements) == num_fields:
				if header is True:
					header = False
					continue
				yield tuple(elements)
			else:
				l = len(elements)
				raise ValueError(file_name, "given:", num_fields, "expected:", l, "on line", line_num)


def no_of_meth(ls):
	"""Find number of methods classes character and line in a python file"""
	num = 0
	meth_cnt = 0
	class_cnt = 0
	length = 0
	for i in ls:
		length += len(i)
		i = i.lstrip()
		i = i.strip("\n")
		if i.startswith("def "):
			meth_cnt += 1
		if i.startswith("class "):
			class_cnt += 1
		num += 1
	return num, meth_cnt, class_cnt, length


def scn_files(directory):
	"""Make Pretty Table"""
	pt = PrettyTable(field_names=["files", "lines", "functions", "classes", "character"])
	files = os.listdir(directory)
	for i in files:
		if i.endswith(".py"):
			a = list(sep_file_read(i))
			classes, functions, chars, lines = no_of_meth(a)
			pt.add_row([i, classes, functions, chars, lines])
	yield pt


def main():
	"""Initialization"""
	# part1 of HW
	a = "1 Jan 2017"
	b = "31 Oct 2017"
	num_days = int(input("number of days"))
	print(date_time(a, b, num_days))

	# part2 of HW
	pt = os.listdir()
	for cwid, name, major in pat(pt, 3, '|', True):  # if i put True it wont show the header
		v = (name, cwid, major)
		print(v)

	# part3 of HW
	e = scn_files(os.getcwd())
	print(PrettyTable(e))

