from tkinter import * 
#functionality
def total():
    #*Cosmetics price calculation
    soapprice=int(bathsoapEntry.get())*20
    facecreamprice=int(facecreamEntry.get())*30
    facewashprice=int(facewashEntry.get())*25
    hairsprayprice=int(hairsprayEntry.get())*50
    hairgelprice=int(hairgelEntry.get())*40
    bodylotionprice=int(bodylotionEntry.get())*60

    totalcosmeticprice=soapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    costmeticpriceEntry.insert(0,'GHS' +str(totalcosmeticprice))

    #*Grocery Price calculation
    riceprice=int(riceEntry.get())*70
    oilprice=int(oilEntry.get())*45
    coffeeprice=int(coffeeEntry.get())*25
    teaprice=int(teaEntry.get())*15
    sugarprice=int(sugarEntry.get())*32
    wheatprice=int(wheatEntry.get())*45

    totalgroceryprice=riceprice+oilprice+coffeeprice+teaprice+sugarprice+wheatprice
    grocerypriceEntry.insert(0,'GHS' +str(totalgroceryprice))

    #*Cold Drink Price calculation
    maazaprice=int(maazaEntry.get())*5
    pepsiprice=int(pepisEntry.get())*7
    dewprice=int(dewEntry.get())*6
    fantaprice=int(fantaEntry.get())*8
    cokeprice=int(cokeEntry.get())*10
    spriteprice=int(spriteEntry.get())*7

    totaldrinksprice=maazaprice+pepsiprice+dewprice+fantaprice+cokeprice+spriteprice
    drinkspriceEntry.insert(0,'GHS' + str(totaldrinksprice))
#! GUI Port
root=Tk()
root.title("Reatail Billing System")
root.geometry("1350x820")
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
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmestics',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

bathsoapEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

facecreamEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

