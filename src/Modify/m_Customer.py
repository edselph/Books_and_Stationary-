from tkinter import *
import tkinter.messagebox as msb
from typing import ValuesView
from src.myDB import getDb, getDbError

def m_Customer_table():
    win = Tk()
    win.title("")
    win.geometry('700x500+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'white')

    # Frame as container for entries.
    customer_frame = Frame(win, bd = 5, height = 450, width = 450, bg = 'light gray')
    customer_frame.place(x = 0, y = 50)

    member_id_label = Label(customer_frame, text = 'Member_ID', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    member_id_entry = Entry(customer_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    member_id_label.place(x = 0, y = 0)
    member_id_entry.place(x = 150, y = 0)

    fname_label = Label(customer_frame, text = 'Fname', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    fname_entry = Entry(customer_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    fname_label.place(x = 0, y = 0 + 50)
    fname_entry.place(x = 150, y = 0 + 50)

    lname_label = Label(customer_frame, text = 'Lname', font = ('Comic Sans', 15),
                                            fg = 'black', bg = 'light gray', justify = LEFT)
    lname_entry = Entry(customer_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                            fg = 'black', justify = LEFT,  width = 25)
    lname_label.place(x = 0, y = 0 + (50 * 2))
    lname_entry.place(x = 150, y = 0 + (50 * 2))

    gender_label = Label(customer_frame, text = 'Gender', font = ('Comic Sans', 15),
                                                    fg = 'black', bg = 'light gray', justify = LEFT)
    gender_entry = Entry(customer_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                    fg = 'black', justify = LEFT,  width = 25)
    gender_label.place(x = 0, y = 0 + (50 * 3))
    gender_entry.place(x = 150, y = 0 + (50 * 3))

    dob_label = Label(customer_frame, text = 'Date Of Birth', font = ('Comic Sans', 15),
                                                 fg = 'black', bg = 'light gray', justify = LEFT)
    dob_entry = Entry(customer_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                 fg = 'black', justify = LEFT,  width = 25)
    dob_label.place(x = 0, y = 0 + (50 * 4))
    dob_entry.place(x = 150, y = 0 + (50 * 4))

    phone_Num_label = Label(customer_frame, text = 'Phone_Num', font = ('Comic Sans', 15),
                                                 fg = 'black', bg = 'light gray', justify = LEFT)
    phone_Num_entry = Entry(customer_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                 fg = 'black', justify = LEFT,  width = 25)
    phone_Num_label.place(x = 0, y = 0 + (50 * 5))
    phone_Num_entry.place(x = 150, y = 0 + (50 * 5))
    
    email_label = Label(customer_frame, text = 'Email', font = ('Comic Sans', 15),
                                               fg = 'black', bg = 'light gray', justify = LEFT)
    email_entry = Entry(customer_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                               fg = 'black', justify = LEFT,  width = 25)
    email_label.place(x = 0, y = 0 + (50 * 6))
    email_entry.place(x = 150, y = 0 + (50 * 6))   
    
    def validate_entries():
        global state
        if(member_id_entry.get() == "" or fname_entry.get() == "" or lname_entry.get() == "" or gender_entry.get() == "" or dob_entry.get() == "" or phone_Num_entry.get() == "" or email_entry.get() == ""):
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

    def customer_insert():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "INSERT INTO Customer(Member_ID, Fname, Lname, Gender, Date_Of_Birth, Phone_Num, Email) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            values = (member_id_entry.get(), fname_entry.get(), lname_entry.get(), gender_entry.get(), dob_entry.get(), phone_Num_entry.get(), email_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def customer_update():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "UPDATE Customer SET Member_ID = %s, Fname = %s, Lname = %s, Gender = %s, Date_Of_Birth = %s, Phone_Num = %s, Email = %s WHERE Member_ID = %s"
            values = (member_id_entry.get(), fname_entry.get(), lname_entry.get(), gender_entry.get(), dob_entry.get(), phone_Num_entry.get(), email_entry.get(), member_id_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def customer_delete():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "DELETE FROM Customer WHERE Member_ID = %s"
            values = (member_id_entry.get() )

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
                             command = lambda: customer_insert())
    insert_btn.place(x = 500, y = 220)

    # Button to update existing data in table referencing PK.
    update_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Update \n via Member_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: customer_update())
    update_btn.place(x = 500, y = 290)

    # Button to delete data from table referencing PK.
    delete_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Delete \n via Member_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: customer_delete())
    delete_btn.place(x = 500, y = 360)

    win.mainloop()
    return