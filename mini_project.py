import csv
from datetime import datetime
# import os

# Function to add an expense
def add_expense(expenses):

    # Get the amount from the user
    amount = float(input("Enter the amount: "))

    # Get the category from the user
    category = input("Enter the category (e.g., Food, Transport, Entertainment): ")

    # Get the date from the user or use today's date if left blank
    date = input("Enter the date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    # Create a dictionary for the expense
    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    # Add the expense to the list
    expenses.append(expense)
    print("Expense added successfully!")

# Function to view summary
def view_summary(expenses):
    category_summary = {}
    total_spending = 0

    # Calculate total spending and spending by category
    for expense in expenses:
        try:
            total_spending += expense["amount"]
            if expense["category"] in category_summary:
                category_summary[expense["category"]] += expense["amount"]

            else:
                category_summary[expense["category"]] = expense["amount"]
        except KeyError as e:
            print(f"Missing key in expense entry: {e}")
            print(f"Expense entry: {expense}")

    # Print the summary
    print("\nTotal Spending by Category:")
    for category, amount in category_summary.items():
        print(f"{category}: ${amount:.2f}")

    print(f"\nTotal Overall Spending: ${total_spending:.2f}")

# Function to save expenses to a CSV file
def save_expenses(expenses, filename="expenses.csv"):

    # Open the file in write mode
    with open(filename, "w", newline='') as file:
        writer = csv.writer(file)

        # Write the header
        writer.writerow(["Amount Spend", "Category", "Date"])

        # Write each expense
        for expense in expenses:
            writer.writerow([expense["amount"], expense["category"], expense["date"]])

    # Print the absolute path of the saved file
    # print(f"Expenses saved to file: {os.path.abspath(filename)}")

# Function to load expenses from a CSV file
def load_expenses(filename="expenses.csv"):
    expenses = []

    try:
        # Open the file in read mode
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            # Read each expense and add to the list
            for row in reader:
                try:
                    expense = {
                        "amount": float(row["Amount Spend"]),
                        "category": row["Category"],
                        "date": row["Date"]
                    }
                    expenses.append(expense)
                except KeyError as e:
                    print(f"Missing key in CSV row: {e}")
                    print(f"CSV row: {row}")
        print("Expenses loaded from file.")
    except FileNotFoundError:
        print("No previous expenses found.")
    return expenses

# Main function to run the expense tracker
def main():
    expenses = load_expenses()
    while True:

        # Display the menu
        print("\nPersonal Expense Tracker")
        print("1. Add an expense")
        print("2. View summary")
        print("3. Save and exit")
        choice = input("Enter your choice: ")

        # Handle user choice
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            save_expenses(expenses)
            break
        else:
            print("Invalid choice. Please try again.")

main()