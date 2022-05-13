def Y5(z1, z2, z3, z4, z5, lo, pa):

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

    L1=tk.StringVar()
    L1.set(" LOGIN_ID: ")

    L2=tk.StringVar()
    L2.set(" PASSWORD: ")

    L3=tk.StringVar()
    L3.set(" BALANCE: ")

    i1 = Image.open("N.jpeg")
    p1 = ImageTk.PhotoImage(i1)
    b1=tk.Button(C, image=p1, width=415, height=27, relief="solid", command=Not)
    b1_window = canvas.create_window(200, 12, window=b1)
    b1.configure(border=4, bg="black")

    l1=tk.Label(C, textvariable=L1,width=30, relief="sunken", anchor=tk.NW)
    l1_window=canvas.create_window(200, 165, window=l1)
    l1.configure(border=1, bg="Purple", fg="White" ,font=("Arial",11))

    l2=tk.Label(C, textvariable=L2,width=30, relief="sunken", anchor=tk.NW)
    l2_window=canvas.create_window(200, 205, window=l2)
    l2.configure(border=1, bg="Purple", fg="White" ,font=("Arial",11))

    l3=tk.Label(C, textvariable=L3, width=30, relief="sunken", anchor=tk.NW)
    l3_window=canvas.create_window(200, 245, window=l3)
    l3.configure(border=1, bg="Purple", fg="White" ,font=("Arial",11))

    mydb = mysql.connector.connect(host="localhost",user="root", password="dkt@2003", database="Project")
    mycursor = mydb.cursor()
    
    a=("SELECT * FROM BANK WHERE LOGIN_ID='"+str(lo)+"' AND PASSWORD='"+str(pa)+"'")
    mycursor.execute(a)

    for i in mycursor:
        L1.set(" LOGIN_ID:  " + str(i[0]))
        L2.set(" PASSWORD:  " + str(i[1]))
        L3.set(" BALANCE:  " + str(i[2]))

    def ok():
        C.destroy()
        YO(z1,z2,z3,z4,z5)

    b2=tk.Button(C, text="OK", width=13, relief="groove", command=ok)
    b2_window = canvas.create_window(200, 302, window=b2)
    b2.configure(border=4, bg="Black", fg="White")

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
