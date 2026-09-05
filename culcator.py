from tkinter import *
import math



def click(num):
   curent=entry.get()
   entry.delete(0,END)
   entry.insert(0,str(curent)+str(num))
def Clear():
   entry.delete(0,END)
def Equail():
   x =eval(entry.get())
   Clear()
   entry.insert(0,x)
def Sin():
   sol=int(entry.get())
   x =math.sin(sol)
   entry.insert(0,x)
def cos():
   sol=int(entry.get())
   x =math.cos(sol)
   entry.insert(0,x)
def tan():
   sol=int(entry.get())
   x =math.tan(sol)
   entry.insert(0,x)
def cot():
   sol=int(entry.get())
   x =math.tanh(sol)
   entry.insert(0,x)
def sec():
   sol=int(entry.get())
   x =math.sinh(sol)
   entry.insert(0,x)
def csc():
   sol=int(entry.get())
   x =math.cosh(sol)
   entry.insert(0,x)
def squre():
   sol =int(entry.get())
   x =math.sqrt(sol)
   entry.insert(0,x)
def mar():
   sol=int(entry.get())
   x =sol*sol
   Clear()
   entry.insert(0,x)
def fact():
   sol=int(entry.get())
   x =math.perm(sol)
   Clear()
   entry.insert(0,x)
def Par():
   sol=int(entry.get())
   x =math.exp(sol)
   entry.insert(0,x)
def t3():
   sol=int(entry.get())
   x =sol*sol*sol
   Clear()
   entry.insert(0,x)
def Pi():
   entry.insert(0,math.pi)
def Log():
   sol=int(entry.get())
   x =math.log10(sol)
   entry.insert(0,x)
def Ln():
   sol=int(entry.get())
   x =math.log1p(sol)
   entry.insert(0,x)
def Dfi():
   sol=int(entry.get())
   x=entry.insert(END,"/")
   y=sol/x
   Clear
   entry.insert(0,y)
def mini():
   to=entry.get()
   if "+" in to:
      c =to.replace("+","-")
      Clear()
      entry.insert(0,c)
   elif "-" in to:
      d =to.replace('-','+')
      Clear()
      entry.insert(0,d)
def Backspace():
   name= entry.get()
   entry.delete(len(name)-1,END)
   
   
   
   
   
window=Tk()
percentage=PhotoImage(file="images\\icons8_percentage_32.png",width=95)
square=PhotoImage (file="images\\icons8_square_number_32.png",width=96)
square2=PhotoImage (file="images\\icons8_square_root_32.png",width=92)
c=PhotoImage(file="images\\icons8_c_32.png",width=96)
exclamation=PhotoImage(file="images\\icons8_exclamation_mark_32.png",width=65)
Clear2=PhotoImage(file="images\\icons8_Clear_Symbol_32.png",width=65)
pi=PhotoImage(file="images\\icons8_pi_32.png",width=96)
image=PhotoImage(file="images\\icons8_calculator1_32.png")
window.geometry("520x561")
window.title("Calculator")
window.iconphoto(True,image)

frame=Frame(window,highlightbackground='black',highlightcolor='white',highlightthickness=10)
entry=Entry(frame)
entry.config(font=("Impact",25),width=26,bg="black",fg='white',bd=10,relief=RAISED)

