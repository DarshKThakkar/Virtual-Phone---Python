def Cl(z1, z2, z3, z4, z5):

    import tkinter as tk
    from PIL import Image, ImageTk
    from datetime import datetime
    from Stopwatch import SW

    c=tk.Tk()
    c.title("O")

    canvas= tk.Canvas(c, width=400, height=600)

    i0 = Image.open("Clock_Screen.jpg")
    p0 = ImageTk.PhotoImage(i0)

    def back():
        c.destroy()
        from App import AV
        AV(z1, z2, z3, z4, z5)

    def home():
        c.destroy()
        from Android import main
        main(z1, z2, z3, z4, z5)
    
    def Not():
        c.destroy()
        import Notifications
        Notifications.notification(z1,z2,z3,z4,z5,"clock")

    i1 = Image.open("N.jpeg")
    p1 = ImageTk.PhotoImage(i1)
    b1=tk.Button(c, image=p1, width=390, height=27, relief="solid", command=Not)
    b1_window = canvas.create_window(200, 12, window=b1)

    d=datetime.now().time()
    a=tk.StringVar()
    a.set(str(d)[:8])

    def time():
        d=datetime.now().time()
        s=(str(d)[:8])
        a.set(s)
        c.update()
        c.after(1000, time)

    def Stop():
        c.destroy()
        SW(z1, z2, z3, z4, z5)

    l1=tk.Label(c, textvariable=a)
    l1_window = canvas.create_window(200, 120, window=l1)
    l1.configure(border=0, bg="Black", fg="White", font=("Calibri", 60))

    b2=tk.Button(c, text="Stop Watch", width=10, command=Stop)
    b2_window = canvas.create_window(200, 500, window=b2)
    b2.configure(border=1, bg="maroon", fg="White")

    i7 = Image.open("bn1.jpg")
    p7 = ImageTk.PhotoImage(i7)
    b7=tk.Button(c, image=p7, width=40, height=20, relief="groove", command=back)
    b7_window = canvas.create_window(100, 575, window=b7)
    b7.configure(border=0)

    i8 = Image.open("bn2.jpg")
    p8 = ImageTk.PhotoImage(i8)
    b8=tk.Button(c, image=p8, width=40, height=20, relief="groove", command=home)
    b8_window = canvas.create_window(200, 575, window=b8)
    b8.configure(border=0)

    i9 = Image.open("bn3.png")
    p9 = ImageTk.PhotoImage(i9)
    l=tk.Label(c, image=p9, width=40, height=20)
    l_window = canvas.create_window(300, 575, window=l)
    l.configure(border=1)

    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    c.geometry("400x600")
    c.resizable(False, False)
    c.wm_attributes("-topmost", "true")

    width=400
    height=600
    sw = c.winfo_screenwidth()
    sh = c.winfo_screenheight()

    x=(sw/2) + 300
    y=(sh/2) - 300

    c.geometry("%dx%d+%d+%d" % (width, height, x, y))

    c.after(50, time)
    c.mainloop()
