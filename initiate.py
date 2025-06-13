import sqlite3
from persistence import *
import sys
import os

# Global connection
conn = None

def open_connection():
    global conn
    if conn is None:
        conn = sqlite3.connect('bgumart.db',10)  # Add a timeout to handle locks

def close_connection():
    global conn
    if conn:
        conn.commit()  # Commit any pending transactions
        conn.close()
        conn = None

def add_branche(splittedline: list[str]):
    id = splittedline[0]
    location = splittedline[1]
    quantity = splittedline[2]
    branche = Branche(id, location, quantity)
    branche_dao = Dao(Branche, conn)
    branche_dao.insert(branche)

def add_supplier(splittedline: list[str]):
    id = splittedline[0]
    name = splittedline[1]
    contact_information = splittedline[2]
    supplier = Supplier(id, name, contact_information)
    supplier_dao = Dao(Supplier, conn)
    supplier_dao.insert(supplier)

def add_product(splittedline: list[str]):
    id = splittedline[0]
    description = splittedline[1]
    price = splittedline[2]
    quantity = splittedline[3]
    product = Product(id, description, price, quantity)
    product_dao = Dao(Product, conn)
    product_dao.insert(product)

def add_employee(splittedline: list[str]):
    id = splittedline[0]
    name = splittedline[1]
    salary = splittedline[2]
    branch_id = splittedline[3]
    employee = Employee(id, name, salary, branch_id)
    employee_dao = Dao(Employee, conn)
    employee_dao.insert(employee)

adders = {  
    "B": add_branche,
    "S": add_supplier,
    "P": add_product,
    "E": add_employee
}

def main(args: list[str]):
    if len(args) < 2:
        print("Usage: python initiate.py <input_file>")
        return

    inputfilename = args[1]
    # delete the database file if it exists
    repo._close()
    if os.path.isfile("bgumart.db"):
        os.remove("bgumart.db")
    repo.__init__()
    repo.create_tables()

    # Open the global connection
    open_connection()

    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline: list[str] = line.strip().split(",")
            adders.get(splittedline[0])(splittedline[1:])

    # Close the connection after all operations
    close_connection()

if __name__ == '__main__':
    main(sys.argv)
