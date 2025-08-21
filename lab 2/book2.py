import json
import os

BOOK_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "book.json")

def load_books():
    if not os.path.exists(BOOK_FILE):
        return []
    try:
        with open(BOOK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_books(books):
    with open(BOOK_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, indent=2, ensure_ascii=False)

def view_books():
    books = load_books()
    if not books:
        print("\nNo books found.\n")
        return
    print("\nBooks:")
    for b in books:
        print(f"Title: {b.get('title','')}")
        print(f"Author: {b.get('author','')}")
        print(f"Genre: {b.get('genre','')}")
        print("\n")

def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()
    books = load_books()
    books.append({"title": title, "author": author, "genre": genre})
    save_books(books)
    print(f'\nAdded "{title}".\n')

def update_book():
    title = input("Enter the title to update: ").strip()
    books = load_books()
    for b in books:
        if (b.get("title") or "").lower() == title.lower():
            new_author = input(f"New author [{b.get('author','')}]: ").strip()
            new_genre  = input(f"New genre  [{b.get('genre','')}]: ").strip()
            if new_author: b["author"] = new_author
            if new_genre:  b["genre"]  = new_genre
            save_books(books)
            print(f'\nUpdated "{title}".\n')
            return
    print(f'\nBook "{title}" not found.\n')

def delete_book():
    title = input("Enter the title to delete: ").strip()
    books = load_books()
    new_books = [b for b in books if (b.get("title") or "").lower() != title.lower()]
    if len(new_books) != len(books):
        save_books(new_books)
        print(f'\nDeleted "{title}".\n')
    else:
        print(f'\nBook "{title}" not found.\n')

if __name__ == "__main__":
    while True:
        print("\nMenu")
        print("1. View books")
        print("2. Add a new book")
        print("3. Update a book")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            view_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Exited")
            break
        else:
            print("")
