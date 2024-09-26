from tkinter import*
from tkinter import messagebox
import random,os,tempfile,smtplib
#functionality part

def clear():

     bathsoapEntry.delete(0,END)
     facecreamEntry.delete(0,END)
     facewashEntry.delete(0,END)
     hairgelEntry.delete(0,END)
     hairsprayEntry.insert(0,0)
     bodylotionEntry.delete(0,END)
     riceEntry.delete(0,END)
     sugarEntry.delete(0,END)
     oilEntry.delete(0,END)
     daalEntry.delete(0,END)
     teaEntry.delete(0,END)
     wheatEntry.delete(0,END)
     pepsiEntry.delete(0,END)
     cokeEntry.delete(0,END)
     coldcoffeeEntry.delete(0,END)
     dewEntry.delete(0,END)
     frootiEntry.delete(0,END)
     spriteEntry.delete(0,END)


     bathsoapEntry.insert(0,0)
     facecreamEntry.insert(0,0)
     facewashEntry.insert(0,0)
     hairgelEntry.insert(0,0)
     hairsprayEntry.insert(0,0)
     bodylotionEntry.insert(0,0)
     riceEntry.insert(0,0)
     sugarEntry.insert(0,0)
     oilEntry.insert(0,0)
     daalEntry.insert(0,0)
     teaEntry.insert(0,0)
     wheatEntry.insert(0,0)
     pepsiEntry.insert(0,0) 
     cokeEntry.insert(0,0)
     coldcoffeeEntry.insert(0,0)
     dewEntry.insert(0,0)
     frootiEntry.insert(0,0)
     spriteEntry.insert(0,0)

     cosmetictaxEntry.delete(0,END)
     grocerytaxEntry.delete(0,END)
     drinkstaxEntry.delete(0,END)

     cosmeticpriceEntry.delete(0,END)
     grocerypriceEntry.delete(0,END)
     drinkspriceEntry.delete(0,END)

     nameEntry.delete(0,END)
     phoneEntry.delete(0,END)
     billnumberEntry.delete(0,END)

     textarea.delete(1.0,END)


def send_email():
     def send_gmail():
          try:
            ob = smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),passwordEntry.get())
            message = email_textarea.get(1.0,END)
            reciever_address = recieverEntry.get()
            ob.sendmail(senderEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent.',parent=root1)
          except:
               messagebox.showerror('Error','Something went wrong, Please try again.',parent=root1)
               root1.destroy()

     if textarea.get(1.0,END)=='\n':
          messagebox.showerror('Error','Bill is empty.')
     else:
          root1 = Toplevel()
          root1.grab_set()
          root1.title('Send Gmail')
          root1.config(bg='indianred')
          root1.resizable(height=False,width=False)

          senderFrame = LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='indianred',fg='white')
          senderFrame.grid(row=0,column=0,padx=40,pady=20)

          senderLabel = Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='indianred',fg='white')
          senderLabel.grid(row=0,column=0,padx=10,pady=8)

          senderEntry = Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
          senderEntry.grid(row=0,column=1,padx=10,pady=8)

          passwordLabel = Label(senderFrame,text='Password',font=('arial',14,'bold'),bd=6,bg='indianred',fg='white')
          passwordLabel.grid(row=1,column=0,padx=10,pady=8)

          passwordEntry = Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
          passwordEntry.grid(row=1,column=1,padx=10,pady=8)

          recipientFrame = LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='indianred',fg='white')
          recipientFrame.grid(row=1,column=0,padx=40,pady=20)

          recieverLabel = Label(recipientFrame,text='Email Address',font=('arial',14,'bold'),bd=6,bg='indianred',fg='white')
          recieverLabel.grid(row=0,column=0,padx=10,pady=8)

          recieverEntry = Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
          recieverEntry.grid(row=0,column=1,padx=10,pady=8)
          
          messageLabel = Label(recipientFrame,text='Message',font=('arial',14,'bold'),bd=6,bg='indianred',fg='white')
          messageLabel.grid(row=1,column=0,padx=10,pady=8)
          
          email_textarea = Text(recipientFrame,font=('arial',14,'bold'),bd=2,relief=SUNKEN,width=42,height=11)
          email_textarea.grid(row=2,column=0,columnspan=2)
          textarea.delete(1.0,END)
          email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))

          sendButton = Button(root1,text='SEND',font=('arial',14,'bold'),command=send_gmail)
          sendButton.grid(row=2,column=0,pady=20)
     
          
          root1.mainloop()


  
