from  tkinter import *
import test 
class w2():
    def w22(r):
        global window
        window=Tk()
        Label(window,text="w2").pack()
        def ww1():
            window.destroy()
            test.w1().w11()
        btn1=Button(window,text="w1",command=ww1)
        btn1.pack()
        window.mainloop()
         