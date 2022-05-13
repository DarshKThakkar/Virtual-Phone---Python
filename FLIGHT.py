import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime

def fly(z1,z2,z3,z4,z5):

    a=tk.Tk()
    a.title("O")

    canvas= tk.Canvas(a, width=1700, height=1000)

    i0 = Image.open("flight_1.jpg")
    p0 = ImageTk.PhotoImage(i0)

    #----------------------------------------------------------------------------------------------------------------------

    def back():
        a.destroy()
        from MMT import mmt_main
        mmt_main(z1,z2,z3,z4,z5)        

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

    D=datetime.now().date()
    B=str(D).split("-")

    options=["MUMBAI","DELHI","CHENNAI","KOLKATA","AHMEDABAD","VADODARA","SURAT","BANGALORE"]

    c1=tk.StringVar()
    c1.set("Choose Source")

    d1=tk.OptionMenu(a, c1, *options, command="")
    d1_window = canvas.create_window(260, 172, window=d1)
    d1.configure(border=0, bg="WHITE", font=("ARIAL",15))
    

    c2=tk.StringVar()
    c2.set("Choose Destination")

    d2=tk.OptionMenu(a, c2, *options, command="")
    d2_window = canvas.create_window(260, 238, window=d2)
    d2.configure(border=0, bg="WHITE", font=("ARIAL",15))
    

    date=[]
    for i in range(1,31):

        if len(str(i))==1:
            i="0"+str(i)
            date.append(str(i))

        else:
            date.append(str(i))

    c3=tk.StringVar()
    c3.set(B[2])

    d3=tk.OptionMenu(a, c3, *date, command="")
    d3_window = canvas.create_window(145, 301, window=d3)
    d3.configure(border=0, bg="WHITE", font=("ARIAL",13))
    

    mon=[]
    for i in range(1,13):
        
        if len(str(i))==1:
            i="0"+str(i)
            mon.append(str(i))

        else:
            mon.append(str(i))


    c4=tk.StringVar()
    c4.set(B[1])

    d4=tk.OptionMenu(a, c4, *mon, command="")
    d4_window = canvas.create_window(253, 303, window=d4)
    d4.configure(border=0, bg="WHITE", font=("ARIAL",12))
    

    ye=[]
    for i in range(2020,2026):
        ye.append(str(i))

    c5=tk.StringVar()
    c5.set(B[0])

    d5=tk.OptionMenu(a, c5, *ye, command="")
    d5_window = canvas.create_window(360, 303, window=d5)
    d5.configure(border=0, bg="WHITE", font=("ARIAL",12))

    def search():
        a.destroy()
        from FLIGHT2 import fly_2
        fly_2(z1,z2,z3,z4,z5)

    b1=tk.Button(a, text="SEARCH", width=14, height=0, relief="raised", command=search)
    b1_window = canvas.create_window(254, 370, window=b1)
    b1.configure(border=5, bg="light sea green", font=("Calibri 10 bold"))

    #----------------------------------------------------------------------------------------------------------------------

    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    a.resizable(False, False)
    a.attributes("-topmost", True)
    a.attributes("-fullscreen", True)
    a.mainloop()