def print_bill():
     if textarea.get(1.0,END)=='\n':
          messagebox.showerror('Error','Bill is empty.')
     else:
         file = tempfile.mkdtemp('.txt')
         open(file,'w').write(textarea.get(1.0,END))
         os.startfile(file,'print')

def search_bill():
     for i in os.listdir('bills/'):
          if i.split('.')[0] == billnumberEntry.get():
               f = open(f'bills/{i}','r')
               textarea.delete('1.0',END)
               for data in f:
                    textarea.insert(END,data)
               f.close()
               break
          else:
               messagebox.showerror('Error','Invalid Bill Number')
   
if not os.path.exists('bills'):
     os.mkdir('bills')

def save_bill():
     global billnumber
     result = messagebox.askyesno('Confirm','Do you want to save the bill?')
     if result:
          bill_content = textarea.get(1.0,END)
          file = open(f'bills/ {billnumber}.txt','w')
          file.write(bill_content)
          file.close()
          messagebox.showinfo('Success',f'Bill number {billnumber} is saved successfully.')
          billnumber = random.randint(500,1000)
 
billnumber = random.randint(500,1000)

def bill_area():

    if nameEntry.get()=='' or phoneEntry.get()=='':
          messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticpriceEntry.get()=='' and grocerypriceEntry.get()=='' and drinkspriceEntry.get()=='':
          messagebox.showerror('Error','No Products Are Selected')
    elif cosmeticpriceEntry.get()=='0 Rs' and grocerypriceEntry.get()=='0 Rs' and drinkspriceEntry.get()=='0 Rs':
          messagebox.showerror('Error','No Products Are Selected') 
          textarea.delete(1.0,END)
    else:                                                                   
         textarea.insert(END,'\t\tWelcome Customer\n')
         textarea.insert(END,f'\nBill Number: {billnumber}')
         textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}')
         textarea.insert(END,f'\nPhone Number: {phoneEntry.get()}')
         textarea.insert(END,'\n=======================================================')
         textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
         textarea.insert(END,'\n=======================================================')
         if bathsoapEntry.get()!='0':
              textarea.insert(END,f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{bathsoapprice} Rs')
         if facecreamEntry.get()!='0':
              textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\t{facecreamprice} Rs')
         if facewashEntry.get()!='0':
              textarea.insert(END,f'\nFace Wash\t\t\t{facewashEntry.get()}\t\t\t{facewashprice} Rs')
         if hairsprayEntry.get()!='0':
              textarea.insert(END,f'\nHair Spray\t\t\t{hairsprayEntry.get()}\t\t\t{hairsprayprice} Rs')
         if hairgelEntry.get()!='0':
              textarea.insert(END,f'\nHair Gel\t\t\t{hairgelEntry.get()}\t\t\t{hairgelprice} Rs')
         if bodylotionEntry.get()!='0':
              textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')
         if riceEntry.get()!='0':
              textarea.insert(END,f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice} Rs')
         if oilEntry.get()!='0':
              textarea.insert(END,f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice} Rs')     
         if sugarEntry.get()!='0':
              textarea.insert(END,f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice} Rs')
         if wheatEntry.get()!='0':
              textarea.insert(END,f'\nWheat\t\t\t{wheatEntry.get()}\t\t\t{wheatprice} Rs')
         if teaEntry.get()!='0':
              textarea.insert(END,f'\nTea\t\t\t{teaEntry.get()}\t\t\t{teaprice} Rs')
              textarea.insert(END,f'\nBody Lotion\t\t\t{bodylotionEntry.get()}\t\t\t{bodylotionprice} Rs')
         if daalEntry.get()!='0':
              textarea.insert(END,f'\nDaal\t\t\t{daalEntry.get()}\t\t\t{daalprice} Rs')
         if frootiEntry.get()!='0':
              textarea.insert(END,f'\nFrooti\t\t\t{frootiEntry.get()}\t\t\t{frootiprice} Rs')
         if pepsiEntry.get()!='0':
              textarea.insert(END,f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice} Rs')
         if cokeEntry.get()!='0':
              textarea.insert(END,f'\nCoke\t\t\t{cokeEntry.get()}\t\t\t{cokeprice} Rs')
         if dewEntry.get()!='0':
              textarea.insert(END,f'\nDew\t\t\t{dewEntry.get()}\t\t\t{dewprice} Rs')
         if coldcoffeeEntry.get()!='0':
              textarea.insert(END,f'\nCold Coffee\t\t\t{coldcoffeeEntry.get()}\t\t\t{coldcoffeeprice} Rs')
         if spriteEntry.get()!='0':
              textarea.insert(END,f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice} Rs')
         textarea.insert(END,'\n-------------------------------------------------------')

         if cosmetictaxEntry.get()!='0':
              textarea.insert(END,f'\nCosmectic Tax\t\t\t\t{cosmetictaxEntry.get()}')
         if grocerytaxEntry.get()!='0':
              textarea.insert(END,f'\nGrocery Tax\t\t\t\t{grocerytaxEntry.get()}')
         if drinkstaxEntry.get()!='0':
              textarea.insert(END,f'\nDrinks Tax\t\t\t\t{drinkstaxEntry.get()}')
         textarea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')
         textarea.insert(END,'\n-------------------------------------------------------')
         save_bill()
def total():
    global bathsoapprice
    global facecreamprice
    global facewashprice
    global hairsprayprice
    global hairgelprice
    global bodylotionprice
    global riceprice
    global oilprice
    global sugarprice
    global wheatprice
    global teaprice
    global daalprice
    global frootiprice
    global pepsiprice
    global cokeprice
    global dewprice
    global coldcoffeeprice
    global spriteprice
    global totalbill

    #cosmeectic price calculation 
    bathsoapprice = int(bathsoapEntry.get())*20
    facecreamprice = int(facecreamEntry.get())*50
    facewashprice = int(facewashEntry.get())*100
    hairsprayprice = int(hairsprayEntry.get())*150
    hairgelprice = int(hairgelEntry.get())*80
    bodylotionprice = int(bodylotionEntry.get())*60

    totalcosmecticprice = bathsoapprice+facecreamprice+facewashprice+hairsprayprice+hairgelprice+bodylotionprice
    cosmeticpriceEntry.delete(0,END)
    cosmeticpriceEntry.insert(0,f'{totalcosmecticprice} Rs')
    cosmetictax = totalcosmecticprice*0.08
    cosmetictaxEntry.delete(0,END)
    cosmetictaxEntry.insert(0,f'{cosmetictax} Rs')

    #grocery price calculation 
    riceprice = int(riceEntry.get())*90
    oilprice = int(oilEntry.get())*145
    sugarprice = int(sugarEntry.get())*40
    wheatprice = int(wheatEntry.get())*80
    teaprice = int(teaEntry.get())*60
    daalprice = int(daalEntry.get())*100

    totalgroceryprice =  riceprice+oilprice+sugarprice+wheatprice+teaprice+daalprice 
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0,f'{totalgroceryprice} Rs')
    grocerytax = totalgroceryprice*0.10
    grocerytaxEntry.delete(0,END)
    grocerytaxEntry.insert(0,f'{grocerytax} Rs')

    #drinks price calculation
    frootiprice = int(frootiEntry.get())*35
    pepsiprice = int(pepsiEntry.get())*20
    cokeprice = int(cokeEntry.get())*20
    dewprice = int(dewEntry.get())*20
    coldcoffeeprice = int(coldcoffeeEntry.get())*50
    spriteprice = int(spriteEntry.get())*20

    totaldrinksprice = frootiprice+pepsiprice+cokeprice+dewprice+coldcoffeeprice+spriteprice
    drinkspriceEntry.delete(0,END)
    drinkspriceEntry.insert(0,f'{totaldrinksprice} Rs')
    drinkstax = totalgroceryprice*0.05
    drinkstaxEntry.delete(0,END)
    drinkstaxEntry.insert(0,f'{drinkstax} Rs')

    totalbill = totalcosmecticprice+totalgroceryprice+totaldrinksprice+cosmetictax+grocerytax+drinkstax

