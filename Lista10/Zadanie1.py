import argparse
import sys
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

engine = sqlalchemy.create_engine('sqlite:///baza.db', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class Book(Base):  # child - one to many (many books to one person)

    __tablename__ = "Book"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)
    parent_id = Column(Integer, ForeignKey('Person.id'))
    parent = relationship("Person", back_populates="children")

    def __repr__(self):
        return "Book: title='%s' author='%s' year='%s'" % (self.title, self.author, self.year)


class Person(Base):  # parent - one to many
    __tablename__ = "Person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mail = Column(String)
    children = relationship("Book", back_populates="parent")

    def __repr__(self):
        return "Person: name='%s', mail='%s'" % (self.name, self.mail)


def add(newBook):
    book = Book(title=newBook.title, author=newBook.author, year=newBook.year)
    session.add(book)
    session.commit()


def addPerson(newPerson):
    person = Person(name=newPerson.name, mail=newPerson.mail)
    session.add(person)
    session.commit()


def displayBooks(options):
    our_books = session.query(Book).order_by(Book.id.asc())  # OR DESC
    for books in our_books:
        print(books.id, books.title, books.author, books.year, "Borrowed by:", books.parent)


def displayPeople(options):
    people = session.query(Person).order_by(Person.id.asc())
    for person in people:
        print(person.id, person.name, person.mail, "Borrowed: ", person.children)


def returnBook(options):
    borrowed_book = session.query(Book).filter(Book.title == options.title).one()
    borrowed_book.parent_id = None
    session.commit()


def borrowBook(options):
    borrower = session.query(Person).filter(Person.name == options.name).one()
    borrowed_book = session.query(Book).filter(Book.title == options.title).one()
    borrower.children.append(borrowed_book)
    session.commit()


Base.metadata.create_all(engine)

parser = argparse.ArgumentParser(description='Organize your books.')
subparsers = parser.add_subparsers()

parser_addBook = subparsers.add_parser("--add",
                                       help="Add a book - type author, title and year")
parser_addBook.add_argument("--title")
parser_addBook.add_argument("--author")
parser_addBook.add_argument("--year")
parser_addBook.set_defaults(func=add)

parser_addPerson = subparsers.add_parser("addPerson",
                                         help="Add a person - type name and e-mail")
parser_addPerson.add_argument("--name")
parser_addPerson.add_argument("--mail")
parser_addPerson.set_defaults(func=addPerson)

parser_displayBooks = subparsers.add_parser("displayBooks", help="Display all books")
parser_displayBooks.set_defaults(func=displayBooks)

parser_displayPeople = subparsers.add_parser("displayPeople", help="Display all people")
parser_displayPeople.set_defaults(func=displayPeople)

parser_return = subparsers.add_parser("return", help="Return a book - title of the book")
parser_return.add_argument("--title")
parser_return.set_defaults(func=returnBook)

parser_borrow = subparsers.add_parser("borrow", help="Borrow a book - type borrower's name and title of the book")
parser_borrow.add_argument("--name")
parser_borrow.add_argument("--title")
parser_borrow.set_defaults(func=borrowBook)

if len(sys.argv) <= 1:
    sys.argv.append('--help')

options = parser.parse_args()
options.func(options)
session.close()
