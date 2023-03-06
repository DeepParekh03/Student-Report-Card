import mysql.connector
from tkinter import *
from tkinter import messagebox
#from homepage import *
#from sem_selection import *



mydb= mysql.connector.connect(host="localhost",user="root",password="",database="student_report")
cur = mydb.cursor()  
def Ok():
 user_verification = username_entry.get()
 pass_verification = password_entry.get()
 if (user_verification == "" and pass_verification == "") :
        messagebox.showinfo('Warning','Enter valid data')
 elif (user_verification == "") :
        messagebox.showinfo('Warning','Please enter username')
 elif (pass_verification == "") :
        messagebox.showinfo('Warning','Please enter password')

 sql = "select * from login where username = %s and password = %s"
 cur.execute(sql,[(user_verification),(pass_verification)])
 results = cur.fetchall()#This will fetch the values of table from the database
 if results:#Boolean its checks whether the result is true or no if true then it will execute 
 	for i in results:
         messagebox.showinfo('Success','Login Success')
         master.destroy()
         
         break
 		 
 else:
 	messagebox.showinfo('Unsuccessful','Login Unsuccessful')




def reset():
	username_entry.delete(0,END)
	password_entry.delete(0,END)

master=Tk()
master.title("Login Form")
l1=Label(master,text="Enter your username: ")
l1.grid(row=0,column=0)
username_entry=Entry(master)
username_entry.grid(row=0,column=1)
l2=Label(master,text="Enter Password: ")
l2.grid(row=1,column=0)
password_entry=Entry(master)
password_entry.grid(row=1,column=1)
okBtn=Button(master,text="Login",command=Ok)
okBtn.grid(row=2,column=0)
resetBtn=Button(master,text="Reset",command=reset)
resetBtn.grid(row=2,column=1)
master.mainloop()
        
