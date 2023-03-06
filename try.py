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
	a=0
	for student_report in cur:
		for b in range(len(student_report)):
			e = Entry(Frame, width=20, fg='red')
			e.place(x=20,y=20)
			e.insert(END, student_report[b])
		a=a+1

	
	sql = "SELECT * from sem1details where SAP_ID= %s and NAME= %s"

	cur.execute(sql,[(sap),(user)])
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=20, fg='blue')
			e.place(x=20,y=21)
			e.insert(END, student_report[j])
		i=i+1

	sql2="SELECT  MAX(PERCENTAGE)  FROM sem1details WHERE PERCENTAGE < (SELECT MAX(PERCENTAGE) FROM sem1details); "
	cur.execute(sql2)
	#max_lbl=Label(Frame,text="Maximum Percentage scored in Sem 1 is:").pack(row=10,column=1)
	c=0
	for student_report in cur:
		for d in range(len(student_report)):
			e = Entry(Frame, width=20, fg='blue')
			e.place(x=20,y=22)
			e.insert(END,'Maximum Percentage  :     ')
			e.insert(END,student_report[d])
		c=c+1



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
	a=0
	for student_report in cur:
		for b in range(len(student_report)):
			e = Entry(Frame, width=10, fg='red')
			e.pack()
			e.insert(END, student_report[b])
		a=a+1

	
	sql = "SELECT * from sem2details where SAP_ID= %s and NAME= %s"

	cur.execute(sql,[(sap),(user)])
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=10, fg='blue')
			e.pack()
			e.insert(END, student_report[j])
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
	a=0
	for student_report in cur:
		for b in range(len(student_report)):
			e = Entry(Frame, width=10, fg='red')
			e.pack()
			e.insert(END, student_report[b])
		a=a+1

	
	sql = "SELECT * from sem3details where SAP_ID= %s and NAME= %s"

	cur.execute(sql,[(sap),(user)])
	i=0
	for student_report in cur:
		for j in range(len(student_report)):
			e = Entry(Frame, width=10, fg='blue')
			e.pack()
			e.insert(END, student_report[j])
		i=i+1
	Frame.mainloop()	



Label


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

