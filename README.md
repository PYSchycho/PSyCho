# PSyCho
from tkinter import *
from tkinter import messagebox
import random, os, tempfile, smtplib

# Functionality part

### Clear Function

```python
def clear():
    # Clear all entry fields
    bathsoapEntry.delete(0, END)
    facecreamEntry.delete(0, END)
    facewashEntry.delete(0, END)
    hairgelEntry.delete(0, END)
    hairsprayEntry.insert(0, 0)
    bodylotionEntry.delete(0, END)
    riceEntry.delete(0, END)
    sugarEntry.delete(0, END)
    oilEntry.delete(0, END)
    daalEntry.delete(0, END)
    teaEntry.delete(0, END)
    wheatEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    cokeEntry.delete(0, END)
    coldcoffeeEntry.delete(0, END)
    dewEntry.delete(0, END)
    frootiEntry.delete(0, END)
    spriteEntry.delete(0, END)

    # Insert default values
    bathsoapEntry.insert(0, 0)
    facecreamEntry.insert(0, 0)
    facewashEntry.insert(0, 0)
    hairgelEntry.insert(0, 0)
    hairsprayEntry.insert(0, 0)
    bodylotionEntry.insert(0, 0)
    riceEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    daalEntry.insert(0, 0)
    teaEntry.insert(0, 0)
    wheatEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)
    cokeEntry.insert(0, 0)
    coldcoffeeEntry.insert(0, 0)
    dewEntry.insert(0, 0)
    frootiEntry.insert(0, 0)
    spriteEntry.insert(0, 0)

    # Clear tax and price fields
    cosmetictaxEntry.delete(0, END)
    grocerytaxEntry.delete(0, END)
    drinkstaxEntry.delete(0, END)
    cosmeticpriceEntry.delete(0, END)
    grocerypriceEntry.delete(0, END)
    drinkspriceEntry.delete(0, END)

    # Clear customer details
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    billnumberEntry.delete(0, END)

    # Clear textarea
    textarea.delete(1.0, END)
def send_email():
    def send_gmail():
        try:
            ob = smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(senderEntry.get(), passwordEntry.get())
            message = email_textarea.get(1.0, END)
            reciever_address = recieverEntry.get()
            ob.sendmail(senderEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is successfully sent.', parent=root1)
        except:
            messagebox.showerror('Error', 'Something went wrong, Please try again.', parent=root1)
            root1.destroy()

    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty.')
    else:
        root1 = Toplevel()
        root1.grab_set()
        root1.title('Send Gmail')
        root1.config(bg='indianred')
        root1.resizable(height=False, width=False)

        # ... rest of the function ...

def print_bill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is empty.')
    else:
        file = tempfile.mkdtemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')

def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete('1.0', END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            break
        else:
            messagebox.showerror('Error', 'Invalid Bill Number')

def save_bill():
    global billnumber
    result = messagebox.askyesno('
