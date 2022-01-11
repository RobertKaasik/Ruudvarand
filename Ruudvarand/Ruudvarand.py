from tkinter import *
from math import *
import matplotlib.pyplot as plt
import numpy as np
global D,t
D=-1
t=0

def lahenda():
    global D,t
    if (a.get()!="" and b.get()!="" and c.get()!=""):
        a_=float(a.get())
        b_=float(b.get())
        c_=float(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_+sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
            graf=True
        elif D==0:
            x1_=round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
            graf=True
        else:
            t="Корней нет"
            graf=False
        vastus.configure(text=f"D={D}\n{t}")
        a.configure(bg="grey")
        b.configure(bg="grey")
        c.configure(bg="grey")
    else:
        if a.get()=="":
             a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")
    return graf,D,t
def graafik():
    graf,D,t=lahenda()
    if graf==True:
        a_=int(a.get())
        b_=int(b.get())
        c_=int(c.get())
        x0=(-b_)/(2*a_)
        y0=a_*x0*x0+b_*x0+c_
        x = np.arange(x0-10, x0+10, 0.5)
        y=a_*x*x+b_*x+c_
        fig = plt.figure()
        plt.plot(x, y,'b:o', x0, y0,'g-d')
        plt.title('Квадратное уравнение')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.grid(True)
        plt.show()
        text=f"Вершина параболлы ({x0},{y0})"
    else:
        text=f"График нет возможности построить"
    vastus.configure(text=f"D={D}\n{t}\n{text}")
def veel():
    global t
    if t==0:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()+200))
        btn_veel.config(text="уменьшить окно")
    else:
        aken.geometry(str(aken.winfo_width())+"x"+str(aken.winfo_height()-200))
        btn_veel.config(text="увеличить окно")
        t=0
def kala():
    x1 = np.arange(0, 9, 0.5)#min max step
    y1=(2/27)*x1*x1-3
    x2 = np.arange(-10, 0, 0.5)
    y2=0.04*x1*x1-3
    x3 = np.arange(-9, 9.5, 0.5)
    y3=(2/9)*(x3+6)**2+1
    x4 = np.arange(-3, 9.5, 0.5)
    y4=(-1/12)*(x4-3)**2+6
    x5 = np.arange(5, 9, 0.5)
    y5=(1/9)*(x5-5)**2+2
    x6 = np.arange(-9, 9.5, 0.5)
    y6=(2/9)*(x3+6)**2+1
    x7 = np.arange(-13, -8.5, 0.5)
    y7=(-0.75)*(x7+11)**2+6
    x8 = np.arange(-15, -12.5, 0.5)
    y8=(-0.5)*(x8+13)**2+3
    x9 = np.arange(-15, -10, 0.5)
    y9=[1]*len(x9)
    x10 = np.arange(3, 4, 0.5)
    y10=[3]*len(x10)
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10)
    plt.title('Кит')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()
def ˇotski():
    x1=np.arange(-9,-1,0.5)#min max step
    y1=(-1/16)*(x1+5)**2+2
    x2=np.arange(1,9,0.5)
    y2=(-1/16)*(x2-5)**2+2
    x3=np.arange(-9,-1,0.5)
    y3=1/4*(x3+5)**2-3
    x4=np.arange(1,9,0.5)
    y4=1/4*(x4-5)**2-3
    x5=np.arange(-9,-6,0.5)
    y5=-(x5+7)**2+5
    x6=np.arange(6,9,0.5)
    y6=-(x6-7)**2+5
    x7=np.arange(-1,1,0.5)
    y7=(-0.5)*x7*x7+1.5
    fig = plt.figure()
    plt.plot(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7)
    plt.title('Очки')
    plt.ylabel('y')
    plt.xlabel('x')
    plt.grid(True)
    plt.show()

aken=Tk()
aken.title("Решение квадртаного уровнения")
aken.geometry("1000x500")
aken.configure(bg="grey")
lbl=Label(aken,text="Решение квадратного уровнения",height=2,width=30,font="Arial 20",fg="black",bg="white")
lbl.pack()
vastus=Label(aken,text="Решение", height=4,width=60,bg="white")
vastus.pack(side=BOTTOM)
a=Entry(aken,font="Arial 20", fg="black",bg="grey",width=3)
a.pack(side=LEFT)#,padx=10,pady=10
x2=Label(aken,text="x**2+",font="Arial 20", fg="black", padx=10)
x2.pack(side=LEFT)
b=Entry(aken,font="Arial 20", fg="black",bg="grey",width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="Arial 20", fg="black")
x.pack(side=LEFT)
c=Entry(aken,font="Arial 20", fg="black",bg="grey",width=3)
c.pack(side=LEFT)
y=Label(aken,text="=0",font="Arial 20", fg="black")
y.pack(side=LEFT)

btn=Button(aken,text="Решить", font="Arial 20",bg="green",command=lahenda)
btn.pack(side=LEFT)
btn_g=Button(aken,text="График", font="Arial 20",bg="green",command=graafik)
btn_g.pack(side=LEFT)
btn_v=Button(aken,text="Размер", font="Arial 20",bg="green",command=kala)
btn_v.pack(side=LEFT)
aken.mainloop()