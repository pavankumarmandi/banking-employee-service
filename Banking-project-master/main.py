#!/usr/bin/pyhton
import os
import tkinter
from tkinter import *

Dict={}
f=open("accountdb.txt",'r')
accno=0

for line in f:
	List=line.split()
	Dict[int(List[0])]=[List[1],float(List[2].rstrip('\n')),List[3],List[4],List[5],List[6]]
	accno=int(List[0])
print (Dict)
f.close()
def ruli():
	class Create(Frame):
		def __init__(self,master):
			Frame.__init__(self,master)
			self.grid()
			self.create_widgets()
		def create_widgets(self):
			self.label=Label(self)
			self.label["text"]="   "
			self.label.grid(row=0,column=0,sticky=S)

			self.label1=Label(self)
			self.label1["text"]="Enter your full name"
			self.label1.grid(row=0,column=1,sticky=S)
			self.name=Entry(self)
			self.name.grid(row=1,column=1,sticky=S)

			self.label2=Label(self)
			self.label2["text"]="Enter your initial balance"
			self.label2.grid(row=2,column=1,sticky=S)
			self.balance=Entry(self)
			self.balance.grid(row=3,column=1,sticky=S)

			self.label3=Label(self)
			self.label3["text"]="Enter your address"
			self.label3.grid(row=4,column=1,sticky=S)
			self.address=Entry(self)
			self.address.grid(row=5,column=1,sticky=S)

			self.label4=Label(self)
			self.label4["text"]="Enter your phone number:"
			self.label4.grid(row=6,column=1,sticky=S)
			self.phone=Entry(self)
			self.phone.grid(row=7,column=1,sticky=S)

			self.label5=Label(self)
			self.label5["text"]="Enter your gmail:"
			self.label5.grid(row=8,column=1,sticky=S)
			self.gmail=Entry(self)
			self.gmail.grid(row=9,column=1,sticky=S)

			self.label6=Label(self)
			self.label6["text"]="Enter your account type:"
			self.label6.grid(row=10,column=1,sticky=S)
			self.acctype=Entry(self)
			self.acctype.grid(row=11,column=1,sticky=S)

			self.button=Button(self)
			self.button["text"]="SUBMIT"
			self.button["fg"]="green"
			self.button["command"]=self.collect_data
			self.button.grid(row=13,column=1,sticky=S)
			self.msg=Text(self,width=30,height=5,wrap=WORD)
			self.msg.insert(0.0,"enter amount greater than 5000")
			self.msg.grid(row=12,column=1,sticky=S)
		def collect_data(self):
			global accno
			global Dict
			while int(self.balance.get())<5000:
				self.msg.delete(0.0,END)
				self.msg.insert(0.0,"Please enter amount greater than 5000")
				self.balance.delete(0,END)
			#List=[accounts[len(accounts)-1][0]+1,self.name.get(),int(self.balance.get())]
			self.msg.delete(0.0,END)
			self.msg.insert(0.0,"Your account number is: "+str(accno+1))
			accno+=1
			Dict[accno]=[self.name.get(),int(self.balance.get()),self.address.get(),self.phone.get(),self.gmail.get(),self.acctype.get()]
			print (Dict)
			self.balance.delete(0,END)
			self.name.delete(0,END)
			self.address.delete(0,END)
			self.phone.delete(0,END)
			self.gmail.delete(0,END)
			self.acctype.delete(0,END)

	class Balance(Frame):
		def __init__(self,master):
			Frame.__init__(self,master)
			self.grid()
			self.create_widgets()
		def create_widgets(self):
			self.label1=Label(self)
			self.label1["text"]="   "
			self.label1.grid(row=0,column=0,sticky=S)
			self.label=Label(self)
			self.label["text"]="Enter your account number"
			self.label.grid(row=0,column=1,sticky=S)
			self.acc=Entry(self)
			self.acc.grid(row=1,column=1,sticky=S)
			self.button=Button(self)
			self.button["text"]="SUBMIT"
			self.button["fg"]="green"
			self.button["command"]=self.collect_data
			self.button.grid(row=2,column=1,sticky=S)
			self.msg=Text(self,width=30,height=5,wrap=WORD)
			self.msg.insert(0.0,"Enter a valid account number.")
			self.msg.grid(row=3,column=1,sticky=S)
		def collect_data(self):
			global Dict
			num=int(self.acc.get())
			if not num in Dict.keys():
				self.msg.delete(0.0,END)
				self.msg.insert(0.0,"Invalid account number!")
				self.acc.delete(0.0,END)
				num=int(self.acc.get())
			self.msg.delete(0.0,END)
			self.msg.insert(0.0,"Balance: "+str(Dict[num][1]))
	class Deposit(Frame):
		def __init__(self,master):
			Frame.__init__(self,master)
			self.grid()
			self.create_widgets()
		def create_widgets(self):
			self.label1=Label(self)
			self.label1["text"]="   "
			self.label1.grid(row=0,column=0,sticky=S)
			self.label=Label(self)
			self.label["text"]="Enter your account number"
			self.label.grid(row=0,column=1,sticky=S)
			self.acc=Entry(self)
			self.acc.grid(row=1,column=1,sticky=S)
			self.label=Label(self)
			self.label["text"]="Enter the amount to be deposited."
			self.label.grid(row=3,column=1,sticky=S)

			self.amt=Entry(self)
			self.amt.grid(row=4,column=1,sticky=S)
			self.button=Button(self)
			self.button["text"]="SUBMIT"
			self.button["fg"]="green"
			self.button["command"]=self.collect_data
			self.button.grid(row=6,column=1,sticky=S)
			self.msg=Text(self,width=30,height=5,wrap=WORD)
			self.msg.insert(0.0,"Final amount will be displayed here.")
			self.msg.grid(row=5,column=1,sticky=S)
		def collect_data(self):
			global Dict
			num=int(self.acc.get())
			if not num in Dict.keys():
				self.msg.delete(0.0,END)
				self.msg.insert(0.0,"Invalid account number!")
				self.acc.delete(0.0,END)
				num=int(self.acc.get())
			add=float(self.amt.get())
			Dict[num][1]=Dict[num][1]+add
			self.msg.delete(0.0,END)
			self.msg.insert(0.0,"Balance: "+str(Dict[num][1]))
	class Withdraw(Frame):
		def __init__(self,master):
			Frame.__init__(self,master)
			self.grid()
			self.create_widgets()
		def create_widgets(self):
			self.label1=Label(self)
			self.label1["text"]="   "
			self.label1.grid(row=0,column=0,sticky=S)
			self.label=Label(self)
			self.label["text"]="Enter your account number"
			self.label.grid(row=0,column=1,sticky=S)
			self.acc=Entry(self)
			self.acc.grid(row=1,column=1,sticky=S)
			self.label=Label(self)
			self.label["text"]="Enter the amount to be withdrawn."
			self.label.grid(row=3,column=1,sticky=S)

			self.amt=Entry(self)
			self.amt.grid(row=4,column=1,sticky=S)
			self.button=Button(self)
			self.button["text"]="SUBMIT"
			self.button["fg"]="green"
			self.button["command"]=self.collect_data
			self.button.grid(row=6,column=1,sticky=S)
			self.msg=Text(self,width=30,height=5,wrap=WORD)
			self.msg.insert(0.0,"Final amount will be displayed here.")
			self.msg.grid(row=5,column=1,sticky=S)
		def collect_data(self):
			global Dict
			num=int(self.acc.get())
			if not num in Dict.keys():
				self.msg.delete(0.0,END)
				self.msg.insert(0.0,"Invalid account number!")
				self.acc.delete(0.0,END)
				num=int(self.acc.get())
			add=float(self.amt.get())
			if add<=Dict[num][1]:
				Dict[num][1]=Dict[num][1]-add
				self.msg.delete(0.0,END)
				self.msg.insert(0.0,"Balance: "+str(Dict[num][1]))
			else:
				self.msg.delete(0.0,END)
				self.msg.insert(0.0,"Amount insufficient!")
	class transact(Frame):
		def __init__(self,master):
			Frame.__init__(self,master)
			self.grid()
			self.create_widgets()
		def create_widgets(self):
			self.label=Label(self)
			self.label["text"]="   "
			self.label.grid(row=0,column=0,sticky=S)
			self.label1=Label(self)
			self.label1["text"]="Enter your account number of sender:"
			self.label1.grid(row=1,column=1,sticky=S)
			self.acc=Entry(self)
			self.acc.grid(row=2,column=1,sticky=S)

			self.label2=Label(self)
			self.label2["text"]="Enter the amount to be send."
			self.label2.grid(row=4,column=1,sticky=S)
			self.amt=Entry(self)
			self.amt.grid(row=5,column=1,sticky=S)

			self.label3=Label(self)
			self.label3["text"]="Enter your account number of reciever:"
			self.label3.grid(row=6,column=1,sticky=S)
			self.accto=Entry(self)
			self.accto.grid(row=7,column=1,sticky=S)

			self.button=Button(self)
			self.button["text"]="SUBMIT"
			self.button["fg"]="green"
			self.button["command"]=self.collect_data
			self.button.grid(row=8,column=1,sticky=S)
			self.msg=Text(self,width=30,height=1,wrap=WORD)
			self.msg.grid(row=9,column=1,sticky=S)
			self.msgto=Text(self,width=30,height=1,wrap=WORD)
			self.msgto.grid(row=10,column=1,sticky=S)
		def update(self,add):
			global Dict
			num=int(self.accto.get())
			if not num in Dict.keys():
				self.msg.delete(0.0,END)
				self.msg.insert(0.0,"Invalid account number!")
				self.acc.delete(0.0,END)
				num=int(self.accto.get())
			Dict[num][1]=Dict[num][1]+add
			self.msg.delete(0.0,END)
			self.msg.insert(0.0,"Reciever Balance:"+str(Dict[num][1]))
		# def collect_data(self):
		# 	global Dict
		# 	num=int(self.accto.get())
		# 	if not num in Dict.keys():
		# 		self.msg.delete(0.0,END)
		# 		self.msg.insert(0.0,"Invalid account number!")
		# 		self.acc.delete(0.0,END)
		# 		num=int(self.accto.get())
		# 	add=float(self.amt.get())
		# 	Dict[num][1]=Dict[num][1]+add
		# 	self.msg.delete(0.0,END)
		# 	self.msg.insert(0.0,"Balance:"+str(Dict[num][1]))
		def collect_data(self):
			global Dict
			num=int(self.acc.get())
			if not num in Dict.keys():
				self.msg.delete(0.0,END)
				self.msg.insert(0.0,"Invalid account number!")
				self.acc.delete(0.0,END)
				num=int(self.acc.get())
			add=float(self.amt.get())
			if add<=Dict[num][1]:
				Dict[num][1]=Dict[num][1]-add
				self.msgto.delete(0.0,END)
				self.msgto.insert(0.0,"Sender Balance :"+str(Dict[num][1]))
			else:
				self.msgto.delete(0.0,END)
				self.msgto.insert(0.0,"Amount insufficient!")
			self.update(add)
	class Search(Frame):
		def __init__(self,master):
			Frame.__init__(self,master)
			self.grid()
			self.create_widgets()
		def create_widgets(self):
			self.label1=Label(self)
			self.label1["text"]="   "
			self.label1.grid(row=0,column=0,sticky=S)
			self.label=Label(self)
			self.label["text"]="Enter name(full or partial)"
			self.label.grid(row=0,column=1,sticky=S)
			self.name=Entry(self)
			self.name.grid(row=1,column=1,sticky=S)

			self.button=Button(self)
			self.button["text"]="SUBMIT"
			self.button["fg"]="green"
			self.button["command"]=self.collect_data
			self.button.grid(row=6,column=1,sticky=S)
			self.msg=Text(self,width=40,height=8,wrap=WORD)
			self.msg.insert(0.0," ")
			self.msg.grid(row=5,column=1,sticky=S)
		def collect_data(self):
			global Dict
			name=self.name.get()
			for num in Dict.keys():
				if Dict[num][0].find(name)!=-1:
					self.msg.delete(0.0,END)
					self.msg.insert(0.0,"Name: "+Dict[num][0]+"\nAccount Number: "+str(num)+"\nBalance:"+str(Dict[num][1])+"\nAddress:"+Dict[num][2]+"\nphone:"+Dict[num][3]+"\ngmail:"+Dict[num][4]+"\nAccount Type:"+Dict[num][5])
					return
			self.msg.delete(0.0,END)
			self.msg.insert(0.0,"Account not found.")
	class Close(Frame):
		def __init__(self,master):
			Frame.__init__(self,master)
			self.grid()
			self.create_widgets()
		def create_widgets(self):
			self.label1=Label(self)
			self.label1["text"]="   "
			self.label1.grid(row=0,column=0,sticky=S)
			self.label=Label(self)
			self.label["text"]="Enter your account number"
			self.label.grid(row=0,column=1,sticky=S)
			self.acc=Entry(self)
			self.acc.grid(row=1,column=1,sticky=S)
			self.button=Button(self)
			self.button["text"]="SUBMIT"
			self.button["fg"]="red"
			self.button["command"]=self.collect_data
			self.button.grid(row=2,column=1,sticky=S)
			self.msg=Text(self,width=30,height=5,wrap=WORD)
			self.msg.insert(0.0,"  ")
			self.msg.grid(row=3,column=1,sticky=S)
		def collect_data(self):
			global Dict
			global accno
			num=int(self.acc.get())
			if not num in Dict.keys():
				self.msg.delete(0.0,END)
				self.msg.insert(0.0,"Invalid account number!")
				self.acc.delete(0.0,END)
				num=int(self.acc.get())
			self.msg.insert(0.0,"amount to be refunded: "+str(Dict[num][1]))
			del Dict[num]
			print (Dict)
			accno-=1
	def win1():
		root=Tk()
		root.title("Create Account")
		root.geometry("300x400")
		Create(root)
		root.mainloop()
	def win2():
		root=Tk()
		root.title("Balance Enquiry")
		root.geometry("300x400")
		app=Balance(root)
		root.mainloop()
	def win3():
		root=Tk()
		root.title("Deposit Amount")
		root.geometry("250x400")
		app=Deposit(root)
		root.mainloop()
	def win4():
		root=Tk()
		root.title("Withdraw  Amount")
		root.geometry("250x400")
		app=Withdraw(root)
		root.mainloop()
	def win5():
		root=Tk()
		root.title("Search")
		root.geometry("250x400")
		app=Search(root)
		root.mainloop()
	def win6():
		root=Tk()
		root.title("Close Account")
		root.geometry("250x400")
		app=Close(root)
		root.mainloop()

	def win7():
		root=Tk()
		root.title("transact amount")
		root.geometry("250x400")
		app=transact(root)
		root.mainloop()

	def quit_fun():
		global Dict
		fi=open("accountdb.txt",'w')
		#Dict=sorted(Dict)
		print (Dict)
		for num in Dict:
			List=[]
			List.append(str(num))
			List.append(Dict[num][0])
			List.append(str(Dict[num][1]))
			List.append(str(Dict[num][2]))
			List.append(str(Dict[num][3]))
			List.append(str(Dict[num][4]))
			List.append(str(Dict[num][5]))
			string='\t'.join(List)+'\n'
			print (string)
			fi.write(string)
		print ('successful')
	root=Tk()
	root.title("online Banking employee services")
	root.geometry("500x500")
	app=Frame(root)
	app.grid()

	label=Label(app)
	label["text"]="Welcome to Banking Services.\n Click on the service you wish to avail."
	label.grid(row=0,column=2,columnspan=5,	sticky=SE)

	button1=Button(app)
	button1["text"]="Create Account"
	button1["bg"]="orange"
	button1["fg"]="blue"
	button1["command"]=win1
	button1.grid(row=1,column=3,sticky=S)

	button2=Button(app)
	button2["text"]="Balance Enquiry"
	button2["bg"]="orange"
	button2["fg"]="blue"
	button2["command"]=win2
	button2.grid(row=3,column=3,sticky=S)

	button3=Button(app)
	button3["text"]="Deposit"
	button3["bg"]="orange"
	button3["fg"]="blue"
	button3["command"]=win3
	button3.grid(row=4,column=3,sticky=S)

	button4=Button(app)
	button4["text"]="Withdraw"
	button4["bg"]="orange"
	button4["fg"]="blue"
	button4["command"]=win4
	button4.grid(row=5,column=3,sticky=S)

	button5=Button(app)
	button5["text"]="Search by Name"
	button5["bg"]="orange"
	button5["fg"]="blue"
	button5["command"]=win5
	button5.grid(row=6,column=3,sticky=S)

	button6=Button(app)
	button6["text"]="Delete Account"
	button6["bg"]="yellow"
	button6["fg"]="red"
	button6["command"]=win6
	button6.grid(row=7,column=3,sticky=S)


	button7=Button(app)
	button7["text"]="transact"
	button7["bg"]="orange"
	button7["fg"]="blue"
	button7["command"]=win7
	button7.grid(row=8,column=3,sticky=S)

	button8=Button(app)
	button8["text"]="Save"
	button8["bg"]="yellow"
	button8["fg"]="green"
	button8["command"]=quit_fun
	button8.grid(row=9,column=3,sticky=S)
