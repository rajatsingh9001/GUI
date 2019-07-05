from tkinter import *

import mysql.connector

def add_entry():
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

    def SaveIt():
      name = entryName.get()
      phone = entryPhone.get()
      email = entryEmail.get()

      print(name, phone, email)
      sql = "insert into Customer values(null, '{}', '{}', '{}'".format(name, phone, email)

      con = mysql.connector.connect(user="root", password="", host="localhost", database="rajat")

      cursor = con.cursor()
      cursor.execute(sql)

      con.commit()

      print(name, " Saved in DataBase")


    Button(window1, text="Save", command=SaveIt).pack(side=BOTTOM)
    window1.mainloop()

def update_entry():

    def update_name():
        window11 = Tk()
        lblTitle = Label(window11, text="Update Name")
        lblTitle.pack()

        lblName = Label(window11, text="Enter Customer New Name")
        lblName.pack()
        entryName = Entry(window11)
        entryName.pack()

        lblEmail = Label(window11, text="Enter Customer Email")
        lblEmail.pack()
        entryEmail = Entry(window11)
        entryEmail.pack()
        def update1():
         name = entryName.get()
         email = entryEmail.get()

         print(name, email)
         sql = "update customer set name='{}' where email='{}'".format(name, email)

         con = mysql.connector.connect(user="root", password="", host="localhost", database="rajat")

         cursor = con.cursor()
         cursor.execute(sql)

         con.commit()

         print(name, " Update in DataBase")

        Button(window11, text="Update Name", command=update1).pack(side=BOTTOM)
        window11.mainloop()

    def update_phone():
        window12 = Tk()
        lblTitle = Label(window12, text="Update Phone")
        lblTitle.pack()

        lblPhone = Label(window12, text="Enter Customer New Phone")
        lblPhone.pack()
        entryPhone = Entry(window12)
        entryPhone.pack()

        lblEmail = Label(window12, text="Enter Customer Email")
        lblEmail.pack()
        entryEmail = Entry(window12)
        entryEmail.pack()
        def update12():
         phone = entryPhone.get()
         email = entryEmail.get()

         print(phone, email)
         sql = "update customer set phone='{}' where email='{}'".format(phone, email)

         con = mysql.connector.connect(user="root", password="", host="localhost", database="rajat")

         cursor = con.cursor()
         cursor.execute(sql)

         con.commit()

         print(phone, " Update in DataBase")

        Button(window12, text="Update Phone", command=update12).pack(side=BOTTOM)
        window12.mainloop()

    def update_email():
        window13 = Tk()
        lblTitle = Label(window13, text="Update Email")
        lblTitle.pack()

        lblEmail = Label(window13, text="Enter Customer New Email")
        lblEmail.pack()
        entryEmail = Entry(window13)
        entryEmail.pack()

        lblPhone = Label(window13, text="Enter Customer Phone")
        lblPhone.pack()
        entryPhone = Entry(window13)
        entryPhone.pack()
        def update13():
         phone = entryPhone.get()
         email = entryEmail.get()

         print(email, phone)
         sql = "update customer set email='{}' where phone='{}'".format(email, phone)

         con = mysql.connector.connect(user="root", password="", host="localhost", database="rajat")

         cursor = con.cursor()
         cursor.execute(sql)

         con.commit()

         print(email, " Update in DataBase")

        Button(window13, text="Update Email", command=update13).pack(side=BOTTOM)
        window13.mainloop()

    def update():
      win1 = Tk()
      frame1 = Frame(win1)
      frame1.pack()
      b1 = Button(frame1, text="Update Customer Name", command=update_name)
      b2 = Button(frame1, text="Update Customer Phone", command=update_phone)
      b3 = Button(frame1, text="Update Customer Email", command=update_email)

      b1.pack()
      b2.pack()
      b3.pack()

    win1 = update()
    win1.mainloop()

def delete_entry():
    window2 = Tk()

    lblTitle = Label(window2, text="Enter Detail")
    lblTitle.pack()

    lblEmail = Label(window2, text="Enter Customer Email")
    lblEmail.pack()

    entryEmail = Entry(window2)
    entryEmail.pack()

    def DeleteIt():
      email = entryEmail.get()
      print(email)

      sql = "delete from customer where Email = '{}'".format(email)
      con = mysql.connector.connect(user="root", password="", host="localhost", database="rajat")

      cursor = con.cursor()
      cursor.execute(sql)

      print(email, " Delete from DataBase")

    Button(window2, text="Delete", command=DeleteIt).pack(side=BOTTOM)
    window2.mainloop()

def view_entry():

    window3 = Tk()

    lblName = Label(window3, text="Enter Customer Name")
    lblName.pack()

    entryName = Entry(window3)
    entryName.pack()

    def ShowIt():
      name = entryName.get()
      print(name)

      sql = "select * from customer where Name = '{}'".format(name)
      con = mysql.connector.connect(user="root", password="", host="localhost", database="rajat")

      cursor = con.cursor()
      cursor.execute(sql)

      rows = cursor.fetchall()
      for row in rows:
        # print(row)
        print(row[1], row[3])

    Button(window3, text="Show", command=ShowIt).pack(side=BOTTOM)
    window3.mainloop()

def view_all_select():


    sql = "select * from Customer"

    con = mysql.connector.connect(user="root", password="", host="localhost", database="rajat")

    cursor = con.cursor()
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        # print(row)
        print(row[1], row[3])


def make_window():

    win = Tk()

    frame2 = Frame(win)
    frame2.pack()
    b1 = Button(frame2, text=" Add Customer", command=add_entry)
    b2 = Button(frame2, text="Update Customer", command=update_entry)
    b3 = Button(frame2, text="Delete Customer", command=delete_entry)
    b4 = Button(frame2, text="View Customer", command=view_entry)
    b5 = Button(frame2, text="View All Customer", command=view_all_select)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    b4.pack(side=LEFT)
    b5.pack(side=LEFT)



    frame3 = Frame(win)
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT, fill=BOTH, expand=1)
    return win



win = make_window()
win.mainloop()