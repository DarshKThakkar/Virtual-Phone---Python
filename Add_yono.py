def Y1(z1, z2, z3, z4, z5):

    import tkinter as tk
    from PIL import Image, ImageTk
    import time
    from Yono_SBI import YO
    import mysql.connector

    C=tk.Tk()
    C.title("O")

    canvas= tk.Canvas(C, width=400, height=600)
    i0 = Image.open("y2.jpg")
    p0 = ImageTk.PhotoImage(i0)
    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    def back():
        C.destroy()
        YO(z1,z2,z3,z4,z5)

    def home():
        C.destroy()
        import Android
        Android.main(z1,z2,z3,z4,z5)
        
    def Not():
        C.destroy()
        import Notifications
        Notifications.notification(z1,z2,z3,z4,z5,"yono")  

    i1 = Image.open("N.jpeg")
    p1 = ImageTk.PhotoImage(i1)
    b1=tk.Button(C, image=p1, width=415, height=27, relief="solid", command=Not)
    b1_window = canvas.create_window(200, 12, window=b1)
    b1.configure(border=4, bg="black")

    E1=tk.Entry(C, width=30, font="Calibri")
    E1_window = canvas.create_window(250, 165, window=E1)
    E1.configure(border=2)

    l1=tk.Label(C, text="Login_ID:",width=16, relief="sunken")
    l1_window=canvas.create_window(66, 165, window=l1)
    l1.configure(border=1, bg="Purple", fg="White" ,font=("Arial",8))

    E2=tk.Entry(C, width=30, font="Calibri", show="*")
    E2_window = canvas.create_window(250, 205, window=E2)
    E2.configure(border=2)

    l2=tk.Label(C, text="Password:",width=16, relief="sunken")
    l2_window=canvas.create_window(66, 205, window=l2)
    l2.configure(border=1, bg="Purple", fg="White" ,font=("Arial",8))

    E3=tk.Entry(C, width=30, font="Calibri", show="*")
    E3_window = canvas.create_window(250, 245, window=E3)
    E3.configure(border=2)

    l3=tk.Label(C, text="Repeat Password:", width=16, relief="sunken")
    l3_window=canvas.create_window(66, 245, window=l3)
    l3.configure(border=1, bg="Purple", fg="White" ,font=("Arial",8))

    def next():

        if E1.get()!="" and E2.get()!="" and E3.get()!="":

            if E2.get()==E3.get():

                mydb = mysql.connector.connect(host="localhost",user="root", password="dkt@2003", database="Project")
                mycursor = mydb.cursor()
                a="SELECT * FROM BANK"
                mycursor.execute(a)
                flag=0
                for i in mycursor:
                    
                    if i[0]==E1.get():
                        flag=1

                if flag==1:

                    def ok():
                        l.destroy()
                        C.destroy()
                        Y1(z1,z2,z3,z4,z5)
                    
                    l=tk.Tk()
                    l.title("")

                    B=tk.Button(l, text="OK", width="15", relief="groove", bg="black", fg="white", command=ok)
                    B.configure(border=1)
                    L=tk.Label(l, text="Login_Id already exists.", bg="black", fg="white")
                    L.pack()
                    B.pack()

                    l.resizable(False, False)
                    l.wm_attributes("-topmost", "true")

                    width=150
                    height=50
                    sw1 = l.winfo_screenwidth()
                    sh1 = l.winfo_screenheight()

                    x1=(sw1/2) + 420
                    y1=(sh1/2) - 50

                    l.geometry("%dx%d+%d+%d" % (width, height, x1, y1))
                    l.configure(bg="black")
                    
                    l.mainloop()

                else:
                    a=("Insert into bank values('" + str(E1.get()) + "','" + str(E2.get()) + "', 0)")
                    
                    mycursor.execute(a)
                    mydb.commit()
                    
                    def ok():
                        l.destroy()
                        C.destroy()
                        YO(z1,z2,z3,z4,z5)

                    l=tk.Tk()
                    l.title("")

                    B=tk.Button(l, text="OK", width="15", relief="groove", bg="black", fg="white", command=ok)
                    B.configure(border=1)
                    L=tk.Label(l, text="Account added.", bg="black", fg="white")
                    L.pack()
                    B.pack()

                    l.resizable(False, False)
                    l.wm_attributes("-topmost", "true")

                    width=150
                    height=50
                    sw1 = l.winfo_screenwidth()
                    sh1 = l.winfo_screenheight()

                    x1=(sw1/2) + 420
                    y1=(sh1/2) - 50

                    l.geometry("%dx%d+%d+%d" % (width, height, x1, y1))
                    l.configure(bg="black")
                    
                    l.mainloop()

                

            else:

                def ok():
                    C.destroy()
                    Y1(z1,z2,z3,z4,z5)
                        
                l=tk.Tk()
                l.title("")

                B=tk.Button(l, text="OK", width="15", relief="groove", bg="black", fg="white", command=ok)
                B.configure(border=1)
                L=tk.Label(l, text="Password not same.", bg="black", fg="white")
                L.pack()
                B.pack()

                l.resizable(False, False)
                l.wm_attributes("-topmost", "true")

                width=150
                height=50
                sw1 = l.winfo_screenwidth()
                sh1 = l.winfo_screenheight()

                x1=(sw1/2) + 420
                y1=(sh1/2) - 50

                l.geometry("%dx%d+%d+%d" % (width, height, x1, y1))
                l.configure(bg="black")
                
                l.mainloop()

    b2=tk.Button(C, text="ADD", width=13, relief="groove", command=next)
    b2_window = canvas.create_window(130, 312, window=b2)
    b2.configure(border=4, bg="Black", fg="White")

    b3=tk.Button(C, text="CANCEL", width=13, relief="groove", command=back)
    b3_window = canvas.create_window(260, 312, window=b3)
    b3.configure(border=4, bg="Black", fg="White")

    """-----------------------------------------------------------"""

    i7 = Image.open("bn1.jpg")
    p7 = ImageTk.PhotoImage(i7)
        
    b7=tk.Button(C, image=p7, width=40, height=20, relief="groove", command=back)
    b7_window = canvas.create_window(100, 575, window=b7)
    b7.configure(border=0)

    i8 = Image.open("bn2.jpg")
    p8 = ImageTk.PhotoImage(i8)

    b8=tk.Button(C, image=p8, width=40, height=20, relief="groove", command=home)
    b8_window = canvas.create_window(200, 575, window=b8)
    b8.configure(border=0)

    i9 = Image.open("bn3.png")
    p9 = ImageTk.PhotoImage(i9)

    l1=tk.Label(C, image=p9, width=40, height=20)
    l1_window = canvas.create_window(300, 575, window=l1)
    l1.configure(border=1)

    """-----------------------------------------------------------"""

    C.geometry("400x600")
    C.resizable(False, False)
    C.wm_attributes("-topmost", "true")

    width=400
    height=600
    sw = C.winfo_screenwidth()
    sh = C.winfo_screenheight()

    x=(sw/2) + 300
    y=(sh/2) - 300

    C.geometry("%dx%d+%d+%d" % (width, height, x, y))
    C.mainloop()
