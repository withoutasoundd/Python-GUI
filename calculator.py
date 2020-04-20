#code made on 20/04/2020 lol 
def cl(haja):
	n.delete(0,END)
def name():
	n1=Label(main,text="Hello "+n.get(),fg="white",bg="black",width=30)
	n.destroy()
	s.destroy()
	n1.grid(row=1,columnspan=4)
	c.grid(row=3,columnspan=4)
	b7.grid(row=4,column=0)
	b8.grid(row=4,column=1)
	b9.grid(row=4,column=2)
	badd.grid(row=4,column=3)
	b4.grid(row=5,column=0)
	b5.grid(row=5,column=1)
	b6.grid(row=5,column=2)
	bminus.grid(row=5,column=3)
	b1.grid(row=6,column=0)
	b2.grid(row=6,column=1)
	b3.grid(row=6,column=2)
	bmult.grid(row=6,column=3)
	bcl.grid(row=7,column=0,columnspan=2)
	beq.grid(row=7,column=2)
	bdiv.grid(row=7,column=3)
def calc(exp):
	s=exp
	n1=""
	n2=""
	f=False
	op=""
	for i in range(len(s)):
		if s[i].isnumeric() and f==False:
			n1+=s[i]
		elif s[i].isnumeric() and f==True:
			n2+=s[i]
		else:
			f=True
			op=s[i]
	if op=="+":
		return int(n1)+int(n2)
	elif op=="-":
		return int(n1)-int(n2)
	elif op=="/":
		return int(n1)/int(n2)
	else:
		return int(n1)*int(n2)
def click(num):
	k=c.get()
	c.delete(0,END)
	c.insert(0,k+num)
def equal():
	r=calc(c.get())
	c.delete(0,END)
	c.insert(0,r)
def cl1():
	c.delete(0,END)
from tkinter import *
main=Tk()
main.title("Calculator ")
w=Label(main,text="Welcome !",fg="blue",bg="grey")
w.grid(row=0,column=0,columnspan=4)
n=Entry(main,width=80,borderwidth=5,fg="white",bg="black")
n.insert(0,"Enter your name sir !")
n.bind("<Button-1>",cl)
n.grid(row=1,columnspan=4)
s=Button(main,text="Submit",padx=30,pady=20,fg="red",bg="black",command=name)
s.grid(row=2,columnspan=4)
c=Entry(main,borderwidth=5,width=80,fg="white",bg="black")

b7=Button(main,text="7",fg="white",bg="black",width=20,height=2,command=lambda: click("7"))
b8=Button(main,text="8",fg="white",bg="black",width=20,height=2,command=lambda: click("8"))
b9=Button(main,text="9",fg="white",bg="black",width=20,height=2,command=lambda: click("9"))
badd=Button(main,text="+",fg="white",bg="red",width=20,height=2,command=lambda: click("+"))

b4=Button(main,text="4",fg="white",bg="black",width=20,height=2,command=lambda: click("4"))
b5=Button(main,text="5",fg="white",bg="black",width=20,height=2,command=lambda: click("5"))
b6=Button(main,text="6",fg="white",bg="black",width=20,height=2,command=lambda: click("6"))
bminus=Button(main,text="-",fg="white",bg="red",width=20,height=2,command=lambda: click("-"))

b1=Button(main,text="1",fg="white",bg="black",width=20,height=2,command=lambda: click("1"))
b2=Button(main,text="2",fg="white",bg="black",width=20,height=2,command=lambda: click("2"))
b3=Button(main,text="3",fg="white",bg="black",width=20,height=2,command=lambda: click("3"))
beq=Button(main,text="=",fg="white",bg="grey",width=20,height=2,command=equal)

bdiv=Button(main,text="/",fg="white",bg="red",width=20,height=2,command=lambda: click("/"))
bmult=Button(main,text="*",fg="white",bg="red",width=20,height=2,command=lambda: click("*"))
bcl=Button(main,text="AC",fg="black",bg="grey",width=45,height=2,command=cl1)









main.mainloop()