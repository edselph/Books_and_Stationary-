from tkinter import *
import tkinter.messagebox as msb
from typing import ValuesView
from src.myDB import getDb, getDbError

def m_invoice_table():
    win = Tk()
    win.title("")
    win.geometry('700x500+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'white')

    # Frame as container for entries.
    invoice_frame = Frame(win, bd = 5, height = 450, width = 450, bg = 'light gray')
    invoice_frame.place(x = 0, y = 50)

    invoice_num_label = Label(invoice_frame, text = 'Invoice_Num', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    invoice_num_entry = Entry(invoice_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    invoice_num_label.place(x = 0, y = 0)
    invoice_num_entry.place(x = 150, y = 0)

    invoice_date_label = Label(invoice_frame, text = 'Invoice_Date', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    invoice_date_entry = Entry(invoice_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    invoice_date_label.place(x = 0, y = 0 + 50)
    invoice_date_entry.place(x = 150, y = 0 + 50)

    member_id_label = Label(invoice_frame, text = 'Member_ID', font = ('Comic Sans', 15),
                                            fg = 'black', bg = 'light gray', justify = LEFT)
    member_id_entry = Entry(invoice_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                            fg = 'black', justify = LEFT,  width = 25)
    member_id_label.place(x = 0, y = 0 + (50 * 2))
    member_id_entry.place(x = 150, y = 0 + (50 * 2))

    employee_id_label = Label(invoice_frame, text = 'Employee_ID', font = ('Comic Sans', 15),
                                                    fg = 'black', bg = 'light gray', justify = LEFT)
    employee_id_entry = Entry(invoice_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                    fg = 'black', justify = LEFT,  width = 25)
    employee_id_label.place(x = 0, y = 0 + (50 * 3))
    employee_id_entry.place(x = 150, y = 0 + (50 * 3))

    equipment_id_label = Label(invoice_frame, text = 'Equipment_ID', font = ('Comic Sans', 15),
                                                 fg = 'black', bg = 'light gray', justify = LEFT)
    equipment_id_entry = Entry(invoice_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                 fg = 'black', justify = LEFT,  width = 25)
    equipment_id_label.place(x = 0, y = 0 + (50 * 4))
    equipment_id_entry.place(x = 150, y = 0 + (50 * 4))

    equipment_quantity_label = Label(invoice_frame, text = 'Equipment_Quantity', font = ('Comic Sans', 15),
                                                 fg = 'black', bg = 'light gray', justify = LEFT)
    equipment_quantity_entry = Entry(invoice_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                 fg = 'black', justify = LEFT,  width = 25)
    equipment_quantity_label.place(x = 0, y = 0 + (50 * 5))
    equipment_quantity_entry.place(x = 150, y = 0 + (50 * 5))
    
    isbn_label = Label(invoice_frame, text = 'ISBN', font = ('Comic Sans', 15),
                                               fg = 'black', bg = 'light gray', justify = LEFT)
    isbn_entry = Entry(invoice_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                               fg = 'black', justify = LEFT,  width = 25)
    isbn_label.place(x = 0, y = 0 + (50 * 6))
    isbn_entry.place(x = 150, y = 0 + (50 * 6)) 

    book_quantity_label = Label(invoice_frame, text = 'Book_Quantity', font = ('Comic Sans', 15),
                                               fg = 'black', bg = 'light gray', justify = LEFT)
    book_quantity_entry = Entry(invoice_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                               fg = 'black', justify = LEFT,  width = 25)
    book_quantity_label.place(x = 0, y = 0 + (50 * 7))
    book_quantity_entry.place(x = 150, y = 0 + (50 * 7))  
    
    total_price_label = Label(invoice_frame, text = 'Total_Price', font = ('Comic Sans', 15),
                                               fg = 'black', bg = 'light gray', justify = LEFT)
    total_price_entry = Entry(invoice_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                               fg = 'black', justify = LEFT,  width = 25)
    total_price_label.place(x = 0, y = 0 + (50 * 8))
    total_price_entry.place(x = 150, y = 0 + (50 * 8))

    def validate_entries():
        global state
        if(invoice_num_entry.get() == "" or invoice_date_entry.get() == "" or member_id_entry.get() == "" or employee_id_entry.get() == "" or equipment_id_entry.get() == "" or equipment_quantity_entry.get() == "" or isbn_entry.get() == "" or book_quantity_entry.get() == "" or total_price_entry.get() == ""):
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

    def invoice_insert():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "INSERT INTO Invoice(Invoice_Num, Invoice_Date, Member_ID, Employee_ID, Equipment_ID, Equipment_Quantity, ISBN, Book_Quantity, Total_Price) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (invoice_num_entry.get(), invoice_date_entry.get(), member_id_entry.get(), employee_id_entry.get(), equipment_id_entry.get(), equipment_quantity_entry.get(), isbn_entry.get(), book_quantity_entry.get(), total_price_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def invoice_update():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "UPDATE Invoice SET Invoice_Num = %s, Invoice_Date = %s, Member_ID = %s, Employee_ID = %s, Equipment_ID = %s, Equipment_Quantity = %s, ISBN = %s, Book_Quantity = %s, Total_Price = %s WHERE Invoice_Num = %s"
            values = (invoice_num_entry.get(), invoice_date_entry.get(), member_id_entry.get(), employee_id_entry.get(), equipment_id_entry.get(), equipment_quantity_entry.get(), isbn_entry.get(), book_quantity_entry.get(), total_price_entry.get(),invoice_num_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def invoice_delete():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "DELETE FROM Invoice WHERE Invoice_Num = %s"
            values = (invoice_num_entry.get())

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
                             command = lambda: invoice_insert())
    insert_btn.place(x = 500, y = 220)

    # Button to update existing data in table referencing PK.
    update_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Update \n via Employee_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: invoice_update())
    update_btn.place(x = 500, y = 290)

    # Button to delete data from table referencing PK.
    delete_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Delete \n via Employee_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: invoice_delete())
    delete_btn.place(x = 500, y = 360)

    win.mainloop()
    return