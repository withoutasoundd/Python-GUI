#TIC TAC TOE game
def clear(eve):
	eve.widget.delete(0,END)
def sub():
	global v1,v2,t
	s.grid_forget()
	w.grid_forget()
	l1=Label(root,text=p1.get()+" Plays with X",width=60,fg="Blue",bg="black").grid(row=0,columnspan=3)
	l2=Label(root,text=p2.get()+" Plays with O",width=60,fg="red",bg="black").grid(row=1,columnspan=3)
	p1.grid_forget()
	p2.grid_forget()
	B0=Button(root,width=20,height=10,bg="black",command=lambda: play(3,0,B0))
	B1=Button(root,width=20,height=10,bg="black",command=lambda: play(3,1,B1))
	B2=Button(root,width=20,height=10,bg="black",command=lambda: play(3,2,B2))
	B3=Button(root,width=20,height=10,bg="black",command=lambda: play(4,0,B3))
	B4=Button(root,width=20,height=10,bg="black",command=lambda: play(4,1,B4))
	B5=Button(root,width=20,height=10,bg="black",command=lambda: play(4,2,B5))
	B6=Button(root,width=20,height=10,bg="black",command=lambda: play(5,0,B6))
	B7=Button(root,width=20,height=10,bg="black",command=lambda: play(5,1,B7))
	B8=Button(root,width=20,height=10,bg="black",command=lambda: play(5,2,B8))
	r1=Button(root,text="Replay !",command=reload)
	B0.grid(row=2,column=0)
	B1.grid(row=2,column=1)
	B2.grid(row=2,column=2)
	B3.grid(row=3,column=0)
	B4.grid(row=3,column=1)
	B5.grid(row=3,column=2)
	B6.grid(row=4,column=0)
	B7.grid(row=4,column=1)
	B8.grid(row=4,column=2)
	v1=Label(root,text=p1.get()+" won",fg="blue",bg="black")
	v2=Label(root,text=p2.get()+" won",fg="red",bg="black")
	t=Label(root,text="It's a TIE",fg="red",bg="black")
def mainscreen():
	global s,w,p1,p2,B0,B1,B2,B3,B4,B5,B6,B7,B8,e1,r1
	w=Label(root,text="Welcome to this simple game !",fg="black",bg="grey",width=80)
	w.grid(row=0)
	p1=Entry(root,width=60,fg="Blue",bg="black",borderwidth=5)
	p1.insert(0,"Player 1 enter your name ! ")
	p1.bind("<Button-1>",clear)
	p1.grid(row=1)
	p2=Entry(root,width=60,fg="blue",bg="black",borderwidth=5)
	p2.insert(0,"Player 2 enter your name ! ")
	p2.bind("<Button-1>",clear)
	p2.grid(row=2)
	s=Button(root,text="Submit",width=20,fg="white",bg="grey",command=sub)
	s.grid(row=3)
	r1=Button(root,text="Replay",command=reload,width=30,fg="Blue",bg="black")
	e1=Button(root,text="Exit",command=ex,width=30,fg="red",bg="black")
