from sqlalchemy import Column, Date, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    full_name = Column(String, nullable=False)
    dob = Column(Date)
    email = Column(String, unique=True)
    phone = Column(String)
    class_id = Column(Integer, ForeignKey("classes.id"))

    class_ = relationship("Class", back_populates="students")
    payments = relationship("Payment", back_populates="student")
    borrowed_books = relationship("BorrowedBook", back_populates="student")
