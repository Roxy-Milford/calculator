from tkinter import *
from math import *


tk = Tk()
tk.geometry("260x370")

entry=Entry(font=14,justify=RIGHT)
entry.place(x=20,y=20,width=220,height=30,)

def BC_click():
    entry.delete(0,END)
    
BC=Button(text="c",font="14",command=BC_click)
BC.place(x=20,y=70,width=40,height=40)

def RADICAL_click():
    global num
    num=float(entry.get())
    entry.delete(0,END)
    if num<0:
        entry.insert(END,"Error")
    else:
        num=sqrt(num)
        entry.insert(END,num)

img=PhotoImage(file='imgs/radical.png')

RADICAL=Button(image=img,font="14",command=RADICAL_click)
RADICAL.place(x=80,y=70,width=40,height=40)

def MODUL_click():
    global num
    num=float(entry.get())
    entry.delete(0,END)
    num=abs(num)
    entry.insert(END,num)
    
MODUL=Button(text="|x|",font="14",command=MODUL_click)
MODUL.place(x=140,y=70,width=40,height=40)

def Equal_click():
    global num,sign

    c=float(entry.get())
    entry.delete(0,END)

    if sign=="+":
        num=num+c
        entry.insert(END,num)
    elif sign=="-":
        num=num-c
        entry.insert(END,num)
    elif sign=="*":
        num=num*c
        entry.insert(END,num)
    elif sign=="/":
        if c!=0:
            num=num/c
            entry.insert(END,num)
        else:
            entry.insert(END,"Error")

Equal=Button(text="=",font="14",command=Equal_click)
Equal.place(x=200,y=70,width=40,height=40)

def B7_click():
    entry.insert(END,"7") 

B7=Button(text="7",font="14",command=B7_click)
B7.place(x=20,y=130,width=40,height=40)

def B8_click():
    entry.insert(END,"8") 

B8=Button(text="8",font="14",command=B8_click)
B8.place(x=80,y=130,width=40,height=40)

def B9_click():
    entry.insert(END,"9") 

B9=Button(text="9",font="14",command=B9_click)
B9.place(x=140,y=130,width=40,height=40)

def DIVIDE_click():
    global num,sign
    num=float(entry.get())
    sign="/"
    entry.delete(0,END)

DIVIDE=Button(text="/",font="14",command=DIVIDE_click)
DIVIDE.place(x=200,y=130,width=40,height=40)

def B4_click():
    entry.insert(END,"4") 

B4=Button(text="4",font="14",command=B4_click)
B4.place(x=20,y=190,width=40,height=40)

def B5_click():
    entry.insert(END,"5") 

B5=Button(text="5",font="14",command=B5_click)
B5.place(x=80,y=190,width=40,height=40)

def B6_click():
    entry.insert(END,"6") 

B6=Button(text="6",font="14",command=B6_click)
B6.place(x=140,y=190,width=40,height=40)

def MULTIPLY_click():
    global num,sign
    num=float(entry.get())
    sign="*"
    entry.delete(0,END)

MULTIPLY=Button(text="*",font="14",command=MULTIPLY_click)
MULTIPLY.place(x=200,y=190,width=40,height=40)

def B1_click():
    entry.insert(END,"1") 

B1=Button(text="1",font="14",command=B1_click)
B1.place(x=20,y=250,width=40,height=40)

def B2_click():
    entry.insert(END,"2") 

B2=Button(text="2",font="14",command=B2_click)
B2.place(x=80,y=250,width=40,height=40)

def B3_click():
    entry.insert(END,"3") 

B3=Button(text="3",font="14",command=B3_click)
B3.place(x=140,y=250,width=40,height=40)

def MINUS_click(): 
    global num,sign
    num=float(entry.get())
    sign="-"
    entry.delete(0,END)

MINUS=Button(text="-",font="14",command=MINUS_click)
MINUS.place(x=200,y=250,width=40,height=40)

def B0_click():
    entry.insert(END,"0") 

B0=Button(text="0",font="14",command=B0_click)
B0.place(x=20,y=310,width=100,height=40)

def DOT_click():
    entry.insert(END,".") 

DOT=Button(text=".",font="14",command=DOT_click)
DOT.place(x=140,y=310,width=40,height=40)

def PLUS_click(): 
    global num,sign
    num=float(entry.get())
    sign="+"
    entry.delete(0,END)
    
PLUS=Button(text="+",font="14",command=PLUS_click)
PLUS.place(x=200,y=310,width=40,height=40)

tk.mainloop()
