from tkinter import Tk, Label, Button, Entry, messagebox, END
from db_manager import arrow
from cart_manager import Enter_item, Enter_grocery, Totalcost, bill 

def create_item_window(title, bg_color, table_name, select_sql):
    """Helper function to create item selection windows (Kitchenware/Sanitation)"""
    window = Tk()
    window.title(title)

    window.geometry("1160x680" if title == "Kitchenware" else "1150x670") 

    def close():
        window.destroy()

    def Enter_item_wrapper():
        global rows 
        Enter_item(EF1, EF2, rows)

    C1 = Label(window, text=title, bg=bg_color, fg="White", font=("Gill Sans Ultra Bold Condensed", 40))
    C1.grid(row=0, column=0, padx=0.000000001) 
    LT = Label(window, text="En", font=("Forte", 25))
    LT.grid(row=0, column=5)

    cursorObj = arrow.cursor()
    cursorObj.execute(select_sql)
    rows = cursorObj.fetchall()
    n = len(rows)

    LIC = Label(window, text="ICode", font=('Arial Black', 23))
    LIC.grid(row=1, column=0)
    LIN = Label(window, text="IName", font=('Arial Black', 23))
    LIN.grid(row=1, column=1)
    LIP = Label(window, text="Price", font=('Arial Black', 23))
    LIP.grid(row=1, column=2)

    for x in range(n):
        Label(window, text=x+1, font=('Constantia', 20)).grid(row=x+2, column=0)
        Label(window, text=rows[x][1], font=('Constantia', 20)).grid(row=x+2, column=1)
        Label(window, text=rows[x][3], font=('Constantia', 20)).grid(row=x+2, column=2)

    LEF1 = Label(window, text='Enter ICode:', font=('AR JULIAN', 20))
    LEF1.grid(row=2, column=4)
    EF1 = Entry(window, font=('Constantia', 20))
    EF1.grid(row=3, column=4)

    LEF2 = Label(window, text='Enter Quantity:', font=('AR JULIAN', 20))
    LEF2.grid(row=5, column=4)
    EF2 = Entry(window, font=('Constantia', 20))
    EF2.grid(row=6, column=4)

    BEnter = Button(window, text="ENTER", font=("Ar Destine", 25), bg="Black", fg="White", command=Enter_item_wrapper)
    BEnter.grid(row=8, column=4)
    
    Bdone = Button(window, text="DONE", font=("Ar Destine", 25), bg="Black", fg="White", command=close)
    Bdone.grid(row=n + 3, column=5)

    window.mainloop()

def Kitchenware():
    create_item_window("Kitchenware", "Brown", "Kitchenware", "SELECT * FROM Kitchenware;")

def Sanitation():
    create_item_window("Sanitation", "Pink", "Sanitation", "SELECT * FROM Sanitation;")

def create_grocery_subsection(item_type, window_title, bg_color):
    """Helper function for Fruits, Vegetables, and Dairy."""
    window = Tk()
    window.title(window_title)

    Label(window, text=' ').grid(row=0, column=1)
    Label(window, text=' ').grid(row=0, column=2)

    def close():
        window.destroy()

    def Enter_grocery_wrapper():
        global rows
        Enter_grocery(EF1, EF2, rows)

    F1 = Label(window, text=window_title, bg=bg_color, fg="White", font=("Gill Sans Ultra Bold Condensed", 40))
    F1.grid(row=0, column=0)
    LT = Label(window, text="En", font=("Forte", 25))
    LT.grid(row=0, column=5)

    cursorObj = arrow.cursor()
    cursorObj.execute(f"SELECT * FROM Grocery WHERE IType='{item_type}';")
    rows = cursorObj.fetchall()
    n = len(rows)

    LIC = Label(window, text="ICode", font=('Arial Black', 23))
    LIC.grid(row=1, column=0)
    LIN = Label(window, text="IName", font=('Arial Black', 23))
    LIN.grid(row=1, column=1)
    LIP = Label(window, text="Price", font=('Arial Black', 23))
    LIP.grid(row=1, column=2)

    for x in range(n):
        Label(window, text=x+1, font=('Constantia', 20)).grid(row=x+2, column=0)
        Label(window, text=rows[x][2], font=('Constantia', 20)).grid(row=x+2, column=1)
        Label(window, text=rows[x][3], font=('Constantia', 20)).grid(row=x+2, column=2)

    LEF1 = Label(window, text='Enter ICode:', font=('AR JULIAN', 20))
    LEF1.grid(row=2, column=4)
    EF1 = Entry(window, font=('Constantia', 20))
    EF1.grid(row=3, column=4)

    LEF2 = Label(window, text='Enter Quantity:', font=('AR JULIAN', 20))
    LEF2.grid(row=5, column=4)
    EF2 = Entry(window, font=('Constantia', 20))
    EF2.grid(row=6, column=4)
    
    BEnter = Button(window, text="ENTER", font=("Ar Destine", 25), bg="Black", fg="White", command=Enter_grocery_wrapper)
    BEnter.grid(row=8, column=4)

    Bdone = Button(window, text="DONE", font=("Ar Destine", 25), bg="Black", fg="White", command=close)
    Bdone.grid(row=n + 3, column=5)

    window.mainloop()

