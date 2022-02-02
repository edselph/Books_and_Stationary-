from tkinter import *
import tkinter.messagebox as msb
from typing import ValuesView
from src.myDB import getDb, getDbError

def m_stationary_table():
    win = Tk()
    win.title("")
    win.geometry('700x500+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'white')

    # Frame as container for entries.
    stationary_frame = Frame(win, bd = 5, height = 450, width = 450, bg = 'light gray')
    stationary_frame.place(x = 0, y = 50)

    item_ID_label = Label(stationary_frame, text = 'Item_ID', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    item_ID_entry = Entry(stationary_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    item_ID_label.place(x = 0, y = 0)
    item_ID_entry.place(x = 150, y = 0)

    item_Name_label = Label(stationary_frame, text = 'Item_Name', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    item_Name_entry = Entry(stationary_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    item_Name_label.place(x = 0, y = 0 + 50)
    item_Name_entry.place(x = 150, y = 0 + 50)

    price_label = Label(stationary_frame, text = 'Equipment_Price', font = ('Comic Sans', 15),
                                            fg = 'black', bg = 'light gray', justify = LEFT)
    price_entry = Entry(stationary_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                            fg = 'black', justify = LEFT,  width = 25)
    price_label.place(x = 0, y = 0 + (50 * 2))
    price_entry.place(x = 150, y = 0 + (50 * 2))

    stock_Num_label = Label(stationary_frame, text = 'stock_Num', font = ('Comic Sans', 15),
                                                    fg = 'black', bg = 'light gray', justify = LEFT)
    stock_Num_entry = Entry(stationary_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                    fg = 'black', justify = LEFT,  width = 25)
    stock_Num_label.place(x = 0, y = 0 + (50 * 3))
    stock_Num_entry.place(x = 150, y = 0 + (50 * 3))

    
    def validate_entries():
        global state
        if(item_ID_entry.get() == "" or item_Name_entry.get() == "" or price_entry.get() == "" or stock_Num_entry.get() == ""):
            state = False
        else:
            state = True
        return state
    
    def disable_foreign_keys():
        my_db = getDb()
        my_cursor = my_db.cursor()
        my_cursor.execute("SET GLOBAL FOREIGN_KEY_CHECKS = 0")
    
    def reactivate_foreign_keys():
        my_db = getDb()
        my_cursor = my_db.cursor()
        my_cursor.execute("SET GLOBAL FOREIGN_KEY_CHECKS = 1")

    def stationary_insert():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "INSERT INTO Stationary(Item_ID, Item_Name, Equipment_Price, Stock_Num) VALUES(%s, %s, %s, %s)"
            values = (item_ID_entry.get(), item_Name_entry.get(), price_entry.get(), stock_Num_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def stationary_update():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "UPDATE stationary SET Item_ID = %s, Item_Name = %s, Equipment_Price = %s, Stock_Num = %s WHERE Item_ID = %s"
            values = (item_ID_entry.get(), item_Name_entry.get(), price_entry.get(), stock_Num_entry.get(),item_ID_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def stationary_delete():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "DELETE FROM Stationary WHERE Item_ID = %s"
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
                             command = lambda: stationary_insert())
    insert_btn.place(x = 500, y = 220)

    # Button to update existing data in table referencing PK.
    update_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Update \n via stationary_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: stationary_update())
    update_btn.place(x = 500, y = 290)

    # Button to delete data from table referencing PK.
    delete_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Delete \n via stationary_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: stationary_delete())
    delete_btn.place(x = 500, y = 360)

    win.mainloop()
    return