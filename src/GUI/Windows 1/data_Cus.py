from window1 import cursor, update, rows_Emp, wrapper2, ttk

# Treeview for Customer
trv_customer = ttk.Treeview(wrapper2,columns=(1,2,3,4,5,6,7), show="headings", height=10)
trv_customer.pack()

trv_customer.heading(1, text="ID")
trv_customer.heading(2, text="First Name")
trv_customer.heading(3, text="Last Name")
trv_customer.heading(4, text="Gender")
trv_customer.heading(5, text="DoB")
trv_customer.heading(6, text="Phone Number")
trv_customer.heading(7, text="Email")

query_Cus = "SELECT Member_ID, Fname, Lname , Sex, Date_Of_Birth, Phone_num, Email FROM Customer"
cursor.execute(query_Cus)
rows_Cus = cursor.fetchall()
update(rows_Emp,rows_Cus)
