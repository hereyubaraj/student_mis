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
		
		print("is in else")
		if course_found :
			print("inside coursefound condition")
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

student_identifier = input("Student Name or id : ")
#check this is the existing student or not
# let say we will save the student record in the student.json file
try:
	# with open("student.json", "r") as fp:
	# 	student_record = fp.read()	
	askStudentInfo()
except:
	askStudentInfo()



