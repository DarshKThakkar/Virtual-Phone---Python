def WApp(z1,z2,z3,z4,z5):

    import tkinter as tk
    from PIL import Image, ImageTk

    w=tk.Tk()

    def back():
        w.destroy()
        from App import AV
        AV(z1, z2, z3, z4, z5)

    def home():
        w.destroy()
        from Android import main
        main(z1, z2, z3, z4, z5)
        
    w.title("O")

    canvas=tk.Canvas(w, width=400, height=600)


    def Not():
        w.destroy()
        import Notifications
        Notifications.notification(z1,z2,z3,z4,z5,"WhatApp")

    i1 = Image.open("N.jpeg")
    p1 = ImageTk.PhotoImage(i1)

    b0=tk.Button(w, image=p1, width=390, height=27, command=Not)
    b0_window = canvas.create_window(200, 12, window=b0)
    b0.configure(border=0)

    def text():
        w.destroy()
        from WhatsApp_2 import CS
        CS(z1, z2, z3, z4, z5)

    b1=tk.Button(w, text="Message", width=7, height=0, command=text)
    b1_window = canvas.create_window(366, 150, window=b1)
    b1.configure(border=1, bg="Green", fg="White", font=("Arial", 7))

    b2=tk.Button(w, text="Message", width=7, height=0, command="")
    b2_window = canvas.create_window(366, 210, window=b2)
    b2.configure(border=1, bg="Green", fg="White", font=("Arial", 7))

    b3=tk.Button(w, text="Message", width=7, height=0, command="")
    b3_window = canvas.create_window(366, 273, window=b3)
    b3.configure(border=1, bg="Green", fg="White", font=("Arial", 7))

    b4=tk.Button(w, text="Message", width=7, height=0, command="")
    b4_window = canvas.create_window(366, 335, window=b4)
    b4.configure(border=1, bg="Green", fg="White", font=("Arial", 7))

    """-----------------------------------------------------------"""

    i7 = Image.open("bn1.jpg")
    p7 = ImageTk.PhotoImage(i7)
        
    b7=tk.Button(w, image=p7, width=40, height=20, relief="groove", command=back)
    b7_window = canvas.create_window(100, 575, window=b7)
    b7.configure(border=0)

    i8 = Image.open("bn2.jpg")
    p8 = ImageTk.PhotoImage(i8)

    b8=tk.Button(w, image=p8, width=40, height=20, relief="groove", command=home)
    b8_window = canvas.create_window(200, 575, window=b8)
    b8.configure(border=0)

    i9 = Image.open("bn3.png")
    p9 = ImageTk.PhotoImage(i9)

    l1=tk.Label(w, image=p9, width=40, height=20)
    l1_window = canvas.create_window(300, 575, window=l1)
    l1.configure(border=1)

    """-----------------------------------------------------------"""

    i0 = Image.open("WhatsApp_Screen.jpg")
    p0 = ImageTk.PhotoImage(i0)

    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()


    w.geometry("400x600")
    w.resizable(False, False)

    width=400
    height=600
    sw = w.winfo_screenwidth()
    sh = w.winfo_screenheight()

    x=(sw/2) + 300
    y=(sh/2) - 300

    w.geometry("%dx%d+%d+%d" % (width, height, x, y))
    w.mainloop()
