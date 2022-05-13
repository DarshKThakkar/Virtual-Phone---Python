from tkinter import *
import random

def chest(b):
        A=Tk()
        A.title("CARD")

        LABEL=Label(A, text=b)
        LABEL.pack()
        LABEL.configure(border=0)

        def ok():
                A.destroy()

        BUTTON=Button(A, text="OK", width=6, command=ok)
        BUTTON.pack()
        BUTTON.configure(border=1, bg="Black", fg="White")
        
        A.attributes("-topmost", True)

        width=350
        height=50
        sw = A.winfo_screenwidth()
        sh = A.winfo_screenheight()

        x=(sw/2) - 150
        y=(sh/2) + 90

        A.geometry("%dx%d+%d+%d" % (width,height,x, y))

        A.mainloop()
