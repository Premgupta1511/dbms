from tkinter import *
from PIL import Image,ImageTk
from bs4 import BeautifulSoup as bs
from lostocks2 import stock2
import requests
def stock(r):
    root2=Toplevel()
    root2.geometry('1000x720+250+50')
    root2.resizable(0,0)
    bgg=ImageTk.PhotoImage(file="stk2.jpg")
    myc1=Canvas(root2,width=1000,height=720,bd=0,highlightthickness=0)
    myc1.pack(fill='both',expand=True)
    myc1.create_image(0,0,image=bgg,anchor="nw")
    link="https://www.google.com/finance/quote/NIFTY_50:INDEXNSE"
    page=requests.get(link)
    soup=bs(page.content,'lxml')
    ltp=soup.find('div',class_="YMlKec fxKbKc").text.replace(',','')
    iltp=float(ltp)
    pre=soup.find('div',class_="M2CUtd").text.replace(',','')
    ipre=float(pre)
    res=round((ipre-iltp),2)
    myc1.create_text(580,150,text=ltp,anchor="nw",font="times 30 bold",fill="black")
    myc1.create_text(620,200,text="+"+str(res)+"  Today",anchor="nw",font="times 17 bold",fill="white")
    myc1.create_text(450,370,text="Top 9 ",anchor="nw",font="times 26 bold underline",fill="white",underline=True)
    def back():
        root2.destroy()
        r.deiconify()
    btnim=ImageTk.PhotoImage(file="wallet1.png")
    btn=Button(myc1,image=btnim,bg="white")
    btn.place(x=20,y=10)
    btnim1=ImageTk.PhotoImage(file="setting1.png")
    btn1=Button(myc1,image=btnim1,bg="white")
    btn1.place(x=100,y=10)
    lo=ImageTk.PhotoImage(file="logout1.png")
    logout=Button(myc1,text="Logout",font="times 15 bold",height=0,bg="red",fg="white",image=lo,compound=LEFT,command=back)
    logout.place(x=900,y=10)

    search=Entry(myc1,font="times 20",fg="grey",width=45)
    search.place(x=200,y=74)
    search.insert(0,"Search Stock")
    def se(e):
        if(search.get()=="Search Stock"):
            search.delete(0,END)
            search.configure(fg="blue")
    def search1():
        root2.withdraw()
        stock2(root2,search.get())
    search.bind('<Button-1>',se)
    sim=ImageTk.PhotoImage(file="search.png")
    sl=Label(myc1,image=sim,bg="white")
    sl.place(x=167,y=75)
    def disp(stk):
        root2.withdraw()
        stock2(root2,stk)
    sbutton=Button(myc1,text="Search",bg="green",fg="White",height=0,width=6,font="times 14",command=search1)
    sbutton.place(x=850,y=74)
    profile=ImageTk.PhotoImage(file="reliance1.png")
    rel=Button(myc1,image=profile,bg="white",command=lambda :disp("RELIANCE"))
    rel.place(x=30,y=450)
    profile1=ImageTk.PhotoImage(file="cipla1.png")
    profile5=ImageTk.PhotoImage(file="nifty1.jpg")
    myc1.create_image(350,150,image=profile5,anchor="nw")
    cipla=Button(myc1,image=profile1,bg="white",command=lambda :disp("CIPLA"))
    cipla.place(x=230,y=450)
    profile2=ImageTk.PhotoImage(file="bajaj2.jpg")
    baj=Button(myc1,image=profile2,bg="white",command=lambda :disp("BAJAJFINSV"))
    baj.place(x=430,y=450)
    profile3=ImageTk.PhotoImage(file="britannia1.jpg")
    brit=Button(myc1,image=profile3,bg="white",command=lambda :disp("BRITANNIA"))
    brit.place(x=630,y=450)
    profile4=ImageTk.PhotoImage(file="tatamotors1.jpg")
    tata=Button(myc1,image=profile4,bg="white",command=lambda :disp("TATAMOTORS"))
    tata.place(x=830,y=450)
    profile6=ImageTk.PhotoImage(file="infosys1.jpg")
    infy=Button(myc1,image=profile6,bg="white",command=lambda :disp("INFY"))
    infy.place(x=100,y=570)
    profile7=ImageTk.PhotoImage(file="mrf1.jpg")
    mrf=Button(myc1,image=profile7,bg="white",command=lambda :disp("MRF"))
    mrf.place(x=300,y=570)
    profile8=ImageTk.PhotoImage(file="airtel1.jpg")
    airtel=Button(myc1,image=profile8,bg="white",command=lambda :disp("BHARTIARTL"))
    airtel.place(x=500,y=570)
    profile9=ImageTk.PhotoImage(file="lt1.jpg")
    lt=Button(myc1,image=profile9,bg="white",command=lambda :disp("LT"))
    lt.place(x=700,y=570)
    root2.mainloop()