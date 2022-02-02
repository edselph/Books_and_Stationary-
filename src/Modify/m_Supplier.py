from tkinter import *
import tkinter.messagebox as msb
from typing import ValuesView
from src.myDB import getDb, getDbError

def m_supplier_table():
    win = Tk()
    win.title("")
    win.geometry('700x500+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'white')

    # Frame as container for entries.
    supplier_frame = Frame(win, bd = 5, height = 450, width = 450, bg = 'light gray')
    supplier_frame.place(x = 0, y = 50)

    item_ID_label = Label(supplier_frame, text = 'Item_ID', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    item_ID_entry = Entry(supplier_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    item_ID_label.place(x = 0, y = 0)
    item_ID_entry.place(x = 150, y = 0)

    company_Name_label = Label(supplier_frame, text = 'Company_Name', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    company_Name_entry = Entry(supplier_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    company_Name_label.place(x = 0, y = 0 + 50)
    company_Name_entry.place(x = 150, y = 0 + 50)

    phone_Num_label = Label(supplier_frame, text = 'Phone_Num', font = ('Comic Sans', 15),
                                            fg = 'black', bg = 'light gray', justify = LEFT)
    phone_Num_entry = Entry(supplier_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                            fg = 'black', justify = LEFT,  width = 25)
    phone_Num_label.place(x = 0, y = 0 + (50 * 2))
    phone_Num_entry.place(x = 150, y = 0 + (50 * 2))

    item_Name_label = Label(supplier_frame, text = 'Item_Name', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    item_Name_entry = Entry(supplier_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    item_Name_label.place(x = 0, y = 0 + (50 * 3))
    item_Name_entry.place(x = 150, y = 0 + (50 * 3))

    item_Quantity_label = Label(supplier_frame, text = 'Item_Quantity', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    item_Quantity_entry = Entry(supplier_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    item_Quantity_label.place(x = 0, y = 0 + (50 * 4))
    item_Quantity_entry.place(x = 150, y = 0 + (50 * 4))

    item_Price_label = Label(supplier_frame, text = 'Item_Price', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    item_Price_entry = Entry(supplier_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    item_Price_label.place(x = 0, y = 0 + (50 * 5))
    item_Price_entry.place(x = 150, y = 0 + (50 * 5))
    
    total_Payment_label = Label(supplier_frame, text = 'Total Payment', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    total_Payment_entry = Entry(supplier_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    total_Payment_label.place(x = 0, y = 0 + (50 * 6))
    total_Payment_entry.place(x = 150, y = 0 + (50 * 6))

    def validate_entries():
        global state
        if(item_ID_entry.get() == "" or item_Name_entry.get() == "" or phone_Num_entry.get() == "" or item_Name_entry.get() == "" or item_Quantity_entry.get() == "" or item_Price_entry.get() == "" or total_Payment_entry.get() == ""):
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

    def supplier_insert():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "INSERT INTO Supplier(Item_ID, Company_Name, Phone_Num, Item_Name, Item_Quantity, Item_Price, Total_Payment) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            values = (item_ID_entry.get(), company_Name_entry.get(), phone_Num_entry.get(), item_Name_entry.get(), item_Quantity_entry.get(), item_Price_entry.get(), total_Payment_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def supplier_update():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "UPDATE supplier SET Item_ID = %s, Company_Name = %s, Phone_Num = %s, Item_Name = %s, Item_Quantity = %s, Item_Price = %s, Total_Payment = %s WHERE Item_ID = %s"
            values = (item_ID_entry.get(), company_Name_entry.get(), phone_Num_entry.get(), item_Name_entry.get(), item_Quantity_entry.get(), item_Price_entry.get(), total_Payment_entry.get(), item_ID_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def supplier_delete():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "DELETE FROM Supplier WHERE Item_ID = %s LIMIT 1"
            values = (item_ID_entry.get(),)

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
                             command = lambda: supplier_insert())
    insert_btn.place(x = 500, y = 220)

    # Button to update existing data in table referencing PK.
    update_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Update \n via supplier_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: supplier_update())
    update_btn.place(x = 500, y = 290)

    # Button to delete data from table referencing PK.
    delete_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Delete \n via supplier_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: supplier_delete())
    delete_btn.place(x = 500, y = 360)

    win.mainloop()
    return