from sqlalchemy import Column, Integer, ForeignKey, String, Time, Date
from sqlalchemy.orm import relationship
from app.database import Base

class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    class_id = Column(Integer, ForeignKey("classes.id"))
    day = Column(String)  # e.g. "Monday"
    time_start = Column(Time)
    time_end = Column(Time)

    course = relationship("Course", back_populates="schedules")