b0 =Button(frame ,text="0",padx=35,pady=14,command=lambda :click(0),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
b1 =Button(frame ,text="1",padx=35,pady=14,command=lambda :click(1),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
b2 =Button(frame ,text="2",padx=35,pady=14,command=lambda :click(2),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
b3 =Button(frame ,text="3",padx=35,pady=14,command=lambda :click(3),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
b4 =Button(frame ,text="4",padx=35,pady=14,command=lambda :click(4),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
b5 =Button(frame ,text="5",padx=35,pady=14,command=lambda :click(5),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
b6 =Button(frame ,text="6",padx=35,pady=14,command=lambda :click(6),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
b7 =Button(frame ,text="7",padx=35,pady=14,command=lambda :click(7),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
b8 =Button(frame ,text="8",padx=35,pady=14,command=lambda :click(8),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
b9 =Button(frame ,text="9",padx=35,pady=14,command=lambda :click(9),bg="#4d0000",fg="white",font=("Arial",16,'bold'))
bEquil =Button(frame,text="=",font=('Arial',14,"bold"),padx=74,pady=15,command=Equail,bg="#cc5200",fg="white")
bAdd =  Button(frame,text="+",padx=24,pady=14,font=('Arial',14,"bold"),command=lambda :click("+"),bg="#00aaff",fg="white")
bmf =   Button(frame,text="-",padx=26,pady=14,font=('Arial',14,"bold"),command=lambda :click("-"),bg="#00aaff",fg="white")
bzf =   Button(frame,text="X",padx=23,pady=14,font=('Arial',14,"bold"),command=lambda :click("*"),bg="#00aaff",fg="white")
bdf =   Button(frame,text="/",padx=26,pady=14,font=('Arial',14,"bold"),command=lambda :click("/"),bg="#00aaff",fg="white")
badmf = Button(frame,text="+/-",font=("Arial",14,'bold'),padx=33,pady=15,command=mini,bg="#269900",fg="white")
bpar =  Button(frame,image=percentage,padx=8,pady=8,command=Par,bg="#ff8080",fg="white",height=60)
bfact = Button(frame,image=exclamation,padx=8,pady=8,command=fact,bg="#00aaff",fg="white",height=59)
btwan = Button(frame,image=square,padx=8,pady=8,command=mar,bg="#ff8080",fg="white",height=60)
bclear =Button(frame,image=c,padx=8,pady=8,command=Clear,bg="#ff8080",fg="white",height=60)
bsin = Button (frame,text="sin",padx=28,pady=14,command=Sin,bg="blue",fg="white",font=("Arial",14,'bold'))
bcos = Button (frame,text="cos",padx=27,pady=14,command=cos,bg="blue",fg="white",font=("Arial",14,'bold'))
btan = Button (frame,text="tan",padx=27,pady=14,command=tan,bg="blue",fg="white",font=("Arial",14,'bold'))
bcot = Button (frame,text="cot ",padx=25,pady=14,command=cot,bg="blue",fg="white",font=("Arial",14,'bold'))
bBack =Button (frame,image=Clear2,padx=8,pady=8,command=Backspace,bg="#800000",fg="white",height=60)
bdidi =Button (frame,text=".",padx=45,pady=22,command=lambda :click('.'),bg="#4d0000",fg="white")
bsqrt =Button (frame,image=square2,padx=8,pady=8,command=squre,bg="#ff8080",fg="white",height=60)
bsec = Button (frame,text="sec",padx=27,pady=14,command=sec,bg="blue",fg="white",font=("Arial",14,'bold'))
bcsc = Button (frame,text="csc",padx=27,pady=14,command=csc,bg="blue",fg="white",font=("Arial",14,'bold'))
btwan1 = Button(frame,text="x^3",padx=28,pady=14,command=t3,bg="#269900",fg="white",font=("Arial",14,'bold'))
bdm = Button(frame,text="x/y",padx=30,pady=14,command=Dfi,bg="#269900",fg="white",font=("Arial",14,'bold'))
bin = Button(frame,text="In",padx=34,pady=14,command=Ln,bg="blue",fg="white",font=("Arial",14,'bold'))
blog = Button(frame,text="log",padx=28,pady=14,command=Log,bg="blue",fg="white",font=("Arial",14,'bold'))
bpi = Button(frame,image=pi,padx=8,pady=14,command=Pi,bg="#269900",fg="white",height=60)

frame.place(x=3,y=5)

entry.grid(row=0,column=0,columnspan=5)

bpar.grid(row=1,column=0)
bBack.grid(row=1,column=4)
bclear.grid(row=1,column=3)
bsqrt.grid(row=1,column=2)
btwan.grid(row=1,column=1)

bsin.grid(row=2,column=0)
bcos.grid(row=2,column=1)
btan.grid(row=2,column=2)
bcot.grid(row=2,column=3)
bsec.grid(row=3,column=0)
bcsc.grid(row=3,column=1)
blog.grid(row=3,column=2)
bin.grid(row=3,column=3)
bdf.grid(row=3,column=4)
bfact.grid(row=2,column=4)

bdm.grid(row=4,column=0)
b7.grid(row=4,column=1)
b8.grid(row=4,column=2)
b9.grid(row=4,column=3)
bzf.grid(row=4,column=4)

bpi.grid(row=5,column=0)
b4.grid(row=5,column=1)
b5.grid(row=5,column=2)
b6.grid(row=5,column=3)
bmf.grid(row=5,column=4)

btwan1.grid(row=6,column=0)
b1.grid(row=6,column=1)
b2.grid(row=6,column=2)
b3.grid(row=6,column=3)
bAdd.grid(row=6,column=4)

badmf.grid(row=7,column=0)
b0.grid(row=7,column=1)
bdidi.grid(row=7,column=2)
bEquil.grid(row=7,column=3,columnspan=2)

window.mainloop()