def YO(z1, z2, z3, z4, z5):

    import tkinter as tk
    from PIL import Image, ImageTk
    import time
    from Add_yono import Y1
    from Delete_yono import Y2
    from BAL_yono import Y3
    from Acc_SBI import Y4

    C=tk.Tk()
    C.title("O")

    canvas= tk.Canvas(C, width=400, height=600)
    i0 = Image.open("y1.jpg")
    p0 = ImageTk.PhotoImage(i0)
    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    def back():
        C.destroy()
        from App import AV
        AV(z1,z2,z3,z4,z5)

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

    def Acc():
        C.destroy()
        Y4(z1,z2,z3,z4,z5)

    b2=tk.Button(C, text="Acc. Info", width=9, relief="raised", command=Acc)
    b2_window = canvas.create_window(55, 247, window=b2)
    b2.configure(border=3, bg="Purple", fg="White")

    def bal():
        C.destroy()
        Y3(z1,z2,z3,z4,z5)

    b3=tk.Button(C, text="Balance", width=9, relief="raised", command=bal)
    b3_window = canvas.create_window(345, 247, window=b3)
    b3.configure(border=3, bg="Purple", fg="White")

    def add():
        C.destroy()
        Y1(z1,z2,z3,z4,z5)
    
    b4=tk.Button(C, text="Add Acc.", width=9, relief="raised", command=add)
    b4_window = canvas.create_window(152, 247, window=b4)
    b4.configure(border=3, bg="Purple", fg="White")

    def delete():
        C.destroy()
        Y2(z1,z2,z3,z4,z5)

    b5=tk.Button(C, text="Delete Acc.", width=9, relief="raised", command=delete)
    b5_window = canvas.create_window(248, 247, window=b5)
    b5.configure(border=3, bg="Purple", fg="White")

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
