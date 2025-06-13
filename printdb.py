from persistence import *
import sqlite3

def print_activities(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM activities")
    activities = cursor.fetchall()
    print("Activities")
    for activity in activities:
        print(activity)

def print_branches(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT location, number_of_employees, id FROM branches")
    branches = cursor.fetchall()
    print("\nBranches")
    for branch in branches:
        print(branch)

def print_employees(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name, salary, branche, id FROM employees")
    employees = cursor.fetchall()
    print("\nEmployees")
    for employee in employees:
        print(employee)

def print_products(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT description, price, quantity, id FROM products")
    products = cursor.fetchall()
    print("\nProducts")
    for product in products:
        print(product)

def print_suppliers(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name, contact_information, id FROM suppliers")
    suppliers = cursor.fetchall()
    print("\nSuppliers")
    for supplier in suppliers:
        print(supplier)

def print_employees_report(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.name, e.salary, b.location, 
               COALESCE(SUM(a.quantity * p.price), 0) AS total_sales
        FROM employees e
        LEFT JOIN branches b ON e.branche = b.id
        LEFT JOIN activities a ON e.id = a.activator_id
        LEFT JOIN products p ON a.product_id = p.id
        GROUP BY e.id
        ORDER BY e.name
    """)
    employees_report = cursor.fetchall()
    print("\nEmployees report")
    for report in employees_report:
        print(f"{report[0]} {report[1]} {report[2]} {abs(report[3])}")


def print_activities_report(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.date, p.description, a.quantity, e.name, s.name
        FROM activities a
        LEFT JOIN products p ON a.product_id = p.id
        LEFT JOIN employees e ON a.activator_id = e.id
        LEFT JOIN suppliers s ON a.activator_id = s.id
        ORDER BY p.description

    """)
    activities_report = cursor.fetchall()
    print("\nActivities report")
    for report in activities_report:
        print(report)
def main():
    conn = sqlite3.connect('bgumart.db')

    print_activities(conn)
    print_branches(conn)
    print_employees(conn)
    print_products(conn)
    print_suppliers(conn)
    print_employees_report(conn)
    print_activities_report(conn)

    conn.close()

if __name__ == '__main__':
    main()