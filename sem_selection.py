import mysql.connector
from tkinter import *
from tkinter import messagebox
from login import *


mydb= mysql.connector.connect(host="localhost",\
	user="root",
	password="",
	database="student_report")
cur = mydb.cursor()

def sem1():
	Frame=Tk()
	#master.destroy()
	Frame.title("Marks Details")
	Frame.geometry("500x500")
	sap=sap_txt.get()
	user=user_txt.get()

	if (sap == "" and user == "") :
		messagebox.showinfo('Warning','Enter valid data')
	elif (sap == "") :
		messagebox.showinfo('Warning','Please enter valid SAP ID')
	elif (user == "") :
		messagebox.showinfo('Warning','Please enter valid Name')

	
	
	sql1 = "SELECT * from sem1details limit 0,1"
	cur.execute(sql1)
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=20, fg='red')
			e.grid(row=i, column=j)
			e.insert(END, student_report[j])
		i=i+1

	
	sql = "SELECT * from sem1details where SAP_ID= %s and NAME= %s"

	cur.execute(sql,[(sap),(user)])
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=20, fg='blue')
			e.grid(row=i+1, column=j)
			e.insert(END, student_report[j])
		i=i+1

	sql2="SELECT  MAX(PERCENTAGE)  FROM sem1details WHERE PERCENTAGE < (SELECT MAX(PERCENTAGE) FROM sem1details); "
	cur.execute(sql2)
	#max_lbl=Label(Frame,text="Maximum Percentage scored in Sem 1 is:").grid(row=10,column=1)
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=60, fg='blue')
			e.place(x=320,y=240)
			e.insert(END,'Maximum Percentage Of Sem 1 is   :     ')
			e.insert(END,student_report[j])
		i=i+1

	sql3="SELECT  MIN(PERCENTAGE)  FROM sem1details "
	cur.execute(sql3)
	#max_lbl=Label(Frame,text="Maximum Percentage scored in Sem 1 is:").grid(row=10,column=1)
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=60, fg='blue')
			e.place(x=320,y=280)
			e.insert(END,'Minimum Percentage Of Sem 1 is   :     ')
			e.insert(END,student_report[j])
		i=i+1


	Frame.mainloop()


def sem2():
	Frame=Tk()
	#master.destroy()
	Frame.title("Marks Details")
	Frame.geometry("500x500")
	sap=sap_txt.get()
	user=user_txt.get()

	if (sap == "" and user == "") :
		messagebox.showinfo('Warning','Enter valid data')
	elif (sap == "") :
		messagebox.showinfo('Warning','Please enter valid SAP ID')
	elif (user == "") :
		messagebox.showinfo('Warning','Please enter valid Name')

	
	
	sql1 = "SELECT * from sem2details limit 0,1"
	cur.execute(sql1)
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=20, fg='red')
			e.grid(row=i, column=j)
			e.insert(END, student_report[j])
		i=i+1

	
	sql = "SELECT * from sem2details where SAP_ID= %s and NAME= %s"

	cur.execute(sql,[(sap),(user)])
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=20, fg='blue')
			e.grid(row=i+1, column=j)
			e.insert(END, student_report[j])
		i=i+1

	sql2="SELECT  MAX(PERCENTAGE)  FROM sem2details WHERE PERCENTAGE < (SELECT MAX(PERCENTAGE) FROM sem2details); "
	cur.execute(sql2)
	
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=60, fg='blue')
			e.place(x=320,y=240)
			e.insert(END,'Maximum Percentage Of Sem 2 is   :     ')
			e.insert(END,student_report[j])
		i=i+1

	sql3="SELECT  MIN(PERCENTAGE)  FROM sem2details "
	cur.execute(sql3)
	
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=60, fg='blue')
			e.place(x=320,y=280)
			e.insert(END,'Minimum Percentage Of Sem 2 is   :     ')
			e.insert(END,student_report[j])
		i=i+1


	Frame.mainloop()		



def sem3():
	Frame=Tk()
	#master.destroy()
	Frame.title("Marks Details")
	Frame.geometry("500x500")
	sap=sap_txt.get()
	user=user_txt.get()

	if (sap == "" and user == "") :
		messagebox.showinfo('Warning','Enter valid data')
	elif (sap == "") :
		messagebox.showinfo('Warning','Please enter valid SAP ID')
	elif (user == "") :
		messagebox.showinfo('Warning','Please enter valid Name')

	
	
	sql1 = "SELECT * from sem3details limit 0,1"
	cur.execute(sql1)
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=20, fg='red')
			e.grid(row=i, column=j)
			e.insert(END, student_report[j])
		i=i+1

	
	sql = "SELECT * from sem3details where SAP_ID= %s and NAME= %s"

	cur.execute(sql,[(sap),(user)])
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=20, fg='blue')
			e.grid(row=i+1, column=j)
			e.insert(END, student_report[j])
		i=i+1

	sql2="SELECT  MAX(PERCENTAGE)  FROM sem3details WHERE PERCENTAGE < (SELECT MAX(PERCENTAGE) FROM sem3details); "
	cur.execute(sql2)
	#max_lbl=Label(Frame,text="Maximum Percentage scored in Sem 1 is:").grid(row=10,column=1)
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=60, fg='blue')
			e.place(x=320,y=240)
			e.insert(END,'Maximum Percentage Of Sem 3 is   :     ')
			e.insert(END,student_report[j])
		i=i+1

	sql3="SELECT  MIN(PERCENTAGE)  FROM sem3details "
	cur.execute(sql3)
	#max_lbl=Label(Frame,text="Maximum Percentage scored in Sem 1 is:").grid(row=10,column=1)
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=60, fg='blue')
			e.place(x=320,y=280)
			e.insert(END,'Minimum Percentage Of Sem 3 is   :     ')
			e.insert(END,student_report[j])
		i=i+1


	


	Frame.mainloop()	





master=Tk()
master.title("Sem Selection")
master.geometry("500x500")
sap_lbl=Label(master,text="Enter SAP ID:").pack(anchor=W)
sap_txt=Entry(master)
sap_txt.pack(anchor=W)
user_lbl=Label(master,text="Enter NAME:").pack(anchor=W)
user_txt=Entry(master)
user_txt.pack(anchor=W)
sem1 =Radiobutton(master, text='Sem 1',command=sem1)
sem1.pack(anchor=W)
sem2=Radiobutton(master, text='Sem 2',command=sem2)	
sem2.pack(anchor=W)
sem3=Radiobutton(master, text='Sem 3',command=sem3)
sem3.pack(anchor=W)
master.mainloop()


