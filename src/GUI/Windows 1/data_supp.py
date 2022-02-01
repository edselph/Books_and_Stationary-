from window1 import cursor, update, wrapper2, ttk

# Treeview for Customer
trv_supp = ttk.Treeview(wrapper2,columns=(1,2,3,4,5,6,7), show="headings", height=10)
trv_supp.pack()

trv_supp.heading(1, text="Supply num")
trv_supp.heading(2, text="Company Name")
trv_supp.heading(3, text="Phone Num")
trv_supp.heading(4, text="Item Name")
trv_supp.heading(5, text="Item Quantity")
trv_supp.heading(6, text="Item Price")
trv_supp.heading(7, text="Total Payment")

query_supp = "SELECT Item_ID, Company_Name, Phone_Num , Item_Name, Item_Quantity, Item_Price, Total_Payment FROM Supplier"
cursor.execute(query_supp)
rows_supp = cursor.fetchall()
update(rows_supp)
