from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
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
        if self.parent:
            return 'Book%s: "%s" by %s, year: %s, borrowed by: %s' % (
                self.id, self.title, self.author, self.year, self.parent.name)
        else:
            return 'Book%s: "%s" by %s, year: %s, not borrowed' % (self.id, self.title, self.author, self.year)


class Person(Base):  # parent - one to many
    __tablename__ = "Person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mail = Column(String)
    children = relationship("Book", back_populates="parent")

    def __repr__(self):
        if self.children:
            titles = ""
            for child in self.children[:len(self.children) - 1]:
                titles += '"' + child.title + '"' + ", "
            titles += '"' + self.children[len(self.children) - 1].title + '"'
            return 'Person%s: %s, email: %s, borrows: %s ' % (self.id, self.name, self.mail, titles)
        else:
            return "Person%s: %s, email: %s, doesn't borrow anything" % (self.id, self.name, self.mail)


Base.metadata.create_all(engine)


def display():
    our_books = session.query(Book).order_by(Book.id.asc())  # OR DESC
    for book in our_books:
        book_list.insert(END, book)

    our_friends = session.query(Person).order_by(Person.id.asc())  # OR DESC
    for friend in our_friends:
        friend_list.insert(END, friend)


def add_book():
    title = simpledialog.askstring("Title", "Please enter title of new book")
    if not title:
        messagebox.showerror("No data", "Title cannot be empty!")
        return
    author = simpledialog.askstring("Author", "Please enter author of the book")
    if not author:
        messagebox.showerror("No data", "Author cannot be empty!")
        return
    year = simpledialog.askstring("Year", "Please enter year of production of the book")
    if not year:
        messagebox.showerror("No data", "Year cannot be empty!")
        return
    new_book = Book(title=title, author=author, year=year)
    session.add(new_book)
    session.commit()
    book_list.insert(END, new_book)


def add_friend():
    name = simpledialog.askstring("Name", "Please enter name of new friend")
    if not name:
        messagebox.showerror("No data", "Name cannot be empty!")
        return
    email = simpledialog.askstring("Email", "Please enter email of the friend")
    if not email:
        messagebox.showerror("No data", "Email cannot be empty!")
        return
    new_friend = Person(name=name, mail=email)
    session.add(new_friend)
    session.commit()
    friend_list.insert(END, new_friend)


def select_book(event):
    global selected_book
    if book_list.curselection():
        index = book_list.curselection()[0]
        selected_book = session.query(Book).filter(Book.id == index + 1).one()


def select_friend(event):
    global selected_friend
    if friend_list.curselection():
        index = friend_list.curselection()[0]
        selected_friend = session.query(Person).filter(Person.id == index + 1).one()


def borrow():
    if selected_book.parent_id:
        messagebox.showerror("Already borrowed", "This book has already been borrowed!")
        return
    else:
        selected_friend.children.append(selected_book)
        session.commit()
        book_list.delete(0, END)
        friend_list.delete(0, END)
        display()


def return_book():
    if selected_book.parent_id:
        selected_book.parent_id = None
        session.commit()
        book_list.delete(0, END)
        friend_list.delete(0, END)
        display()
    else:
        messagebox.showerror("Not borrowed", "This book is not borrowed!")


# Make app
app = Tk()
app.title("Book manager")
app.geometry("880x370")

# Book label
book_label = Label(app, text="Books", font="bold")
book_label.grid(row=1, column=0, sticky=W, padx=(20, 0))
# Book list
book_list = Listbox(app, height=14, width=50, exportselection=False)
book_list.grid(row=2, column=0, columnspan=2, rowspan=6, padx=(20, 0))
# Book scrollbar
book_scrollbar = Scrollbar()
book_scrollbar.grid(row=2, column=2, pady=(0, 205))
book_list.configure(yscrollcommand=book_scrollbar.set)
book_scrollbar.configure(command=book_list.yview)

# Bind select
book_list.bind("<<ListboxSelect>>", select_book)

# Friend label
friend_label = Label(app, text="Friends", font="bold")
friend_label.grid(row=1, column=3, sticky=W, padx=(20, 0))
# Friend list
friend_list = Listbox(app, height=14, width=50, exportselection=False)
friend_list.grid(row=2, column=3, columnspan=2, rowspan=6, padx=(20, 0))
# Friend scrollbar
friend_scrollbar = Scrollbar()
friend_scrollbar.grid(row=2, column=5, pady=(0, 205))
friend_list.configure(yscrollcommand=friend_scrollbar.set)
friend_scrollbar.configure(command=friend_list.yview)

xfriend_scrollbar = Scrollbar(app, orient='horizontal')
xfriend_scrollbar.grid(row=8, column=3, padx=(0, 162))
friend_list.configure(xscrollcommand=xfriend_scrollbar.set)
xfriend_scrollbar.configure(command=friend_list.xview)
# Bind select
friend_list.bind("<<ListboxSelect>>", select_friend)

# Add buttons
addB_btn = Button(app, text="Add book", width=10, command=add_book)
addB_btn.grid(row=0, column=0, padx=20, pady=(20, 10))

addF_btn = Button(app, text="Add friend", width=10, command=add_friend)
addF_btn.grid(row=0, column=1, padx=20, pady=(20, 10))

borrow_btn = Button(app, text="Lend a book", width=10, command=borrow)
borrow_btn.grid(row=0, column=3, padx=20, pady=(20, 10))

return_btn = Button(app, text="Return a book", width=10, command=return_book)
return_btn.grid(row=0, column=4, padx=20, pady=(20, 10))

display()

# Run app
app.mainloop()
session.close()
