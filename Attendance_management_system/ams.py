import sys
import os

stud_rollNo = []
def inputData():
	noStu = int(input("Enter the number of students: "))
	for i in range(1,noStu+1):
			stud_rollNo.append(i)
			mark = input("\n\tRoll Number :{} \n\tEnter P or p if present \n\t and A or a if abset: ".format(i))
			if mark == 'p' or mark == 'P':
				with open("present.txt",'a') as pFile:
					pFile.write('\t{}'.format(i))
			elif mark == 'a' or mark == 'A':
				with open("absent.txt",'a') as aFile:
					aFile.write('\t{}'.format(i))
			else:
				displayData()

def displayData():
	print("\tPresent Students are: ")
	with open("present.txt",'r+') as pFile:
		print(pFile.read())
	print("\n\tAbsent Students are: ")
	with open("absent.txt",'r+') as aFile:
		print(aFile.read())

x = int(input("\t Enter [0] to exit() and \t[1] to mark the attendees \t[2]: See attendance list\n"))
while x!=0:
	if x==0:
		sys.exit()
	elif x == 1:
		inputData()
	elif x == 2:
		file_size_1 = os.stat('present.txt').st_size
		file_size_2 = os.stat('absent.txt').st_size

		if file_size_1 == 0 and file_size_2 == 0:
			print("\tNo students marked")
		else:
			print("Roll Numbers of Present Student:\n")
			file = open("present.txt",'r+')
			for line in file.readlines(): print(line)
			print("\nRoll Numbers of Absent Student:\n")
			file2 = open("absent.txt",'r+')
			for line2 in file2.readlines(): print(line2)
		
		sys.exit()

	else:
		print("\tInvalid Input")
		sys.exit()
	x = int(input("\t Enter [0] to exit() and \t[1] to mark the attendees \t[2]: See attendance list\n"))


