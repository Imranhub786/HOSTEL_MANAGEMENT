from tkinter import *
import tkinter.messagebox as MessageBox
from mysql.connector import (connection)
from PIL import ImageTk, Image
from tkinter import ttk


# before executing change path of picture

def submit6():
    fee = Toplevel()
    fee.geometry("800x450")
    fee.title("INSERTION")

    bcg = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\hotel-booking-background_23-2148136947.jpg'))

    my_canvas = Canvas(fee, width=500, height=200)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bcg, anchor="nw")

    hostelid = Label(fee, text='ENTER  MONTH', font=('bold', 10))
    hostelid.place(x=40, y=50)

    sname = Label(fee, text='FEE STATUS', font=('bold', 10))
    sname.place(x=40, y=100)

    sname = Label(fee, text='HOSTEL ID', font=('bold', 10))
    sname.place(x=40, y=150)

    e1_month = Entry(fee, show=None, font=('Arial', 14))
    e1_status = Entry(fee, show=None, font=('Arial', 14))
    e1_hostelid = Entry(fee, show=None, font=('Arial', 14))

    e1_month.place(x=200, y=50)
    e1_status.place(x=200, y=100)
    e1_hostelid.place(x=200, y=150)

    def a6():
        feemonth = e1_month.get()
        fstatus = e1_status.get()
        hostelid = e1_hostelid.get()

        mydb = connection.MySQLConnection(
            host="localhost",
            user="root",
            passwd="shivam",
            database="hostel"

        )
        cursor = mydb.cursor()
        cursor.execute(
            "insert into fee(month,status,hostelid)values('" + feemonth + "','" + fstatus + "','" + hostelid + "')")
        cursor.execute("commit")

        MessageBox.showinfo("inserted values are!", "('" + feemonth + "','" + fstatus + "','" + hostelid + "')")
        cursor.execute("commit")

        e1_month.delete(0, 'end')
        e1_status.delete(0, 'end')
        e1_hostelid.delete(0, 'end')

        mydb.close()

    submitfee1 = Button(fee, text="SUBMIT", font=("italic", 15), bg="#10044d", fg="white", command=a6)
    submitfee1.place(x=200, y=190)
    fee.mainloop()


