from tkinter import *

import mysql.connector

def onClick():
    window1 = Tk()


    lblTitle = Label(window1, text="Add Customer")
    lblTitle.pack()

    lblName = Label(window1, text="Enter Customer Name")
    lblName.pack()

    entryName = Entry(window1)
    entryName.pack()

    lblPhone = Label(window1, text="Enter Customer Phone")
    lblPhone.pack()

    entryPhone = Entry(window1)
    entryPhone.pack()

    lblEmail = Label(window1, text="Enter Customer Email")
    lblEmail.pack()

    entryEmail = Entry(window1)
    entryEmail.pack()

    btnSave = Button(window1, text="Save Customer", command=onClick1)
    btnSave.pack()

    def onClick1():


      cursor = con.name = entryName.get()
      phone = entryPhone.get()
      email = entryEmail.get()

      print(name, phone, email)

      sql = "insert into Customer values(null, '{}', '{}', '{}')".format(name, phone, email)

      con = mysql.connector.connect(user="root", password="", host="localhost", database="rajat")

      cursor()
      cursor.execute(sql)

      con.commit()


      print(name," Saved in DataBase")
    window1.mainloop()


window = Tk()



btnAdd = Button(window, text="Add Customer", command=onClick)
btnAdd.pack()

btnUpdate = Button(window, text="Update Customer", command=upClick)
btnUpdate.pack()


window.mainloop()