from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Style
from tkinter.ttk import Scrollbar

from src.myDB import getDb, getDbError

def v_stationary_table():
    win = Tk()
    win.title("Stationary Table")
    win.geometry("1080x500")                         
    win.resizable(height = False, width = False)        # Disable resizing.

    # Retrieve all rows and keep them in cursor.
    myDb = getDb()
    myCursor = myDb.cursor()
    myCursor.execute("SELECT * FROM Stationary")

    tree = Treeview(win, height = 25)

    # Omit the first empty column.
    tree["show"] = "headings"

   # Style the treeview columns and rows.
    style = Style(win)
    style.theme_use("clam")                                                                             # Table style.
    style.configure("Treeview.Heading", font = ("Times New Roman", 12, "bold"), foreground = "blue")    # Heading(columns)
    style.configure(".", font = ("Times New Roman", 12))                                                # Rows

    # Define the columns.
    tree["columns"] = ("Item_ID", "Item_Name","Equipment_Price" , "Stock_Num")

    # Assign column width, min-width attributes & align column names to center.
    tree.column("Item_ID", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Item_Name", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Equipment_Price", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Stock_Num", width = 150, minwidth = 150, anchor = CENTER)

    # Assign column heading names.
    tree.heading("Item_ID", text = "Item ID", anchor = CENTER)
    tree.heading("Item_Name", text = "Item Name ", anchor = CENTER)
    tree.heading("Equipment_Price", text = "Equipment Price", anchor = CENTER)
    tree.heading("Stock_Num", text = "Stock Num ", anchor = CENTER)

    # Iterate through and insert rows from the 'teacher' table in database into treeview.
    # start variable tells how many rows available in treeview.
    start = 0
    for row in myCursor:
        tree.insert("", start, text = "", values = (row[0], row[1], row[2], row[3]))
        start = start + 1
    
    # Vertical scrollbar for treeview.
    vsb = Scrollbar(win, orient = "vertical")
    vsb.configure(command = tree.yview)

    # Add the vertical scrollbar to the right of treeview.
    tree.configure(yscrollcommand = vsb.set)
    vsb.pack(fill = Y, side = RIGHT)

    # Display treeview(table) at center & top positions.
    tree.place(x = 0, y = 0)

    win.mainloop()
    return