from datetime import datetime, timedelta

# ===== IN-MEMORY STORAGE (NO MYSQL) =====
books = []
issued_books = []

book_id_counter = 1
issue_id_counter = 1

# ===== ADD BOOK =====
def add_book():
    global book_id_counter
    title = input("Book Title: ")
    author = input("Author: ")
    quantity = int(input("Quantity: "))

    books.append({
        "id": book_id_counter,
        "title": title,
        "author": author,
        "quantity": quantity
    })
    book_id_counter += 1
    print("Book Added Successfully")

# ===== REMOVE BOOK =====
def remove_book():
    book_id = int(input("Enter Book ID to remove: "))
    global books
    books = [b for b in books if b["id"] != book_id]
    print("Book Removed Successfully")

# ===== ISSUE BOOK =====
def issue_book():
    global issue_id_counter
    book_id = int(input("Book ID: "))
    user_name = input("User Name: ")

    for book in books:
        if book["id"] == book_id and book["quantity"] > 0:
            issue_date = datetime.now()
            return_date = issue_date + timedelta(days=7)

            issued_books.append({
                "id": issue_id_counter,
                "book_id": book_id,
                "user_name": user_name,
                "issue_date": issue_date,
                "return_date": return_date,
                "fine": 0
            })

            book["quantity"] -= 1
            issue_id_counter += 1
            print("Book Issued Successfully")
            return

    print("Book not available")

# ===== RETURN BOOK =====
def return_book():
    issue_id = int(input("Issue ID: "))

    for issue in issued_books:
        if issue["id"] == issue_id:
            today = datetime.now()
            fine = 0

            if today > issue["return_date"]:
                days_late = (today - issue["return_date"]).days
                fine = days_late * 2

            issue["fine"] = fine

            for book in books:
                if book["id"] == issue["book_id"]:
                    book["quantity"] += 1

            print(f"Book Returned. Fine = {fine}")
            return

    print("Invalid Issue ID")

# ===== VIEW BOOKS =====
def view_books():
    for book in books:
        print(book)

# ===== MENU =====
while True:
    print("\n1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        remove_book()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        view_books()
    elif choice == '6':
        break
    else:
        print("Invalid Choice")