from window1 import cursor, update, rows_Emp, wrapper2, ttk

# Treeview for Stats
trv_Books = ttk.Treeview(wrapper2,columns=(1,2,3,4,5,6), show="headings", height=10)
trv_Books.pack()

trv_Books.heading(1, text="Item ID")
trv_Books.heading(2, text="ISBN")
trv_Books.heading(3, text="Author")
trv_Books.heading(4, text="Item Name")
trv_Books.heading(5, text="Book Price")
trv_Books.heading(6, text="Stock Num")


query_Cus = "SELECT Item_ID, ISBN, Author , Item_Name, Book_Price, Stock_Num FROM Book"
cursor.execute(query_Cus)
rows_Cus = cursor.fetchall()
update(rows_Emp,rows_Cus)