def Fruits():
    create_grocery_subsection("Fruit", "Fruits", "Orange")

def Vegetables():
    create_grocery_subsection("Vegetable", "Vegetables", "Light Green")

def Dairy():
    create_grocery_subsection("Dairy", "Dairy", "Light Blue")

def create_clothing_subsection(item_type, window_title, bg_color, query):
    """Helper function for TShirts and Jeans"""
    window = Tk()
    window.title(window_title)

    def close():
        window.destroy()

    def Enter_clothing_wrapper():
        global rows

        Enter_shirts(ED1, ED2, rows)

    Sh1 = Label(window, text=window_title, bg=bg_color, fg="White", font=("Gill Sans Ultra Bold Condensed", 40))
    Sh1.grid(row=0, column=0)
    LT = Label(window, text="En", font=("Forte", 25))
    LT.grid(row=0, column=5)

    cursorObj = arrow.cursor()
    cursorObj.execute(query)
    rows = cursorObj.fetchall()
    n = len(rows)

    L32 = Label(window, text="ICode", font=('Arial Black', 23))
    L32.grid(row=1, column=0)
    L33 = Label(window, text="IName", font=('Arial Black', 23))
    L33.grid(row=1, column=1)
    L34 = Label(window, text="Price", font=('Arial Black', 23))
    L34.grid(row=1, column=2)

    for x in range(n):
        Label(window, text=x+1, font=('Constantia', 18)).grid(row=x+2, column=0)
        Label(window, text=rows[x][1], font=('Constantia', 18)).grid(row=x+2, column=1)
        Label(window, text=rows[x][3], font=('Constantia', 18)).grid(row=x+2, column=2)

    LED1 = Label(window, text='Enter ICode:', font=('AR JULIAN', 20))
    LED1.grid(row=2, column=4)
    ED1 = Entry(window, font=('Constantia', 20))
    ED1.grid(row=3, column=4)

    LED2 = Label(window, text='Enter Quantity:', font=('AR JULIAN', 20))
    LED2.grid(row=5, column=4)
    ED2 = Entry(window, font=('Constantia', 20))
    ED2.grid(row=6, column=4)

    BEnter = Button(window, text="ENTER", font=("Ar Destine", 25), bg="Black", fg="White", command=Enter_clothing_wrapper)
    BEnter.grid(row=8, column=4)

    Bdone = Button(window, text="DONE", font=("Ar Destine", 25), bg="Black", fg="White", command=close)
    Bdone.grid(row=n + 3, column=5)

    window.mainloop()

def TShirts():
    create_clothing_subsection("TShirts", "TShirts", "Orange", "SELECT * FROM Clothing WHERE IType='TShirts';")

def Jeans():
    create_clothing_subsection("Jeans", "Jeans", "Grey", "SELECT * FROM Clothing WHERE IType='Jeans';")
