from persistence import *
import sys


def process_activity(splittedline: list[str]):
    product_id = int(splittedline[0])
    quantity = int(splittedline[1])
    activator_id = int(splittedline[2])
    date = splittedline[3]

    product = repo.products.find(id=product_id)
    if not product:
        return  # Product does not exist

    product = product[0]  # Extract the product from the list
    if quantity < 0 and product.quantity < abs(quantity):
        return  # Not enough stock to complete the sale

    # Update product quantity
    new_quantity = product.quantity + quantity
    repo.products.delete(id=product.id)  # Remove old entry
    updated_product = Product(product.id, product.description, product.price, new_quantity)
    repo.products.insert(updated_product)

    # Insert the activity into the activities table
    activity = Activitie(product_id, quantity, activator_id, date)
    repo.activities.insert(activity)


def main(args: list[str]):
    if len(args) < 2:
        print("Usage: python action.py <action_file>")
        return

    inputfilename: str = args[1]
    try:
        with open(inputfilename) as inputfile:
            for line in inputfile:
                splittedline: list[str] = line.strip().split(", ")
                if len(splittedline) != 4:
                    continue  # Skip invalid lines
                process_activity(splittedline)
    except FileNotFoundError:
        print(f"Error: File '{inputfilename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main(sys.argv)