facewashLabel=Label(cosmeticsFrame,text='Face Wash:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

facewashEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
facewashEntry.grid(row=2,column=1,pady=9,padx=10)
facewashEntry.insert(0,0)

hairsprayLabel=Label(cosmeticsFrame,text='Hair Spray:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

hairsprayEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
hairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

hairgelEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
hairgelEntry.grid(row=4,column=1,pady=9,padx=10)
hairgelEntry.insert(0,0)

bodylotionLabel=Label(cosmeticsFrame,text='Body Lotion:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

bodylotionEntry=Entry(cosmeticsFrame,font=("times new roman",15,'bold'),width=10,bd=7)
bodylotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
groceryFrame.grid(row=0,column=1)

riceLabel=Label(groceryFrame,text='Rice:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

riceEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
riceEntry.grid(row=0,column=1,pady=9,padx=10)
riceEntry.insert(0,0)

oilLabel=Label(groceryFrame,text='Oil:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

oilEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
oilEntry.grid(row=1,column=1,pady=9,padx=10)
oilEntry.insert(0,0)

coffeeLabel=Label(groceryFrame,text='Coffee:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
coffeeLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

coffeeEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
coffeeEntry.grid(row=2,column=1,pady=9,padx=10)
coffeeEntry.insert(0,0)

teaLabel=Label(groceryFrame,text='Tea:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

teaEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
teaEntry.grid(row=3,column=1,pady=9,padx=10)
teaEntry.insert(0,0)

sugarLabel=Label(groceryFrame,text='Sugar:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

sugarEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
sugarEntry.grid(row=4,column=1,pady=9,padx=10)
sugarEntry.insert(0,0)

wheatLabel=Label(groceryFrame,text='Rice:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

wheatEntry=Entry(groceryFrame,font=("times new roman",15,'bold'),width=10,bd=7)
wheatEntry.grid(row=5,column=1,pady=9,padx=10)
wheatEntry.insert(0,0)

drinksFrame=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
drinksFrame.grid(row=0,column=2)

maazaLabel=Label(drinksFrame,text='Maaza:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

maazaEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)
maazaEntry.insert(0,0)

pepisLabel=Label(drinksFrame,text='Pepis:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
pepisLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

pepisEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
pepisEntry.grid(row=1,column=1,pady=9,padx=10)
pepisEntry.insert(0,0)

dewLabel=Label(drinksFrame,text='Dew:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
dewLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

dewEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
dewEntry.grid(row=2,column=1,pady=9,padx=10)
dewEntry.insert(0,0)

fantaLabel=Label(drinksFrame,text='Fanta:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
fantaLabel.grid(row=3,column=0,pady=9,padx=10,sticky="w")

fantaEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
fantaEntry.grid(row=3,column=1,pady=9,padx=10)
fantaEntry.insert(0,0)

cokeLabel=Label(drinksFrame,text='Coca Cola:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
cokeLabel.grid(row=4,column=0,pady=9,padx=10,sticky="w")

cokeEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
cokeEntry.grid(row=4,column=1,pady=9,padx=10)
cokeEntry.insert(0,0)

spriteLabel=Label(drinksFrame,text='Sprite:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=5,column=0,pady=9,padx=10,sticky="w")

spriteEntry=Entry(drinksFrame,font=("times new roman",15,'bold'),width=10,bd=7)
spriteEntry.grid(row=5,column=1,pady=9,padx=10)
spriteEntry.insert(0,0)

billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=("times new roman",15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=60,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=12,relief=GROOVE)
billmenuFrame.pack()

costmeticpriceLabel=Label(billmenuFrame,text='Costmetic Price:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
costmeticpriceLabel.grid(row=0,column=0,pady=9,padx=10,sticky="w")

costmeticpriceEntry=Entry(billmenuFrame,font=("times new roman",15,'bold'),width=10,bd=7)
costmeticpriceEntry.grid(row=0,column=1,pady=9,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=9,padx=10,sticky="w")

grocerypriceEntry=Entry(billmenuFrame,font=("times new roman",15,'bold'),width=10,bd=7)
grocerypriceEntry.grid(row=1,column=1,pady=9,padx=10)

drinkspriceLabel=Label(billmenuFrame,text='Cold Drinks Price:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=9,padx=10,sticky="w")

drinkspriceEntry=Entry(billmenuFrame,font=("times new roman",15,'bold'),width=10,bd=7)
drinkspriceEntry.grid(row=2,column=1,pady=9,padx=10)

costmetaxLabel=Label(billmenuFrame,text='Costmetic Tax:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
costmetaxLabel.grid(row=0,column=2,pady=9,padx=10,sticky="w")

costmetaxEntry=Entry(billmenuFrame,font=("times new roman",15,'bold'),width=10,bd=7)
costmetaxEntry.grid(row=0,column=3,pady=9,padx=10)

grocerytaxLabel=Label(billmenuFrame,text='Grocery Tax:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=9,padx=10,sticky="w")

grocerytaxEntry=Entry(billmenuFrame,font=("times new roman",15,'bold'),width=10,bd=7)
grocerytaxEntry.grid(row=1,column=3,pady=9,padx=10)

drinksTaxLabel=Label(billmenuFrame,text='Cold Drinks Tax:', font=("times new roman",15,'bold'),bg='gray20',fg='white')
drinksTaxLabel.grid(row=2,column=2,pady=9,padx=10,sticky="w")

drinksTaxEntry=Entry(billmenuFrame,font=("times new roman",15,'bold'),width=10,bd=7)
drinksTaxEntry.grid(row=2,column=3,pady=9,padx=10)

buttonFrame=Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=2)

billButton=Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
billButton.grid(row=0,column=1,pady=20,padx=2)

emailButton=Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
emailButton.grid(row=0,column=2,pady=20,padx=2)

printButton=Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
printButton.grid(row=0,column=3,pady=20,padx=2)

clearButton=Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,pady=10)
clearButton.grid(row=0,column=4,pady=20,padx=2)

root.mainloop() 