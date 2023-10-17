"""
	Student API(application program interface)
"""
from Student import * #import all properties from Student file
from os import system

slist:list = []
filename:str = "student.csv" #comma-separated-variables

def header(message:str)->None:
	system("cls")
	print(message)
	print("---------------------")


	
def checkid(student: Student) -> bool:
    with open(filename, 'r') as file:
        for stud in file:
           # ID, last_name, first_name, course, level = stud.strip().split(',') 
		   # e ditso nalang ni ayaw na isulod ug variable ang tanan fields, ang need raman diri is ang ID so ato nalng e ditso
            if student.idno == stud.split(',')[0]: # ang 0 is ang IDno
                return True
    return False
	
def addStudent()->None:
	header("Add Student")
	idno:str = input("Enter IDNO :")
	lastname:str = input("Enter LASTNAME :")
	firstname:str = input("Enter FIRSTNAME :")
	course:str = input("Enter COURSE :")
	level:str = input("Enter LEVEL :")
	#call checkid for duplicate student entry
	if checkid(Student(idno,lastname,firstname,course,level)):
		print("Duplicate ID NO.")
	else:
		student = Student(idno,lastname,firstname,course,level)
		f = open(filename,"a")
		f.write(student.__str__())
		f.write("\n")
		f.close()
		print()
		print("New Student Added")
	
	
	
def findStudent()->None:
	header("Find Student")
	idNum = input("Enter id num to find: ")
	#counter:int = 0
	found:bool = False

	with open(filename, 'r') as file:
		for stud in file:
			ID, last_name, first_name, course, level = stud.strip().split(',')

			if idNum == ID:
				foundStudent = Student(ID,last_name,first_name,course,level)
				print("Student found!")
				print(foundStudent.__str__())
				#counter = 1
				found = True
				break
		if found != True:
			print("Student not found!")

def deleteStudent()->None:
	header("Delete Student")
	idNum = input("Enter id num to find: ")

	with open(filename, 'r') as file:
		for stud in file:
			ID, last_name, first_name, course, level = stud.strip().split(',')

			if idNum == ID:
				foundStudent = Student(ID,last_name,first_name,course,level)
				print("Student found!")
				
				confirm = input("Do You Really Really Want To Delete This Student?: ")
				if confirm == 'Y' or confirm =='y':
					foundStudent

				print(foundStudent.__str__())
				found = True
				break

		if found != True:
			print("Student not found!")



def updateStudent()->None:
	header("Update Student")
	idNum = input("Enter id num to Update: ")
	studentL: list = []
	found = False
	with open(filename, 'r') as file:

		studentL = list(file)
		for i,stud in enumerate(studentL):
			ID, last_name, first_name, course, level = stud.strip().split(',')

			if idNum == ID:
				foundStudent = Student(ID, last_name, first_name, course, level)
				print("Student found!")
				print(foundStudent.__str__())
				print("Update!")
				last: str = input("Enter New LASTNAME")
				first: str = input("Enter New FIRSTNAME")
				c: str = input("Enter New COURSE")
				l: str = input("Enter New LEVEL")
				newStudent = Student(foundStudent.idno,last,first,c,l)
				studentL[i]= newStudent.__str__()
				found = True
	if found:
		with open(filename, 'w+') as writer:
			writer.write(''.join(studentL))
		print("Student updated.")
	else:
		print("Student not found.")

def displayAllStudent()->None:
	header("Display All Student")
	#must check if file to be opened is existing
	f = open(filename)
	slist = f.readlines()
	f.close()
	for s in slist:
		print(s,end="")
	print("---------------------------")
	print("Nothing follows")
	
def quit()->None:
	header("Program Terminated")

def studentList()->list:
	f = open(filename)
	studList = f.readlines()

	return studList
