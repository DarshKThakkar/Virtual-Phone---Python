def Camera(z1, z2, z3, z4, z5):

    import tkinter as tk
    from PIL import Image, ImageTk
    import cv2

    h=tk.Tk()
    h.title("O")

    def Exit():
        h.destroy()
        from App import AV
        AV(z1, z2, z3, z4, z5)

    def Preview():

        cv2.namedWindow("Camera")
        vc = cv2.VideoCapture(0)
        
        if vc.isOpened(): # try to get the first frame
            rval, frame = vc.read()
        else:
            rval = False

        while rval:
            cv2.imshow("Camera", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(20)
            if key == 27: # exit on ESC
                h.after(250, Exit)
                break
                

        vc.release()
        cv2.destroyWindow("Camera")

    canvas= tk.Canvas(h, width=400, height=600)

    i0 = Image.open("Camera_Screen.jpg")
    p0 = ImageTk.PhotoImage(i0)

    canvas.create_image(0,0, anchor=tk.NW, image=p0)
    canvas.pack()

    h.geometry("400x600")
    h.resizable(False, False)
    h.wm_attributes("-topmost", "true")

    width=400
    height=600
    sw = h.winfo_screenwidth()
    sh = h.winfo_screenheight()

    x=(sw/2) + 300
    y=(sh/2) - 300

    h.geometry("%dx%d+%d+%d" % (width, height, x, y))

    h.after(1000, Preview)

    h.mainloop()
