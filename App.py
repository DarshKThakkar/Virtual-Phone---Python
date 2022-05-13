def AV(z1,z2,z3,z4,z5):
    
    import tkinter as tk
    from PIL import Image, ImageTk

    def back():
        v.destroy()
        from Android import main
        main(z1, z2, z3, z4, z5)

    def calculator():
        v.destroy()
        from Calculator import calci
        calci(z1,z2,z3,z4,z5)

    def camera():
        v.destroy()
        from Camera import Camera
        Camera(z1,z2,z3,z4,z5)

    def chrome():
        v.destroy()
        from Chrome import ch
        ch(z1,z2,z3,z4,z5, "app")

    def clock():
        v.destroy()
        from Clock import Cl
        Cl(z1,z2,z3,z4,z5)

    def mmt():
        v.destroy()
        from MMT import mmt
        mmt(z1,z2,z3,z4,z5)

    def message():
        v.destroy()
        from Messaging import messages
        messages(z1, z2, z3, z4, z5, "app")

    def P():
        v.destroy()
        import Phone
        Phone.Ph(z1,z2,z3,z4,z5, "app")

    def spotify():
        v.destroy()
        from Spotify_1 import Play1
        Play1(z1, z2, z3, z4, z5, 0)

    def WhatsApp():
        v.destroy()
        from WhatsApp_1 import WApp
        WApp(z1, z2, z3, z4, z5)

    def monopoly():
        v.destroy()
        from Mono import start
        start(z1,z2,z3,z4,z5)

    def YONO():
        v.destroy()
        from Yono_SBI import YO
        YO(z1,z2,z3,z4,z5)

    def Mole():
        v.destroy()
        from WACK import Main
        Main(z1,z2,z3,z4,z5)

    v=tk.Tk()
    v.title("O")

    canvas= tk.Canvas(v, width=400, height=600)

    i0 = Image.open("Apps_Vault.jpg")
    p0 = ImageTk.PhotoImage(i0)

    def Not():
        v.destroy()
        import Notifications
        Notifications.notification(z1,z2,z3,z4,z5,"apps")

    #---------------------------------------------------------

    i1 = Image.open("N.jpeg")
    p1 = ImageTk.PhotoImage(i1)
    b1=tk.Button(v, image=p1, width=390, height=27, relief="solid", command=Not)
    b1_window = canvas.create_window(200, 12, window=b1)

    #---------------------------------------------------------

    i2 = Image.open("Amazon.jpg")
    p2 = ImageTk.PhotoImage(i2)
    b2=tk.Button(v, image=p2, width=50, height=50, relief="groove", command="")
    b2_window = canvas.create_window(60, 130, window=b2)
    b2.configure(border=0, bg="lightgrey")

    l2=tk.Label(v, text="Amazon", relief="groove")
    l2_window = canvas.create_window(60, 163, window=l2)
    l2.configure(border=0, bg="Lightgrey", fg="Black")

    #---------------------------------------------------------

    i3 = Image.open("Calculator.jpg")
    p3 = ImageTk.PhotoImage(i3)
    b3=tk.Button(v, image=p3, width=50, height=50, relief="groove", command=calculator)
    b3_window = canvas.create_window(150, 130, window=b3)
    b3.configure(border=0, bg="Lightgrey")

    l3=tk.Label(v, text="Calculator", relief="groove")
    l3_window = canvas.create_window(150, 163, window=l3)
    l3.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------
    
    i4 = Image.open("Camera.jpg")
    p4 = ImageTk.PhotoImage(i4)
    b4=tk.Button(v, image=p4, width=50, height=50, relief="groove", command=camera)
    b4_window = canvas.create_window(240, 130, window=b4)
    b4.configure(border=0, bg="Lightgrey")

    l4=tk.Label(v, text="Camera", relief="groove")
    l4_window = canvas.create_window(240, 163, window=l4)
    l4.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------
 
    i5 = Image.open("Chrome.jpg")
    p5 = ImageTk.PhotoImage(i5)
    b5=tk.Button(v, image=p5, width=50, height=50, relief="groove", command=chrome)
    b5_window = canvas.create_window(330, 130, window=b5)
    b5.configure(border=0, bg="Lightgrey")

    l5=tk.Label(v, text="Chrome", relief="groove")
    l5_window = canvas.create_window(330, 163, window=l5)
    l5.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------

    i6 = Image.open("Clock.jpg")
    p6 = ImageTk.PhotoImage(i6)
    b6=tk.Button(v, image=p6, width=50, height=50, relief="groove", command=clock)
    b6_window = canvas.create_window(60, 230, window=b6)
    b6.configure(border=0, bg="Lightgrey")

    l6=tk.Label(v, text="Clock", relief="groove")
    l6_window = canvas.create_window(60, 263, window=l6)
    l6.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------

    i7 = Image.open("mmt.jpg")
    p7 = ImageTk.PhotoImage(i7)
    b7=tk.Button(v, image=p7, width=50, height=50, relief="groove", command=mmt)
    b7_window = canvas.create_window(150, 230, window=b7)
    b7.configure(border=0, bg="Lightgrey")

    l7=tk.Label(v, text="Make My Trip", relief="groove")
    l7_window = canvas.create_window(150, 263, window=l7)
    l7.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------

    i8 = Image.open("message.jpg")
    p8 = ImageTk.PhotoImage(i8)
    b8=tk.Button(v, image=p8, width=50, height=50, relief="groove", command=message)
    b8_window = canvas.create_window(240, 230, window=b8)
    b8.configure(border=0, bg="Lightgrey")

    l8=tk.Label(v, text="Message", relief="groove")
    l8_window = canvas.create_window(240, 263, window=l8)
    l8.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------

    i9 = Image.open("phone.jpg")
    p9 = ImageTk.PhotoImage(i9)
    b9=tk.Button(v, image=p9, width=50, height=50, relief="groove", command=P)
    b9_window = canvas.create_window(330, 230, window=b9)
    b9.configure(border=0, bg="Lightgrey")

    l9=tk.Label(v, text="Phone", relief="groove")
    l9_window = canvas.create_window(330, 263, window=l9)
    l9.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------

    i10 = Image.open("Spotify.jpg")
    p10 = ImageTk.PhotoImage(i10)
    b10=tk.Button(v, image=p10, width=50, height=50, relief="groove", command=spotify)
    b10_window = canvas.create_window(60, 330, window=b10)
    b10.configure(border=0, bg="Lightgrey")

    l10=tk.Label(v, text="Spotify", relief="groove")
    l10_window = canvas.create_window(60, 363, window=l10)
    l10.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------

    i11 = Image.open("WhatsApp.jpg")
    p11 = ImageTk.PhotoImage(i11)
    b11=tk.Button(v, image=p11, width=50, height=50, relief="groove", command=WhatsApp)
    b11_window = canvas.create_window(150, 330, window=b11)
    b11.configure(border=0, bg="Lightgrey")

    l11=tk.Label(v, text="WhatsApp", relief="groove")
    l11_window = canvas.create_window(150, 363, window=l11)
    l11.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------

    i12 = Image.open("Monopoly.jpg")
    p12 = ImageTk.PhotoImage(i12)
    b12=tk.Button(v, image=p12, width=50, height=50, relief="groove", command=monopoly)
    b12_window = canvas.create_window(240, 330, window=b12)
    b12.configure(border=0, bg="Lightgrey")

    l12=tk.Label(v, text="Monopoly", relief="groove")
    l12_window = canvas.create_window(240, 363, window=l12)
    l12.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------

    i13 = Image.open("SBI.jpg")
    p13 = ImageTk.PhotoImage(i13)
    b13=tk.Button(v, image=p13, width=50, height=50, relief="groove", command=YONO)
    b13_window = canvas.create_window(330, 330, window=b13)
    b13.configure(border=0, bg="Lightgrey")

    l13=tk.Label(v, text="YONO", relief="groove")
    l13_window = canvas.create_window(330, 363, window=l13)
    l13.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------

    i14 = Image.open("mole.png")
    p14 = ImageTk.PhotoImage(i14)
    b14=tk.Button(v, image=p14, width=50, height=50, relief="groove", command=Mole)
    b14_window = canvas.create_window(60, 427, window=b14)
    b14.configure(border=0, bg="Lightgrey")

    l14=tk.Label(v, text="WHAK MOLE", relief="groove")
    l14_window = canvas.create_window(60, 460, window=l14)
    l14.configure(border=0, bg="lightgrey", fg="Black")

    #---------------------------------------------------------
    
    i17 = Image.open("bn1.jpg")
    p17 = ImageTk.PhotoImage(i17)
        
    b17=tk.Button(v, image=p17, width=40, height=20, relief="groove", command=back)
    b17_window = canvas.create_window(100, 575, window=b17)
    b17.configure(border=0)

    i18 = Image.open("bn2.jpg")
    p18 = ImageTk.PhotoImage(i18)

    b18=tk.Button(v, image=p18, width=40, height=20, relief="groove", command=back)
    b18_window = canvas.create_window(200, 575, window=b18)
    b18.configure(border=0)

    i19 = Image.open("bn3.png")
    p19 = ImageTk.PhotoImage(i19)

    l=tk.Label(v, image=p19, width=40, height=20)
    l_window = canvas.create_window(300, 575, window=l)
    l.configure(border=1)

    #---------------------------------------------------------------------------------------------

    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    v.geometry("400x600")
    v.resizable(False, False)
    v.wm_attributes("-topmost", "true")

    width=400
    height=600
    sw = v.winfo_screenwidth()
    sh = v.winfo_screenheight()

    x=(sw/2) + 300
    y=(sh/2) - 300

    v.geometry("%dx%d+%d+%d" % (width, height, x, y))
    v.mainloop()
