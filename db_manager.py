import sqlite3

arrow = sqlite3.connect(":memory:")
cursorObj = arrow.cursor()

cursorObj.execute('''CREATE TABLE IF NOT EXISTS Grocery
(ICode varchar(10), IType char(20), IName char(30), Price float(8,2));''')
cursorObj.execute('''CREATE TABLE IF NOT EXISTS Kitchenware
(ICode varchar(10), IName char(30), IType char(20), Price float(8,2));''')
cursorObj.execute('''CREATE TABLE IF NOT EXISTS Sanitation
(ICode varchar(10), IName char(30), IType char(20), Price float(8,2));''')
cursorObj.execute('''CREATE TABLE IF NOT EXISTS Clothing
(ICode varchar(10), IName char(30), IType char(20), Price float(8,2));''')

grocery_data = [
    ('f001', 'Fruit', 'Mango(500g)', 200.00), ('f002', 'Fruit', 'Apple(500g)', 60.00), ('f003', 'Fruit', 'Banana(500g)', 25.00),
    ('f004', 'Fruit', 'Orange(500g)', 70.00), ('f005', 'Fruit', 'Watermelon (1Kg)', 50.00), ('f006', 'Fruit', 'Strawberry(500g)', 50.00),
    ('f007', 'Fruit', 'Guava(500g)', 40.00), ('f008', 'Fruit', 'Litchi(500g)', 80.00), ('f009', 'Fruit', 'Apricot(500g)', 100.00),
    ('f010', 'Fruit', 'Grapes(500g)', 30.00), ('f011', 'Fruit', 'Custard Apple(500g)', 50.00), ('f012', 'Fruit', 'Pineapple(500g)', 40.00),
    ('v001', 'Vegetable', 'Spinach(1Bunch)', 30.00), ('v002', 'Vegetable', 'Cucumber(500g)', 20.00), ('v003', 'Vegetable', 'Tomato(500g)', 20.00),
    ('v004', 'Vegetable', 'Kidney Beans (500g)', 30.00), ('v005', 'Vegetable', 'Lady Finger(500g)', 20.00), ('v006', 'Vegetable', 'Potato(500g)', 15.00),
    ('v007', 'Vegetable', 'Onion(500g)', 30.00), ('v008', 'Vegetable', 'Drumsticks(500g)', 30.00), ('v009', 'Vegetable', 'Pumpkin (500g)', 20.00),
    ('v010', 'Vegetable', 'Cauliflower(500g)', 40.00), ('v011', 'Vegetable', 'Cabbage(500g)', 30.00),
    ('d001', 'Dairy', 'Mozerella Cheese(250g)', 110.00), ('d002', 'Dairy', 'Amul Cheese Cubes(10pcs)', 150.00), ('d003', 'Dairy', 'Amul Cheese Slices(10)', 170.00),
    ('d004', 'Dairy', 'Cheddar Cheese(500g)', 250.00), ('d005', 'Dairy', 'Gokul Cow Milk(500mL)', 25.00), ('d006', 'Dairy', 'Amul Chaas(500mL)', 25.00),
    ('d007', 'Dairy', 'Amul Butter(100g)', 56.00), ('d008', 'Dairy', 'Amul Garlic Butter(100g)', 66.00), ('d009', 'Dairy', 'En Mart Mango Lassi (250mL)', 99.00),
    ('d010', 'Dairy', 'Amul Curd(500g)', 30.00), ('d011', 'Dairy', 'Gowardhan Cow Ghee (250g)', 125.00)
]
cursorObj.executemany("INSERT INTO Grocery VALUES(?, ?, ?, ?)", grocery_data)

kitchenware_data = [
    ('k001', 'Cups And Saucers (2 sets)', 'Kitchenware', 350.00), ('k002', '"Office Dude" Coffee Mug', 'Kitchenware', 650.00),
    ('k003', 'Dinner Dishes En Mart', 'Kitchenware', 450.00), ('k004', 'Ceramic Plates Ceraware', 'Kitchenware', 850.00),
    ('k005', 'Spoons Steelware (4 Dozen)', 'Kitchenware', 100.00), ('k006', 'Forks Steelware (4 Dozen)', 'Kitchenware', 100.00),
    ('k007', 'Tea Cup Cuppa(1 psc)', 'Kitchenware', 120.00), ('k008', 'Sprinkler', 'Kitchenware', 70.00),
    ('k009', 'Squeeze Bottle Utilize', 'Kitchenware', 99.00), ('k010', 'Serving Spatula Steel (5psc)', 'Kitchenware', 79.00),
    ('k011', 'Dish Holder Wooden', 'Kitchenware', 140.00)
]
cursorObj.executemany("INSERT INTO Kitchenware VALUES(?, ?, ?, ?)", kitchenware_data)

