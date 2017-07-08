#build a pure fram 

import tkinter as tk
#it is grapic (visual) 
#from tkinter import ttk (not nessary needed if have tkinter import)

window = tk.Tk()
window.geometry("300x200")


alabel = tk.Label(text ="Apple")# create a str  & need a location 
alabel.grid( column = 0, row = 0)# help you use sth in colum and row 
#grid function need a find the counterpart to be able to move the position 
blabel = tk.Label(text = "Banana")
blabel.grid(column = 0, row = 2)
# creat the other to be counterpart of alabel 
window.mainloop()