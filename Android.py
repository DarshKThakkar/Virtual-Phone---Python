def main(z1,z2,z3,z4,z5):

    import tkinter as tk
    from PIL import Image, ImageTk
    import sys

    a=tk.Tk() 
        
    a.title("O")

    canvas=tk.Canvas(a, width=400, height=600)

    def Not():
        a.destroy()
        import Notifications
        Notifications.notification(z1,z2,z3,z4,z5,"home")

    i1 = Image.open("N.jpeg")
    p1 = ImageTk.PhotoImage(i1)

    b0=tk.Button(a, image=p1, width=390, height=27, command=Not)
    b0_window = canvas.create_window(200, 12, window=b0)
    b0.configure(border=0)

    def search():
        a.destroy()
        from Google_Search import GS
        GS(z1,z2,z3,z4,z5)

    i2 = Image.open("Search.jpg")
    p2 = ImageTk.PhotoImage(i2)

    b2=tk.Button(a, image=p2, width=330, height=31, command=Not)
    b2_window = canvas.create_window(200, 80, window=b2)
    b2.configure(border=0)

    def search():
        a.destroy()
        from Google_Search import GS
        GS(z1,z2,z3,z4,z5)

    i2 = Image.open("Search.jpg")
    p2 = ImageTk.PhotoImage(i2)

    b2=tk.Button(a, image=p2, width=330, height=31, command=search)
    b2_window = canvas.create_window(200, 80, window=b2)
    b2.configure(border=0)

    def phone():
        a.destroy()
        from Phone import Ph
        Ph(z1,z2,z3,z4,z5,"home")

    i3 = Image.open("phone.jpg")
    p3 = ImageTk.PhotoImage(i3)

    b3=tk.Button(a, image=p3, width=50, height=50, command=phone)
    b3_window = canvas.create_window(65, 500, window=b3)
    b3.configure(border=0)

    def mess():
        a.destroy()
        from Messaging import messages
        messages(z1,z2,z3,z4,z5,"home")

    i4 = Image.open("message.jpg")
    p4 = ImageTk.PhotoImage(i4)

    b4=tk.Button(a, image=p4, width=50, height=50, command=mess)
    b4_window = canvas.create_window(153, 500, window=b4)
    b4.configure(border=0)

    def chrome():
        a.destroy()
        from Chrome import ch
        ch(z1,z2,z3,z4,z5,"home")

    i5 = Image.open("chrome.jpg")
    p5 = ImageTk.PhotoImage(i5)

    b5=tk.Button(a, image=p5, width=50, height=50, command=chrome)
    b5_window = canvas.create_window(240, 500, window=b5)
    b5.configure(border=0)

    def apps():
        a.destroy()
        from App import AV
        AV(z1,z2,z3,z4,z5)

    i6 = Image.open("Apps.jpg")
    p6 = ImageTk.PhotoImage(i6)

    b6=tk.Button(a, image=p6, width=50, height=50, command=apps)
    b6_window = canvas.create_window(330, 500, window=b6)
    b6.configure(border=0)

    def Exit():
        a.destroy()
        sys.exit()

    b=tk.Button(a, text="x", width=2, height=0, command=Exit)
    b_window = canvas.create_window(45, 13, window=b)
    b.configure(border=1, bg="Maroon", fg="White", font=("Arial",6))

    """-----------------------------------------------------------"""

    i7 = Image.open("bn1.jpg")
    p7 = ImageTk.PhotoImage(i7)
        
    b7=tk.Button(a, image=p7, width=40, height=20, relief="groove", command="")
    b7_window = canvas.create_window(100, 575, window=b7)
    b7.configure(border=0)

    i8 = Image.open("bn2.jpg")
    p8 = ImageTk.PhotoImage(i8)

    b8=tk.Button(a, image=p8, width=40, height=20, relief="groove", command="")
    b8_window = canvas.create_window(200, 575, window=b8)
    b8.configure(border=0)

    i9 = Image.open("bn3.png")
    p9 = ImageTk.PhotoImage(i9)

    l1=tk.Label(a, image=p9, width=40, height=20)
    l1_window = canvas.create_window(300, 575, window=l1)
    l1.configure(border=1)

    """-----------------------------------------------------------"""
    
    i0 = Image.open("B1.jpg")
    p0 = ImageTk.PhotoImage(i0)

    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()


    a.geometry("400x600")
    a.resizable(False, False)

    width=400
    height=600
    sw = a.winfo_screenwidth()
    sh = a.winfo_screenheight()

    x=(sw/2) + 300
    y=(sh/2) - 300

    a.attributes("-topmost", True)
    a.geometry("%dx%d+%d+%d" % (width, height, x, y))
    a.mainloop()
