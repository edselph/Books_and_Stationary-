from window1 import cursor, update, wrapper2, ttk

# Treeview for Customer
trv_Invoice = ttk.Treeview(wrapper2,columns=(1,2,3,4,5,6,7,8,9), show="headings", height=10)
trv_Invoice.pack()

trv_Invoice.heading(1, text="Invoice num")
trv_Invoice.heading(2, text="Invoice Date")
trv_Invoice.heading(3, text="Member ID")
trv_Invoice.heading(4, text="Employee ID")
trv_Invoice.heading(5, text="Equipment ID")
trv_Invoice.heading(6, text="Equipment Quantity")
trv_Invoice.heading(7, text="ISBN")
trv_Invoice.heading(8, text="Book Quantity")
trv_Invoice.heading(9, text="Total Price")


query_Invoice = "SELECT Invoice_Num, Invoice_Date, Member_ID , Employee_ID, Equipment_ID, Equipment_Quantity, ISBN, Book_Quantity, Total_Price FROM Invoice"
cursor.execute(query_Invoice)
rows_Invoice = cursor.fetchall()
update(rows_Invoice)
