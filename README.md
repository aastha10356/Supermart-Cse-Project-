# Project Overview
This project is a simple application that uses python, sqlite3 module for database management and tkinter library for creating user interface for an online supermarket billing system in which a user can browse through multiple products and add it to their cart and once finished can checkout. While checking out, the user can see the bill, choose mode of payment and delivery method.
# Features
The project provides the following features:
* Multiple products browsing: user can navigate through multiple categories of products divided into 4 broad categories of: grocery (futher broken into fruits,vegetables,dairy) ,kitchenware,sanitation and clothing (further broken down by T-Shirts, Jeans, and Size-Specific Shirts)
* Cart Management: user can add multiple items while browsing with their quantities and simultaneously the items will get added to the final bill.
* Checkout: once the user is done with shopping, they can checkout and an online bill will be generated and they can also avail options of mode of payment and delivery method.
* Error-handling: user cannot enter invalid inputs
# Technologies and Tools Used
* Language used: python 3.x
* User interface: tkinter
* Database: sqlite3
* Version control: Git/GitHub
# Steps to Install & Run the Project
1. Python 3.x must be installed in your device.
2. Clone the Repository: Use Git to download all project files into a folder on your computer.
3. Execute the code: Open your system's command-line application, navigate to the project folder, and run the primary application script:
python main_app.py
4. Using the GUI: The main "En Mart" welcome window will appear. Click the "ENTER" button. Scroll through the categories and add items to the cart. Click the "FINISH" button to view the final Cart and billing summary.
# Instructions for Testing
## Test case 1: Browse & Add Item (Grocery)
Steps: 
1. Click ENTER. 
2. Click Grocery -> Fruits. 
3. Enter a valid ICode (e.g., 1 or f001) and a Quantity (2). 
4. Click ENTER.


Expected result: An informational pop-up confirms the addition. The item is tracked in the cart

## Test case 2: Input Validation (Quantity)
Steps:
1. Navigate to any category(e.g., Kitchenware). 
2. Enter a valid ICode but leave the Quantity field blank. 
3. Click ENTER.


Expected result: An error message should appear showing “Please Enter Quantity of Item Required.”

## Test case 3: Input Validation (ICode)
Steps: 
1. Navigate to any category. 
2. Enter a non-numeric value (e.g., abc) for ICode. 
3. Click ENTER.


Expected result: An error message should appear showing “Please enter valid numbers for ICode and Quantity”

## Test case 4: Generate Final Bill
Steps: 
1. Add desired products. 
2. Click FINISH from the Aisle window.


Expected result: The final Cart window should display all added iitems, quantities, and a calculated, rounded Totalcost
