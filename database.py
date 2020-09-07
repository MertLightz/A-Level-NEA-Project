from tkinter import *

root = Tk()
root.title('STOCK CONTROL SYSTEM')

for i in range(5):
    for j in range(4):
        e = Entry(root, width = 20)
        e.grid(row = i, column = j)
        
root.mainloop()