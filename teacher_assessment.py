class Student:
	def __init__(self):
		print()
		print()
		print("Enter the name of the student:")
		self.name=input()
		print("Enter the id of the student:")
		self.s_id=int(input())
		
	def getDetails(self):
		print()
		print("Name:",self.name)
		print("id:",self.s_id)
class Student_marks(Student):
	
	def __init__(self):
		self.total=0
		self.percentage=0
		self.ma=0
		self.mi=0
		super().__init__()	
		print("Enter the Roll No. of the Student:")
		self.roll_no=int(input())

		print("Enter the semester of the Student of which you want marks(available upto 4 semester):")
		self.sem=int(input()) 
		print("Enter the marks for each subject of Semester(out of 100)")
	def setter(self):
		
		if(self.sem==1):
			
			print("Enter the marks for C Programming:")
			cprog=int(input())
			print("Enter the marks for Engineering Graphics:")
			eg=int(input())
			print("Enter the marks for Basic Electronics:")
			be=int(input())
			print("Enter the marks for Coummunication Skill:")
			cs=int(input())
			print("Enter the marks for Engineering Mathematics:")
			em=int(input())
			self.total=cprog+eg+be+em+cs
			self.mi=min(cprog,eg,be,cs,em)
			self.ma=max(cprog,eg,be,cs,em)
			self.percentage=(float(self.total)/500)*100
			
		elif(self.sem==2):
			print("Enter the marks for C++ Programming:")
			cpp=int(input())
			print("Enter the marks for Physics:")
			phy=int(input())
			print("Enter the marks for Digital Electronics:")
			de=int(input())
			print("Enter the marks for Website Development:")
			wsd=int(input())
			print("Enter the marks for Applied Mathematics:")
			amt=int(input())
			self.total=cpp+phy+de+wsd+amt
			self.mi=min(cpp,phy,de,wsd,amt)
			self.ma=max(cpp,phy,de,wsd,amt)
			
			self.percentage=(float(self.total)/500)*100
			
		elif(self.sem==3):
			print("Enter the marks for Programming in Java:")
			java=int(input())
			print("Enter the marks for Data Base Management System(DBMS):")
			dbms=int(input())
			print("Enter the marks for Data Structures:")
			ds=int(input())
			print("Enter the marks for Computer Graphics:")
			cg=int(input())
			print("Enter the marks for Data Coummunication and Network:")
			dcn=int(input())
			self.total=java+dbms+ds+cg+dcn
			self.mi=min(java,dbms,ds,cg,dcn)
			self.ma=max(java,dbms,ds,cg,dcn)
	
			self.percentage=(float(self.total)/500)*100
		
		elif(self.sem==4):
			print("Enter the marks for Programming in Python:")
			py=int(input())
			print("Enter the marks for Fundatmentals of Operating System(FOS):")
			fos=int(input())
			print("Enter the marks for Software Engineering:")
			se=int(input())
			print("Enter the marks for Object Oriented Modelling and Design(OOMD):")
			oomd=int(input())
			print("Enter the marks for Data Warehousing and Management(DWM):")
			dwm=int(input())
			self.total=py+fos+se+oomd+dwm
			self.mi=min(py,fos,se,oomd,dwm)
			self.ma=max(py,fos,se,oomd,dwm)
			
			self.percentage=(float(self.total)/500)*100
		



		else:
			print("Invalid choice")

	def getter(self):
		
		print("Roll No:",self.roll_no)
		print("Semester=",self.sem)
		print("Total=",self.total)
		print("Percentage=",self.percentage)
		print("Minimum Marks=",self.mi)
		print("Maximum Marks=",self.ma)



print()
print()
print("'!!!TEACHERS ASSESMENT PROJECT!!!'")
print()
print()
s1=[]
print("Enter for how many students you want to calculate the marks:")
n=int(input())
for i in range(n):
	s1=Student_marks()
	s1.setter()
	s1.getDetails()
	s1.getter()
	
	
