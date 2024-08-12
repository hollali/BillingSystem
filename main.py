from tkinter import * 

root=Tk()
root.title("Reatail Billing System")
root.geometry("1350x800")
root.iconbitmap('')
headingLabel=Label(root,text="Retail Billing System",font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text="Customer Details",font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name:',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number:',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number:',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=8)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack(pady=10)

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmestics',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10)

bathsoapEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10)

facecreamEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)


facewashLabel=Label(cosmeticsFrame,text='Face Wash:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10)

facewashEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10)

hairsprayEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10)

hairgelEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10)

bodylotionEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)

root.mainloop() 