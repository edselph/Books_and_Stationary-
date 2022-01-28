import tkinter as tk
from tkinter import *
from tkinter import ttk
# from Db_B_n_S import db
# Main window.

window = Tk()
window.title("Books and Stationary")
window.geometry("1000x800")
window.resizable(height = False, width = False)
window.config(bg = "white")

# Frame
frame = tk.Frame(window, bg = "black")
frame.pack(side =tk.LEFT, padx=20, pady=20)

tv = ttk.Treeview(frame, height = 5, columns= (1,2,3,4,5,6,7), show= "headings")
tv.heading(1, text="Employee_ID")
tv.heading(2, text="Fname")
tv.heading(3, text="Gender")
tv.heading(4, text="Age")
tv.heading(5, text="Phone_num")
tv.heading(6, text="Email")
tv.heading(7, text="Salary")

window.mainloop()