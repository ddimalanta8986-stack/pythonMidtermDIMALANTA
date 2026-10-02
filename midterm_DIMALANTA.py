FILE_NAME = "midterm_DIMALANTA.py"


def display_menu():
    """Displays the main interactive menu options."""
    print("==========================================")
    print("      SALES RECORD MANAGEMENT SYSTEM      ")
    print("==========================================")
    print("1. Add Sale Record")
    print("2. View All Records & Summary Statistics")
    print("3. Clear All Sales Data")
    print("4. Exit System")
    print("==========================================")


def add_sale_record():
    """Prompts for sale details, calculates total, and appends record to sales_log.txt."""
    print("\n--- Add Sale Record ---")

    # Prompt and validate Item Name
    item_name = input("Enter Item Name: ").strip()
    while not item_name:
        print("Item name cannot be empty.")
        item_name = input("Enter Item Name: ").strip()

    # Prompt and validate Quantity Sold
    while True:
        try:
            quantity = int(input("Enter Quantity Sold: "))
            if quantity <= 0:
                print("Quantity must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for quantity.")

    # Prompt and validate Price Per Unit
    while True:
        try:
            price = float(input("Enter Price Per Unit: "))
            if price <= 0:
                print("Price must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for price.")

    # Calculate total transaction amount
    total_amount = quantity * price

    # Write CSV row to file
    try:
        with open(FILE_NAME, "a", encoding="utf-8") as file:
            file.write(f"{item_name},{quantity},{price:.2f},{total_amount:.2f}\n")
        print("Sale record saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the record: {e}")


def view_records_and_summary():
    """Reads sales_log.txt line by line, parses CSV data, and displays records with summary statistics."""
    print("\n--- View All Records & Summary Statistics ---")

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            print("No records found.")
            return

        total_units_sold = 0
        grand_total_revenue = 0.0

        print(
            f"{'Item Name':<20} | {'Quantity':<10} | {'Price/Unit':<12} | {'Total Amount':<12}"
        )
        print("-" * 62)

        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) == 4:
                item_name = parts[0]
                quantity = int(parts[1])
                price = float(parts[2])
                total_amount = float(parts[3])

                total_units_sold += quantity
                grand_total_revenue += total_amount

                print(
                    f"{item_name:<20} | {quantity:<10} | ${price:<11.2f} | ${total_amount:<11.2f}"
                )

        print("-" * 62)
        print(f"Total Units Sold: {total_units_sold}")
        print(f"Grand Total Revenue: ${grand_total_revenue:.2f}")

    except FileNotFoundError:
        print("No records found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def clear_sales_data():
    """Overwrites sales_log.txt to permanently clear all data."""
    try:
        open(FILE_NAME, "w", encoding="utf-8").close()
        print("All records cleared. No records remaining.")
    except Exception as e:
        print(f"An error occurred while clearing data: {e}")


def main():
    """Main program execution loop."""
    while True:
        display_menu()
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_sale_record()
        elif choice == "2":
            view_records_and_summary()
        elif choice == "3":
            clear_sales_data()
        elif choice == "4":
            exit("Goodbye! ")
        else:
            print("Invalid option selected. Please enter a number between 1 and 4.")
        print()

main()

