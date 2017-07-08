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
blabel.grid(column = 0, row = 1)
# creat the other to be counterpart of alabel 

#creat a botton 
button1 = tk.Button(text = "Eat Apples")
button1.grid(column = 1, row = 0)
button2 = tk.Button(text = "Eat Bananas")# miss the parethesis 
button2.grid(column = 1, row = 1)
window.mainloop()