def submit5():
    show1 = Tk()
    mydb = connection.MySQLConnection(
        host="localhost",
        user="root",
        passwd="shivam",
        database="hostel"

    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM hostel.student;")
    student1 = cursor.fetchall()

    show1.title("SHOW")
    show1.configure(bg='#041d78')

    label = Label(show1, text="Student Records", font=("Arial", 10)).grid(row=0, columnspan=3)

    cols = ('hostelid', 'sname', 'address', 'phone', 'fathername', 'mothername', 'sem', 'roomno')
    listBox = ttk.Treeview(show1, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)

    # for row in rows:
    # insertdata=str(row[0])+ '  '+ row[1]+ ' '+row[2]+ ' '+ row[3]+ ' '+ row[4]+ '   '+ row[5]+ ' ' + str(row[6])
    # listBox = ttk.Treeview(show1, columns=insertdata, show='headings')
    # list.insert(list.size()+1,insertdata)

    i = 0
    for student in student1:
        for j in range(len(student)):
            e = Entry(listBox, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    show1.mainloop()

    mydb.close()


#UPDATION PROCESS


def submit4():
    update = Toplevel()
    update.geometry("800x450")
    update.title("UPDATION")

    bcg = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\hotel-booking-background_23-2148136947.jpg'))

    my_canvas = Canvas(update, width=800, height=450)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bcg, anchor="nw")

    hostelid = Label(update, text='ENTER HOSTELID', font=('bold', 10))
    hostelid.place(x=40, y=50)

    sname = Label(update, text='ENTER STUDENT NAME', font=('bold', 10))
    sname.place(x=40, y=100)

    address = Label(update, text='ENTER ADDRESS', font=('bold', 10))
    address.place(x=40, y=150)

    phone = Label(update, text='ENTER PHONE NUMBER', font=('bold', 10))
    phone.place(x=40, y=200)

    sem = Label(update, text='ENTER SEM', font=('bold', 10))
    sem.place(x=40, y=250)

    sem = Label(update, text='ENTER ROOM NUMBER', font=('bold', 10))
    sem.place(x=40, y=300)

    father = Label(update, text='ENTER Father Name', font=('bold', 10))
    father.place(x=40, y=350)

    mother = Label(update, text='ENTER Mother name', font=('bold', 10))
    mother.place(x=40, y=400)

    e1_hostelid = Entry(update, show=None, font=('Arial', 14))
    e1_sname = Entry(update, show=None, font=('Arial', 14))
    e1_phone = Entry(update, show=None, font=('Arial', 14))
    e1_address = Entry(update, show=None, font=('Arial', 14))
    e1_sem = Entry(update, show=None, font=('Arial', 14))

    e1_roomno = Entry(update, show=None, font=('Arial', 14))

    e1_father = Entry(update, show=None, font=('Arial', 14))
    e1_mother = Entry(update, show=None, font=('Arial', 14))

    e1_hostelid.place(x=200, y=50)
    e1_sname.place(x=200, y=100)
    e1_address.place(x=200, y=150)
    e1_phone.place(x=200, y=200)
    e1_sem.place(x=200, y=250)
    e1_roomno.place(x=200, y=300)

    e1_father.place(x=200, y=350)
    e1_mother.place(x=200, y=400)

    def a4():
        hostelid = e1_hostelid.get()
        sname = e1_sname.get()
        address = e1_address.get()
        phone = e1_phone.get()
        sem = e1_sem.get()
        roomno = e1_roomno.get()
        father = e1_father.get()
        mother = e1_mother.get()


        if (hostelid == "" or sname == "" or address == "" or phone == "" or sem == ""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            mydb = connection.MySQLConnection(
                host="localhost",
                user="root",
                passwd="shivam",
                database="hostel"

            )
            cursor = mydb.cursor()
            cursor.execute(
                "update student set sname='" + sname + "',address='" + address + "',phone='" + phone + "',sem='" + sem + "',roomno='" + roomno + "',father='"+ father + " ',mother='"+ mother+ "'where hostelid='" + hostelid + "'")
            cursor.execute("commit")

            MessageBox.showinfo("updating values are!",
                                " ('" + hostelid + "','" + sname + "','" + address + "','" + phone + "','" + sem + "',' "+ father +"',' "+ mother +" ')'")
            cursor.execute("commit")

            e1_hostelid.delete(0, 'end')
            e1_sname.delete(0, 'end')
            e1_address.delete(0, 'end')
            e1_phone.delete(0, 'end')
            e1_sem.delete(0, 'end')
            e1_roomno.delete(0, 'end')

            e1_father.delete(0, 'end')
            e1_mother.delete(0, 'end')

            MessageBox.showinfo("Update Status", "updated Successfully")
            mydb.close()

    update1 = Button(update, text="UPDATE", font=("italic", 15), bg="#10044d", fg="white", command=a4)
    update1.place(x=200, y=405)
    update.mainloop()


#UPDATION END


def submit2():
    insert = Toplevel()
    insert.geometry("800x500")
    insert.title("INSERTION")

    bcg = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\hotel-booking-background_23-2148136947.jpg'))

    my_canvas = Canvas(insert, width=800, height=450)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bcg, anchor="nw")

    hostelid = Label(insert, text='ENTER HOSTELID', font=('bold', 10))
    hostelid.place(x=40, y=50)

    sname = Label(insert, text='ENTER STUDENT NAME', font=('bold', 10))
    sname.place(x=40, y=100)

    address = Label(insert, text='ENTER ADDRESS', font=('bold', 10))
    address.place(x=40, y=150)

    phone = Label(insert, text='ENTER PHONE NUMBER', font=('bold', 10))
    phone.place(x=40, y=200)

    father = Label(insert, text='FATHER NAME', font=('bold', 10))
    father.place(x=40, y=250)

    mother = Label(insert, text='MOTHER NAME', font=('bold', 10))
    mother.place(x=40, y=300)

    sem = Label(insert, text='ENTER SEM', font=('bold', 10))
    sem.place(x=40, y=350)

    sem = Label(insert, text='ENTER ROOM NUMBER', font=('bold', 10))
    sem.place(x=40, y=400)

    e1_hostelid = Entry(insert, show=None, font=('Arial', 14))
    e1_sname = Entry(insert, show=None, font=('Arial', 14))
    e1_phone = Entry(insert, show=None, font=('Arial', 14))
    e1_address = Entry(insert, show=None, font=('Arial', 14))
    e1_father = Entry(insert, show=None, font=('Arial', 14))
    e1_mother = Entry(insert, show=None, font=('Arial', 14))
    e1_sem = Entry(insert, show=None, font=('Arial', 14))
    e1_roomno = Entry(insert, show=None, font=('Arial', 14))

    e1_hostelid.place(x=200, y=50)
    e1_sname.place(x=200, y=100)
    e1_address.place(x=200, y=150)
    e1_phone.place(x=200, y=200)
    e1_father.place(x=200, y=250)
    e1_mother.place(x=200, y=300)
    e1_sem.place(x=200, y=350)
    e1_roomno.place(x=200, y=400)

    def a1():
        hostelid = e1_hostelid.get()
        sname = e1_sname.get()
        address = e1_address.get()
        phone = e1_phone.get()
        father = e1_father.get()
        mother = e1_mother.get()
        sem = e1_sem.get()
        roomno = e1_roomno.get()

        if (hostelid == "" or sname == "" or address == "" or phone == "" or father == "" or mother == "" or sem == ""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            mydb = connection.MySQLConnection(
                host="localhost",
                user="root",
                passwd="shivam",
                database="hostel"

            )
            cursor = mydb.cursor()
            cursor.execute(
                "insert into student values('" + hostelid + " ','" + sname + "','" + address + "','" + phone + "','" + father + "','" + mother + "','" + sem + "','" + roomno + "')")
            cursor.execute("commit")

            MessageBox.showinfo("inserted values are!",
                                "('" + hostelid + "','" + sname + "','" + address + "','" + phone + "','" + father + "','" + mother + "','" + sem + "','" + roomno + "')")
            cursor.execute("commit")

            e1_hostelid.delete(0, 'end')
            e1_sname.delete(0, 'end')
            e1_address.delete(0, 'end')
            e1_phone.delete(0, 'end')
            e1_father.delete(0, 'end')
            e1_mother.delete(0, 'end')
            e1_sem.delete(0, 'end')
            e1_roomno.delete(0, 'end')

            MessageBox.showinfo("Insert Status", "Inserted Successfully")
            mydb.close()

    insert1 = Button(insert, text="INSERT", font=("italic", 15), bg="#10044d", fg="white", command=a1)
    insert1.place(x=200, y=450)
    insert.mainloop()


def submit3():
    dele = Toplevel()
    dele.geometry("400x400")
    dele.title("DELETION")

    bcg = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\hotel-booking-background_23-2148136947.jpg'))

    my_canvas = Canvas(dele, width=400, height=400)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bcg, anchor="nw")

    hostelid = Label(dele, text='ENTER HOSTELID', font=('bold', 20))
    hostelid.place(x=50, y=70)

    e1_hostelid = Entry(dele, show=None, font=('Arial', 15))

    e1_hostelid.place(x=50, y=130)

    def a2():
        if (e1_hostelid.get() == ""):
            MessageBox.showinfo("delete status", "ID is compolsary for delete")
        else:
            mydb = connection.MySQLConnection(
                host="localhost",
                user="root",
                passwd="shivam",
                database="hostel"

            )
            cursor = mydb.cursor()
            cursor.execute("delete from student where hostelid='" + e1_hostelid.get() + "'")
            cursor.execute("commit")

            MessageBox.showinfo("Delete Status", "Deleted Successfully")
            mydb.close()

    dele1 = Button(dele, text="DELETE", font=("italic", 15), bg="#5cf5f7", fg="#10044d", command=a2)
    dele1.place(x=100, y=190)
    dele.mainloop()


def option():
    option = Toplevel()
    option.geometry("1000x600")
    option.title("HOSTEL PAGE")

    bcg = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\hotel-booking-background_23-2148136947.jpg'))

    my_canvas = Canvas(option, width=1000, height=600)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bcg, anchor="nw")

    insert = Button(option, text="INSERT NEW STUDENT", font=("italic", 20), bg="#10044d", fg="white", command=submit2)
    insert.place(x=10, y=75)

    delete = Button(option, text="DELETE STUDENT", font=("italic", 20), bg="#10044d", fg="white", command=submit3)
    delete.place(x=10, y=150)

    update = Button(option, text="UPDATE STUDENT", font=("italic", 20), bg="#10044d", fg="white", command=submit4)
    update.place(x=10, y=250)

    total = Button(option, text="ENTER FEE DETAILS", font=("italic", 20), bg="#10044d", fg="white", command=submit6)
    total.place(x=750, y=75)

    details = Button(option, text="STUDENT DETAILS", font=("italic", 20), bg="#10044d", fg="white", command=submit5)
    details.place(x=750, y=150)

    info = Button(option, text="GET INFO", font=("italic", 20), bg="#10044d", fg="white", command=submit8)
    info.place(x=750, y=250)
    total = Button(option, text="GET FEE DETAILS", font=("italic", 20), bg="#10044d", fg="white", command=submit9)
    total.place(x=750, y=350)

    total = Button(option, text="Enter Room Details", font=("italic", 20), bg="#10044d", fg="white", command=submit11)
    total.place(x=10, y=350)

    option.mainloop()

