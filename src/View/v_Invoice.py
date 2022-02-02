from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Style
from tkinter.ttk import Scrollbar

from src.myDB import getDb, getDbError

def v_invoice_table():
    win = Tk()
    win.title("Invoice Table")
    win.geometry("1080x500")                         
    win.resizable(height = False, width = False)        # Disable resizing.

    # Retrieve all rows and keep them in cursor.
    myDb = getDb()
    myCursor = myDb.cursor()
    myCursor.execute("SELECT * FROM Invoice")

    tree = Treeview(win, height = 25)

    # Omit the first empty column.
    tree["show"] = "headings"

   # Style the treeview columns and rows.
    style = Style(win)
    style.theme_use("clam")                                                                             # Table style.
    style.configure("Treeview.Heading", font = ("Times New Roman", 12, "bold"), foreground = "blue")    # Heading(columns)
    style.configure(".", font = ("Times New Roman", 12))                                                # Rows

    # Define the columns.
    tree["columns"] = ("Invoice_Num", "Invoice_Date","Member_ID" , "Employee_ID", "Equipment_ID", "Equipment_Quantity"
    , "ISBN", "Book_Quantity","Total_Price")

    # Assign column width, min-width attributes & align column names to center.
    tree.column("Invoice_Num", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Invoice_Date", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Member_ID", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Employee_ID", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Equipment_ID", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Equipment_Quantity", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("ISBN", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Book_Quantity", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Total_Price", width = 150, minwidth = 150, anchor = CENTER)

    # Assign column heading names.
    tree.heading("Invoice_Num", text = "Invoice Num ", anchor = CENTER)
    tree.heading("Invoice_Date", text = "Invoice Date ", anchor = CENTER)
    tree.heading("Member_ID", text = "Member ID", anchor = CENTER)
    tree.heading("Employee_ID", text = "Employee ID", anchor = CENTER)
    tree.heading("Equipment_ID", text = "Equipment ID", anchor = CENTER)
    tree.heading("Equipment_Quantity", text = "Equipment Quantity", anchor = CENTER)
    tree.heading("ISBN", text = "ISBN", anchor = CENTER)
    tree.heading("Book_Quantity", text = "Book Quantity", anchor = CENTER)
    tree.heading("Total_Price", text = "Total Price", anchor = CENTER)

    # Iterate through and insert rows from the 'teacher' table in database into treeview.
    # start variable tells how many rows available in treeview.
    start = 0
    for row in myCursor:
        tree.insert("", start, text = "", values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6],row[7],row[8]))
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