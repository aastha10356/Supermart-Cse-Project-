from tkinter import Tk, Label, Button, Entry, messagebox, OptionMenu, StringVar, END
from gui_helpers import Kitchenware, Sanitation, Fruits, Vegetables, Dairy, TShirts, Jeans
from cart_manager import Totalcost, bill, Enter_shirts
from db_manager import arrow
import math

Sz = None

def Done(window):
    """Generic function to destroy a sub-window (used by Grocery, Fruits, etc.)"""
    window.destroy()

def Mall():
    """Opens the Aisle window after pressing ENTER on the initial screen."""
    global Hall
    Hall = Tk()
    Hall.title("Aisle")
    Hall.geometry("1100x650")

    LT = Label(Hall, text="En", font=("Forte", 25))
    LT.place(x=1000, y=20)
    L11 = Label(Hall, text="AISLE", font=("Gill Sans Ultra Bold Condensed", 40), bg="Orange", fg="White")
    L11.place(x=480, y=20)

    B11 = Button(Hall, text="Grocery", font=("Ar Cena", 40), bg="Green", fg="Black", command=Grocery)
    B11.place(x=15, y=300)
    B12 = Button(Hall, text="Kitchenware", font=("Ar Cena", 40), bg="Brown", fg="Black", command=Kitchenware)
    B12.place(x=270, y=300)
    B13 = Button(Hall, text="Sanitation", font=("Ar Cena", 40), bg="Pink", fg="Black", command=Sanitation)
    B13.place(x=610, y=300)
    B14 = Button(Hall, text="Clothing", font=("Ar Cena", 40), bg="Red", fg="Black", command=Clothing)
    B14.place(x=900, y=300)

    BFinish = Button(Hall, text="FINISH", font=("Ar Destine", 25), bg="Black", fg="White", command=Finish)
    BFinish.place(x=970, y=570)
    Hall.mainloop()

def Finish():
    """Opens the Billing/Cart window and displays the total cost."""
    global Billing
    Hall.destroy()
    Billing = Tk()
    Billing.title("Cart")
    Billing.geometry("1100x650")

    BT = Label(Billing, text="Your Cart", font=("Gill Sans Ultra Bold Condensed", 40), bg="Red", fg="White")
    BT.grid(row=0, column=0)
    
    SB1 = Label(Billing, text=' ')
    SB1.grid(row=0, column=1)
    SB2 = Label(Billing, text=' ')
    SB2.grid(row=0, column=4)

    i = 0
    for a in bill:
        lst = bill[a]
        lt1 = Label(Billing, text=a, font=('Constantia', 18))
        lt1.grid(row=i+2, column=0)
        lt2 = Label(Billing, text=lst[0], font=('Constantia', 18))
        lt2.grid(row=i+2, column=1)
        lt3 = Label(Billing, text=lst[1], font=('Constantia', 18))
        lt3.grid(row=i+2, column=2)
        i += 1

    LN = Label(Billing, text="Item", font=('Arial Black', 23))
    LN.grid(row=1, column=0)
    LQ = Label(Billing, text="Quantity", font=('Arial Black', 23))
    LQ.grid(row=1, column=1)
    LP = Label(Billing, text="Cost", font=('Arial Black', 23))
    LP.grid(row=1, column=2)

    global Totalcost
    LTC1 = Label(Billing, text='The total cost is:', font=('Forte', 20))
    LTC1.grid(row=2, column=4)

    LTC2 = Label(Billing, text=math.floor(Totalcost), font=('Forte', 20))
    LTC2.grid(row=2, column=5)
    
    LT = Label(Billing, text="En", font=("Forte", 25))
    LT.grid(row=0, column=5)

    var1 = StringVar(Billing)
    var1.set("Cash")
    P1 = OptionMenu(Billing, var1, "Cash", "Credit Card")
    P1.grid(row=5, column=5)
    PT1 = Label(Billing, text="Mode Of Payment", font=('Forte', 20))
    PT1.grid(row=5, column=4)

    var2 = StringVar(Billing)
    var2.set("Home Delivery")
    P2 = OptionMenu(Billing, var2, "Home Delivery", "Take Away")
    P2.grid(row=6, column=5)
    PT2 = Label(Billing, text="Delivery of Goods", font=('Forte', 20))
    PT2.grid(row=6, column=4)

    BPay = Button(Billing, text="Pay", font=("Ar Destine", 25), bg="Black", fg="White", command=End)
    BPay.grid(row=13, column=5)
    
    Billing.mainloop()

def End():
    """Shows the final message after payment and destroys the Billing window."""
    if Totalcost == 0:
        messagebox.showinfo("Windowshopping?", "Do come back again.")
    else:
        messagebox.showinfo("Done", "Your goods are ready.\n Thank you for choosing us!!!")
    Billing.destroy()

