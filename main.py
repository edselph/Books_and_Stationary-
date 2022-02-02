# Main page for the app.
from tkinter import *

from src.View.v_Customer import v_Customer_table
from src.View.v_Book import v_book_table
from src.View.v_Employee import v_employee_table
from src.View.v_Invoice import v_invoice_table
from src.View.v_Stationary import v_stationary_table
from src.View.v_Supplier import v_supplier_table

from src.Modify.m_Customer import m_Customer_table
from src.Modify.m_Book import m_Book_table
from src.Modify.m_Employee import m_Employee_table
from src.Modify.m_Stationary import m_stationary_table
from src.Modify.m_Supplier import m_supplier_table
from src.Modify.m_Invoice import m_invoice_table


# Main window.
root = Tk()                                             
root.geometry("800x600+0+0")                            
root.resizable(height = False, width = False)           
root.title("Books_and_Stationary")  
root.config(bg = "white")              

# Employee View and Modify
v_btn_employee = Button(root, 
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "View Employee Table", 
width = 20, 
bg = "light gray", 
fg = "black", 
        command = lambda: v_employee_table())
v_btn_employee.place(x = 30, y = 30)

m_btn_employee = Button(root, 
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "Modify Employee Table", 
width = 20, 
bg = "light gray", 
fg = "black", 
command = lambda: m_Employee_table())
m_btn_employee.place(x = 400, y = 30)



# Customer View and Modify
v_btn_customer = Button(root,
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "View Customer Table", 
width = 20, 
bg = "light gray", 
fg = "black", 
command = lambda: v_Customer_table())
v_btn_customer.place(x = 30, y = 100)

m_btn_customer = Button(root, 
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "Modify Customer Table", 
width = 20, 
bg = "light gray", 
fg = "black", 
command = lambda: m_Customer_table())
m_btn_customer.place(x = 400, y = 100)



# Books View and Modify
v_btn_book = Button(root, 
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "View Book Table", 
width = 20, 
bg = "light gray", 
fg = "black", 
command = lambda: v_book_table())
v_btn_book.place(x = 30, y = 170)

m_btn_book = Button(root, 
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "Modify Book Table", 
width = 20, 
bg = "light gray", 
fg = "black", 
command = lambda: m_Book_table())
m_btn_book.place(x = 400, y = 170)



# Stationary View and Modify
v_btn_stationary = Button(root, 
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "View Stationary Table", 
width = 20, 
bg = "light gray", 
fg = "black",  
command = lambda: v_stationary_table())
v_btn_stationary.place(x = 30, y = 240)

m_btn_stationary = Button(root,
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "Modify Stationary Table", 
width = 20, 
bg = "light gray", 
fg = "black", 
command = lambda: m_stationary_table())
m_btn_stationary.place(x = 400, y = 240)



# Supplier View and Modify
v_btn_supplier = Button(root, 
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "View Supplier Table", 
width = 20, 
bg = "light gray", 
fg = "black",  
command = lambda: v_supplier_table())
v_btn_supplier.place(x = 30, y = 310)

m_btn_supplier = Button(root,
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "Modify Supplier Table", 
width = 20, 
bg = "light gray", 
fg = "black", 
command = lambda: m_supplier_table())
m_btn_supplier.place(x = 400, y = 310)



# Invoice View and Modify
v_btn_invoice = Button(root, 
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "View Invoice Table", 
width = 20, 
bg = "light gray", 
fg = "black",  
command = lambda: v_invoice_table())
v_btn_invoice.place(x = 30, y = 380)

m_btn_invoice = Button(root,
justify = LEFT,
font = ("Comic Sans", 18, "bold"),
text = "Modify Invoice Table", 
width = 20, 
bg = "light gray", 
fg = "black", 
command = lambda: m_invoice_table())
m_btn_invoice.place(x = 400, y = 380)


root.mainloop()