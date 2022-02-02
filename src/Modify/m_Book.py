from tkinter import *
import tkinter.messagebox as msb
from typing import ValuesView
from src.myDB import getDb, getDbError

def m_Book_table():
    win = Tk()
    win.title("")
    win.geometry('700x500+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'white')

    # Frame as container for entries.
    book_frame = Frame(win, bd = 5, height = 450, width = 450, bg = 'light gray')
    book_frame.place(x = 0, y = 50)

    item_ID_label = Label(book_frame, text = 'Item_ID', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    item_ID_entry = Entry(book_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    item_ID_label.place(x = 0, y = 0)
    item_ID_entry.place(x = 150, y = 0)

    isbn_label = Label(book_frame, text = 'ISBN', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    isbn_entry = Entry(book_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    isbn_label.place(x = 0, y = 0 + 50)
    isbn_entry.place(x = 150, y = 0 + 50)

    author_label = Label(book_frame, text = 'Author', font = ('Comic Sans', 15),
                                            fg = 'black', bg = 'light gray', justify = LEFT)
    author_entry = Entry(book_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                            fg = 'black', justify = LEFT,  width = 25)
    author_label.place(x = 0, y = 0 + (50 * 2))
    author_entry.place(x = 150, y = 0 + (50 * 2))

    item_name_label = Label(book_frame, text = 'Item Name', font = ('Comic Sans', 15),
                                                    fg = 'black', bg = 'light gray', justify = LEFT)
    item_name_entry = Entry(book_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                    fg = 'black', justify = LEFT,  width = 25)
    item_name_label.place(x = 0, y = 0 + (50 * 3))
    item_name_entry.place(x = 150, y = 0 + (50 * 3))

    book_price_label = Label(book_frame, text = 'Book Price', font = ('Comic Sans', 15),
                                                 fg = 'black', bg = 'light gray', justify = LEFT)
    book_price_entry = Entry(book_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                 fg = 'black', justify = LEFT,  width = 25)
    book_price_label.place(x = 0, y = 0 + (50 * 4))
    book_price_entry.place(x = 150, y = 0 + (50 * 4))

    stock_Num_label = Label(book_frame, text = 'Stock_Num', font = ('Comic Sans', 15),
                                                 fg = 'black', bg = 'light gray', justify = LEFT)
    stock_Num_entry = Entry(book_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                 fg = 'black', justify = LEFT,  width = 25)
    stock_Num_label.place(x = 0, y = 0 + (50 * 5))
    stock_Num_entry.place(x = 150, y = 0 + (50 * 5))  
    
    def validate_entries():
        global state
        if(item_ID_entry.get() == "" or isbn_entry.get() == "" or author_entry.get() == "" or item_name_entry.get() == "" or book_price_entry.get() == "" or stock_Num_entry.get() == ""):
            state = False
        else:
            state =True
        return state
    
    def disable_foreign_keys():
        my_db = getDb()
        my_cursor = my_db.cursor()
        my_cursor.execute("SET GLOBAL FOREIGN_KEY_CHECKS = 0")
    
    def reactivate_foreign_keys():
        my_db = getDb()
        my_cursor = my_db.cursor()
        my_cursor.execute("SET GLOBAL FOREIGN_KEY_CHECKS = 1")

    def book_insert():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "INSERT INTO Book(Item_ID, ISBN, Author, Item_Name, Book_Price, Stock_Num) VALUES(%s, %s, %s, %s, %s, %s)"
            values = (item_ID_entry.get(), isbn_entry.get(), author_entry.get(), item_name_entry.get(), book_price_entry.get(), stock_Num_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def book_update():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "UPDATE Employee SET Item_ID = %s, ISBN = %s, Author = %s, Item_Name = %s, Book_Price = %s, Stock_Num = %s WHERE Item_ID = %s"
            values = (item_ID_entry.get(), isbn_entry.get(), author_entry.get(), item_name_entry.get(), book_price_entry.get(), stock_Num_entry.get(),item_ID_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def book_delete():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "DELETE FROM Book WHERE Item_ID = %s"
            values = (item_ID_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()


    # Button to insert data into table.
    insert_btn = Button(win, justify = CENTER, width = 15, height = 2, bg = 'black', fg = 'light gray', text = 'Insert \n to table',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: book_insert())
    insert_btn.place(x = 500, y = 220)

    # Button to update existing data in table referencing PK.
    update_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Update \n via Employee_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: book_update())
    update_btn.place(x = 500, y = 290)

    # Button to delete data from table referencing PK.
    delete_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Delete \n via Employee_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: book_delete())
    delete_btn.place(x = 500, y = 360)

    win.mainloop()
    return