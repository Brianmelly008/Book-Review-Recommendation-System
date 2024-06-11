from faker import Faker
from models import SessionLocal, Author, Book, create_tables

def seed_data():
    fake = Faker()
    session = SessionLocal()

    for _ in range(10):
        author = Author(name=fake.name())
        session.add(author)
        session.commit()
        
        for _ in range(3):
            book = Book(title=fake.catch_phrase(), author_id=author.id)
            session.add(book)
            session.commit()

    session.close()
    print("Database seeded with test data!")

if __name__ == "__main__":
    create_tables()
    seed_data()
