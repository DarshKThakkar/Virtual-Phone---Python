def calci(z1, z2, z3, z4, z5):

    import tkinter as tk
    from PIL import Image, ImageTk

    c=tk.Tk()
    c.title("O")

    class A:
        ans=""
        r=0

    T=tk.StringVar()
    T.set(A.ans)

    def back():
        c.destroy()
        from App import AV
        AV(z1, z2, z3, z4, z5)

    def home():
        c.destroy()
        from Android import main
        main(z1, z2, z3, z4, z5)


    canvas= tk.Canvas(c, width=402, height=600)

    def B1():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"1"
        T.set(A.ans)
        A.r=0

    def B2():

        if A.r==1:
            A.ans=""
        
        A.ans=A.ans+"2"
        T.set(A.ans)
        A.r=0

    def B3():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"3"
        T.set(A.ans)
        A.r=0

    def B4():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"4"
        T.set(A.ans)
        A.r=0

    def B5():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"5"
        T.set(A.ans)
        A.r=0

    def B6():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"6"
        T.set(A.ans)
        A.r=0

    def B7():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"7"
        T.set(A.ans)
        A.r=0

    def B8():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"8"
        T.set(A.ans)
        A.r=0

    def B9():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"9"
        T.set(A.ans)
        A.r=0

    def B10():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"0"
        T.set(A.ans)
        A.r=0

    def B11():

        if A.r==1:
            A.ans=""
            
        A.ans=A.ans+"."
        T.set(A.ans)
        A.r=0

    def B14():

        if len(A.ans)>=1:
            d=(A.ans[len(A.ans)-1])

        else:
            d=""
        
        if d=="+" or d=="-" or d=="*" or d=="/":
            A.ans=A.ans[:len(A.ans)-1]
            A.ans=A.ans+"/"
            T.set(A.ans)
            A.r=0

        else:
            A.ans=A.ans+"/"
            T.set(A.ans)
            A.r=0
            
    def B15():
            
        if len(A.ans)>=1:
            d=(A.ans[len(A.ans)-1])

        else:
            d=""

        if d=="+" or d=="-" or d=="*" or d=="/":
            A.ans=A.ans[:len(A.ans)-1]
            A.ans=A.ans+"*"
            T.set(A.ans)
            A.r=0

        else:
            A.ans=A.ans+"*"
            T.set(A.ans)
            A.r=0

    def B16():
            
        if len(A.ans)>=1:
            d=(A.ans[len(A.ans)-1])

        else:
            d=""

        if d=="+" or d=="-" or d=="*" or d=="/":
            A.ans=A.ans[:len(A.ans)-1]
            A.ans=A.ans+"-"
            T.set(A.ans)
            A.r=0

        else:
            A.ans=A.ans+"-"
            T.set(A.ans)
            A.r=0

    def B17():

        if len(A.ans)>=1:
            d=(A.ans[len(A.ans)-1])

        else:
            d=""

        if d=="+" or d=="-" or d=="*" or d=="/":
            A.ans=A.ans[:len(A.ans)-1]
            A.ans=A.ans+"+"
            T.set(A.ans)
            A.r=0

        else:
            A.ans=A.ans+"+"
            T.set(A.ans)
            A.r=0

    def B12():
        if A.ans=="Error" or A.r==1:
            A.ans=""
            T.set(A.ans)
            A.r=0

        else:    
            A.ans=A.ans[:len(A.ans)-1]
            T.set(A.ans)

    def B13():
        A.ans=""
        T.set(A.ans)

    def B18():
        
        if len(A.ans)>=1 and A.ans!="." and A.ans!="/" and A.ans!="*" and A.ans!="-" and A.ans!="+":

            try:
                A.ans=str(eval(A.ans))

            except:
                A.ans="Error"
                T.set(A.ans)
                A.r=1

            else:
                T.set(A.ans)
                A.r=1

        else:
            A.ans="Error"
            T.set(A.ans)
            A.r=1

    def Not():
        c.destroy()
        import Notifications
        Notifications.notification(z1,z2,z3,z4,z5,"calculator")

    io = Image.open("N.jpeg")
    po = ImageTk.PhotoImage(io)

    bo=tk.Button(c, image=po, width=390, height=27, relief="solid", command=Not)
    bo_window = canvas.create_window(200, 12, window=bo)


    b1=tk.Button(c, text="1", relief="groove", width=8, height=3, command=B1)
    b1_window = canvas.create_window(51, 262, window=b1)
    b1.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b2=tk.Button(c, text="2", relief="groove", width=8, height=3, command=B2)
    b2_window = canvas.create_window(151, 262, window=b2)
    b2.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b3=tk.Button(c, text="3", relief="groove", width=8, height=3, command=B3)
    b3_window = canvas.create_window(251, 262, window=b3)
    b3.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b4=tk.Button(c, text="4", relief="groove", width=8, height=3, command=B4)
    b4_window = canvas.create_window(51, 342, window=b4)
    b4.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b5=tk.Button(c, text="5", relief="groove", width=8, height=3, command=B5)
    b5_window = canvas.create_window(151, 342, window=b5)
    b5.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b6=tk.Button(c, text="6", relief="groove", width=8, height=3, command=B6)
    b6_window = canvas.create_window(251, 342, window=b6)
    b6.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b7=tk.Button(c, text="7", relief="groove", width=8, height=3, command=B7)
    b7_window = canvas.create_window(51, 422, window=b7)
    b7.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b8=tk.Button(c, text="8", relief="groove", width=8, height=3, command=B8)
    b8_window = canvas.create_window(151, 422, window=b8)
    b8.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b9=tk.Button(c, text="9", relief="groove", width=8, height=3, command=B9)
    b9_window = canvas.create_window(251, 422, window=b9)
    b9.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b10=tk.Button(c, text="0", relief="groove", width=17, height=3, command=B10)
    b10_window = canvas.create_window(101, 502, window=b10)
    b10.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b11=tk.Button(c, text=".", relief="groove", width=8, height=3, command=B11)
    b11_window = canvas.create_window(251, 502, window=b11)
    b11.configure(bg="Black", fg="White", font=("ArialBlack", 14))

    b12=tk.Button(c, text="DEL", relief="groove", width=8, height=3, command=B12)
    b12_window = canvas.create_window(51, 181, window=b12)
    b12.configure(bg="Maroon", fg="White", font=("ArialBlack", 14))

    b13=tk.Button(c, text="C", relief="groove", width=8, height=3, command=B13)
    b13_window = canvas.create_window(151, 181, window=b13)
    b13.configure(bg="Gray", fg="Black", font=("ArialBlack", 14))

    b14=tk.Button(c, text="/", relief="groove", width=8, height=3, command=B14)
    b14_window = canvas.create_window(251, 181, window=b14)
    b14.configure(bg="Gray", fg="Black", font=("ArialBlack", 14))

    b15=tk.Button(c, text="*", relief="groove", width=8, height=3, command=B15)
    b15_window = canvas.create_window(351, 181, window=b15)
    b15.configure(bg="Gray", fg="Black", font=("ArialBlack", 14))

    b16=tk.Button(c, text="-", relief="groove", width=8, height=3, command=B16)
    b16_window = canvas.create_window(351, 343, window=b16)
    b16.configure(bg="Gray", fg="Black", font=("ArialBlack", 14))

    b17=tk.Button(c, text="+", relief="groove", width=8, height=3, command=B17)
    b17_window = canvas.create_window(351, 262, window=b17)
    b17.configure(bg="Gray", fg="Black", font=("ArialBlack", 14))

    b18=tk.Button(c, text="=", width=9, height=6, command=B18)
    b18_window = canvas.create_window(351, 463, window=b18)
    b18.configure(border=1, bg="Orange", fg="Black", font=("Calibri", 14))

    L=tk.Label(c, textvariable=T, width=20)
    L_window = canvas.create_window(210, 107, window=L)
    L.configure(border=0, bg="Black", fg="White", font=("Calibri", 27), anchor=tk.E)

    """-----------------------------------------------------------"""

    i70 = Image.open("bn1.jpg")
    p70 = ImageTk.PhotoImage(i70)
        
    b70=tk.Button(c, image=p70, width=40, height=20, relief="groove", command=back)
    b70_window = canvas.create_window(100, 575, window=b70)
    b70.configure(border=0)

    i80 = Image.open("bn2.jpg")
    p80 = ImageTk.PhotoImage(i80)

    b80=tk.Button(c, image=p80, width=40, height=20, relief="groove", command=home)
    b80_window = canvas.create_window(200, 575, window=b80)
    b80.configure(border=0)

    i90 = Image.open("bn3.png")
    p90 = ImageTk.PhotoImage(i90)

    l1=tk.Label(c, image=p90, width=40, height=20)
    l1_window = canvas.create_window(300, 575, window=l1)
    l1.configure(border=1)

    """-----------------------------------------------------------"""

    i0 = Image.open("Calci.jpg")
    p0 = ImageTk.PhotoImage(i0)

    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    c.geometry("402x600")
    c.resizable(False, False)
    c.wm_attributes("-topmost", "true")

    width=402
    height=600
    sw = c.winfo_screenwidth()
    sh = c.winfo_screenheight()

    x=(sw/2) + 300
    y=(sh/2) - 300

    c.geometry("%dx%d+%d+%d" % (width, height, x, y))
    c.mainloop()
