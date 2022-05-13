def CS(z1, z2, z3, z4, z5):
    
    import tkinter as tk
    from PIL import Image, ImageTk

    w1=tk.Tk()
    w1.title("O")

    canvas= tk.Canvas(w1, width=400, height=600)

    i0 = Image.open("Chat_Screen.jpg")
    p0 = ImageTk.PhotoImage(i0)

    def back():
        w1.destroy()
        from WhatsApp_1 import WApp
        WApp(z1, z2, z3, z4, z5)

    def home():
        w1.destroy()
        from Android import main
        main(z1, z2, z3, z4, z5)

    def Not():
        w1.destroy()
        import Notifications
        Notifications.notification(z1,z2,z3,z4,z5,"WhatApp")

    i1 = Image.open("N.jpeg")
    p1 = ImageTk.PhotoImage(i1)

    b0=tk.Button(w1, image=p1, width=410, height=27, command=Not)
    b0_window = canvas.create_window(200, 12, window=b0)
    b0.configure(border=0, bg="black")

    E=tk.Entry(w1, width=34, font="Calibri")
    E_window = canvas.create_window(190, 519, window=E)
    E.configure(border=2, bg="Grey", fg="Black")

    class F:
        h=0
        D=0
        

    def send():
        a=E.get()

        if len(a)>0 and len(a)<20 and F.D<10:

            E.delete(0, 'end')
            F.D+=1

            if F.h==0:
                F.h=200

            else:
                F.h+=30

            if len(a)<11:
                f=15
                w=11

            else:
                f=11
                w=13
            
            l=tk.Label(w1, text=" " + a, width=w, height=1)
            l_window = canvas.create_window(328, F.h, window=l)
            l.configure(border=0, bg="Black", fg="White", font=("Arial", f), anchor=tk.W)

    i2 = Image.open("Send.jpg")
    p2 = ImageTk.PhotoImage(i2)
    b2=tk.Button(w1, image=p2, width=28, height=28, command=send)
    b2_window = canvas.create_window(373, 520, window=b2)
    b2.configure(border=0)

    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    w1.resizable(False, False)
    w1.wm_attributes("-topmost", "true")

    """-----------------------------------------------------------"""

    i7 = Image.open("bn1.jpg")
    p7 = ImageTk.PhotoImage(i7)
        
    b7=tk.Button(w1, image=p7, width=40, height=20, relief="groove", command=back)
    b7_window = canvas.create_window(100, 575, window=b7)
    b7.configure(border=0)

    i8 = Image.open("bn2.jpg")
    p8 = ImageTk.PhotoImage(i8)

    b8=tk.Button(w1, image=p8, width=40, height=20, relief="groove", command=home)
    b8_window = canvas.create_window(200, 575, window=b8)
    b8.configure(border=0)

    i9 = Image.open("bn3.png")
    p9 = ImageTk.PhotoImage(i9)

    l1=tk.Label(w1, image=p9, width=40, height=20)
    l1_window = canvas.create_window(300, 575, window=l1)
    l1.configure(border=1)

    """-----------------------------------------------------------"""

    width=400
    height=600
    sw = w1.winfo_screenwidth()
    sh = w1.winfo_screenheight()

    x=(sw/2) + 300
    y=(sh/2) - 300

    w1.geometry("%dx%d+%d+%d" % (width, height, x, y))

    w1.mainloop()