#GUI part
root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')

headingLabel = Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),
                          bg='indianred',fg='gold',bd=12,relief=GROOVE)
headingLabel.pack(fill=X)

customer_details_frame = LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),
                                    fg='gold',bd=8,relief=GROOVE,bg='indianred')
customer_details_frame.pack(fill=X)

nameLabel = Label(customer_details_frame,text='Name',font=('times new roman',15,'bold'),bg='indianred',fg='white')
nameLabel.grid(row=0,column=0,padx=20)

phoneLabel = Label(customer_details_frame,text='Phone Number',font=('times new roman',15,'bold'),bg='indianred',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)


nameEntry = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneEntry = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel = Label(customer_details_frame,text='Bill Number',font=('times new roman',15,'bold'),bg='indianred',fg='white')
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry = Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton = Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,
                      width=10,command=search_bill)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame = Frame(root)
productsFrame.pack()

cosmeticsFrame = LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),bg='indianred',fg='gold')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel = Label(cosmeticsFrame,text='Bath Soap',font=('times new roman',15,'bold'),bg='indianred',fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathsoapEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathsoapEntry.insert(0,0)

facecreamLabel = Label(cosmeticsFrame,text='Face Cream',font=('times new roman',15,'bold'),bg='indianred',fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

facecreamEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,padx=10,pady=9)
facecreamEntry.insert(0,0)

facewashLabel = Label(cosmeticsFrame,text='FaceWash',font=('times new roman',15,'bold'),bg='indianred',fg='white')
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

facewashEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facewashEntry.grid(row=2,column=1,padx=10,pady=9)
facewashEntry.insert(0,0)

hairsprayLabel = Label(cosmeticsFrame,text='Hair Spray',font=('times new roman',15,'bold'),bg='indianred',fg='white')
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairsprayEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,padx=10,pady=9)
hairsprayEntry.insert(0,0)