p=0
r=[[0,0,0],[0,0,0],[0,0,0]]
def win(l,c,C):
	w=False
	if l==0:
		if c==0:
			if r[l][c+1]==C and r[l][c+2]==C:
				return True
			elif r[l+1][c]==C and r[l+2][c]==C:
				return True 
			elif r[l+1][c+1]==C and r[l+2][c+2]==C:
				return True
		elif c==1:
			if r[l][c-1]==C and r[l][c+1]==C:
				return True
			elif r[l+1][c]==C and r[l+2][c]==C:
				return True
		elif c==2:
			if r[l][c-1]==C and r[l][c-2]==C:
				return True
			elif r[l+1][c]==C and r[l+2][c]==C:
				return True 
			elif r[l+1][c-1]==C and r[l+2][c-2]==C:
				return True
	elif l==1:
		if c==0:
			if r[l][c+1]==C and r[l][c+2]==C:
				return True
			elif r[l-1][c]==C and r[l+1][c]==C:
				return True 
		elif c==1:
			if r[l][c-1]==C and r[l][c+1]==C:
				return True
			elif r[l-1][c]==C and r[l+1][c]==C:
				return True
			elif r[l-1][c-1]==C and r[l+1][c+1]==C:
				return True 
			elif r[l+1][c-1]==C and r[l-1][c+1]==C:
				return True 
		elif c==2:
			if r[l][c-1]==C and r[l][c-2]==C:
				return True
			elif r[l+1][c]==C and r[l-1][c]==C:
				return True 
	elif l==2:
		if c==0:
			if r[l][c+1]==C and r[l][c+2]==C:
				return True
			elif r[l-1][c]==C and r[l-2][c]==C:
				return True 
			elif r[l-1][c+1]==C and r[l-2][c+2]==C:
				return True
		elif c==1:
			if r[l][c-1]==C and r[l][c+1]==C:
				return True
			elif r[l-1][c]==C and r[l-2][c]==C:
				return True
		elif c==2:
			if r[l][c-1]==C and r[l][c-2]==C:
				return True
			elif r[l-1][c]==C and r[l-2][c]==C:
				return True 
			elif r[l-1][c-1]==C and r[l-2][c-2]==C:
				return True
	return False
def ex():
	root.quit()
def tie():
	for i in range(len(r)):
		for k in r[i]:
			if k!="X" and k!="O":
				return False
	return True 
def wt():
	r1.grid(columnspan=3)
	e1.grid(columnspan=3)
def reload():
	global p,r
	v1.grid_forget()
	v2.grid_forget()
	e1.grid_forget()
	r1.grid_forget()
	r=[[0,0,0],[0,0,0],[0,0,0]]
	l1=Label(root,text=p1.get()+" Plays with X",width=60,fg="Blue",bg="black").grid(row=0,columnspan=3)
	l2=Label(root,text=p2.get()+" Plays with O",width=60,fg="red",bg="black").grid(row=1,columnspan=3)
	B0=Button(root,width=20,height=10,bg="black",command=lambda: play(3,0,B0))
	B1=Button(root,width=20,height=10,bg="black",command=lambda: play(3,1,B1))
	B2=Button(root,width=20,height=10,bg="black",command=lambda: play(3,2,B2))
	B3=Button(root,width=20,height=10,bg="black",command=lambda: play(4,0,B3))
	B4=Button(root,width=20,height=10,bg="black",command=lambda: play(4,1,B4))
	B5=Button(root,width=20,height=10,bg="black",command=lambda: play(4,2,B5))
	B6=Button(root,width=20,height=10,bg="black",command=lambda: play(5,0,B6))
	B7=Button(root,width=20,height=10,bg="black",command=lambda: play(5,1,B7))
	B8=Button(root,width=20,height=10,bg="black",command=lambda: play(5,2,B8))
	B0.grid(row=2,column=0)
	B1.grid(row=2,column=1)
	B2.grid(row=2,column=2)
	B3.grid(row=3,column=0)
	B4.grid(row=3,column=1)
	B5.grid(row=3,column=2)
	B6.grid(row=4,column=0)
	B7.grid(row=4,column=1)
	B8.grid(row=4,column=2)
def play(f,c,k):
	global p,r																																						 																
	f-=3																		 
	if p%2==0:																
		k.config(text="X",disabledforeground="blue",state=DISABLED)											 
		r[f][c]="X"															
		v=win(f,c,"X")
		x=tie()											 
		if v==True:													
			v1.grid(columnspan=3)
			wt()
		elif x==True:
			t.grid(columnspan=3)
			wt()
	else:
		k.config(text="O",disabledforeground="red",state=DISABLED)
		r[f][c]="O"
		v=win(f,c,"O")
		x=tie()
		if v==True:
			v2.grid(columnspan=3)
			wt()
		elif x==True:
			t.grid(columnspan=3)
			wt()
	p+=1
from tkinter import *
root=Tk()
T=[[0,0,0],[0,0,0],[0,0,0]]
root.title("Tic Tac Toe")
mainscreen()
root.mainloop()

