'''
	Student management information system
'''
import time
import os
import json
from student import Student

def askStudentInfo():
	course_info = input("Desired Course: ")
	# check this course exists or not
	with open("courses.json", "r") as fp:
		courses_detail = fp.read()
		course_list = json.loads(courses_detail)
		course_found = False
		for course in course_list:
			if course['name'].lower() == course_info.lower():
				course_found = True	
				print("course is found")
				break
				 # course found
		if course_found :
			student = Student().askDetail(course_info)
			print(student.saveToFile())
			# save student to json
		else:
			print("We dont have {} available".format(course_info))	 

# Get the student name or id
print("\n\n\n \t\t\t Welcome to management system")
# this will delay the execution for two second
time.sleep(2)
# this clear the screen
os.system("clear")

student_identifier = input("Student Name : ")
#check this is the existing student or not
# let say we will save the student record in the student.json file
try:
	with open("student.json", "r") as fp:
		student_record = fp.read()	
		if student_record :
			i = 0
			student_list = json.loads(student_record)
			student_found = False
			for i in range(len(student_list)):
				stu = student_list[i]
				if stu['name'].lower() == student_identifier.lower():
					student_found = True
					break
			if not student_found:
				print("New student/ Welcome to our instititute")
				askStudentInfo()
			else:
				print("you have paid {} ".format(student_list[i]['fee']))

		else:
			print("student record not found")
			askStudentInfo()

except:
	print("New student \n")
	askStudentInfo()