sanitation_data = [
    ('s001', 'Napkins Home Clean', 'Sanitation', 120.00), ('s002', 'Hand Towels En Mart Homies', 'Sanitation', 119.00),
    ('s003', 'Towels (1pair)', 'Sanitation', 130.00), ('s004', 'Bath Soap', 'Sanitation', 60.00),
    ('s005', 'Toothpaste', 'Sanitation', 40.00), ('s006', 'Toothbrush', 'Sanitation', 125.00),
    ('s007', 'Shampoo Homies', 'Sanitation', 180.00), ('s008', 'Floor Mop', 'Sanitation', 200.00),
    ('s009', 'Detergent 50g', 'Sanitation', 110.00), ('s010', 'Face Wash', 'Sanitation', 150.00),
    ('s011', 'Shampoo Homies', 'Sanitation', 180.00)
]
cursorObj.executemany("INSERT INTO Sanitation VALUES(?, ?, ?, ?)", sanitation_data)

clothing_data = [
    ('sh001', 'Raymond Formal Shirts Size40', 'Shirts', 1000.00), ('sh002', 'Raymond Formal Shirts Size42', 'Shirts', 1100.00),
    ('sh003', 'Peter England Formal Shirts Size40', 'Shirts', 1300.00), ('sh004', 'Peter England Formal Shirts Size42', 'Shirts', 1400.00),
    ('sh005', 'Van Hausen Formal Shirts Size40', 'Shirts', 1100.00), ('sh006', 'Van Hausen Formal Shirts Size42', 'Shirts', 1150.00),
    ('sh007', 'Arrow Formal Shirts Size40', 'Shirts', 900.00), ('sh008', 'Arrow Formal Shirts Size42', 'Shirts', 900.00),
    ('sh009', 'John Players Formal Shirts Size40', 'Shirts', 1100.00), ('sh010', 'John Players Formal Shirts Size42', 'Shirts', 1100.00),
    ('sh011', 'Indo Primo Casual Shirts Size40', 'Shirts', 800.00), ('sh012', 'Indo Primo Casual Shirts Size42', 'Shirts', 8500.00),
    ('sh013', 'Tommy Hilfiger Casual Shirts Size40', 'Shirts', 1500.00), ('sh014', 'Tommy Hilfiger Casual Shirts Size42', 'Shirts', 1500.00),
    ('sh015', 'Pepe Jeans Casual Shirts Size40', 'Shirts', 1300.00), ('sh016', 'Pepe Jeans Shirts Size42', 'Shirts', 1350.00),
    ('sh017', 'Roadster Shirts Size40', 'Shirts', 900.00), ('sh018', 'Roadster Shirts Size42', 'Shirts', 1000.00),
    ('ts001', 'Levi TShirts Colour Red', 'TShirts', 1100.00), ('ts002', 'Levi TShirts Colour Black', 'TShirts', 1100.00),
    ('ts003', 'Levi TShirts Colour Blue', 'TShirts', 1100.00), ('ts004', 'U.S. Polo TShirts Colour Red', 'TShirts', 1200.00),
    ('ts005', 'U.S. Polo TShirts Colour Black', 'TShirts', 1250.00), ('ts006', 'U.S. Polo TShirts Colour Blue', 'TShirts', 1300.00),
    ('ts007', 'Lee Cooper TShirts Colour Red', 'TShirts', 900.00), ('ts008', 'Lee Cooper TShirts Colour Black', 'TShirts', 1000.00),
    ('ts009', 'Lee Cooper TShirts Colour Blue', 'TShirts', 1000.00), ('ts010', 'Spykar TShirts Colour Red', 'TShirts', 1200.00),
    ('ts011', 'Spykar TShirts Colour Blue', 'TShirts', 1200.00), ('ts012', 'Spykar TShirts Colour Black', 'TShirts', 1200.00),
    ('ts013', 'Allen Solly TShirts Colour Red', 'TShirts', 1300.00), ('ts014', 'Allen Solly TShirts Colour Black', 'TShirts', 1350.00),
    ('ts015', 'Allen Solly TShirts Colour Blue', 'TShirts', 1400.00),
    ('j001', 'Lee Cooper Faded Jeans', 'Jeans', 2000.00), ('j002', 'Lee Cooper Faded Jeans', 'Jeans', 2100.00),
    ('j003', 'Pantaloon Cropped Jeans', 'Jeans', 1500.00), ('j004', 'Pantaloon Solid Jeans', 'Jeans', 1500.00),
    ('j005', 'En Special Faded Jeans', 'Jeans', 1700.00), ('j006', 'En Special Cropped Jeans', 'Jeans', 1600.00),
    ('j007', 'Pepe Jeans Rugged Jeans', 'Jeans', 1900.00), ('j008', 'Pepe Jeans Solid Jeans', 'Jeans', 1800.00),
    ('j009', 'Denim Cropped Jeans', 'Jeans', 1500.00), ('j010', 'Denim Rugged Jeans', 'Jeans', 1400.00)
]
cursorObj.executemany("INSERT INTO Clothing VALUES(?, ?, ?, ?)", clothing_data)
arrow.commit()
