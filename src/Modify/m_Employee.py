from tkinter import *
import tkinter.messagebox as msb
from typing import ValuesView
from src.myDB import getDb, getDbError

def m_Employee_table():
    win = Tk()
    win.title("")
    win.geometry('700x500+0+0')
    win.resizable(height = False, width = False)
    win.config(bg = 'white')

    # Frame as container for entries.
    employee_frame = Frame(win, bd = 5, height = 450, width = 450, bg = 'light gray')
    employee_frame.place(x = 0, y = 50)

    employee_ID_label = Label(employee_frame, text = 'Employee_ID', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    employee_ID_entry = Entry(employee_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    employee_ID_label.place(x = 0, y = 0)
    employee_ID_entry.place(x = 150, y = 0)

    fname_label = Label(employee_frame, text = 'Fname', font = ('Comic Sans', 15),
                                             fg = 'black', bg = 'light gray', justify = LEFT)
    fname_entry = Entry(employee_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                             fg = 'black', justify = LEFT,  width = 25)
    fname_label.place(x = 0, y = 0 + 50)
    fname_entry.place(x = 150, y = 0 + 50)

    lname_label = Label(employee_frame, text = 'Lname', font = ('Comic Sans', 15),
                                            fg = 'black', bg = 'light gray', justify = LEFT)
    lname_entry = Entry(employee_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                            fg = 'black', justify = LEFT,  width = 25)
    lname_label.place(x = 0, y = 0 + (50 * 2))
    lname_entry.place(x = 150, y = 0 + (50 * 2))

    gender_label = Label(employee_frame, text = 'Gender', font = ('Comic Sans', 15),
                                                    fg = 'black', bg = 'light gray', justify = LEFT)
    gender_entry = Entry(employee_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                    fg = 'black', justify = LEFT,  width = 25)
    gender_label.place(x = 0, y = 0 + (50 * 3))
    gender_entry.place(x = 150, y = 0 + (50 * 3))

    dob_label = Label(employee_frame, text = 'Date Of Birth', font = ('Comic Sans', 15),
                                                 fg = 'black', bg = 'light gray', justify = LEFT)
    dob_entry = Entry(employee_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                 fg = 'black', justify = LEFT,  width = 25)
    dob_label.place(x = 0, y = 0 + (50 * 4))
    dob_entry.place(x = 150, y = 0 + (50 * 4))

    phone_Num_label = Label(employee_frame, text = 'Phone_Num', font = ('Comic Sans', 15),
                                                 fg = 'black', bg = 'light gray', justify = LEFT)
    phone_Num_entry = Entry(employee_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                                 fg = 'black', justify = LEFT,  width = 25)
    phone_Num_label.place(x = 0, y = 0 + (50 * 5))
    phone_Num_entry.place(x = 150, y = 0 + (50 * 5))
    
    email_label = Label(employee_frame, text = 'Email', font = ('Comic Sans', 15),
                                               fg = 'black', bg = 'light gray', justify = LEFT)
    email_entry = Entry(employee_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                               fg = 'black', justify = LEFT,  width = 25)
    email_label.place(x = 0, y = 0 + (50 * 6))
    email_entry.place(x = 150, y = 0 + (50 * 6)) 

    salary_label = Label(employee_frame, text = 'Salary', font = ('Comic Sans', 15),
                                               fg = 'black', bg = 'light gray', justify = LEFT)
    salary_entry = Entry(employee_frame, bg = 'white', bd = 3, font = ('Comic Sans', 15, "bold"),
                                               fg = 'black', justify = LEFT,  width = 25)
    salary_label.place(x = 0, y = 0 + (50 * 7))
    salary_entry.place(x = 150, y = 0 + (50 * 7))  
    
    def validate_entries():
        global state
        if(employee_ID_entry.get() == "" or fname_entry.get() == "" or lname_entry.get() == "" or gender_entry.get() == "" or dob_entry.get() == "" or phone_Num_entry.get() == "" or email_entry.get() == "" or salary_entry.get() == ""):
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

    def employee_insert():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')

        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "INSERT INTO Employee(Employee_ID, Fname, Lname, Gender, Date_Of_Birth, Phone_Num, Email, Salary) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (employee_ID_entry.get(), fname_entry.get(), lname_entry.get(), gender_entry.get(), dob_entry.get(), phone_Num_entry.get(), email_entry.get(), salary_entry.get())

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def employee_update():
        if(validate_entries() == False):
            msb.showwarning('ERROR!! Make sure you have entered all the fields needed.')
        
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "UPDATE Employee SET Employee_ID = %s, Fname = %s, Lname = %s, Gender = %s, Date_Of_Birth = %s, Phone_Num = %s, Email = %s, Salary = %s WHERE Employee_ID = %s "
            values = (employee_ID_entry.get(), fname_entry.get(), lname_entry.get(), gender_entry.get(), dob_entry.get(), phone_Num_entry.get(), email_entry.get(), salary_entry.get(),employee_ID_entry.get(),)

            my_cursor.execute(queries, values)
            my_db.commit()
            msb.showinfo('Success', str(my_cursor.rowcount) + 'row/s affected.')
        except getDbError() as err:
            msb.showerror('Error', str(err))
        finally:
            reactivate_foreign_keys()

    def employee_delete():
        try:
            disable_foreign_keys()
            my_db = getDb()
            my_cursor = my_db.cursor()

            queries = "DELETE FROM Employee WHERE Employee_ID = %s LIMIT 1"
            values = (employee_ID_entry.get(),)

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
                             command = lambda: employee_insert())
    insert_btn.place(x = 500, y = 220)

    # Button to update existing data in table referencing PK.
    update_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Update \n via Employee_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: employee_update())
    update_btn.place(x = 500, y = 290)

    # Button to delete data from table referencing PK.
    delete_btn = Button(win, justify = CENTER, width = 15, bg = 'black', fg = 'light gray', text = 'Delete \n via Employee_ID',
                             font = ('Comic Sans', 12, "bold"),  
                             command = lambda: employee_delete())
    delete_btn.place(x = 500, y = 360)

    win.mainloop()
    return