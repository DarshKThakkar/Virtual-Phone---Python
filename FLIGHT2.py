import tkinter as tk
from PIL import Image, ImageTk
import datetime

Pass=1

def fly_2(z1,z2,z3,z4,z5):

    global Pass

    a=tk.Tk()
    a.title("O")

    canvas= tk.Canvas(a, width=1700, height=1000)

    i0 = Image.open("flight_2.jpg")
    p0 = ImageTk.PhotoImage(i0)

    #----------------------------------------------------------------------------------------------------------------------

    def back():
        a.destroy()
        from TRAIN import rail
        rail(z1,z2,z3,z4,z5)        

    i7 = Image.open("bm1.jpg")
    p7 = ImageTk.PhotoImage(i7)
        
    b7=tk.Button(a, image=p7, width=60, height=20, relief="groove", command=back)
    b7_window = canvas.create_window(600, 868, window=b7)
    b7.configure(border=2, bg="black")

    def home():
        a.destroy()
        from Android import main
        main(z1,z2,z3,z4,z5)

    i8 = Image.open("bm2.jpg")
    p8 = ImageTk.PhotoImage(i8)

    b8=tk.Button(a, image=p8, width=60, height=20, relief="groove", command=home)
    b8_window = canvas.create_window(850, 868, window=b8)
    b8.configure(border=2, bg="black")

    i9 = Image.open("bm3.jpg")
    p9 = ImageTk.PhotoImage(i9)

    l=tk.Label(a, image=p9, width=60, height=25, relief="groove")
    l_window = canvas.create_window(1100, 868, window=l)
    l.configure(border=2, bg="black")

    #------------------------------------------------------------------------------------------------------

    passenger=[1,2,3]

    c1=tk.StringVar()
    c1.set(1)

    def P(e):
        global Pass
        Pass=e

        if e==1:
            E4.configure(border=2, state="disabled")
            E5.configure(border=2, state="disabled")
            E6.configure(border=2, state="disabled")
            E7.configure(border=2, state="disabled")
            E8.configure(border=2, state="disabled")
            E9.configure(border=2, state="disabled")

        elif e==2:
            E4.configure(border=2, state="normal")
            E5.configure(border=2, state="normal")
            E6.configure(border=2, state="normal")
            E7.configure(border=2, state="disabled")
            E8.configure(border=2, state="disabled")
            E9.configure(border=2, state="disabled")

        elif e==3:
            E4.configure(border=2, state="normal")
            E5.configure(border=2, state="normal")
            E6.configure(border=2, state="normal")
            E7.configure(border=2, state="normal")
            E8.configure(border=2, state="normal")
            E9.configure(border=2, state="normal")


    d1=tk.OptionMenu(a, c1, *passenger, command=P)
    d1_window = canvas.create_window(385, 180, window=d1)
    d1.configure(border=2, bg="WHITE", font=("ARIAL",10), relief="flat")

    #------------------------------------------------------------------------------------------------------

    ID=["Adhaar Card","Driving Licence","Any Other ID"]

    c2=tk.StringVar()
    c2.set("Adhaar Card")

    d2=tk.OptionMenu(a, c2, *ID, command="")
    d2_window = canvas.create_window(417, 213, window=d2)
    d2.configure(border=2, bg="WHITE", font=("ARIAL",10), relief="flat")
    
    #------------------------------------------------------------------------------------------------------

    E1=tk.Entry(a, width=30, font="Calibri")
    E1_window = canvas.create_window(333, 379, window=E1)
    E1.configure(border=2)

    #------------------------------------------------------------------------------------------------------

    E2=tk.Entry(a, width=30, font="Calibri")
    E2_window = canvas.create_window(333, 410, window=E2)
    E2.configure(border=2)

    #------------------------------------------------------------------------------------------------------

    E3=tk.Entry(a, width=30, font="Calibri")
    E3_window = canvas.create_window(333, 441, window=E3)
    E3.configure(border=2)

    #------------------------------------------------------------------------------------------------------

    E4=tk.Entry(a, width=30, font="Calibri")
    E4_window = canvas.create_window(333, 544, window=E4)
    E4.configure(border=2, state="disabled")

    #------------------------------------------------------------------------------------------------------

    E5=tk.Entry(a, width=30, font="Calibri")
    E5_window = canvas.create_window(333, 574, window=E5)
    E5.configure(border=2, state="disabled")

    #------------------------------------------------------------------------------------------------------

    E6=tk.Entry(a, width=30, font="Calibri")
    E6_window = canvas.create_window(333, 605, window=E6)
    E6.configure(border=2, state="disabled")

    #------------------------------------------------------------------------------------------------------

    E7=tk.Entry(a, width=30, font="Calibri")
    E7_window = canvas.create_window(333, 704, window=E7)
    E7.configure(border=2, state="disabled")

    #------------------------------------------------------------------------------------------------------

    E8=tk.Entry(a, width=30, font="Calibri")
    E8_window = canvas.create_window(333, 734, window=E8)
    E8.configure(border=2, state="disabled")

    #------------------------------------------------------------------------------------------------------

    E9=tk.Entry(a, width=30, font="Calibri")
    E9_window = canvas.create_window(333, 765, window=E9)
    E9.configure(border=2, state="disabled")

    #------------------------------------------------------------------------------------------------------

    def Next():
        a.destroy()
        from Transaction2 import trans
        trans(z1,z2,z3,z4,z5,Pass)

    b1=tk.Button(a, text="Next", width=10, height=0, relief="groove", command=Next)
    b1_window = canvas.create_window(1050, 768, window=b1)
    b1.configure(border=2, font=("Arial 14 bold"), bg="deepskyblue")

    #--------------------------------------------------------------------------------------------------------
    
    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    a.resizable(False, False)
    a.attributes("-topmost", True)
    a.attributes("-fullscreen", True)
    a.mainloop()
