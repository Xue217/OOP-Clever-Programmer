#build a pure fram 

import tkinter as tk
#it is grapic (visual) 
#from tkinter import ttk (not nessary needed if have tkinter import)

def doorbell(event):
	print ("You rang the doorbell!!!")
window = tk.Tk()
window.geometry("300x200")


alabel = tk.Label(text ="Apple")# create a str  & need a location 
alabel.grid( column = 0, row = 0)# help you use sth in colum and row 
#grid function need a find the counterpart to be able to move the position 
blabel = tk.Label(text = "Banana")
blabel.grid(column = 0, row = 1)
# creat the other to be counterpart of alabel 

#creat a botton 
button1 = tk.Button(window,text = "Eat Apples") #window make sure it is in the window
button1.grid(column = 1, row = 0)
button2 = tk.Button(window,text = "Eat Bananas")# miss the parethesis 
button2.grid(column = 1, row = 1)


#window.bind("<Button-1>",doorbell)#bind the mouse to function -1/ bind the lelf click to hold window 
button1.bind("<Button-2>",doorbell)#only bind the button to button1
window.mainloop()



#event handdle: waiting for some event happening then deal with it 