def submit11():
        room = Toplevel()
        room.geometry("800x450")
        room.title("Room Details")

        bcg = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\hotel-booking-background_23-2148136947.jpg'))

        my_canvas = Canvas(room, width=500, height=200)
        my_canvas.pack(fill="both", expand=True)

        my_canvas.create_image(0, 0, image=bcg, anchor="nw")





        roomno = Label(room, text='ROOMNO', font=('bold', 10))
        roomno.place(x=40, y=50)

        noofbeds = Label(room, text='NO OF BEDS', font=('bold', 10))
        noofbeds.place(x=40, y=100)

        roomcapacity = Label(room, text='ROOM CAPACITY', font=('bold', 10))
        roomcapacity.place(x=40, y=150)

        e1_roomno = Entry(room, show=None, font=('Arial', 14))
        e1_noofbeds = Entry(room, show=None, font=('Arial', 14))
        e1_roomcapacity = Entry(room, show=None, font=('Arial', 14))

        e1_roomno.place(x=200, y=50)
        e1_noofbeds.place(x=200, y=100)
        e1_roomcapacity.place(x=200, y=150)

        def a22():
            roNo = e1_roomno.get()
            noOf = e1_noofbeds.get()
            roCap = e1_roomcapacity.get()

            mydb = connection.MySQLConnection(
                host="localhost",
                user="root",
                passwd="shivam",
                database="hostel"

            )
            cursor = mydb.cursor()
            cursor.execute(
                "insert into room(roomno,noofbeds,roomcapacity)values('" + roNo + "','" + noOf + "','" + roCap + "')")
            cursor.execute("commit")

            MessageBox.showinfo("inserted values are!", "('" + roNo + "','" + noOf + "','" + roCap + "')")
            cursor.execute("commit")

            '''e1_roomno.delete(0, 'end')
            e1_noofbeds.delete(0, 'end')
            e1_roomcapacity.delete(0, 'end')'''

            mydb.close()

        submitroom22 = Button(room, text="SUBMIT", font=("italic", 15), bg="#10044d", fg="white", command=a22)
        submitroom22.place(x=200, y=190)
        room.mainloop()


