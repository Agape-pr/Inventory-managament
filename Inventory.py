#add product
#add product name, category eg: electronics , groceries,, stock quantity and price
#
#
#
#track stock level
# Display a table of all products with their details
#
#update product details and stock quantities.
#update product name category or price
#restock products
#remove the product from the inventory
#
#Generates low stock alerts
#when stock <5 generate alerts for products with stock below a specified threshold
#
#
#search and sort procucts: by name categoty or stock quantity
#by name or category
#sort product by price or stock quantity.
#ghcgh
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Donatha0784748183!",
    database = "stock_inventory_management_system"
    
)
mycursor =  mydb.cursor()
class Product:
    def __init__(self, name, category, quantity, price):
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
    def add_product(self):
            sql = "INSERT INTO inventory(Name, Category, Quantity, Price) VALUES (%s, %s, %s, %s)"
            val = (self.name, self.category, self.quantity, self.price)
            mycursor.execute(sql,val)
            mydb.commit()

def checkall() :
    sql = "SELECT * FROM inventory"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()        
    for item in myresult:
        print(item)

while True :
    print("WELCOME TO THE STOCK MANAGEMENT SYSTEM")
    print("Select 1 to add product to the stock")
    print("Select 2 to Check the stock")
    print("Select 3 update product details")
    print("Select 4 to delete product")
    print("Select 5 to search and sort product")
    print("Select 6 for checking the stock")


    task = int(input("enter the right option: "))
    match task:
        case 1 :
            fl = True
            while fl :
                print("You are going to add product to the stock")
                namep = input("enter the name of product: ")
                categoryp = input("enter category eg: electronics , gloceries: ")
                quantityp = int(input("enter the quantity: "))
                pricep = float(input("Enter the price: "))
                product1 = Product(namep, categoryp, quantityp, pricep)
                product1.add_product()   
                print(mycursor.rowcount, "Product added to the stock successfully ")
                print("Enter 1 to add other product")
                print("Enter 2 Go The main menu")
                promp = int(input("Enter your choic: "))
                if promp == 1 :
                    continue
                elif promp == 2 :
                    fl = False
                else:
                    print("enter the right option")
        case 2 :
            while True:
                print("This the current stock level")
                checkall()
                pro = int(input("enter 1 to go to the main menu: "))
                if pro == 1:
                    break
                else :
                    pass
            
        case 3 :
            print("Choose wht you want to modify")
            print("1 modify quantity or restock")
            print("2 modify price")
            print("3 modify Name of product")
            mod = int(input("Enter your choice: "))
            match mod:
                case 1 :
                    print("")
                    productid = input("enter PRODUCT ID")
                    print("Here is the product you selected")
                    
                    sql = "SELECT * FROM inventory WHERE proeduct_id = %s"
                    val = (productid,)
                    mycursor.execute(sql, val)
                    result = mycursor.fetchone()
                    print(result)
                    new_quantiry = input("enter new quantity: ")
                    
                    sql = "UPDATE INVENTORY SET Quantity = %s WHERE proeduct_id = %s"
                    val = (new_quantiry, productid)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Updating quantity is successful")
                case 2 :
                    productid = input("enter PRODUCT ID ")
                    print("Here is the product you selected")
                    sql = "SELECT * FROM inventory WHERE proeduct_id = %s"
                    val = (productid,)
                    mycursor.execute(sql, val)
                    result = mycursor.fetchone()
                    print(result)
                    new_price = input("enter new price: ")
                    sql = "UPDATE INVENTORY SET Price = %s WHERE proeduct_id = %s"
                    val = (new_price, productid)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Updating price is successful")
                
                case 3 :
                    
                    productid = input("enter PRODUCT ID ")
                    print("Here is the product you selected")
                    sql = "SELECT * FROM inventory WHERE proeduct_id = %s"
                    val = (productid,)
                    mycursor.execute(sql, val)
                    result = mycursor.fetchone()
                    print(result)
                    new_name = input("enter new name of product: ")
                    sql = "UPDATE INVENTORY SET Name = %s WHERE proeduct_id = %s"
                    val = (new_name, productid)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Updating name of product is successful")
                    
                
                    
                case _:
                    print("wrong input")
                    
        case 4 :
                    
                    productid = input("enter PRODUCT ID  of product you want to delete")
                    slt = input("Are you sure you want to delete this product . yes/no? ")
                    if slt == "yes" :
                        sql = "DELETE FROM inventory WHERE proeduct_id = %s"
                        val = (productid,)
                        mycursor.execute(sql, val)
                        mydb.commit()   
                        print("the deletion is successful")     
                    else: 
                        pass 
        
        
        case 5 :
            print("1. Search product")
            print("2. Sort product to generate report")
            prom = int(input("Enter your choice: "))
            if prom == 1 :
                searchname= input("Enter the name of product: ")
                sql = ("SELECT * FROM inventory WHERE Name = %s")
                val = (searchname,)
                mycursor.execute(sql,val)
                result = mycursor.fetchone()
                print(result)
            elif prom == 2 :
                print("1. sort by name")
                print("2. sort by category")
                print("3. sort by quantity")
                print("4. sort by price")
                pro = int(input("enter youe choice: "))
                if pro == 1 :
                    sql = "SELECT * FROM inventory ORDER BY Name ASC"
                    mycursor.execute(sql)
                    myresult = mycursor.fetchall()
                    for item in myresult:
                        print(item)
                elif pro == 2 :
                    sql = "SELECT * FROM inventory ORDER BY Category ASC"
                    mycursor.execute(sql)
                    myresult = mycursor.fetchall()
                    for item in myresult:
                        print(item)
                elif pro == 3 :
                    sql = "SELECT * FROM inventory ORDER BY Quantity ASC"
                    mycursor.execute(sql)
                    myresult = mycursor.fetchall()
                    for item in myresult:
                        print(item)
                if pro == 4 :
                    sql = "SELECT * FROM inventory ORDER BY Price ASC"
                    mycursor.execute(sql)
                    myresult = mycursor.fetchall()
                    for item in myresult:
                        print(item)
            else:
                pass
            
        case 6 :
        
            print("Following products needs restock ")  
            sql = "SELECT * FROM inventory WHERE Quantity < 10"
            mycursor.execute(sql)
            myresult = mycursor.fetchall() 
            if myresult:       
                for item in myresult:
                    print(item)
            else:
                print("All product are well stocked")
            
            check = input("Do you want to check the whole stock here? -yes/no: ")
            if check == "yes":
                checkall()
            
        case _:
            print("enter right option")  
            
            
mycursor.close()
mydb.close()
