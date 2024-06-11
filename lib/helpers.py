from db.models import SessionLocal, Author, Book

def create_author():
    name = input("Enter author name: ")
    session = SessionLocal()
    author = Author(name=name)
    session.add(author)
    session.commit()
    session.close()
    print(f"Author '{name}' created successfully!")

def create_book():
    title = input("Enter book title: ")
    author_id = input("Enter author ID: ")
    session = SessionLocal()
    book = Book(title=title, author_id=author_id)
    session.add(book)
    session.commit()
    session.close()
    print(f"Book '{title}' created successfully!")

def list_authors():
    session = SessionLocal()
    authors = session.query(Author).all()
    session.close()
    for author in authors:
        print(author)

def list_books():
    session = SessionLocal()
    books = session.query(Book).all()
    session.close()
    for book in books:
        print(book)

def find_author():
    author_id = input("Enter author ID: ")
    session = SessionLocal()
    author = session.query(Author).get(author_id)
    session.close()
    if author:
        print(author)
    else:
        print("Author not found")

def find_book():
    book_id = input("Enter book ID: ")
    session = SessionLocal()
    book = session.query(Book).get(book_id)
    session.close()
    if book:
        print(book)
    else:
        print("Book not found")

def delete_author():
    author_id = input("Enter author ID: ")
    session = SessionLocal()
    author = session.query(Author).get(author_id)
    if author:
        session.delete(author)
        session.commit()
        print(f"Author '{author.name}' deleted successfully!")
    else:
        print("Author not found")
    session.close()

def delete_book():
    book_id = input("Enter book ID: ")
    session = SessionLocal()
    book = session.query(Book).get(book_id)
    if book:
        session.delete(book)
        session.commit()
        print(f"Book '{book.title}' deleted successfully!")
    else:
        print("Book not found")
    session.close()
