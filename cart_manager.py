from tkinter import messagebox, END
from db_manager import arrow
import math

Totalcost = 0
bill = {}

def Enter_item(EF1, EF2, rows):
    """Logic to add an item from Kitchenware/Sanitation to the bill."""
    global Totalcost
    try:
        Qty = EF2.get()
        if Qty == "":
            messagebox.showinfo("Quantity", "Please Enter Quantity of Item Required.")
            return
        
        Nm = int(EF1.get())
        if Nm < 1 or Nm > len(rows):
            messagebox.showerror("Error", "Invalid ICode.")
            return

        Item = rows[Nm-1][1]
        Price = rows[Nm-1][3]
        cost = Price * int(Qty)
        Totalcost += cost
        bill[Item] = [Qty, cost]
        EF1.delete(0, END)
        EF2.delete(0, END)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for ICode and Quantity.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def Enter_grocery(EF1, EF2, rows):
    """Logic to add an item from Grocery subsections to the bill."""
    global Totalcost
    try:
        Qty = EF2.get()
        if Qty == "":
            messagebox.showinfo("Quantity", "Please Enter Quantity of Item Required.")
            return
        
        Nm = int(EF1.get())
        if Nm < 1 or Nm > len(rows):
            messagebox.showerror("Error", "Invalid ICode.")
            return

        Item = rows[Nm-1][2] 
        Price = rows[Nm-1][3]
        cost = Price * int(Qty)
        Totalcost += cost
        bill[Item] = [Qty, cost]
        EF1.delete(0, END)
        EF2.delete(0, END)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for ICode and Quantity.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def Enter_shirts(ED1, ED2, rows):
    """Logic to add an item from Shirts (clothing) to the bill."""
    global Totalcost
    try:
        Qty = ED2.get()
        if Qty == "":
            messagebox.showinfo("Quantity", "Please Enter Quantity of Item Required.")
            return
        
        Nm = int(ED1.get())
        if Nm < 1 or Nm > len(rows):
            messagebox.showerror("Error", "Invalid ICode.")
            return

        Item = rows[Nm-1][1] 
        Price = rows[Nm-1][3]
        cost = Price * int(Qty)
        Totalcost += cost
        bill[Item] = [Qty, cost]
        ED1.delete(0, END)
        ED2.delete(0, END)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for ICode and Quantity.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