hairgelLabel = Label(cosmeticsFrame,text='Hair Gel',font=('times new roman',15,'bold'),bg='indianred',fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairgelEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,padx=10,pady=9)
hairgelEntry.insert(0,0)

bodylotionLabel = Label(cosmeticsFrame,text='Body Lotion',font=('times new roman',15,'bold'),bg='indianred',fg='white')
bodylotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodylotionEntry = Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bodylotionEntry.grid(row=5,column=1,padx=10,pady=9)
bodylotionEntry.insert(0,0)

groceryFrame = LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),bg='indianred',fg='gold')
groceryFrame.grid(row=0,column=1)

riceLabel = Label(groceryFrame,text='Rice',font=('times new roman',15,'bold'),bg='indianred',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
riceEntry.grid(row=0,column=1,padx=10,pady=9)
riceEntry.insert(0,0)

oilLabel = Label(groceryFrame,text='Oil',font=('times new roman',15,'bold'),bg='indianred',fg='white')
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oilEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
oilEntry.grid(row=1,column=1,padx=10,pady=9)
oilEntry.insert(0,0)

wheatLabel = Label(groceryFrame,text='Wheat',font=('times new roman',15,'bold'),bg='indianred',fg='white')
wheatLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

wheatEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
wheatEntry.grid(row=2,column=1,padx=10,pady=9)
wheatEntry.insert(0,0)

sugarLabel = Label(groceryFrame,text='Sugar',font=('times new roman',15,'bold'),bg='indianred',fg='white')
sugarLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

sugarEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
sugarEntry.grid(row=3,column=1,padx=10,pady=9)
sugarEntry.insert(0,0)

daalLabel = Label(groceryFrame,text='Daal',font=('times new roman',15,'bold'),bg='indianred',fg='white')
daalLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

daalEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
daalEntry.grid(row=4,column=1,padx=10,pady=9)
daalEntry.insert(0,0)

teaLabel = Label(groceryFrame,text='Tea',font=('times new roman',15,'bold'),bg='indianred',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry = Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
teaEntry.grid(row=5,column=1,padx=10,pady=9)
teaEntry.insert(0,0)

drinksFrame = LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),bg='indianred',fg='gold')
drinksFrame.grid(row=0,column=2)

frootiLabel = Label(drinksFrame,text='Frooti',font=('times new roman',15,'bold'),bg='indianred',fg='white')
frootiLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

frootiEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
frootiEntry.grid(row=0,column=1,padx=10,pady=9)
frootiEntry.insert(0,0)

pepsiLabel = Label(drinksFrame,text='Pepsi',font=('times new roman',15,'bold'),bg='indianred',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,padx=10,pady=9)
pepsiEntry.insert(0,0)

