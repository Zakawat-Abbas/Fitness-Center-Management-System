# Import
from tkinter import *
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time


# Add Member
def addmember():
    def submitaddm():
        id = idval.get()
        name = nameval.get()
        age = ageval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        try:
            strr = 'insert into Member values(%s,%s,%s,%s,%s,%s)'
            my_cursor.execute(strr, (id, name, age, mobile, email, address))
            con.commit()
            res = messagebox.askyesnocancel('Notifications', 'Id {} Name {} Added successfully..and want '
                                                             'to clean the form'.format(id, name), parent=addrootm)
            if res:
                idval.set('')
                nameval.set('')
                ageval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')

        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=addrootm)
        strr = 'select * from Member'
        my_cursor.execute(strr)
        datas = my_cursor.fetchall()
        Membertable.delete(*Membertable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
            Membertable.insert('', END, values=vv)

    addrootm = Toplevel(master=DataEntryFrame)
    addrootm.grab_set()
    addrootm.geometry('472x410+350+160')
    addrootm.title('Fitness Center Management System')
    addrootm.config(bg='blue')
    addrootm.iconbitmap('Gym.ico')
    addrootm.resizable(False, False)
    # --------------------------------------------------- Add member Labels
    idlabel = Label(addrootm, text='Enter Mem. Id : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addrootm, text='Enter Name : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    namelabel.place(x=10, y=70)

    agelabel = Label(addrootm, text='Enter Age : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    agelabel.place(x=10, y=130)

    mobilelabel = Label(addrootm, text='Enter Mobile : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    mobilelabel.place(x=10, y=190)

    emaillabel = Label(addrootm, text='Enter Email : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    emaillabel.place(x=10, y=250)

    addresslabel = Label(addrootm, text='Enter Address : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    addresslabel.place(x=10, y=310)

    # Add Member Entry
    idval = StringVar()
    nameval = StringVar()
    ageval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()

    identry = Entry(addrootm, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    nameentry = Entry(addrootm, font=('arial', 15, 'bold'), bd=5, textvariable=nameval, width='23')
    nameentry.place(x=205, y=70)

    ageentry = Entry(addrootm, font=('arial', 15, 'bold'), bd=5, textvariable=ageval, width='23')
    ageentry.place(x=205, y=130)

    mobileentry = Entry(addrootm, font=('arial', 15, 'bold'), bd=5, textvariable=mobileval, width='23')
    mobileentry.place(x=205, y=190)

    emailentry = Entry(addrootm, font=('arial', 15, 'bold'), bd=5, textvariable=emailval, width='23')
    emailentry.place(x=205, y=250)

    addressentry = Entry(addrootm, font=('arial', 15, 'bold'), bd=5, textvariable=addressval, width='23')
    addressentry.place(x=205, y=310)

    # Add button
    submitbtn = Button(addrootm, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=submitaddm)
    submitbtn.place(x=150, y=360)
    addrootm.mainloop()


# Search Member
def searchmember():
    def searchm():
        id = idval.get()
        name = nameval.get()
        age = ageval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()

        if id != '':
            strr = 'select * from Member where id=%s'
            my_cursor.execute(strr, id)
            datas = my_cursor.fetchall()
            Membertable.delete(*Membertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Membertable.insert('', END, values=vv)
        elif name != '':
            strr = 'select * from Member where name=%s'
            my_cursor.execute(strr, name)
            datas = my_cursor.fetchall()
            Membertable.delete(*Membertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Membertable.insert('', END, values=vv)
        elif age != '':
            strr = 'select * from Member where age=%s'
            my_cursor.execute(strr, age)
            datas = my_cursor.fetchall()
            Membertable.delete(*Membertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Membertable.insert('', END, values=vv)
        elif mobile != '':
            strr = 'select * from Member where mobile=%s'
            my_cursor.execute(strr, mobile)
            datas = my_cursor.fetchall()
            Membertable.delete(*Membertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Membertable.insert('', END, values=vv)
        elif email != '':
            strr = 'select *from Member where email=%s'
            my_cursor.execute(strr, email)
            datas = my_cursor.fetchall()
            Membertable.delete(*Membertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Membertable.insert('', END, values=vv)
        elif address != '':
            strr = 'select *from Member where address=%s'
            my_cursor.execute(strr, address)
            datas = my_cursor.fetchall()
            Membertable.delete(*Membertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Membertable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('472x410+350+160')
    searchroot.title('Fitness Center Management System')
    searchroot.config(bg='blue')
    searchroot.iconbitmap('Gym.ico')
    searchroot.resizable(False, False)
    # --------------------------------------------------- Search member Labels
    idlabel = Label(searchroot, text='Enter Mem. Id : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    namelabel.place(x=10, y=70)

    agelabel = Label(searchroot, text='Enter Age : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    agelabel.place(x=10, y=130)

    mobilelabel = Label(searchroot, text='Enter Mobile : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    mobilelabel.place(x=10, y=190)

    emaillabel = Label(searchroot, text='Enter Email : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    emaillabel.place(x=10, y=250)

    addresslabel = Label(searchroot, text='Enter Address : ', bg='blue', font=('times', 20, 'bold'), width=12,
                         anchor='w')
    addresslabel.place(x=10, y=310)

    # Search Member Entry
    idval = StringVar()
    nameval = StringVar()
    ageval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()

    identry = Entry(searchroot, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    nameentry = Entry(searchroot, font=('arial', 15, 'bold'), bd=5, textvariable=nameval, width='23')
    nameentry.place(x=205, y=70)

    ageentry = Entry(searchroot, font=('arial', 15, 'bold'), bd=5, textvariable=ageval, width='23')
    ageentry.place(x=205, y=130)

    mobileentry = Entry(searchroot, font=('arial', 15, 'bold'), bd=5, textvariable=mobileval, width='23')
    mobileentry.place(x=205, y=190)

    emailentry = Entry(searchroot, font=('arial', 15, 'bold'), bd=5, textvariable=emailval, width='23')
    emailentry.place(x=205, y=250)

    addressentry = Entry(searchroot, font=('arial', 15, 'bold'), bd=5, textvariable=addressval, width='23')
    addressentry.place(x=205, y=310)

    # Add button
    submitbtn = Button(searchroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=searchm)
    submitbtn.place(x=150, y=360)
    searchroot.mainloop()


# Delete Member
def deletemember():
    cc = Membertable.focus()
    content = Membertable.item(cc)
    pp = content['values'][0]
    strr = 'delete from Member where id=%s'
    my_cursor.execute(strr, pp)
    con.commit()
    messagebox.showinfo('Notifications', 'Id {} deleted successfully...'.format(pp))
    strr = 'select *from Member'
    my_cursor.execute(strr)
    datas = my_cursor.fetchall()
    Membertable.delete(*Membertable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
        Membertable.insert('', END, values=vv)


# Update Member
def updatemember():
    def updatem():
        id = idval.get()
        name = nameval.get()
        age = ageval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()

        strr = 'update Member set name=%s,age=%s,mobile=%s,email=%s,address=%s where id=%s'
        my_cursor.execute(strr, (name, age, mobile, email, address, id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified successfully...'.format(id), parent=updaterootm)
        strr = 'select *from Member'
        my_cursor.execute(strr)
        datas = my_cursor.fetchall()
        Membertable.delete(*Membertable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
            Membertable.insert('', END, values=vv)

    updaterootm = Toplevel(master=DataEntryFrame)
    updaterootm.grab_set()
    updaterootm.geometry('472x410+350+160')
    updaterootm.title('Fitness Center Management System')
    updaterootm.config(bg='blue')
    updaterootm.iconbitmap('Gym.ico')
    updaterootm.resizable(False, False)
    # --------------------------------------------------- Update member Labels
    idlabel = Label(updaterootm, text='Enter Mem. Id : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updaterootm, text='Enter Name : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    namelabel.place(x=10, y=70)

    agelabel = Label(updaterootm, text='Enter Age : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    agelabel.place(x=10, y=130)

    mobilelabel = Label(updaterootm, text='Enter Mobile : ', bg='blue', font=('times', 20, 'bold'), width=12,
                        anchor='w')
    mobilelabel.place(x=10, y=190)

    emaillabel = Label(updaterootm, text='Enter Email : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    emaillabel.place(x=10, y=250)

    addresslabel = Label(updaterootm, text='Enter Address : ', bg='blue', font=('times', 20, 'bold'), width=12,
                         anchor='w')
    addresslabel.place(x=10, y=310)

    # Update Member Entry
    idval = StringVar()
    nameval = StringVar()
    ageval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()

    identry = Entry(updaterootm, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    nameentry = Entry(updaterootm, font=('arial', 15, 'bold'), bd=5, textvariable=nameval, width='23')
    nameentry.place(x=205, y=70)

    ageentry = Entry(updaterootm, font=('arial', 15, 'bold'), bd=5, textvariable=ageval, width='23')
    ageentry.place(x=205, y=130)

    mobileentry = Entry(updaterootm, font=('arial', 15, 'bold'), bd=5, textvariable=mobileval, width='23')
    mobileentry.place(x=205, y=190)

    emailentry = Entry(updaterootm, font=('arial', 15, 'bold'), bd=5, textvariable=emailval, width='23')
    emailentry.place(x=205, y=250)

    addressentry = Entry(updaterootm, font=('arial', 15, 'bold'), bd=5, textvariable=addressval, width='23')
    addressentry.place(x=205, y=310)

    # Add button
    submitbtn = Button(updaterootm, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=updatem)
    submitbtn.place(x=150, y=360)
    cc = Membertable.focus()
    content = Membertable.item(cc)
    pp = content['values']
    if len(pp) != 0:
        idval.set(pp[0])
        nameval.set(pp[1])
        ageval.set(pp[2])
        mobileval.set(pp[3])
        emailval.set(pp[4])
        addressval.set(pp[5])

    updaterootm.mainloop()


# Show all Member
def showmember():
    strr = 'select *from Member'
    my_cursor.execute(strr)
    datas = my_cursor.fetchall()
    Membertable.delete(*Membertable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
        Membertable.insert('', END, values=vv)


# Export data Member
def exportmember():
    ff = filedialog.asksaveasfilename()
    gg = Membertable.get_children()
    id, name, age, mobile, email, address = [], [], [], [], [], []
    for i in gg:
        content = Membertable.item(i)
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), age.append(pp[2]), mobile.append(pp[3]), email.append(pp[4]),
        address.append(pp[5])
    dd = ['Id', 'Name', 'Age', 'Mobile', 'Email', 'Address']
    df = pandas.DataFrame(list(zip(id, name, age, mobile, email, address)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Member data is Saved {}'.format(paths))


# Add Trainer
def addtrainer():
    def submitaddt():
        id1 = idval.get()
        Fitness_id = Fitness_idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        try:
            strr = 'insert into Trainer values(%s,%s,%s,%s,%s,%s)'
            my_cursor.execute(strr, (id1, Fitness_id, name, mobile, email, address))
            con.commit()
            res = messagebox.askyesnocancel('Notifications', 'Id {} Name {} Added successfully..and want '
                                                             'to clean the form'.format(id1, name), parent=addroott)
            if res:
                idval.set('')
                Fitness_idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')

        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=addroott)
        strr = 'select * from Trainer'
        my_cursor.execute(strr)
        datas = my_cursor.fetchall()
        Trainertable.delete(*Trainertable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
            Trainertable.insert('', END, values=vv)

    addroott = Toplevel(master=DataEntryFrame)
    addroott.grab_set()
    addroott.geometry('472x410+350+160')
    addroott.title('Fitness Center Management System')
    addroott.config(bg='blue')
    addroott.iconbitmap('Gym.ico')
    addroott.resizable(False, False)
    # --------------------------------------------------- Add Trainer Labels
    idlabel = Label(addroott, text='Enter Train. Id: ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    Fitness_idlabel = Label(addroott, text='Enter Fitness Id: ', bg='blue', font=('times', 20, 'bold'), width=12,
                            anchor='w')
    Fitness_idlabel.place(x=10, y=70)

    namelabel = Label(addroott, text='Enter Name : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    namelabel.place(x=10, y=130)

    mobilelabel = Label(addroott, text='Enter Mobile : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    mobilelabel.place(x=10, y=190)

    emaillabel = Label(addroott, text='Enter Email : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    emaillabel.place(x=10, y=250)

    addresslabel = Label(addroott, text='Enter Address : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    addresslabel.place(x=10, y=310)

    # Add Trainer Entry
    idval = StringVar()
    Fitness_idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()

    identry = Entry(addroott, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    Fitness_identry = Entry(addroott, font=('arial', 15, 'bold'), bd=5, textvariable=Fitness_idval, width='23')
    Fitness_identry.place(x=205, y=70)

    nameentry = Entry(addroott, font=('arial', 15, 'bold'), bd=5, textvariable=nameval, width='23')
    nameentry.place(x=205, y=130)

    mobileentry = Entry(addroott, font=('arial', 15, 'bold'), bd=5, textvariable=mobileval, width='23')
    mobileentry.place(x=205, y=190)

    emailentry = Entry(addroott, font=('arial', 15, 'bold'), bd=5, textvariable=emailval, width='23')
    emailentry.place(x=205, y=250)

    addressentry = Entry(addroott, font=('arial', 15, 'bold'), bd=5, textvariable=addressval, width='23')
    addressentry.place(x=205, y=310)

    # Add button
    submitbtn = Button(addroott, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=submitaddt)
    submitbtn.place(x=150, y=360)
    addroott.mainloop()


# Search Trainer
def searchtrainer():
    def searcht():
        id1 = idval.get()
        Fitness_id = Fitness_idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()

        if id1 != '':
            strr = 'select * from Trainer where id1=%s'
            my_cursor.execute(strr, id1)
            datas = my_cursor.fetchall()
            Trainertable.delete(*Trainertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Trainertable.insert('', END, values=vv)
        elif Fitness_id != '':
            strr = 'select * from Trainer where Fitness_id=%s'
            my_cursor.execute(strr, Fitness_id)
            datas = my_cursor.fetchall()
            Trainertable.delete(*Trainertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Trainertable.insert('', END, values=vv)
        elif name != '':
            strr = 'select * from Trainer where name=%s'
            my_cursor.execute(strr, name)
            datas = my_cursor.fetchall()
            Trainertable.delete(*Trainertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Trainertable.insert('', END, values=vv)
        elif mobile != '':
            strr = 'select * from Trainer where mobile=%s'
            my_cursor.execute(strr, mobile)
            datas = my_cursor.fetchall()
            Trainertable.delete(*Trainertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Trainertable.insert('', END, values=vv)
        elif email != '':
            strr = 'select *from Trainer where email=%s'
            my_cursor.execute(strr, email)
            datas = my_cursor.fetchall()
            Trainertable.delete(*Trainertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Trainertable.insert('', END, values=vv)
        elif address != '':
            strr = 'select *from Trainer where address=%s'
            my_cursor.execute(strr, address)
            datas = my_cursor.fetchall()
            Trainertable.delete(*Trainertable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                Trainertable.insert('', END, values=vv)

    searchroott = Toplevel(master=DataEntryFrame)
    searchroott.grab_set()
    searchroott.geometry('472x410+350+160')
    searchroott.title('Fitness Center Management System')
    searchroott.config(bg='blue')
    searchroott.iconbitmap('Gym.ico')
    searchroott.resizable(False, False)
    # --------------------------------------------------- Search member Labels
    idlabel = Label(searchroott, text='Enter Train. Id: ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    Fitness_idlabel = Label(searchroott, text='Enter Fitness Id: ', bg='blue', font=('times', 20, 'bold'), width=12,
                            anchor='w')
    Fitness_idlabel.place(x=10, y=70)

    namelabel = Label(searchroott, text='Enter Name : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    namelabel.place(x=10, y=130)

    mobilelabel = Label(searchroott, text='Enter Mobile : ', bg='blue', font=('times', 20, 'bold'), width=12,
                        anchor='w')
    mobilelabel.place(x=10, y=190)

    emaillabel = Label(searchroott, text='Enter Email : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    emaillabel.place(x=10, y=250)

    addresslabel = Label(searchroott, text='Enter Address : ', bg='blue', font=('times', 20, 'bold'), width=12,
                         anchor='w')
    addresslabel.place(x=10, y=310)

    # Search Member Entry
    idval = StringVar()
    Fitness_idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()

    identry = Entry(searchroott, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    Fitness_identry = Entry(searchroott, font=('arial', 15, 'bold'), bd=5, textvariable=Fitness_idval, width='23')
    Fitness_identry.place(x=205, y=70)

    nameentry = Entry(searchroott, font=('arial', 15, 'bold'), bd=5, textvariable=nameval, width='23')
    nameentry.place(x=205, y=130)

    mobileentry = Entry(searchroott, font=('arial', 15, 'bold'), bd=5, textvariable=mobileval, width='23')
    mobileentry.place(x=205, y=190)

    emailentry = Entry(searchroott, font=('arial', 15, 'bold'), bd=5, textvariable=emailval, width='23')
    emailentry.place(x=205, y=250)

    addressentry = Entry(searchroott, font=('arial', 15, 'bold'), bd=5, textvariable=addressval, width='23')
    addressentry.place(x=205, y=310)

    # Add button
    submitbtn = Button(searchroott, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=searcht)
    submitbtn.place(x=150, y=360)
    searchroott.mainloop()


# Delete Trainer
def deletetrainer():
    cc = Trainertable.focus()
    content = Trainertable.item(cc)
    pp = content['values'][0]
    strr = 'delete from Trainer where id1=%s'
    my_cursor.execute(strr, pp)
    con.commit()
    messagebox.showinfo('Notifications', 'Id {} deleted successfully...'.format(pp))
    strr = 'select *from Trainer'
    my_cursor.execute(strr)
    datas = my_cursor.fetchall()
    Trainertable.delete(*Trainertable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
        Trainertable.insert('', END, values=vv)


# Update Trainer
def updatetrainer():
    def updatet():
        id1 = idval.get()
        Fitness_id = Fitness_idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()

        strr = 'update Trainer set Fitness_id=%s,name=%s,mobile=%s,email=%s,address=%s where id1=%s'
        my_cursor.execute(strr, (Fitness_id, name, mobile, email, address, id1))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified successfully...'.format(id1), parent=updateroott)
        strr = 'select *from Trainer'
        my_cursor.execute(strr)
        datas = my_cursor.fetchall()
        Trainertable.delete(*Trainertable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
            Trainertable.insert('', END, values=vv)

    updateroott = Toplevel(master=DataEntryFrame)
    updateroott.grab_set()
    updateroott.geometry('472x410+350+160')
    updateroott.title('Fitness Center Management System')
    updateroott.config(bg='blue')
    updateroott.iconbitmap('Gym.ico')
    updateroott.resizable(False, False)
    # --------------------------------------------------- Updater Trainer Labels
    idlabel = Label(updateroott, text='Enter Train. Id: ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    Fitness_idlabel = Label(updateroott, text='Enter Fitness Id: ', bg='blue', font=('times', 20, 'bold'), width=12,
                            anchor='w')
    Fitness_idlabel.place(x=10, y=70)

    namelabel = Label(updateroott, text='Enter Name : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    namelabel.place(x=10, y=130)

    mobilelabel = Label(updateroott, text='Enter Mobile : ', bg='blue', font=('times', 20, 'bold'), width=12,
                        anchor='w')
    mobilelabel.place(x=10, y=190)

    emaillabel = Label(updateroott, text='Enter Email : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    emaillabel.place(x=10, y=250)

    addresslabel = Label(updateroott, text='Enter Address : ', bg='blue', font=('times', 20, 'bold'), width=12,
                         anchor='w')
    addresslabel.place(x=10, y=310)

    # Update Trainer Entry
    idval = StringVar()
    Fitness_idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()

    identry = Entry(updateroott, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    Fitness_identry = Entry(updateroott, font=('arial', 15, 'bold'), bd=5, textvariable=Fitness_idval, width='23')
    Fitness_identry.place(x=205, y=70)

    nameentry = Entry(updateroott, font=('arial', 15, 'bold'), bd=5, textvariable=nameval, width='23')
    nameentry.place(x=205, y=130)

    mobileentry = Entry(updateroott, font=('arial', 15, 'bold'), bd=5, textvariable=mobileval, width='23')
    mobileentry.place(x=205, y=190)

    emailentry = Entry(updateroott, font=('arial', 15, 'bold'), bd=5, textvariable=emailval, width='23')
    emailentry.place(x=205, y=250)

    addressentry = Entry(updateroott, font=('arial', 15, 'bold'), bd=5, textvariable=addressval, width='23')
    addressentry.place(x=205, y=310)

    # Add button
    submitbtn = Button(updateroott, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=updatet)
    submitbtn.place(x=150, y=360)
    updateroott.mainloop()


# Show All Trainer
def showtrainer():
    strr = 'select *from Trainer'
    my_cursor.execute(strr)
    datas = my_cursor.fetchall()
    Trainertable.delete(*Trainertable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
        Trainertable.insert('', END, values=vv)


# Export Data Trainer
def exporttrainer():
    ff = filedialog.asksaveasfilename()
    gg = Trainertable.get_children()
    id1, Fitness_id, name, mobile, email, address = [], [], [], [], [], []
    for i in gg:
        content = Trainertable.item(i)
        pp = content['values']
        id1.append(pp[0]), Fitness_id.append(pp[1]), name.append(pp[2]), mobile.append(pp[3]), email.append(pp[4]),
        address.append(pp[5])
    dd = ['Id', 'Fitness Id', 'Name', 'Mobile', 'Email', 'Address']
    df = pandas.DataFrame(list(zip(id1, Fitness_id, name, mobile, email, address)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Trainer data is Saved {}'.format(paths))


# Add Branch
def addbranch():
    def submitaddb():
        id2 = idval.get()
        name = nameval.get()
        city = cityval.get()
        type = typeval.get()
        address = addressval.get()
        try:
            strr = 'insert into Branch values(%s,%s,%s,%s,%s)'
            my_cursor.execute(strr, (id2, name, city, type, address))
            con.commit()
            res = messagebox.askyesnocancel('Notifications', 'Id {} Name {} Added successfully..and want '
                                                             'to clean the form'.format(id2, name), parent=addrootb)
            if res:
                idval.set('')
                nameval.set('')
                cityval.set('')
                typeval.set('')
                addressval.set('')

        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=addrootb)
        strr = 'select * from Branch'
        my_cursor.execute(strr)
        datas = my_cursor.fetchall()
        Branchtable.delete(*Branchtable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            Branchtable.insert('', END, values=vv)

    addrootb = Toplevel(master=DataEntryFrame)
    addrootb.grab_set()
    addrootb.geometry('472x380+350+160')
    addrootb.title('Fitness Center Management System')
    addrootb.config(bg='blue')
    addrootb.iconbitmap('Gym.ico')
    addrootb.resizable(False, False)
    # --------------------------------------------------- Add Branch Labels
    idlabel = Label(addrootb, text='Enter Bran. Id: ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addrootb, text='Enter Name : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    namelabel.place(x=10, y=70)

    citylabel = Label(addrootb, text='Enter City : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    citylabel.place(x=10, y=130)

    typelabel = Label(addrootb, text='Enter Type : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    typelabel.place(x=10, y=190)

    addresslabel = Label(addrootb, text='Enter Address : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    # Add Branch Entry
    idval = StringVar()
    nameval = StringVar()
    cityval = StringVar()
    typeval = StringVar()
    addressval = StringVar()

    identry = Entry(addrootb, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    nameentry = Entry(addrootb, font=('arial', 15, 'bold'), bd=5, textvariable=nameval, width='23')
    nameentry.place(x=205, y=70)

    cityentry = Entry(addrootb, font=('arial', 15, 'bold'), bd=5, textvariable=cityval, width='23')
    cityentry.place(x=205, y=130)

    typeentry = Entry(addrootb, font=('arial', 15, 'bold'), bd=5, textvariable=typeval, width='23')
    typeentry.place(x=205, y=190)

    addressentry = Entry(addrootb, font=('arial', 15, 'bold'), bd=5, textvariable=addressval, width='23')
    addressentry.place(x=205, y=250)

    # Add button
    submitbtn = Button(addrootb, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=submitaddb)
    submitbtn.place(x=150, y=300)
    addrootb.mainloop()


# Search Branch
def searchbranch():
    def searchb():
        id2 = idval.get()
        name = nameval.get()
        city = cityval.get()
        type = typeval.get()
        address = addressval.get()

        if id2 != '':
            strr = 'select * from Branch where id2=%s'
            my_cursor.execute(strr, id2)
            datas = my_cursor.fetchall()
            Branchtable.delete(*Branchtable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Branchtable.insert('', END, values=vv)
        elif name != '':
            strr = 'select * from Branch where name=%s'
            my_cursor.execute(strr, name)
            datas = my_cursor.fetchall()
            Branchtable.delete(*Branchtable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Branchtable.insert('', END, values=vv)
        elif city != '':
            strr = 'select * from Branch where city=%s'
            my_cursor.execute(strr, city)
            datas = my_cursor.fetchall()
            Branchtable.delete(*Branchtable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Branchtable.insert('', END, values=vv)
        elif type != '':
            strr = 'select *from Branch where type=%s'
            my_cursor.execute(strr, type)
            datas = my_cursor.fetchall()
            Branchtable.delete(*Branchtable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Branchtable.insert('', END, values=vv)
        elif address != '':
            strr = 'select *from Branch where address=%s'
            my_cursor.execute(strr, address)
            datas = my_cursor.fetchall()
            Branchtable.delete(*Branchtable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Branchtable.insert('', END, values=vv)

    searchrootb = Toplevel(master=DataEntryFrame)
    searchrootb.grab_set()
    searchrootb.geometry('472x380+350+160')
    searchrootb.title('Fitness Center Management System')
    searchrootb.config(bg='blue')
    searchrootb.iconbitmap('Gym.ico')
    searchrootb.resizable(False, False)
    # --------------------------------------------------- Search Branch Labels
    idlabel = Label(searchrootb, text='Enter Bran. Id: ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    nameentrylabel = Label(searchrootb, text='Enter Name : ', bg='blue', font=('times', 20, 'bold'), width=12,
                           anchor='w')
    nameentrylabel.place(x=10, y=70)

    citylabel = Label(searchrootb, text='Enter City : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    citylabel.place(x=10, y=130)

    typelabel = Label(searchrootb, text='Enter Type : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    typelabel.place(x=10, y=190)

    addresslabel = Label(searchrootb, text='Enter Address : ', bg='blue', font=('times', 20, 'bold'), width=12,
                         anchor='w')
    addresslabel.place(x=10, y=250)

    # Search Branch Entry
    idval = StringVar()
    nameval = StringVar()
    cityval = StringVar()
    typeval = StringVar()
    addressval = StringVar()

    identry = Entry(searchrootb, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    nameentry = Entry(searchrootb, font=('arial', 15, 'bold'), bd=5, textvariable=nameval, width='23')
    nameentry.place(x=205, y=70)

    cityentry = Entry(searchrootb, font=('arial', 15, 'bold'), bd=5, textvariable=cityval, width='23')
    cityentry.place(x=205, y=130)

    typeentry = Entry(searchrootb, font=('arial', 15, 'bold'), bd=5, textvariable=typeval, width='23')
    typeentry.place(x=205, y=190)

    addressentry = Entry(searchrootb, font=('arial', 15, 'bold'), bd=5, textvariable=addressval, width='23')
    addressentry.place(x=205, y=250)

    # Add button
    submitbtn = Button(searchrootb, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=searchb)
    submitbtn.place(x=150, y=300)
    searchrootb.mainloop()


# Delete Branch
def deletebranch():
    cc = Branchtable.focus()
    content = Branchtable.item(cc)
    pp = content['values'][0]
    strr = 'delete from Branch where id2=%s'
    my_cursor.execute(strr, pp)
    con.commit()
    messagebox.showinfo('Notifications', 'Id {} deleted successfully...'.format(pp))
    strr = 'select *from Branch'
    my_cursor.execute(strr)
    datas = my_cursor.fetchall()
    Branchtable.delete(*Branchtable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4]]
        Branchtable.insert('', END, values=vv)


# Update Branch
def updatebranch():
    def updateb():
        id2 = idval.get()
        name = nameval.get()
        city = cityval.get()
        type = typeval.get()
        address = addressval.get()

        strr = 'update Branch set name=%s,city=%s,type=%s,address=%s where id2=%s'
        my_cursor.execute(strr, (name, city, type, address, id2))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified successfully...'.format(id2), parent=updaterootb)
        strr = 'select *from Branch'
        my_cursor.execute(strr)
        datas = my_cursor.fetchall()
        Branchtable.delete(*Branchtable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            Branchtable.insert('', END, values=vv)

    updaterootb = Toplevel(master=DataEntryFrame)
    updaterootb.grab_set()
    updaterootb.geometry('472x380+350+160')
    updaterootb.title('Fitness Center Management System')
    updaterootb.config(bg='blue')
    updaterootb.iconbitmap('Gym.ico')
    updaterootb.resizable(False, False)
    # --------------------------------------------------- Update Branch Labels
    idlabel = Label(updaterootb, text='Enter Bran. Id: ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    nameentrylabel = Label(updaterootb, text='Enter Name : ', bg='blue', font=('times', 20, 'bold'), width=12,
                           anchor='w')
    nameentrylabel.place(x=10, y=70)

    mobilelabel = Label(updaterootb, text='Enter City : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updaterootb, text='Enter Type : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updaterootb, text='Enter Address : ', bg='blue', font=('times', 20, 'bold'), width=12,
                         anchor='w')
    addresslabel.place(x=10, y=250)

    # Update Branch Entry
    idval = StringVar()
    nameval = StringVar()
    cityval = StringVar()
    typeval = StringVar()
    addressval = StringVar()

    identry = Entry(updaterootb, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    nameentry = Entry(updaterootb, font=('arial', 15, 'bold'), bd=5, textvariable=nameval, width='23')
    nameentry.place(x=205, y=70)

    cityentry = Entry(updaterootb, font=('arial', 15, 'bold'), bd=5, textvariable=cityval, width='23')
    cityentry.place(x=205, y=130)

    typeentry = Entry(updaterootb, font=('arial', 15, 'bold'), bd=5, textvariable=typeval, width='23')
    typeentry.place(x=205, y=190)

    addressentry = Entry(updaterootb, font=('arial', 15, 'bold'), bd=5, textvariable=addressval, width='23')
    addressentry.place(x=205, y=250)

    # Add button
    submitbtn = Button(updaterootb, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=updateb)
    submitbtn.place(x=150, y=300)
    updaterootb.mainloop()


# Show all Branch
def showbranch():
    strr = 'select *from Branch'
    my_cursor.execute(strr)
    datas = my_cursor.fetchall()
    Branchtable.delete(*Branchtable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4]]
        Branchtable.insert('', END, values=vv)


# Export all Branch
def exportbranch():
    ff = filedialog.asksaveasfilename()
    gg = Branchtable.get_children()
    id2, name, city, type, address = [], [], [], [], []
    for i in gg:
        content = Branchtable.item(i)
        pp = content['values']
        id2.append(pp[0]), name.append(pp[1]), city.append(pp[2]), type.append(pp[3]), address.append(pp[4])
    dd = ['Id', 'Name', 'City', 'Type', 'Address']
    df = pandas.DataFrame(list(zip(id2, name, city, type, address)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Branch data is Saved {}'.format(paths))


# Add Payment
def addpayment():
    def submitaddp():
        id3 = idval.get()
        customer_id = customer_idval.get()
        date = dateval.get()
        amount = amountval.get()
        description = descriptionval.get()
        try:
            strr = 'insert into Payment values(%s,%s,%s,%s,%s)'
            my_cursor.execute(strr, (id3, customer_id, date, amount, description))
            con.commit()
            res = messagebox.askyesnocancel('Notifications', 'Id {} Name {} Added successfully..and want to clean '
                                                             'the form'.format(id3, customer_id), parent=addrootp)
            if res:
                idval.set('')
                customer_idval.set('')
                dateval.set('')
                amountval.set('')
                descriptionval.set('')

        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=addrootp)
        strr = 'select * from Payment'
        my_cursor.execute(strr)
        datas = my_cursor.fetchall()
        Paymenttable.delete(*Paymenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            Paymenttable.insert('', END, values=vv)

    addrootp = Toplevel(master=DataEntryFrame)
    addrootp.grab_set()
    addrootp.geometry('472x380+350+160')
    addrootp.title('Fitness Center Management System')
    addrootp.config(bg='blue')
    addrootp.iconbitmap('Gym.ico')
    addrootp.resizable(False, False)
    # --------------------------------------------------- Add Payment Labels
    idlabel = Label(addrootp, text='Enter Pay. Id: ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    customer_identrylabel = Label(addrootp, text='Enter Custo. Id: ', bg='blue', font=('times', 20, 'bold'), width=12,
                                  anchor='w')
    customer_identrylabel.place(x=10, y=70)

    datelabel = Label(addrootp, text='Enter Date : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    datelabel.place(x=10, y=130)

    amountlabel = Label(addrootp, text='Enter Amount : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    amountlabel.place(x=10, y=190)

    descriptionlabel = Label(addrootp, text='Enter Descrip. : ', bg='blue', font=('times', 20, 'bold'), width=12,
                             anchor='w')
    descriptionlabel.place(x=10, y=250)

    # Add Payment Entry
    idval = StringVar()
    customer_idval = StringVar()
    dateval = StringVar()
    amountval = StringVar()
    descriptionval = StringVar()

    identry = Entry(addrootp, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    customer_identry = Entry(addrootp, font=('arial', 15, 'bold'), bd=5, textvariable=customer_idval, width='23')
    customer_identry.place(x=205, y=70)

    dateentry = Entry(addrootp, font=('arial', 15, 'bold'), bd=5, textvariable=dateval, width='23')
    dateentry.place(x=205, y=130)

    amountentry = Entry(addrootp, font=('arial', 15, 'bold'), bd=5, textvariable=amountval, width='23')
    amountentry.place(x=205, y=190)

    descriptionentry = Entry(addrootp, font=('arial', 15, 'bold'), bd=5, textvariable=descriptionval, width='23')
    descriptionentry.place(x=205, y=250)

    # Add button
    submitbtn = Button(addrootp, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=submitaddp)
    submitbtn.place(x=150, y=300)
    addrootp.mainloop()


# Search Payment
def searchpayment():
    def searchp():
        id3 = idval.get()
        customer_id = customer_idval.get()
        date = dateval.get()
        amount = amountval.get()
        description = descriptionval.get()

        if id3 != '':
            strr = 'select * from Payment where id3=%s'
            my_cursor.execute(strr, id3)
            datas = my_cursor.fetchall()
            Paymenttable.delete(*Paymenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Paymenttable.insert('', END, values=vv)
        elif customer_id != '':
            strr = 'select * from Payment where name=%s'
            my_cursor.execute(strr, customer_id)
            datas = my_cursor.fetchall()
            Paymenttable.delete(*Paymenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Paymenttable.insert('', END, values=vv)
        elif date != '':
            strr = 'select * from Payment where date=%s'
            my_cursor.execute(strr, date)
            datas = my_cursor.fetchall()
            Paymenttable.delete(*Paymenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Paymenttable.insert('', END, values=vv)
        elif amount != '':
            strr = 'select *from Payment where amount=%s'
            my_cursor.execute(strr, amount)
            datas = my_cursor.fetchall()
            Paymenttable.delete(*Paymenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Paymenttable.insert('', END, values=vv)
        elif description != '':
            strr = 'select *from Payment where description=%s'
            my_cursor.execute(strr, description)
            datas = my_cursor.fetchall()
            Paymenttable.delete(*Paymenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                Paymenttable.insert('', END, values=vv)

    searchrootp = Toplevel(master=DataEntryFrame)
    searchrootp.grab_set()
    searchrootp.geometry('472x380+350+160')
    searchrootp.title('Fitness Center Management System')
    searchrootp.config(bg='blue')
    searchrootp.iconbitmap('Gym.ico')
    searchrootp.resizable(False, False)
    # --------------------------------------------------- Search Payment Labels
    idlabel = Label(searchrootp, text='Enter Pay. Id: ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    customer_identrylabel = Label(searchrootp, text='Enter Custo. Id: ', bg='blue', font=('times', 20, 'bold'),
                                  width=12,
                                  anchor='w')
    customer_identrylabel.place(x=10, y=70)

    datelabel = Label(searchrootp, text='Enter Date : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    datelabel.place(x=10, y=130)

    amountlabel = Label(searchrootp, text='Enter Amount : ', bg='blue', font=('times', 20, 'bold'), width=12,
                        anchor='w')
    amountlabel.place(x=10, y=190)

    descriptionlabel = Label(searchrootp, text='Enter Descrip. : ', bg='blue', font=('times', 20, 'bold'), width=12,
                             anchor='w')
    descriptionlabel.place(x=10, y=250)

    # Search Payment Entry
    idval = StringVar()
    customer_idval = StringVar()
    dateval = StringVar()
    amountval = StringVar()
    descriptionval = StringVar()

    identry = Entry(searchrootp, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    customer_identry = Entry(searchrootp, font=('arial', 15, 'bold'), bd=5, textvariable=customer_idval, width='23')
    customer_identry.place(x=205, y=70)

    dateentry = Entry(searchrootp, font=('arial', 15, 'bold'), bd=5, textvariable=dateval, width='23')
    dateentry.place(x=205, y=130)

    amountentry = Entry(searchrootp, font=('arial', 15, 'bold'), bd=5, textvariable=amountval, width='23')
    amountentry.place(x=205, y=190)

    descriptionentry = Entry(searchrootp, font=('arial', 15, 'bold'), bd=5, textvariable=descriptionval, width='23')
    descriptionentry.place(x=205, y=250)

    # Add button
    submitbtn = Button(searchrootp, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=searchp)
    submitbtn.place(x=150, y=300)
    searchrootp.mainloop()


# Delete Payment
def deletepayment():
    cc = Paymenttable.focus()
    content = Paymenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from Payment where id3=%s'
    my_cursor.execute(strr, pp)
    con.commit()
    messagebox.showinfo('Notifications', 'Id {} deleted successfully...'.format(pp))
    strr = 'select *from Payment'
    my_cursor.execute(strr)
    datas = my_cursor.fetchall()
    Paymenttable.delete(*Paymenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4]]
        Paymenttable.insert('', END, values=vv)


# Update Payment
def updatepayment():
    def updatep():
        id3 = idval.get()
        customer_id = customer_idval.get()
        date = dateval.get()
        amount = amountval.get()
        description = descriptionval.get()

        strr = 'update Payment set customer_id=%s,date=%s,amount=%s,description=%s where id3=%s'
        my_cursor.execute(strr, (customer_id, date, amount, description, id3))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified successfully...'.format(id3), parent=updaterootp)
        strr = 'select *from Payment'
        my_cursor.execute(strr)
        datas = my_cursor.fetchall()
        Paymenttable.delete(*Paymenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            Paymenttable.insert('', END, values=vv)

    updaterootp = Toplevel(master=DataEntryFrame)
    updaterootp.grab_set()
    updaterootp.geometry('472x380+350+160')
    updaterootp.title('Fitness Center Management System')
    updaterootp.config(bg='blue')
    updaterootp.iconbitmap('Gym.ico')
    updaterootp.resizable(False, False)
    # --------------------------------------------------- Update Payment Labels
    idlabel = Label(updaterootp, text='Enter Pay. Id: ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    idlabel.place(x=10, y=10)

    customer_identrylabel = Label(updaterootp, text='Enter Custo. Id: ', bg='blue', font=('times', 20, 'bold'),
                                  width=12,
                                  anchor='w')
    customer_identrylabel.place(x=10, y=70)

    datelabel = Label(updaterootp, text='Enter Date : ', bg='blue', font=('times', 20, 'bold'), width=12, anchor='w')
    datelabel.place(x=10, y=130)

    amountlabel = Label(updaterootp, text='Enter Amount : ', bg='blue', font=('times', 20, 'bold'), width=12,
                        anchor='w')
    amountlabel.place(x=10, y=190)

    descriptionlabel = Label(updaterootp, text="Enter Descrip. : ", bg='blue', font=('times', 20, 'bold'), width=12,
                             anchor='w')
    descriptionlabel.place(x=10, y=250)

    # Update Payment Entry
    idval = StringVar()
    customer_idval = StringVar()
    dateval = StringVar()
    amountval = StringVar()
    descriptionval = StringVar()

    identry = Entry(updaterootp, font=('arial', 15, 'bold'), bd=5, textvariable=idval, width='23')
    identry.place(x=205, y=10)

    customer_identry = Entry(updaterootp, font=('arial', 15, 'bold'), bd=5, textvariable=customer_idval, width='23')
    customer_identry.place(x=205, y=70)

    dateentry = Entry(updaterootp, font=('arial', 15, 'bold'), bd=5, textvariable=dateval, width='23')
    dateentry.place(x=205, y=130)

    amountentry = Entry(updaterootp, font=('arial', 15, 'bold'), bd=5, textvariable=amountval, width='23')
    amountentry.place(x=205, y=190)

    descriptionentry = Entry(updaterootp, font=('arial', 15, 'bold'), bd=5, textvariable=descriptionval, width='23')
    descriptionentry.place(x=205, y=250)

    # Add button
    submitbtn = Button(updaterootp, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=updatep)
    submitbtn.place(x=150, y=300)
    updaterootp.mainloop()


# Show all Payment
def showpayment():
    strr = 'select *from Payment'
    my_cursor.execute(strr)
    datas = my_cursor.fetchall()
    Paymenttable.delete(*Paymenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4]]
        Paymenttable.insert('', END, values=vv)


# Export all Payment
def exportpayment():
    ff = filedialog.asksaveasfilename()
    gg = Paymenttable.get_children()
    id3, customer_id, date, amount, description = [], [], [], [], []
    for i in gg:
        content = Paymenttable.item(i)
        pp = content['values']
        id3.append(pp[0]), customer_id.append(pp[1]), date.append(pp[2]), amount.append(pp[3]), description.append(
            pp[4])
    dd = ['Id', 'Customer Id', 'Date', 'Amount', 'Description']
    df = pandas.DataFrame(list(zip(id3, customer_id, date, amount, description)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Payment data is Saved {}'.format(paths))


# Exit
def exitprogram():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if res:
        root.destroy()


# Connection of Database
def Connectdb():
    def submitdb():
        global con, my_cursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            my_cursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect please try again', parent=dbroot)
            return
        try:
            strr = 'create database FitnessCenterManagementSystem'
            my_cursor.execute(strr)
            strr = 'use FitnessCenterManagementSystem'
            my_cursor.execute(strr)
            strr = 'create table Member(id int,name varchar(20),age varchar(10),mobile varchar(12),email varchar(' \
                   '30),address varchar(100)) '
            my_cursor.execute(strr)
            strr = 'alter table Member modify column id int not null'
            my_cursor.execute(strr)
            strr = 'alter table Member modify column id int primary key'
            my_cursor.execute(strr)
            strr = 'create table Trainer(id1 int,Fitness_ID varchar(20),name varchar(20),mobile varchar(12),' \
                   'email varchar(30),address varchar(100))'
            my_cursor.execute(strr)
            strr = 'alter table Trainer modify column id1 int not null'
            my_cursor.execute(strr)
            strr = 'alter table Trainer modify column id1 int primary key'
            my_cursor.execute(strr)
            strr = 'create table Branch(id2 int,name varchar(20),city varchar(20),type varchar(100),address varchar(' \
                   '100)) '
            my_cursor.execute(strr)
            strr = 'alter table Branch modify column id2 int not null'
            my_cursor.execute(strr)
            strr = 'alter table Branch modify column id2 int primary key'
            my_cursor.execute(strr)
            strr = 'create table Payment(id3 int,Customer_ID varchar(20),date varchar(30),amount varchar(50),' \
                   'description varchar(100)) '
            my_cursor.execute(strr)
            strr = 'alter table Payment modify column id3 int not null'
            my_cursor.execute(strr)
            strr = 'alter table Payment modify column id3 int primary key'
            my_cursor.execute(strr)
            messagebox.showinfo('Notification',
                                'Database created and now you are connected connected to the database ....',
                                parent=dbroot)

        except:
            strr = 'use FitnessCenterManagementSystem'
            my_cursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database ....', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('Gym.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='blue')
    # -------------------------------Connect db Labels
    hostlabel = Label(dbroot, text="Enter Host : ", bg='blue', font=('times', 20, 'bold'), width=13, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text="Enter User : ", bg='blue', font=('times', 20, 'bold'), width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password : ", bg='blue', font=('times', 20, 'bold'), width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    # -------------------------Connect db Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('arial', 15, 'bold'), bd=5, textvariable=hostval, width='21')
    hostentry.place(x=226, y=10)

    userentry = Entry(dbroot, font=('arial', 15, 'bold'), bd=5, textvariable=userval, width='21')
    userentry.place(x=226, y=70)

    passwordentry = Entry(dbroot, font=('arial', 15, 'bold'), bd=5, textvariable=passwordval, width='21')
    passwordentry.place(x=226, y=130)

    # -------------------------------- Connect db button
    submitbutton = Button(dbroot, text='Submit', font=('roman', 15, 'bold'), bg='red', bd=5, width=20,
                          activebackground='blue',
                          activeforeground='white', command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()


# Time
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :' + date_string + "\n" + "Time : " + time_string)
    clock.after(200, tick)


# Tkinter
root = Tk()
root.title('Fitness Center Management System')
root.config(bg='blue')
root.geometry('1350x680+1+10')
root.iconbitmap('Gym.ico')
root.resizable(False, False)
# Frames
# Data Entry frame

DataEntryFrame = Frame(root, bg='blue', borderwidth='6', relief=RIDGE)
DataEntryFrame.place(x=3, y=80, width=330, height=600)

# Buttons
front_label = Label(DataEntryFrame, text='---Welcome---', width=15, font=('arial', 20, 'italic bold'), bg='blue')
front_label.place(x=20, y=0)

front_label2 = Label(DataEntryFrame, text='---Member---', width=9, font=('arial', 15, 'italic bold'), bg='blue')
front_label2.place(x=0, y=40)

add_btn_m = Button(DataEntryFrame, text='1. Add Member', width=15, bd=6, bg='skyblue3', activebackground='blue',
                   anchor='w', relief=RIDGE, activeforeground='white', command=addmember)
add_btn_m.place(x=0, y=70)

search_btn_m = Button(DataEntryFrame, text='2. Search Member', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=searchmember)
search_btn_m.place(x=0, y=110)

delete_btn_m = Button(DataEntryFrame, text='3. Delete Member', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=deletemember)
delete_btn_m.place(x=0, y=150)

update_btn_m = Button(DataEntryFrame, text='4. Update Member', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=updatemember)
update_btn_m.place(x=0, y=190)

show_all_btn_m = Button(DataEntryFrame, text='5. Show All', width=15, bd=6, bg='skyblue3', anchor='w',
                        activebackground='blue', relief=RIDGE, activeforeground='white', command=showmember)
show_all_btn_m.place(x=0, y=230)

export_btn_m = Button(DataEntryFrame, text='6. Export data', width=15, bd=6, bg='skyblue3', anchor='w',
                      activebackground='blue', relief=RIDGE, activeforeground='white', command=exportmember)
export_btn_m.place(x=0, y=270)

front_label3 = Label(DataEntryFrame, text='---Trainer---', width=9, font=('arial', 15, 'italic bold'), bg='blue')
front_label3.place(x=180, y=40)

add_btn_t = Button(DataEntryFrame, text='1. Add Trainer', width=15, bd=6, bg='skyblue3', activebackground='blue',
                   anchor='w'
                   , relief=RIDGE, activeforeground='white', command=addtrainer)
add_btn_t.place(x=180, y=70)

search_btn_t = Button(DataEntryFrame, text='2. Search Trainer', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=searchtrainer)
search_btn_t.place(x=180, y=110)

delete_btn_t = Button(DataEntryFrame, text='3. Delete Trainer', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=deletetrainer)
delete_btn_t.place(x=180, y=150)

update_btn_t = Button(DataEntryFrame, text='4. Update Trainer', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=updatetrainer)
update_btn_t.place(x=180, y=190)

show_all_btn_t = Button(DataEntryFrame, text='5. Show All', width=15, bd=6, bg='skyblue3', anchor='w',
                        activebackground='blue', relief=RIDGE, activeforeground='white', command=showtrainer)
show_all_btn_t.place(x=180, y=230)

export_btn_t = Button(DataEntryFrame, text='6. Export data', width=15, bd=6, bg='skyblue3', anchor='w',
                      activebackground='blue', relief=RIDGE, activeforeground='white', command=exporttrainer)
export_btn_t.place(x=180, y=270)

front_label4 = Label(DataEntryFrame, text='---Branch---', width=9, font=('arial', 15, 'italic bold'), bg='blue')
front_label4.place(x=0, y=300)

add_btn_b = Button(DataEntryFrame, text='1. Add Branch', width=15, bd=6, bg='skyblue3', activebackground='blue',
                   anchor='w'
                   , relief=RIDGE, activeforeground='white', command=addbranch)
add_btn_b.place(x=0, y=330)

search_btn_b = Button(DataEntryFrame, text='2. Search Branch', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=searchbranch)
search_btn_b.place(x=0, y=370)

delete_btn_b = Button(DataEntryFrame, text='3. Delete Branch', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=deletebranch)
delete_btn_b.place(x=0, y=410)

update_btn_b = Button(DataEntryFrame, text='4. Update Branch', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=updatebranch)
update_btn_b.place(x=0, y=450)

show_all_btn_b = Button(DataEntryFrame, text='5. Show All', width=15, bd=6, bg='skyblue3', anchor='w',
                        activebackground='blue', relief=RIDGE, activeforeground='white', command=showbranch)
show_all_btn_b.place(x=0, y=490)

export_btn_b = Button(DataEntryFrame, text='6. Export data', width=15, bd=6, bg='skyblue3', anchor='w',
                      activebackground='blue', relief=RIDGE, activeforeground='white', command=exportbranch)
export_btn_b.place(x=0, y=530)

front_label5 = Label(DataEntryFrame, text='---Payment---', width=9, font=('arial', 15, 'italic bold'), bg='blue')
front_label5.place(x=180, y=300)

add_btn_p = Button(DataEntryFrame, text='1. Add Payment', width=15, bd=6, bg='skyblue3', activebackground='blue',
                   anchor='w'
                   , relief=RIDGE, activeforeground='white', command=addpayment)
add_btn_p.place(x=180, y=330)

search_btn_p = Button(DataEntryFrame, text='2. Search Payment', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=searchpayment)
search_btn_p.place(x=180, y=370)

delete_btn_p = Button(DataEntryFrame, text='3. Delete Payment', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=deletepayment)
delete_btn_p.place(x=180, y=410)

update_btn_p = Button(DataEntryFrame, text='4. Update Payment', width=15, bd=6, bg='skyblue3', activebackground='blue'
                      , anchor='w', relief=RIDGE, activeforeground='white', command=updatepayment)
update_btn_p.place(x=180, y=450)

show_all_btn_p = Button(DataEntryFrame, text='5. Show All', width=15, bd=6, bg='skyblue3', anchor='w',
                        activebackground='blue', relief=RIDGE, activeforeground='white', command=showpayment)
show_all_btn_p.place(x=180, y=490)

export_btn_p = Button(DataEntryFrame, text='6. Export data', width=15, bd=6, bg='skyblue3', anchor='w',
                      activebackground='blue', relief=RIDGE, activeforeground='white', command=exportpayment)
export_btn_p.place(x=180, y=530)

exit_btn = Button(DataEntryFrame, text='7.  Exit', width=6, font=('arial', 10, "bold"), bd=3, bg='skyblue3',
                  activebackground='blue', relief=RIDGE, activeforeground='white', command=exitprogram)
exit_btn.place(x=120, y=558)

# Show data frame
ShowDataFrame = Frame(root, bg='blue', borderwidth='5', relief=RIDGE)
ShowDataFrame.place(x=400, y=80, width=950, height=600)

# Show member data frame
style = ttk.Style()
style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), foreground='blue', height=10)
style.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')
Membertable = Treeview(ShowDataFrame, columns=('Id', 'Name', 'Age', 'Mobile No', 'Email', 'Address'))
Membertable.heading('Id', text='Id')
Membertable.heading('Name', text='Name')
Membertable.heading('Age', text='Age')
Membertable.heading('Mobile No', text='Mobile No')
Membertable.heading('Email', text='Email')
Membertable.heading('Address', text='Address')
Membertable['show'] = 'headings'
Membertable.column('Id', width=70)
Membertable.column('Name', width=200)
Membertable.column('Age', width=70)
Membertable.column('Mobile No', width=100)
Membertable.column('Email', width=200)
Membertable.column('Address', width=200)
Membertable.place(x=0, y=0, width=940, height=150)

# Show trainer data frame
style1 = ttk.Style()
style1.configure('Treeview.Heading', font=('chiller', 20, 'bold'), foreground='blue')
style1.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')
Trainertable = Treeview(ShowDataFrame, columns=('Id', 'Fitness ID', 'Name', 'Mobile No', 'Email', 'Address'))
Trainertable.heading('Id', text='Id')
Trainertable.heading('Fitness ID', text='Fitness ID')
Trainertable.heading('Name', text='Name')
Trainertable.heading('Mobile No', text='Mobile No')
Trainertable.heading('Email', text='Email')
Trainertable.heading('Address', text='Address')
Trainertable['show'] = 'headings'
Trainertable.column('Id', width=70)
Trainertable.column('Fitness ID', width=100)
Trainertable.column('Name', width=200)
Trainertable.column('Mobile No', width=100)
Trainertable.column('Email', width=200)
Trainertable.column('Address', width=200)
Trainertable.place(x=0, y=150, width=940, height=150)

# Show Branch data frame
style2 = ttk.Style()
style2.configure('Treeview.Heading', font=('chiller', 20, 'bold'), foreground='blue')
style2.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')
Branchtable = Treeview(ShowDataFrame, columns=('Id', 'Name', 'City', 'Type', 'Address'))
Branchtable.heading('Id', text='Id')
Branchtable.heading('Name', text='Name')
Branchtable.heading('City', text='City')
Branchtable.heading('Type', text='Type')
Branchtable.heading('Address', text='Address')
Branchtable['show'] = 'headings'
Branchtable.column('Id', width=70)
Branchtable.column('Name', width=200)
Branchtable.column('City', width=100)
Branchtable.column('Type', width=200)
Branchtable.column('Address', width=200)
Branchtable.place(x=0, y=300, width=940, height=150)

# Show Payment data frame
style3 = ttk.Style()
style3.configure('Treeview.Heading', font=('chiller', 20, 'bold'), foreground='blue')
style3.configure('Treeview', font=('times', 15, 'bold'), background='cyan', foreground='black')
Paymenttable = Treeview(ShowDataFrame, columns=('Id', 'Customer ID', 'Date', 'Amount', 'Description'))
Paymenttable.heading('Id', text='Id')
Paymenttable.heading('Customer ID', text='Customer ID')
Paymenttable.heading('Date', text='Date')
Paymenttable.heading('Amount', text='Amount')
Paymenttable.heading('Description', text='Description')
Paymenttable['show'] = 'headings'
Paymenttable.column('Id', width=70)
Paymenttable.column('Customer ID', width=100)
Paymenttable.column('Date', width=200)
Paymenttable.column('Amount', width=100)
Paymenttable.column('Description', width=200)
Paymenttable.place(x=0, y=450, width=940, height=150)

# Main Label
MainLabel = Label(root, text='Welcome To Fitness Center Management System', font=('chiller', 30, 'italic bold'),
                  relief=RIDGE, borderwidth=4, width=40, bg='skyblue')
MainLabel.place(x=310, y=0)

# clock label
clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4, bg='lawn green')
clock.place(x=0, y=0)
tick()
# ConnectDatabaseButton Label
connectbutton = Button(root, text='Connect To Database', width=20, font=('chiller', 19, 'italic bold'), relief=RIDGE,
                       borderwidth=4, bg='green2',
                       activebackground='blue', activeforeground='white', command=Connectdb)
connectbutton.place(x=1136, y=0)
root.mainloop()
