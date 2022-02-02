from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Style
from tkinter.ttk import Scrollbar

from src.myDB import getDb, getDbError

def v_book_table():
    win = Tk()
    win.title("Book Table")
    win.geometry("1080x500")                         
    win.resizable(height = False, width = False)        

    myDb = getDb()
    myCursor = myDb.cursor()
    myCursor.execute("SELECT * FROM Book")

    tree = Treeview(win, height = 25)

    tree["show"] = "headings"

    style = Style(win)
    style.theme_use("clam")                                                                             
    style.configure("Treeview.Heading", font = ("Times New Roman", 12, "bold"), foreground = "blue")    
    style.configure(".", font = ("Times New Roman", 12))                                                

    tree["columns"] = ("Item_ID", "ISBN", "Author", "Item_Name", "Book_Price", "Stock_Num")

    tree.column("Item_ID", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("ISBN", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Author", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Item_Name", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Book_Price", width = 150, minwidth = 150, anchor = CENTER)
    tree.column("Stock_Num", width = 150, minwidth = 150, anchor = CENTER)

    tree.heading("Item_ID", text = "Item ID", anchor = CENTER)
    tree.heading("ISBN", text = "ISBN", anchor = CENTER)
    tree.heading("Author", text = "Author", anchor = CENTER)
    tree.heading("Item_Name", text = "Item Name", anchor = CENTER)
    tree.heading("Book_Price", text = "Book Price", anchor = CENTER)
    tree.heading("Stock_Num", text = "Stock Num", anchor = CENTER)


    start = 0
    for row in myCursor:
        tree.insert("", start, text = "", values = (row[0], row[1], row[2], row[3], row[4], row[5]))
        start = start + 1
    
    vsb = Scrollbar(win, orient = "vertical")
    vsb.configure(command = tree.yview)

    tree.configure(yscrollcommand = vsb.set)
    vsb.pack(fill = Y, side = RIGHT)

    tree.place(x = 0, y = 0)

    win.mainloop()
    return