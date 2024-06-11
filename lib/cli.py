import sys
from helpers import create_author, create_book, list_authors, list_books, find_author, find_book, delete_author, delete_book

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("Goodbye!")
            sys.exit()
        elif choice == "1":
            create_author()
        elif choice == "2":
            create_book()
        elif choice == "3":
            list_authors()
        elif choice == "4":
            list_books()
        elif choice == "5":
            find_author()
        elif choice == "6":
            find_book()
        elif choice == "7":
            delete_author()
        elif choice == "8":
            delete_book()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit")
    print("1. Create Author")
    print("2. Create Book")
    print("3. List Authors")
    print("4. List Books")
    print("5. Find Author by ID")
    print("6. Find Book by ID")
    print("7. Delete Author by ID")
    print("8. Delete Book by ID")

if __name__ == "__main__":
    main()
