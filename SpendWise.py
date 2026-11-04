# SpendWise: Student Expense Tracker
# ITE 260 - Computer Programming 1

from datetime import date

expenses = []
budget = 0.0


def calculate_total(expense_list):
    total = 0.0

    for expense in expense_list:
        total += expense[3]

    return total


def calculate_remaining(current_budget, expense_list):
    total = calculate_total(expense_list)
    remaining = current_budget - total

    return remaining


def show_budget_status():
    total = calculate_total(expenses)
    remaining = calculate_remaining(budget, expenses)

    print(f"\nTotal Budget:   ₱{budget:.2f}")
    print(f"Total Expenses: ₱{total:.2f}")

    if remaining >= 0:
        print(f"Remaining Budget: ₱{remaining:.2f}")
    else:
        over_budget = abs(remaining)

        print("\n⚠️ WARNING!")
        print(f"You have exceeded your budget by ₱{over_budget:.2f}.")
        print("Please monitor your spending.")


def set_budget():
    global budget

    if budget == 0:
        prompt = "Enter your initial budget: ₱"
    else:
        prompt = "Enter additional budget: ₱"

    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            if budget == 0:
                budget = amount

                print("\nBudget successfully set.")
                print(f"Initial Budget: ₱{amount:.2f}")

            else:
                budget += amount

                print("\nBudget successfully added.")
                print(f"Additional Budget: ₱{amount:.2f}")

            show_budget_status()
            return

        except ValueError:
            print("Invalid input. Please enter a number.")


def add_expense():
    if budget <= 0:
        print("\nPlease set your budget first.")
        return

    description = input("Enter expense description: ").strip()

    if description == "":
        print("Description cannot be empty.")
        return

    print("\nCategories:")
    print("1. Food")
    print("2. Transportation")
    print("3. School Needs")
    print("4. Other")

    while True:
        category_choice = input("Choose a category: ")

        if category_choice == "1":
            category = "Food"
            break
        elif category_choice == "2":
            category = "Transportation"
            break
        elif category_choice == "3":
            category = "School Needs"
            break
        elif category_choice == "4":
            category = "Other"
            break
        else:
            print("Invalid category. Please choose 1-4.")

    while True:
        try:
            amount = float(input("Enter expense amount: ₱"))

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    expense_date = date.today().strftime("%m/%d/%y")

    expenses.append([
        expense_date,
        description,
        category,
        amount
    ])

    print("\n========== EXPENSE ADDED ==========")

    print(
        f"{'No.':<3} | "
        f"{'Date':<8} | "
        f"{'Category':<14} | "
        f"{'Description':<12} | "
        f"{'Amount':>8}"
    )

    print("-" * 59)

    print(
        f"{len(expenses):<3} | "
        f"{expense_date:<8} | "
        f"{category:<14} | "
        f"{description:<12} | "
        f"₱{amount:>6.2f}"
    )

    show_budget_status()


def view_expenses():
    if len(expenses) == 0:
        print("\nNo expenses recorded.")
        return

    print("\n========== EXPENSE RECORDS ==========")

    print(
        f"{'No.':<3} | "
        f"{'Date':<8} | "
        f"{'Category':<14} | "
        f"{'Description':<12} | "
        f"{'Amount':>8}"
    )

    print("-" * 59)

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i:<3} | "
            f"{expense[0]:<8} | "
            f"{expense[2]:<14} | "
            f"{expense[1]:<12} | "
            f"₱{expense[3]:>6.2f}"
        )


def edit_expense():
    if len(expenses) == 0:
        print("\nNo expenses to edit.")
        return

    view_expenses()

    while True:
        try:
            choice = int(input("\nEnter expense number to edit: "))

            if 1 <= choice <= len(expenses):
                index = choice - 1
                break
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    new_description = input(
        "Enter new description (press Enter to keep current): "
    ).strip()

    if new_description != "":
        expenses[index][1] = new_description

    print("\nCategories:")
    print("1. Food")
    print("2. Transportation")
    print("3. School Needs")
    print("4. Other")
    print("Press Enter to keep the current category.")

    while True:
        category_choice = input("Choose new category: ").strip()

        if category_choice == "":
            break
        elif category_choice == "1":
            expenses[index][2] = "Food"
            break
        elif category_choice == "2":
            expenses[index][2] = "Transportation"
            break
        elif category_choice == "3":
            expenses[index][2] = "School Needs"
            break
        elif category_choice == "4":
            expenses[index][2] = "Other"
            break
        else:
            print("Invalid category. Please choose 1-4.")

    while True:
        try:
            new_amount = input(
                "Enter new amount (press Enter to keep current): ₱"
            ).strip()

            if new_amount == "":
                break

            new_amount = float(new_amount)

            if new_amount > 0:
                expenses[index][3] = new_amount
                break
            else:
                print("Amount must be greater than 0.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nExpense successfully updated.")
    show_budget_status()


def delete_expense():
    if len(expenses) == 0:
        print("\nNo expenses to delete.")
        return

    view_expenses()

    while True:
        try:
            choice = int(input("\nEnter expense number to delete: "))

            if 1 <= choice <= len(expenses):
                index = choice - 1
                break
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")

    deleted_expense = expenses.pop(index)

    print(f"\nDeleted expense: {deleted_expense[1]}")
    print("Expense record successfully deleted.")

    show_budget_status()


def view_summary():
    if budget <= 0:
        print("\nPlease set your budget first.")
        return

    print("\n========== BUDGET SUMMARY ==========")
    show_budget_status()

    remaining = calculate_remaining(budget, expenses)

    if remaining > 0:
        print("\nYou still have budget remaining.")
    elif remaining == 0:
        print("\nYour budget has been fully used.")
    else:
        print("\nYour expenses have exceeded your budget.")


def main():
    while True:
        print("\n========== SPENDWISE ==========")
        print("1. Set Budget / Add Budget")
        print("2. Add Expense")
        print("3. View Expenses")
        print("4. Edit Expense")
        print("5. Delete Expense")
        print("6. View Summary")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            set_budget()

        elif choice == "2":
            add_expense()

        elif choice == "3":
            view_expenses()

        elif choice == "4":
            edit_expense()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            view_summary()

        elif choice == "7":
            print("\nThank you for using SpendWise!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


main()