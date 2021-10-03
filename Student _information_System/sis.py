
import sys
import re
# -*- coding:utf-8 -*-
menus="""
1. Add student information
 2. Delete student information
 3. Search student information
 4. Display all student information
 5. Display Sorted List
 6. Save Current student information!
 0. Clear screen information
"""

# PArent dictionary to store all student information
studentDict = {}

#For email validation
email_validators = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

#function to make all inputs mandatory		
def inputData():	
	'''Student id as dictionary key '''
	student_inf={}
	   
	#Check if name field has been left empty   
	def mandatory_name():
		nm=input("\tEnter the student name: ")

		#check if name is empty
		if len(nm) != 0:
			student_inf['name']=nm
		else:
			nm = print("Can't be empty:\n")
			mandatory_name()

	#Check if city field has been left empty
	def mandatory_city():
		city=input("\tEnter the student city: ")

		#check if city is empty
		if len(city) != 0:
			student_inf['city']=city
		else:
			city = print("Can't be empty:\n")
			mandatory_city()

	#Check if state field has been left empty
	def mandatory_state():
		state=input("\tEnter the student state: ")

		#check if state is empty
		if len(state) != 0:
			student_inf['state']=state
		else:
			state = print("Can't be empty:\n")
			mandatory_state()

	#Check if phone number is of 10 digits	
	def validate_phone():
		mobNo=input("\tEnter mobNo: ")
		if mobNo not in sorted(studentDict.keys()):
			#Check if phone number is of 10 digits
			if len(mobNo)==10:
				student_inf['mobNo'] = mobNo
			else:
				print("\tInvalid mobNo")
				validate_phone()
		else:
			print("Student Already Exists!")

	#Check if prn is of 10 digits
	def validate_prn():
		prn=input("\tEnter prn: ")
		if prn in sorted(studentDict.keys()):
			print("Ok")

			#check if prn is of 10 digits
			if len(prn)==10:
				student_inf['prn'] = prn
			else:
				print("\tInvalid prn")
				validate_prn()

		# check if dictionary is empty
		elif not studentDict:
			student_inf['prn'] = prn
			
		else:
			print("Student Already Exists!")
			
	#Check if email format is valid or not!
	def validate_email():
		email=input("\tEnter email: ")
		if email not in sorted(studentDict.keys()):
			if(re.search(email_validators,email)):   
				#re is a regular expression operator, using thsi email validation became easy
				student_inf['email'] = email
			else:
				print("\nInalid Mail:")
				validate_email()
		else:
			print("Student Already Exists!")


	while True:
		rollNo = input("\tEnter student rollNo:")
		sorted(studentDict.keys())
		if rollNo in studentDict.keys():
			print("Student number already exists!" )
			continue
		else:
			validate_prn()
			validate_phone()
			mandatory_name()
			validate_email()
			mandatory_city()
			mandatory_state()
			studentDict[rollNo]=student_inf
			break
		

def delete_student():
	rollNo=input("\tEnter the student rollNo number to be deleted:")
	if rollNo in studentDict.keys():
		del studentDict[rollNo]
		print("Student number [%s] student information has been deleted!" %(rollNo))
	else:
		print("Does not exist [%s] student number" %(rollNo))

#Search a particular student by it's rollNo
def query_student():
	rollNo = input("\tEnter the student rollNo number to be Searched:")
	if rollNo in studentDict.keys():
		print('rollNo:{:<20}'.format(rollNo)) 
		print('prn:{:<20}'.format(studentDict[rollNo]['prn']), end='')
		print('name:{:<20}'.format(studentDict[rollNo]['name']), end='')
		print('mobNo:{:<20}'.format(studentDict[rollNo]['mobNo']), end='')
		print('email:{:<20}'.format(studentDict[rollNo]['email']), end='')
		print('city:{:<20}'.format(studentDict[rollNo]['city']), end='')
		print('state:{:<20}'.format(studentDict[rollNo]['state']), end='')
	else:
		print("Does not exist [%s] student number" % (rollNo))

#function to Display a unsorted list		
def traverse_student():
	if len(studentDict):
		for rollNo in studentDict.keys():
			print('rollNo:{:<20}'.format(rollNo)) 
			print('name:{:<20}'.format(studentDict[rollNo]['name']), end='')
			print('mobNo:{:<20}'.format(studentDict[rollNo]['mobNo']), end='')
			print('email:{:<20}'.format(studentDict[rollNo]['email']), end='')
			print('city:{:<20}'.format(studentDict[rollNo]['city']), end='')
			print('state:{:<20}'.format(studentDict[rollNo]['state']), end='')
			print("\n")
	else:
		print('no record')

#function to Display a sorted list
def sortedList():
	for rollNo in sorted(studentDict.keys()):
		print('rollNo:{:<20}'.format(rollNo)) 
		print('prn:{:<20}'.format(studentDict[rollNo]['prn']), end='')
		print('name:{:<20}'.format(studentDict[rollNo]['name']), end='')
		print('mobNo:{:<20}'.format(studentDict[rollNo]['mobNo']), end='')
		print('email:{:<20}'.format(studentDict[rollNo]['email']), end='')
		print('city:{:<20}'.format(studentDict[rollNo]['city']), end='')
		print('state:{:<20}'.format(studentDict[rollNo]['state']), end='')
		print("\n")

'''
Above format tags are used just to give a tabuluar view by giving space (eg: {:<20})
'''


#Store each student object in the dictionary separately into a file
def write_file(**studentDict):
	with open('student.txt', 'w+') as fp:
		for key, value in studentDict.items():
			student_dict_tmp={}
			student_dict_tmp[key]=value
			fp.write(str(student_dict_tmp)+'\n')

#First read the file and store it in the studentDict dictionary
def read_file():
	student_dict_tmp = {}
	try:
		with open('student.txt', 'r+') as fp:
			for line in fp.readlines():
				line=line.strip()
				student_dict_tmp.update(eval(line))
		studentDict.update(student_dict_tmp)
	except IOError:
		print('no stock data')
read_file()

#Local DB
print("\n\nData Stored in Local Database:\n")
print(studentDict)
while True:
	print(menus)
	num = input("Please enter the menu number:")
	if num.isdigit():
		if int(num) not in range(0,7):
			print("Menu number input error, please re-enter!")
			continue
		else:
			if int(num)==1:
				inputData()
			elif int(num)==2:
				delete_student()
			elif int(num)==3:
				query_student()
			elif int(num)==4:
				traverse_student()
			elif int(num)==5:
				sortedList()
			elif int(num)==6:
				write_file(**studentDict)
				break
			elif int(num)==0:
				sys.exit()  #Reason to import sys
			else:
				print("Enter number error")
	else:
		print("Please enter a numeric menu number")


