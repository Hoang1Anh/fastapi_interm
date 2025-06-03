from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    quantity = Column(Integer)

    borrowed_books = relationship("BorrowedBook", back_populates="book")


class BorrowedBook(Base):
    __tablename__ = "borrowed_books"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    borrowed_date = Column(Date)
    return_date = Column(Date)

    book = relationship("Book", back_populates="borrowed_books")
    student = relationship("Student", back_populates="borrowed_books")