def submit8():
    show5 = Tk()
    mydb = connection.MySQLConnection(
        host="localhost",
        user="root",
        passwd="shivam",
        database="hostel"

    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM hostel.login;")
    student1 = cursor.fetchall()

    show5.title("SHOW")
    show5.configure(bg='#041d78')

    label = Label(show5, text="Student Records", font=("Arial", 10)).grid(row=0, columnspan=3)

    cols = ('hostelid', 'sname', 'place', 'sem', 'date', 'time')
    listBox = ttk.Treeview(show5, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)

    # for row in rows:
    # insertdata=str(row[0])+ '  '+ row[1]+ ' '+row[2]+ ' '+ row[3]+ ' '+ row[4]+ '   '+ row[5]+ ' ' + str(row[6])
    # listBox = ttk.Treeview(show1, columns=insertdata, show='headings')
    # list.insert(list.size()+1,insertdata)

    i = 0
    for student in student1:
        for j in range(len(student)):
            e = Entry(listBox, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    show5.mainloop()

    mydb.close()



def submit9():
    show7 = Tk()
    mydb = connection.MySQLConnection(
        host="localhost",
        user="root",
        passwd="shivam",
        database="hostel"

    )
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM hostel.fee;")
    student1 = cursor.fetchall()

    show7.title("SHOW")
    show7.configure(bg='#041d78')

    label = Label(show7, text="Student Records", font=("Arial", 10)).grid(row=0, columnspan=3)

    cols = ('hostelid', 'month', 'status')
    listBox = ttk.Treeview(show7, columns=cols, show='headings')

    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)

    # for row in rows:
    # insertdata=str(row[0])+ '  '+ row[1]+ ' '+row[2]+ ' '+ row[3]+ ' '+ row[4]+ '   '+ row[5]+ ' ' + str(row[6])
    # listBox = ttk.Treeview(show1, columns=insertdata, show='headings')
    # list.insert(list.size()+1,insertdata)

    i = 0
    for student in student1:
        for j in range(len(student)):
            e = Entry(listBox, width=20, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, student[j])
        i = i + 1
    show7.mainloop()

    mydb.close()








def Hostellogin():
    hostel = Toplevel()
    hostel.geometry("1920x1080")
    hostel.title("HOSTEL Login page")

    bcg = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\hotel-booking-background_23-2148136947.jpg'))

    my_canvas = Canvas(hostel, width=525, height=328)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bcg, anchor="nw")

    ide = Label(hostel, text='HOSTEL LOGIN PAGE', bg="#041d78", fg="#83e6e6", font=('bold', 20))

    ide.place(x=200, y=20)

    name = Label(hostel, text='USER NAME', font=('bold', 15))
    name.place(x=70, y=80)

    name = Label(hostel, text='PASSWORD', font=('bold', 15))
    name.place(x=70, y=130)

    e1 = Entry(hostel, show=None, font=('Arial', 17))
    e2 = Entry(hostel, show='*', font=('Arial', 17))
    e1.place(x=230, y=80)
    e2.place(x=230, y=130)

    def submit():
        name = e1.get()
        password = e2.get()

        if (name == "" or password == ""):
            MessageBox.showerror("Insert Status", "All Fields are required")
        else:

            mydb = connection.MySQLConnection(
                host="localhost",
                user="root",
                passwd="shivam",
                database="hostel"

            )
            mycursor = mydb.cursor()
            sql = "SELECT * FROM hostellogin WHERE  name = '%s' AND  password = '%s'" % (e1.get(), e2.get())

            mycursor.execute(sql)

            if mycursor.fetchone():

                MessageBox.showinfo("LOGIN Status", "successful")
                option()
                hostel.quit()

            else:

                MessageBox.showerror("LOGIN Status", "Invalid password or username")

    submits = Button(hostel, text="SUBMIT", font=("italic", 20), bg="#05f6fa", fg="blue", command=submit)
    submits.place(x=200, y=200)
    hostel.mainloop()


