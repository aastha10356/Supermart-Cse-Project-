from tkinter import Tk, Label, Button, StringVar
from gui_windows import Mall, Sz

if __name__ == '__main__':
    supermart = Tk()
    supermart.title("En Mart")
    supermart.geometry("1100x650")
    
    if Sz is None:
        Sz = StringVar(supermart)
        Sz.set("40") 

    L1 = Label(supermart, text="WELCOME TO", font=("Forte", 25), bg="Red", fg="White")
    L1.place(x=450, y=10)
    L2 = Label(supermart, text="En Mart", font=("Forte", 120))
    L2.place(x=250, y=100)
    L3 = Label(supermart, text="ESTD.1969", font=("Forte", 25))
    L3.place(x=650, y=246)
    L4 = Label(supermart, text="Things You Need.", font=("Gill Sans Ultra Bold Condensed", 30))
    L4.place(x=400, y=300)
    L5 = Label(supermart, text="Nutrition. Cover.Hygiene.", font=("Gill Sans Ultra Bold Condensed", 30))
    L5.place(x=335, y=350)

    B1 = Button(supermart, text="ENTER", font=("Ar Destine", 30), bg="Red", fg="White", command=Mall)
    B1.place(x=480, y=500)

    Tg = Label(supermart, text="©En Mart.All Rights Reserved.", font=("Forte", 15))
    Tg.place(x=800, y=600)

    supermart.mainloop()
