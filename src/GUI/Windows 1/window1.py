import tkinter as tk
from tkinter import *
from tkinter import ttk
from Db_B_n_S import getdb , geterror
from data_Cus import * 

#Connect to database
db = getdb()
cursor = db.cursor()

# code for getting the data from database
def update(rows_Emp,rows_Cus):
    for i in rows_Emp, rows_Cus:
        trv_employee.insert('', 'end', values=i)

# Main window 
root = Tk()

wrapper1 = LabelFrame(root,width=100, height=100, text="Table list")
wrapper2 = LabelFrame(root,width=700, height=300, text="Table content")
wrapper3 = LabelFrame(root,width=700, height=300, text="Change Data")

wrapper1.pack(side="left", fill="both", expand=True, padx= 10, pady=30)
wrapper2.pack(side="right", fill="both", expand=True, padx= 50, pady=30)
wrapper3.pack(side="bottom", fill="both", expand=True, padx= 50, pady=30)

# Treeview for EmployeeD
trv_employee = ttk.Treeview(wrapper2,columns=(1,2,3,4,5,6,7,8), show="headings", height=10)
trv_employee.pack()

trv_employee.heading(1, text="ID")
trv_employee.heading(2, text="First Name")
trv_employee.heading(3, text="Last Name")
trv_employee.heading(4, text="Gender")
trv_employee.heading(5, text="DoB")
trv_employee.heading(6, text="Phone Number")
trv_employee.heading(7, text="Email")
trv_employee.heading(8, text="Salary")

query_Emp = "SELECT Employee_ID, Fname, Lname, Sex, Date_Of_Birth, Phone_num, Email, Salary FROM Employee"
cursor.execute(query_Emp)
rows_Emp = cursor.fetchall()




#button (command=update(rows_Emp,rows_Cus),)
btn_Emp = Button(wrapper1, text="Employee",  fg="black", bg="light green")
btn_Emp.place(height=35, width=50)
btn_Emp.pack()

btn_Cus = Button(wrapper1, text="Customer",  fg="black", bg="light green")
btn_Cus.place(height=35, width=50)
btn_Cus.pack()

btn_Inv = Button(wrapper1, text="Invoice",  fg="black", bg="light green")
btn_Inv.place(height=35, width=50)
btn_Inv.pack()

btn_Book = Button(wrapper1, text="Book",  fg="black", bg="light green")
btn_Book.place(height=35, width=50)
btn_Book.pack()

btn_Sta = Button(wrapper1, text="Stationary",  fg="black", bg="light green")
btn_Sta.place(height=35, width=50)
btn_Sta.pack()

btn_Supp = Button(wrapper1, text="Supplier",  fg="black", bg="light green")
btn_Supp.place(height=35, width=50)
btn_Supp.pack()


# button for edit 
btn_edit = Button(wrapper1, text="Edit",  fg="black", bg="light green")
btn_edit.pack()

root.title("Books and Stationary")
root.geometry("800x600")
root.mainloop()