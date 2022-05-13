def call(o, z1, z2, z3, z4, z5, w):

    import tkinter as tk
    from PIL import Image, ImageTk
    from pygame import mixer, time
    import time as t
    import random
    import multiprocessing
            
    c=tk.Tk()
    c.title("O")

    mixer.init()
    mixer.music.set_volume(0.02)

    

    class C:
        Speaker="off"
        Mic="on"
        
    canvas=tk.Canvas(width=400, height=600)

    def CUT():
        mixer.music.pause()
        import Phone
        c.destroy()
        Phone.Ph(z1, z2, z3, z4, z5, w)

    i1=Image.open("Cut.jpg")
    p1=ImageTk.PhotoImage(i1)
    b1=tk.Button(c, image=p1, width=50, height=50, command=CUT)
    b1_window= canvas.create_window(200, 500, window=b1)
    b1.configure(border=0, bg="black", fg="black")
        
    i2=Image.open("speaker_off.jpg")
    p2=ImageTk.PhotoImage(i2)

    def speaker():

        if C.Speaker=="off":
            b2.configure(border=2, bg="orange")
            mixer.music.set_volume(1)
            C.Speaker="on"

        elif C.Speaker=="on":
            b2.configure(border=0, bg="black")
            mixer.music.set_volume(0.02)
            C.Speaker="off"

    def mic():

        if C.Mic=="on":
            b3.configure(border=1, bg="orange")
            C.Mic="off"

        elif C.Mic=="off":
            b3.configure(border=0, bg="black")
            C.Mic="on"
            
                         
    b2=tk.Button(c, image=p2, width=40, height=40, command=speaker)
    b2_window= canvas.create_window(110, 500, window=b2)
    b2.configure(border=0, bg="black", fg="black")

    i3=Image.open("mic_on.jpg")
    p3=ImageTk.PhotoImage(i3)
    b3=tk.Button(c, image=p3, width=40, height=40, command=mic)
    b3_window= canvas.create_window(284, 500, window=b3)
    b3.configure(border=0, bg="black", fg="black")

    i4=Image.open("hold.jpg")
    p4=ImageTk.PhotoImage(i4)
    l4=tk.Label(c, image=p4, width=45, height=45)
    l4_window= canvas.create_window(284, 430, window=l4)
    l4.configure(border=0, bg="black", fg="black")

    i5=Image.open("AddCall.jpg")
    p5=ImageTk.PhotoImage(i5)
    l5=tk.Label(c, image=p5, width=45, height=45)
    l5_window= canvas.create_window(198, 430, window=l5)
    l5.configure(border=0, bg="black", fg="black")

    i6=Image.open("Video.jpg")
    p6=ImageTk.PhotoImage(i6)
    l6=tk.Label(c, image=p6, width=45, height=45)
    l6_window= canvas.create_window(110, 432, window=l6)
    l6.configure(border=0, bg="black", fg="black")

    i7=Image.open("pad.jpg")
    p7=ImageTk.PhotoImage(i7)
    l7=tk.Label(c, image=p7, width=45, height=45)
    l7_window= canvas.create_window(284, 366, window=l7)
    l7.configure(border=0, bg="black", fg="black")

    i8=Image.open("note.jpg")
    p8=ImageTk.PhotoImage(i8)
    l8=tk.Label(c, image=p8, width=45, height=45)
    l8_window= canvas.create_window(199, 366, window=l8)
    l8.configure(border=0, bg="black", fg="black")

    i9=Image.open("record.jpg")
    p9=ImageTk.PhotoImage(i9)
    l9=tk.Label(c, image=p9, width=45, height=45)
    l9_window= canvas.create_window(110, 368, window=l9)
    l9.configure(border=0, bg="black", fg="black")

    l9=tk.Label(c, text=o, width=10, height=0)
    l9_window= canvas.create_window(194, 140, window=l9)
    l9.configure(border=0, bg="black", fg="grey", font=("arialblack", 18))

    l10=tk.Label(c, text="Dialing...", width=10, height=0)
    l10_window= canvas.create_window(198, 167, window=l10)
    l10.configure(border=0, bg="black", fg="grey", font=("arialblack", 12))

    i0=Image.open("Call.jpg")
    p0=ImageTk.PhotoImage(i0)

    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    c.geometry("400x600")
    c.resizable(False, False)

    width=400
    height=600
    sw = c.winfo_screenwidth()
    sh = c.winfo_screenheight()

    x=(sw/2) + 300
    y=(sh/2) - 300
    
    c.geometry("%dx%d+%d+%d" % (width, height, x, y))

    if z3=="off":

        if (len(o)==10 or o=="100" or o=="102" or o=="103"):

            List=[1,2,3,4]
            rd=random.choice(List)

            if rd==1 or rd==4:
                mixer.music.load("notans.mp3")
                mixer.music.play()
                c.after(30500, CUT)

            elif rd==2:
                mixer.music.load("busy.mp3")
                mixer.music.play()
                c.after(12500, CUT)

            elif rd==3:
                mixer.music.load("Switchoff.mp3")
                mixer.music.play()
                c.after(17000, CUT)

            else:
                pass

        else:
            mixer.music.load("invalid.mp3")
            mixer.music.play()
            c.after(13200, CUT)
            

    else:
        l=tk.Tk()
        l.title("")

        def fl():
            l.destroy()
            CUT()

        B=tk.Button(l, text="OK", width="15", relief="groove", bg="black", fg="white", command=fl)
        B.configure(border=1)
        L=tk.Label(l, text="Flight Mode is on.", bg="black", fg="white")
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

    c.mainloop()
