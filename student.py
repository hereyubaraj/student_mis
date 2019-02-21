import json
class Student:
	def askDetail(self, course_info):
		self.name = input("Enter your name : ")
		self.address = input("Enter your address: ")
		self.phone_number = input("Enter your phone number")
		self.course = course_info
		return self

	def toDict(self):
		student_dict =  {
			'name': self.name,
			'address': self.address,
			'phone_number': self.phone_number,
			'course': self.course
		}
		return student_dict

	def saveToFile(self):
		try:
			with open("student.json", "w+") as fp:
				student_content = fp.read()
				if not student_content:
					# create the empty list
					student_list = []
					# add the student in the empty list
					student_list.append(self.toDict())
					# print(student_list)
					print(json.dumps(student_list))
					# write the list in the file
					fp.write(json.dumps(student_list))
				else:
					# if file is not empty
					# convert the string to list
					print(student_content)
					student_list = json.loads(student_content)
					# append the student record to list
					student_list.append(self.toDict())
					print(student_list)
					# convert the list to string and write in the file
					fp.write(json.dumps(student_list))
		except:
			print('cannot create the student json file')
