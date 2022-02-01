from window1 import cursor, update,  wrapper2, ttk

# Treeview for Stats
trv_Stat = ttk.Treeview(wrapper2,columns=(1,2,3,4), show="headings", height=10)
trv_Stat.pack()

trv_Stat.heading(1, text="Item ID")
trv_Stat.heading(2, text="Item Name")
trv_Stat.heading(3, text="Price")
trv_Stat.heading(4, text="Stock Num")


query_Stat = "SELECT Item_ID, Item_Name, Equipment_Price , Stock_Num FROM Stationary"
cursor.execute(query_Stat)
rows_Stat = cursor.fetchall()
update(rows_Stat)
