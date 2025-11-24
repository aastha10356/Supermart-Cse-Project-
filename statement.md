# Problem Statement
The traditional method of buying items on a regular basis in a grocery store is tedious and time consuming and gives an overall an inconsistent customer experience and may even cause delays at checkouts or error in billing. This project aims to remove all these difficulties by creating a software that modernizes and automates this process of adding items to the cart and checking out without any inconvenience being caused to the user.
# Scope of the Project
The scope defines clear boundaries of what this project can do:
* GUI is made using tkinter for an overall better user experience.
* Use of SQLite for database management for products.
* Products have been broadly divided into different categories (groceries, clothing, sanitation and kitchenware) and sub sections (within groceries and kitchenware).
* Use of modules to define functions like cart management and billing.
* Makes sure valid input is to be submitted and is well trained for error handling (checking non numeric values)
# Target Users
* Cashier/retail staff: users who will use the system for efficient billing and checkout.
* Developers: users who will interact with the code for testing the functionality for evaluation or their personal projects.
# High-Level Features
The project provides the following features to fulfill its goal:
* Aisle-Based Navigation: Provides a clear, organized menu system to browse products by category (Grocery, Kitchenware, Sanitation, Clothing).
* Dynamic Item Selection: Retrieves and displays product lists dynamically from the SQLite database based on the selected category or sub-category (e.g., only "Size 42" shirts are shown if that size is selected).
* Transaction: Accurately calculates the final amount to be paid by the customer based on the quantity and items added.
* Billing and checkout: generates a structured summary of customer’s order, quantity and total bill calculated.

