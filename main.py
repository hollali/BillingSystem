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
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

bathsoapEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

facecreamEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)


facewashLabel=Label(cosmeticsFrame,text='Face Wash:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

facewashEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

hairsprayEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

hairgelEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

bodylotionEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

riceEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
riceEntry.grid(row=0,column=1,pady=9,padx=10)

oilLabel=Label(groceryFrame,text='Oil:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

riceEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
riceEntry.grid(row=1,column=1,pady=9,padx=10)

coffeeLabel=Label(groceryFrame,text='Coffee:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
coffeeLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

coffeeEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
coffeeEntry.grid(row=2,column=1,pady=9,padx=10)

teaLabel=Label(groceryFrame,text='Tea:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

teaEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
teaEntry.grid(row=3,column=1,pady=9,padx=10)

sugarLabel=Label(groceryFrame,text='Sugar:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

sugarEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)

wheatLabel=Label(groceryFrame,text='Rice:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

wheatEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
wheatEntry.grid(row=5,column=1,pady=9,padx=10)

drinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
drinksFrame.grid(row=0,column=2)

maazaLabel=Label(drinksFrame,text='Maaza:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

maazaEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)

pepisLabel=Label(drinksFrame,text='Pepis:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
pepisLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

PepisEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
PepisEntry.grid(row=1,column=1,pady=9,padx=10)

dewLabel=Label(drinksFrame,text='Dew:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
dewLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

dewEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
dewEntry.grid(row=2,column=1,pady=9,padx=10)

fantaLabel=Label(drinksFrame,text='Fanta:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
fantaLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

fantaEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
fantaEntry.grid(row=3,column=1,pady=9,padx=10)

cokeLabel=Label(drinksFrame,text='Coca Cola:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
cokeLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

cokeEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
cokeEntry.grid(row=4,column=1,pady=9,padx=10)

spriteLabel=Label(drinksFrame,text='Sprite:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

spriteEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
spriteEntry.grid(row=5,column=1,pady=9,padx=10)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3)

billareaLabel=Label(billframe,text='Label Area',font=("times new roman",15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

textarea=Text(billframe,height=18,width=60)
textarea.pack()


root.mainloop() 