from tkinter import * 

root=Tk()
root.title("Reatail Billing System")
root.geometry("1270x685")
root.iconbitmap()
headingLabel=Label(root,text="Retail Billing System",font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
customer_details_frame.pack()

nameLabel=Label(customer_details_frame,text='Name:',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1)

root.mainloop()