def login():
    login = Toplevel()
    login.geometry("1920x1080")
    login.title("student Login page")

    bcg = ImageTk.PhotoImage(Image.open(r'C:\Users\imran\Documents\project\hms\images\login.png'))

    my_canvas = Canvas(login, width=600, height=300)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bcg, anchor="nw")

    hostelid = Label(login, text='ENTER YOUR HOSTELID', font=('bold', 10))
    hostelid.place(x=20, y=30)

    sname = Label(login, text='ENTER YOUR NAME', font=('bold', 10))
    sname.place(x=20, y=70)

    place = Label(login, text='ENTER PLACE', font=('bold', 10))
    place.place(x=20, y=100)

    sem = Label(login, text='ENTER SEM', font=('bold', 10))
    sem.place(x=20, y=130)

    date= Label(login, text='ENTER DATE', font=('bold', 10))
    date.place(x=20, y=160)

    time = Label(login, text='ENTER TIME', font=('bold', 10))
    time.place(x=20, y=190)

    e1_sname = Entry(login, show=None, font=('Arial', 14))
    e1_hostelid = Entry(login, show=None, font=('Arial', 14))
    e1_place = Entry(login, show=None, font=('Arial', 14))
    e1_sem = Entry(login, show=None, font=('Arial', 14))
    e1_date = Entry(login, show=None, font=('Arial', 14))
    e1_time = Entry(login, show=None, font=('Arial', 14))

    e1_hostelid.place(x=200, y=30)
    e1_sname.place(x=200, y=70)
    e1_place.place(x=200, y=100)
    e1_sem.place(x=200, y=130)
    e1_date.place(x=200, y=160)
    e1_time.place(x=200, y=190)

    def loginsubmit():
        hostelid = e1_hostelid.get()
        sname = e1_sname.get()
        place = e1_place.get()
        sem = e1_sem.get()
        date = e1_date.get()
        time = e1_time.get()

        if (hostelid == "" or sname == "" or place == "" or sem == "" or date == "" or time == ""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            con = connection.MySQLConnection(host="localhost", user="root", password="shivam", database="hostel")
            cursor = con.cursor()
            cursor.execute(
                "insert into login (hostelid,sname,place,sem,date,time) values('" + hostelid + "','" + sname + "','" + place + "','" + sem + "','" + date + "','" + time + "')")
            cursor.execute("commit")
            MessageBox.showinfo("Insert Status", "Inserted Successfully")

            cursor.execute("commit")

            e1_hostelid.delete(0, 'end')
            e1_sname.delete(0, 'end')
            e1_place.delete(0, 'end')
            e1_sem.delete(0, 'end')
            e1_date.delete(0, 'end')
            e1_time.delete(0, 'end')

            con.close()

    loginsubmit = Button(login, text="SUBMIT", font=("italic", 15), bg="#8cfffb", command=loginsubmit)
    loginsubmit.place(x=130, y=250)
    login.mainloop()


def logout():
    logout = Toplevel()
    logout.geometry("1920x1080")
    logout.title("student Login page")

    bcg = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\hotel-booking-background_23-2148136947.jpg'))

    my_canvas = Canvas(logout, width=600, height=300)
    my_canvas.pack(fill="both", expand=True)

    my_canvas.create_image(0, 0, image=bcg, anchor="nw")

    sname = Label(logout, text='ENTER YOUR NAME', font=('bold', 10))
    sname.place(x=20, y=30)

    hostelid = Label(logout, text='ENTER YOUR HOSTELID', font=('bold', 10))
    hostelid.place(x=20, y=60)

    place = Label(logout, text='ENTER PLACE', font=('bold', 10))
    place.place(x=20, y=100)

    sem = Label(logout, text='ENTER SEM', font=('bold', 10))
    sem.place(x=20, y=130)

    date = Label(logout, text='ENTER DATE', font=('bold', 10))
    date.place(x=20, y=160)

    time = Label(logout, text='ENTER TIME', font=('bold', 10))
    time.place(x=20, y=190)

    e1_sname = Entry(logout, show=None, font=('Arial', 14))
    e1_hostelid = Entry(logout, show=None, font=('Arial', 14))
    e1_place = Entry(logout, show=None, font=('Arial', 14))
    e1_sem = Entry(logout, show=None, font=('Arial', 14))
    e1_date = Entry(logout, show=None, font=('Arial', 14))
    e1_time = Entry(logout, show=None, font=('Arial', 14))

    e1_hostelid.place(x=200, y=30)
    e1_sname.place(x=200, y=70)
    e1_place.place(x=200, y=100)
    e1_sem.place(x=200, y=130)
    e1_date.place(x=200, y=160)
    e1_time.place(x=200, y=190)

    def logoutsubmit():
        hostelid = e1_hostelid.get()
        sname = e1_sname.get()
        place = e1_place.get()
        sem = e1_sem.get()
        date = e1_date.get()
        time = e1_time.get()

        if (hostelid == "" or sname == "" or place == "" or sem == "" or date == "" or time == ""):
            MessageBox.showinfo("Insert Status", "All Fields are required")
        else:
            con = connection.MySQLConnection(host="localhost", user="root", password="shivam", database="hostel")
            cursor = con.cursor()
            cursor.execute(
                "insert into logout (hostelid,sname,place,sem,date,time)  values('" + hostelid + "','" + sname + "','" + place + "','" + sem + "','" + date + "','" + time + "')")
            cursor.execute("commit")
            MessageBox.showinfo("Insert Status", "Inserted Successfully")

            e1_hostelid.delete(0, 'end')
            e1_sname.delete(0, 'end')
            e1_place.delete(0, 'end')
            e1_sem.delete(0, 'end')
            e1_date.delete(0, 'end')
            e1_time.delete(0, 'end')
            con.close()

    logoutsubmit = Button(logout, text="SUBMIT", font=("italic", 15), bg="#0afff7", command=logoutsubmit)
    logoutsubmit.place(x=130, y=250)

    logout.mainloop()


def LOG():
    log = Toplevel()
    log.geometry("1920x1080")
    log.title("LOG PAGE")
    # log.configure(bg='blue')
    back = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\360_F_219669327_v12pBKc7TB62E3uCJrgRRkDhfVENK3z5.jpg'))

    my_canvas1 = Canvas(log, width=600, height=500)
    my_canvas1.pack()

    my_canvas1.create_image(0, 0, image=back, anchor="nw")

    ide = Label(log, text="HOSTEL", bg="GRAY", fg="#83e6e6", font=('bold', 30))

    ide.place(x=250, y=40)

    butLI = Button(log, text="LOGIN", font=("italic", 20), bg="#07f7cb", command=lambda: [login()])
    butLI.place(x=190, y=200)

    butLO = Button(log, text="LOGOUT", font=("italic", 20), bg="#07f7cb", command=logout)
    butLO.place(x=190, y=300)

    log.mainloop()


def root():
    root = Tk()

    root.geometry("1920x1080")
    root.title("HOSTEL DATABASE")

    canvas = Canvas(root, width=1920, height=1080)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(r'C:\Users\Imran Hussain\Desktop\python\360_F_219669327_v12pBKc7TB62E3uCJrgRRkDhfVENK3z5.jpg'))
    canvas.create_image(20, 20, anchor=NW, image=img)

    ide = Label(root, text='LOGIN PAGE', bg="#041d78", fg="#83e6e6", font=('bold', 30))

    ide.place(x=180, y=30)

    but1 = Button(root, text="HOSTEL LOGIN", font=("italic", 20), bg="AQUA", command=lambda: [Hostellogin()])

    but1.place(x=190, y=170)

    but2 = Button(root, text="STUDENT LOGIN", font=("italic", 20), bg="AQUA", command=lambda: [LOG(), root.quit])
    but2.place(x=190, y=250)
    root.mainloop()


root()
exit(0)




