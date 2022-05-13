from tkinter import *

def show(e):  
    card=Tk()
    card.title("Card")
    card.resizable(False, False)
    l=Label(card, text=e)
    l.pack()
    width=185
    height=180
    sw = card.winfo_screenwidth()
    sh = card.winfo_screenheight()

    x=(sw/2)
    y=(sh/2)

    card.geometry("%dx%d+%d+%d" % (width, height, x, y))
    card.attributes("-topmost", True)


def Property():
    
    C=Tk()
    C.title("PROPERTIES")
    C.attributes("-topmost",True)

    canvas=Canvas(C, width=200, height=780)

    def B1():
        f=open("Gydnia.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b1=Button(C, text="GYDNIA", width=20, command=B1)
    b1_window=canvas.create_window(0, 0, anchor=NW, window=b1)
    b1.configure(border=2, bg="Brown")

    def B2():
        f=open("TAIPEI.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b2=Button(C, text="TAIPEI", width=20, command=B2)
    b2_window=canvas.create_window(0, 28, anchor=NW, window=b2)
    b2.configure(border=2, bg="Brown")

    def B3():
        f=open("Rails.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b3=Button(C, text="READING RAILROAD", width=20, command=B3)
    b3_window=canvas.create_window(0, 56, anchor=NW, window=b3)
    b3.configure(border=2, bg="grey")

    def B4():
        f=open("TOKYO.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b4=Button(C, text="TOKYO", width=20, command=B4)
    b4_window=canvas.create_window(0, 84, anchor=NW, window=b4)
    b4.configure(border=2, bg="cyan")

    def B5():
        f=open("BARCELONA.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b5=Button(C, text="BARCELONA", width=20, command=B5)
    b5_window=canvas.create_window(0, 112, anchor=NW, window=b5)
    b5.configure(border=2, bg="cyan")

    def B6():
        f=open("ATHENS.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b6=Button(C, text="ATHENS", width=20, command=B6)
    b6_window=canvas.create_window(0, 140, anchor=NW, window=b6)
    b6.configure(border=2, bg="cyan")

    def B7():
        f=open("ISTANBUL.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b7=Button(C, text="ISTANBUL", width=20, command=B7)
    b7_window=canvas.create_window(0, 168, anchor=NW, window=b7)
    b7.configure(border=2, bg="magenta")

    def B22():
        f=open("UTILITY.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b22=Button(C, text="ELECTRIC COMPANY", width=20, command=B22)
    b22_window=canvas.create_window(0, 196, anchor=NW, window=b22)
    b22.configure(border=2, bg="grey")

    def B8():
        f=open("KYIV.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b8=Button(C, text="KYIV", width=20, command=B8)
    b8_window=canvas.create_window(0, 224, anchor=NW, window=b8)
    b8.configure(border=2, bg="magenta")

    def B9():
        f=open("TORONTO.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b9=Button(C, text="TORONTO", width=20, command=B9)
    b9_window=canvas.create_window(0, 252, anchor=NW, window=b9)
    b9.configure(border=2, bg="magenta")

    b23=Button(C, text="PENNSYLAVANIA", width=20, command=lambda:B3())
    b23_window=canvas.create_window(0, 280, anchor=NW, window=b23)
    b23.configure(border=2, bg="grey")

    def B10():
        f=open("ROME.txt","r")
        u=f.readlines()
        f.close()
        show(u)


    b10=Button(C, text="ROME", width=20, command=B10)
    b10_window=canvas.create_window(0, 308, anchor=NW, window=b10)
    b10.configure(border=2, bg="orange")

    def B11():
        f=open("SHANGHAI.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b11=Button(C, text="SHANGHAI", width=20, command=B11)
    b11_window=canvas.create_window(0, 336, anchor=NW, window=b11)
    b11.configure(border=2, bg="orange")

    def B12():
        f=open("VANCOUVER.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b12=Button(C, text="VANCOUVER", width=20, command=B12)
    b12_window=canvas.create_window(0, 364, anchor=NW, window=b12)
    b12.configure(border=2, bg="orange")

    def B13():
        f=open("SYDNEY.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b13=Button(C, text="SYDNEY", width=20, command=B13)
    b13_window=canvas.create_window(0, 392, anchor=NW, window=b13)
    b13.configure(border=2, bg="red")

    def B14():
        f=open("NEWYORK.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b14=Button(C, text="NEW YORK", width=20, command=B14)
    b14_window=canvas.create_window(0, 420, anchor=NW, window=b14)
    b14.configure(border=2, bg="red")

    def B15():
        f=open("LONDON.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b15=Button(C, text="LONDON", width=20, command=B15)
    b15_window=canvas.create_window(0, 448, anchor=NW, window=b15)
    b15.configure(border=2, bg="red")

    b24=Button(C, text="SHORT LINE", width=20, command=B3)
    b24_window=canvas.create_window(0, 476, anchor=NW, window=b24)
    b24.configure(border=2, bg="grey")

    def B16():
        f=open("BEIJING.txt","r")
        u=f.readlines()
        f.close()
        show(u)


    b16=Button(C, text="BEIJING", width=20, command=B16)
    b16_window=canvas.create_window(0, 504, anchor=NW, window=b16)
    b16.configure(border=2, bg="yellow")

    def B17():
        f=open("Gydnia.txt","r")
        u=f.readlines()
        f.close()
        show(u)
    
    b17=Button(C, text="HONGKONG", width=20, command=B17)
    b17_window=canvas.create_window(0, 532, anchor=NW, window=b17)
    b17.configure(border=2, bg="yellow")

    b25=Button(C, text="WATER WORKS", width=20, command=B22)
    b25_window=canvas.create_window(0, 560, anchor=NW, window=b25)
    b25.configure(border=2, bg="grey")

    def B18():
        f=open("JERUSALEM.txt","r")
        u=f.readlines()
        f.close()
        show(u)


    b18=Button(C, text="JERUSALEM", width=20, command=B18)
    b18_window=canvas.create_window(0, 588, anchor=NW, window=b18)
    b18.configure(border=2, bg="yellow")

    def B19():
        f=open("PARIS.txt","r")
        u=f.readlines()
        f.close()
        show(u)


    b19=Button(C, text="PARIS", width=20, command=B19)
    b19_window=canvas.create_window(0, 616, anchor=NW, window=b19)
    b19.configure(border=2, bg="green")

    def B20():
        f=open("BELGRADE.txt","r")
        u=f.readlines()
        f.close()
        show(u)


    b20=Button(C, text="BELGRADE", width=20, command=B20)
    b20_window=canvas.create_window(0, 644, anchor=NW, window=b20)
    b20.configure(border=2, bg="green")

    def B21():
        f=open("CAPETOWN.txt","r")
        u=f.readlines()
        f.close()
        show(u)


    b21=Button(C, text="CAPETOWN", width=20, command=B21)
    b21_window=canvas.create_window(0, 672, anchor=NW, window=b21)
    b21.configure(border=2, bg="green")

    b26=Button(C, text="B & O RAILROAD", width=20, command=B3)
    b26_window=canvas.create_window(0, 700, anchor=NW, window=b26)
    b26.configure(border=2, bg="grey")

    def B27():
        f=open("RIGA.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b27=Button(C, text="RIGA", width=20, command=B27)
    b27_window=canvas.create_window(0, 728, anchor=NW, window=b27)
    b27.configure(border=2, bg="Blue", fg="White")

    def B28():
        f=open("MONTREAL.txt","r")
        u=f.readlines()
        f.close()
        show(u)

    b28=Button(C, text="MONTREAL", width=20, command=B28)
    b28_window=canvas.create_window(0, 756, anchor=NW, window=b28)
    b28.configure(border=2, bg="Blue", fg="White")

    options=["-","R","B","G","Y"]

    c1=StringVar()
    c1.set("-")

    def h1(e):
        
        if e=="R":
            D1.configure(bg="red")

        elif e=="B":
            D1.configure(bg="cyan")

        elif e=="Y":
            D1.configure(bg="Yellow")

        elif e=="G":
            D1.configure(bg="green")

        elif e=="-":
            D1.configure(bg="White")


    D1=OptionMenu(C, c1, *options, command=h1)
    D1_window = canvas.create_window(177, 13, window=D1)
    D1.configure(border=2, bg="White", )

    c2=StringVar()
    c2.set("-")

    def h2(e):
        
        if e=="R":
            D2.configure(bg="red")

        elif e=="B":
            D2.configure(bg="cyan")

        elif e=="Y":
            D2.configure(bg="Yellow")

        elif e=="G":
            D2.configure(bg="green")

        elif e=="-":
            D2.configure(bg="White")

    D2=OptionMenu(C, c2, *options, command=h2)
    D2_window = canvas.create_window(177, 40, window=D2)
    D2.configure(border=2, bg="White", )

    c3=StringVar()
    c3.set("-")

    def h3(e):
        
        if e=="R":
            d3.configure(bg="red")

        elif e=="B":
            d3.configure(bg="cyan")

        elif e=="Y":
            d3.configure(bg="Yellow")

        elif e=="G":
            d3.configure(bg="green")

        elif e=="-":
            d3.configure(bg="White")

    d3=OptionMenu(C, c3, *options, command=h3)
    d3_window = canvas.create_window(177, 69, window=d3)
    d3.configure(border=2, bg="White", )

    c4=StringVar()
    c4.set("-")

    def h4(e):
        
        if e=="R":
            d4.configure(bg="red")

        elif e=="B":
            d4.configure(bg="cyan")

        elif e=="Y":
            d4.configure(bg="Yellow")

        elif e=="G":
            d4.configure(bg="green")

        elif e=="-":
            d4.configure(bg="White")

    d4=OptionMenu(C, c4, *options, command=h4)
    d4_window = canvas.create_window(177, 97, window=d4)
    d4.configure(border=2, bg="White", )

    c5=StringVar()
    c5.set("-")

    def h5(e):
        
        if e=="R":
            d5.configure(bg="red")

        elif e=="B":
            d5.configure(bg="cyan")

        elif e=="Y":
            d5.configure(bg="Yellow")

        elif e=="G":
            d5.configure(bg="green")

        elif e=="-":
            d5.configure(bg="White")

    d5=OptionMenu(C, c5, *options, command=h5)
    d5_window = canvas.create_window(177, 125, window=d5)
    d5.configure(border=2, bg="White", )

    c6=StringVar()
    c6.set("-")

    def h6(e):
        
        if e=="R":
            d6.configure(bg="red")

        elif e=="B":
            d6.configure(bg="cyan")

        elif e=="Y":
            d6.configure(bg="Yellow")

        elif e=="G":
            d6.configure(bg="green")

        elif e=="-":
            d6.configure(bg="White")

    d6=OptionMenu(C, c6, *options, command=h6)
    d6_window = canvas.create_window(177, 153, window=d6)
    d6.configure(border=2, bg="White", )

    c7=StringVar()
    c7.set("-")

    def h7(e):
        
        if e=="R":
            d7.configure(bg="red")

        elif e=="B":
            d7.configure(bg="cyan")

        elif e=="Y":
            d7.configure(bg="Yellow")

        elif e=="G":
            d7.configure(bg="green")

        elif e=="-":
            d7.configure(bg="White")

    d7=OptionMenu(C, c7, *options, command=h7)
    d7_window = canvas.create_window(177, 180, window=d7)
    d7.configure(border=2, bg="White", )

    c8=StringVar()
    c8.set("-")

    def h8(e):
        
        if e=="R":
            d8.configure(bg="red")

        elif e=="B":
            d8.configure(bg="cyan")

        elif e=="Y":
            d8.configure(bg="Yellow")

        elif e=="G":
            d8.configure(bg="green")

        elif e=="-":
            d8.configure(bg="White")

    d8=OptionMenu(C, c8, *options, command=h8)
    d8_window = canvas.create_window(177, 208, window=d8)
    d8.configure(border=2, bg="White", )

    c9=StringVar()
    c9.set("-")

    def h9(e):
        
        if e=="R":
            d9.configure(bg="red")

        elif e=="B":
            d9.configure(bg="cyan")

        elif e=="Y":
            d9.configure(bg="Yellow")

        elif e=="G":
            d9.configure(bg="green")

        elif e=="-":
            d9.configure(bg="White")

    d9=OptionMenu(C, c9, *options, command=h9)
    d9_window = canvas.create_window(177, 236, window=d9)
    d9.configure(border=2, bg="White", )

    c10=StringVar()
    c10.set("-")

    def h10(e):
        
        if e=="R":
            D10.configure(bg="red")

        elif e=="B":
            D10.configure(bg="cyan")

        elif e=="Y":
            D10.configure(bg="Yellow")

        elif e=="G":
            D10.configure(bg="green")

        elif e=="-":
            D10.configure(bg="White")

    D10=OptionMenu(C, c10, *options, command=h10)
    D10_window = canvas.create_window(177, 264, window=D10)
    D10.configure(border=2, bg="White", )

    c11=StringVar()
    c11.set("-")

    def h11(e):
        
        if e=="R":
            D11.configure(bg="red")

        elif e=="B":
            D11.configure(bg="cyan")

        elif e=="Y":
            D11.configure(bg="Yellow")

        elif e=="G":
            D11.configure(bg="green")

        elif e=="-":
            D11.configure(bg="White")

    D11=OptionMenu(C, c11, *options, command=h11)
    D11_window = canvas.create_window(177, 292, window=D11)
    D11.configure(border=2, bg="White", )

    c12=StringVar()
    c12.set("-")

    def h12(e):
        
        if e=="R":
            D12.configure(bg="red")

        elif e=="B":
            D12.configure(bg="cyan")

        elif e=="Y":
            D12.configure(bg="Yellow")

        elif e=="G":
            D12.configure(bg="green")

        elif e=="-":
            D12.configure(bg="White")

    D12=OptionMenu(C, c12, *options, command=h12)
    D12_window = canvas.create_window(177, 320, window=D12)
    D12.configure(border=2, bg="White", )

    c13=StringVar()
    c13.set("-")

    def h13(e):
        
        if e=="R":
            D13.configure(bg="red")

        elif e=="B":
            D13.configure(bg="cyan")

        elif e=="Y":
            D13.configure(bg="Yellow")

        elif e=="G":
            D13.configure(bg="green")

        elif e=="-":
            D13.configure(bg="White")

    D13=OptionMenu(C, c13, *options, command=h13)
    D13_window = canvas.create_window(177, 348, window=D13)
    D13.configure(border=2, bg="White", )

    c14=StringVar()
    c14.set("-")

    def h14(e):
        
        if e=="R":
            D14.configure(bg="red")

        elif e=="B":
            D14.configure(bg="cyan")

        elif e=="Y":
            D14.configure(bg="Yellow")

        elif e=="G":
            D14.configure(bg="green")

        elif e=="-":
            D14.configure(bg="White")

    D14=OptionMenu(C, c14, *options, command=h14)
    D14_window = canvas.create_window(177, 376, window=D14)
    D14.configure(border=2, bg="White", )

    c15=StringVar()
    c15.set("-")

    def h15(e):
        
        if e=="R":
            D15.configure(bg="red")

        elif e=="B":
            D15.configure(bg="cyan")

        elif e=="Y":
            D15.configure(bg="Yellow")

        elif e=="G":
            D15.configure(bg="green")

        elif e=="-":
            D15.configure(bg="White")

    D15=OptionMenu(C, c15, *options, command=h15)
    D15_window = canvas.create_window(177, 404, window=D15)
    D15.configure(border=2, bg="White", )

    c16=StringVar()
    c16.set("-")

    def h16(e):
        
        if e=="R":
            D16.configure(bg="red")

        elif e=="B":
            D16.configure(bg="cyan")

        elif e=="Y":
            D16.configure(bg="Yellow")

        elif e=="G":
            D16.configure(bg="green")

        elif e=="-":
            D16.configure(bg="White")

    D16=OptionMenu(C, c16, *options, command=h16)
    D16_window = canvas.create_window(177, 432, window=D16)
    D16.configure(border=2, bg="White", )

    c17=StringVar()
    c17.set("-")

    def h17(e):
        
        if e=="R":
            D17.configure(bg="red")

        elif e=="B":
            D17.configure(bg="cyan")

        elif e=="Y":
            D17.configure(bg="Yellow")

        elif e=="G":
            D17.configure(bg="green")

        elif e=="-":
            D17.configure(bg="White")

    D17=OptionMenu(C, c17, *options, command=h17)
    D17_window = canvas.create_window(177, 460, window=D17)
    D17.configure(border=2, bg="White", )

    c18=StringVar()
    c18.set("-")

    def h18(e):
        
        if e=="R":
            D18.configure(bg="red")

        elif e=="B":
            D18.configure(bg="cyan")

        elif e=="Y":
            D18.configure(bg="Yellow")

        elif e=="G":
            D18.configure(bg="green")

        elif e=="-":
            D18.configure(bg="White")

    D18=OptionMenu(C, c18, *options, command=h18)
    D18_window = canvas.create_window(177, 488, window=D18)
    D18.configure(border=2, bg="White", )

    c19=StringVar()
    c19.set("-")

    def h19(e):
        
        if e=="R":
            D19.configure(bg="red")

        elif e=="B":
            D19.configure(bg="cyan")

        elif e=="Y":
            D19.configure(bg="Yellow")

        elif e=="G":
            D19.configure(bg="green")

        elif e=="-":
            D19.configure(bg="White")

    D19=OptionMenu(C, c19, *options, command=h19)
    D19_window = canvas.create_window(177, 516, window=D19)
    D19.configure(border=2, bg="White", )

    c20=StringVar()
    c20.set("-")

    def h20(e):
        
        if e=="R":
            D20.configure(bg="red")

        elif e=="B":
            D20.configure(bg="cyan")

        elif e=="Y":
            D20.configure(bg="Yellow")

        elif e=="G":
            D20.configure(bg="green")

        elif e=="-":
            D20.configure(bg="White")

    D20=OptionMenu(C, c20, *options, command=h20)
    D20_window = canvas.create_window(177, 544, window=D20)
    D20.configure(border=2, bg="White", )

    c21=StringVar()
    c21.set("-")

    def h21(e):
        
        if e=="R":
            D21.configure(bg="red")

        elif e=="B":
            D21.configure(bg="cyan")

        elif e=="Y":
            D21.configure(bg="Yellow")

        elif e=="G":
            D21.configure(bg="green")

        elif e=="-":
            D21.configure(bg="White")

    D21=OptionMenu(C, c21, *options, command=h21)
    D21_window = canvas.create_window(177, 572, window=D21)
    D21.configure(border=2, bg="White", )

    c22=StringVar()
    c22.set("-")

    def h22(e):
        
        if e=="R":
            D22.configure(bg="red")

        elif e=="B":
            D22.configure(bg="cyan")

        elif e=="Y":
            D22.configure(bg="Yellow")

        elif e=="G":
            D22.configure(bg="green")

        elif e=="-":
            D22.configure(bg="White")

    D22=OptionMenu(C, c22, *options, command=h22)
    D22_window = canvas.create_window(177, 600, window=D22)
    D22.configure(border=2, bg="White", )

    c23=StringVar()
    c23.set("-")

    def h23(e):
        
        if e=="R":
            D23.configure(bg="red")

        elif e=="B":
            D23.configure(bg="cyan")

        elif e=="Y":
            D23.configure(bg="Yellow")

        elif e=="G":
            D23.configure(bg="green")

        elif e=="-":
            D23.configure(bg="White")

    D23=OptionMenu(C, c23, *options, command=h23)
    D23_window = canvas.create_window(177, 628, window=D23)
    D23.configure(border=2, bg="White")

    c24=StringVar()
    c24.set("-")

    def h24(e):
        
        if e=="R":
            D24.configure(bg="red")

        elif e=="B":
            D24.configure(bg="cyan")

        elif e=="Y":
            D24.configure(bg="Yellow")

        elif e=="G":
            D24.configure(bg="green")

        elif e=="-":
            D24.configure(bg="White")

    D24=OptionMenu(C, c24, *options, command=h24)
    D24_window = canvas.create_window(177, 656, window=D24)
    D24.configure(border=2, bg="White", )

    c25=StringVar()
    c25.set("-")

    def h25(e):
        
        if e=="R":
            D25.configure(bg="red")

        elif e=="B":
            D25.configure(bg="cyan")

        elif e=="Y":
            D25.configure(bg="Yellow")

        elif e=="G":
            D25.configure(bg="green")

        elif e=="-":
            D25.configure(bg="White")

    D25=OptionMenu(C, c25, *options, command=h25)
    D25_window = canvas.create_window(177, 684, window=D25)
    D25.configure(border=2, bg="White", )

    c26=StringVar()
    c26.set("-")

    def h26(e):
        
        if e=="R":
            D26.configure(bg="red")

        elif e=="B":
            D26.configure(bg="cyan")

        elif e=="Y":
            D26.configure(bg="Yellow")

        elif e=="G":
            D26.configure(bg="green")

        elif e=="-":
            D26.configure(bg="White")

    D26=OptionMenu(C, c26, *options, command=h26)
    D26_window = canvas.create_window(177, 712, window=D26)
    D26.configure(border=2, bg="White", )

    c27=StringVar()
    c27.set("-")

    def h27(e):
        
        if e=="R":
            D27.configure(bg="red")

        elif e=="B":
            D27.configure(bg="cyan")

        elif e=="Y":
            D27.configure(bg="Yellow")

        elif e=="G":
            D27.configure(bg="green")

        elif e=="-":
            D27.configure(bg="White")

    D27=OptionMenu(C, c27, *options, command=h27)
    D27_window = canvas.create_window(177, 740, window=D27)
    D27.configure(border=2, bg="White", )

    c28=StringVar()
    c28.set("-")

    def h28(e):
        
        if e=="R":
            D28.configure(bg="red")

        elif e=="B":
            D28.configure(bg="cyan")

        elif e=="Y":
            D28.configure(bg="Yellow")

        elif e=="G":
            D28.configure(bg="green")

        elif e=="-":
            D28.configure(bg="White")

    D28=OptionMenu(C, c28, *options, command=h28)
    D28_window = canvas.create_window(177, 768, window=D28)
    D28.configure(border=2, bg="White", )

    canvas.pack()

    width=202
    height=783
    sw = C.winfo_screenwidth()
    sh = C.winfo_screenheight()

    x=(sw/2) - 750
    y=(sh/2) - 420

    C.geometry("%dx%d+%d+%d" % (width, height, x, y))

    C.resizable(False,False)
    C.attributes("-toolwindow", True)
    C.attributes("-topmost", True)
