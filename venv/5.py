from tkinter import * # GUI

import mysql.connector



window = Tk()



btnSave = Button(window, text="Save Customer", command=onClick)
btnSave.pack()

window.mainloop()