def Grocery():
    """Opens the Grocery Aisle window."""
    global Grocery_win
    Grocery_win = Tk()
    Grocery_win.title("Grocery")
    Grocery_win.geometry("1100x650")

    def close():
        Grocery_win.destroy()

    G1 = Label(Grocery_win, text="Grocery", bg="Green", fg="White", font=("Gill Sans Ultra Bold Condensed", 40))
    G1.place(x=440, y=10)
    
    B21 = Button(Grocery_win, text="Fruits", font=("Ar Cena", 40), bg="Orange", fg="Black", command=Fruits)
    B21.place(x=50, y=300)
    B22 = Button(Grocery_win, text="Vegetables", font=("Ar Cena", 40), bg="Light Green", fg="Black", command=Vegetables)
    B22.place(x=410, y=300)
    B23 = Button(Grocery_win, text="Dairy", font=("Ar Cena", 40), bg="Light Blue", fg="Black", command=Dairy)
    B23.place(x=815, y=300)
    
    Bdone = Button(Grocery_win, text="DONE", font=("Ar Destine", 25), bg="Black", fg="White", command=close)
    Bdone.place(x=970, y=570)
    LT = Label(Grocery_win, text="En", font=("Forte", 25))
    LT.place(x=1000, y=20)
    Grocery_win.mainloop()

def Clothing():
    """Opens the Clothing Aisle window."""
    global Clothing_win, Sz
    Clothing_win = Tk()
    Clothing_win.title("Clothing")
    Clothing_win.geometry("1100x650")
    
    def close():
        Clothing_win.destroy()

    Cl1 = Label(Clothing_win, text="Clothing", bg="Red", fg="White", font=("Gill Sans Ultra Bold Condensed", 40))
    Cl1.place(x=450, y=20)
    
    C21 = Button(Clothing_win, text="Shirts", font=("Ar Cena", 40), bg="Cyan", fg="Black", command=Shirts)
    C21.place(x=50, y=300)
    C22 = Button(Clothing_win, text="T Shirts", font=("Ar Cena", 40), bg="Orange", fg="Black", command=TShirts)
    C22.place(x=410, y=300)
    C23 = Button(Clothing_win, text="Jeans", font=("Ar Cena", 40), bg="Grey", fg="Black", command=Jeans)
    C23.place(x=815, y=300)
    
    Sz1 = OptionMenu(Clothing_win, Sz, "40", "42")
    Sz1.place(x=210, y=510)
    Sz2 = Label(Clothing_win, text="Select Size:", font=('Ar Cena', 25))
    Sz2.place(x=50, y=500)

    Bdone = Button(Clothing_win, text="DONE", font=("Ar Destine", 25), bg="Black", fg="White", command=close)
    Bdone.place(x=970, y=570)
    LT = Label(Clothing_win, text="En", font=("Forte", 25))
    LT.place(x=1000, y=20)
    Clothing_win.mainloop()

def Shirts():
    """Opens the Shirts window, querying items based on the globally selected size (Sz)."""
    global rows
    Shirts_win = Tk()
    Shirts_win.title("Shirts")
    Shirts_win.geometry("1100x650")

    def close():
        Shirts_win.destroy()
    
    def Enter_shirts_wrapper():
        global rows
        Enter_shirts(ED1, ED2, rows)

    Sh1 = Label(Shirts_win, text="Shirts", bg="Cyan", fg="White", font=("Gill Sans Ultra Bold Condensed", 40))
    Sh1.grid(row=0, column=0)
    LT = Label(Shirts_win, text="En", font=("Forte", 25))
    LT.grid(row=0, column=5)

    current_size = Sz.get()
    cursorObj = arrow.cursor()
    cursorObj.execute(f"SELECT * FROM Clothing WHERE IType='Shirts' AND IName LIKE '%Size{current_size}';")
    rows = cursorObj.fetchall()
    n = len(rows)

    L32 = Label(Shirts_win, text="ICode", font=('Arial Black', 23))
    L32.grid(row=1, column=0)
    L33 = Label(Shirts_win, text="IName", font=('Arial Black', 23))
    L33.grid(row=1, column=1)
    L34 = Label(Shirts_win, text="Price", font=('Arial Black', 23))
    L34.grid(row=1, column=2)

    for x in range(n):
        Label(Shirts_win, text=x+1, font=('Constantia', 16)).grid(row=x+2, column=0)
        Label(Shirts_win, text=rows[x][1], font=('Constantia', 16)).grid(row=x+2, column=1)
        Label(Shirts_win, text=rows[x][3], font=('Constantia', 16)).grid(row=x+2, column=2)

    LED1 = Label(Shirts_win, text='Enter ICode:', font=('AR JULIAN', 20))
    LED1.grid(row=2, column=4)
    ED1 = Entry(Shirts_win, font=('Constantia', 20))
    ED1.grid(row=3, column=4)

    LED2 = Label(Shirts_win, text='Enter Quantity:', font=('AR JULIAN', 20))
    LED2.grid(row=5, column=4)
    ED2 = Entry(Shirts_win, font=('Constantia', 20))
    ED2.grid(row=6, column=4)

    BEnter = Button(Shirts_win, text="ENTER", font=("Ar Destine", 25), bg="Black", fg="White", command=Enter_shirts_wrapper)
    BEnter.grid(row=8, column=4)

    Bdone = Button(Shirts_win, text="DONE", font=("Ar Destine", 25), bg="Black", fg="White", command=close)
    Bdone.grid(row=n + 3, column=5)

    Shirts_win.mainloop()