spriteLabel = Label(drinksFrame,text='Sprite',font=('times new roman',15,'bold'),bg='indianred',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
spriteEntry.grid(row=2,column=1,padx=10,pady=9)
spriteEntry.insert(0,0)

cokeLabel = Label(drinksFrame,text='Coke',font=('times new roman',15,'bold'),bg='indianred',fg='white')
cokeLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

cokeEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cokeEntry.grid(row=3,column=1,padx=10,pady=9)
cokeEntry.insert(0,0)

coldcoffeeLabel = Label(drinksFrame,text='Cold Coffee',font=('times new roman',15,'bold'),bg='indianred',fg='white')
coldcoffeeLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

coldcoffeeEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
coldcoffeeEntry.grid(row=4,column=1,padx=10,pady=9)
coldcoffeeEntry.insert(0,0)

dewLabel = Label(drinksFrame,text='Dew',font=('times new roman',15,'bold'),bg='indianred',fg='white')
dewLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

dewEntry = Entry(drinksFrame,font=('times new roman',15,'bold'),width=10,bd=5)
dewEntry.grid(row=5,column=1,padx=10,pady=9)
dewEntry.insert(0,0)

billframe = Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel = Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE,)
billareaLabel.pack(fill=X)

Scrollbar = Scrollbar(billframe,orient=VERTICAL)
Scrollbar.pack(side=RIGHT,fill=Y)
textarea = Text(billframe,height=18,width=55,yscrollcommand=Scrollbar.set)
textarea.pack()
Scrollbar.config(command=textarea.yview)

billmenuFrame = LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),bg='indianred',fg='gold',
                           relief=GROOVE,bd=8)
billmenuFrame.pack()

cosmeticpriceLabel = Label(billmenuFrame,text='Cosmetic Price',font=('times new roman',14,'bold'),bg='indianred',fg='white')
cosmeticpriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

cosmeticpriceEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmeticpriceEntry.grid(row=0,column=1,padx=10,pady=6)

grocerypriceLabel = Label(billmenuFrame,text='Grocery Price',font=('times new roman',14,'bold'),bg='indianred',fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

grocerypriceEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,padx=10,pady=6)

drinkspriceLabel = Label(billmenuFrame,text='Drinks Price',font=('times new roman',14,'bold'),bg='indianred',fg='white')
drinkspriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

drinkspriceEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkspriceEntry.grid(row=2,column=1,padx=10,pady=6)

cosmetictaxLabel = Label(billmenuFrame,text='Cosmetic Tax',font=('times new roman',14,'bold'),bg='indianred',fg='white')
cosmetictaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmetictaxEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
cosmetictaxEntry.grid(row=0,column=3,padx=10,pady=6)

grocerytaxLabel = Label(billmenuFrame,text='Grocery Tax',font=('times new roman',14,'bold'),bg='indianred',fg='white')
grocerytaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

grocerytaxEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
grocerytaxEntry.grid(row=1,column=3,padx=10,pady=6)

drinkstaxLabel = Label(billmenuFrame,text='Drinks Tax',font=('times new roman',14,'bold'),bg='indianred',fg='white')
drinkstaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

drinkstaxEntry = Entry(billmenuFrame,font=('times new roman',14,'bold'),width=10,bd=5)
drinkstaxEntry.grid(row=2,column=3,padx=10,pady=6)

buttonFrame = Frame(billmenuFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3)

totalbutton = Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='indianred',fg='white',
                     bd=5,width=8,padx=10,pady=6,command=total)
totalbutton.grid(row=0,column=0,pady=19,padx=4)

billbutton = Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='indianred',fg='white',
                    bd=5,width=8,padx=10,pady=6,command=bill_area)
billbutton.grid(row=0,column=1,padx=4,pady=19)

emailbutton = Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='indianred',fg='white',
                     
bd=5,width=8,padx=10,pady=6,command=send_email)
emailbutton.grid(row=0,column=2,pady=19,padx=4)

printbutton = Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='indianred',fg='white',
                     bd=5,width=8,padx=10,pady=6,command=print_bill)
printbutton.grid(row=0,column=3,pady=19,padx=4)

clearbutton = Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='indianred',fg='white',
                     bd=5,width=8,padx=10,pady=6,command=clear)
clearbutton.grid(row=0,column=4,pady=19,padx=4)


root.mainloop()