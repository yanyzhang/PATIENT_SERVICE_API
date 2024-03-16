import datetime
import uuid
from sqlalchemy import Column, ForeignKey, Date
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
from lib.models.department import Department
from sqlalchemy.orm import mapped_column, relationship
import sqlalchemy.dialects.postgresql as pg

class Employee(ModelBase):
    __tablename__ = "employee"
    EmployeeID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    Firstname = Column(pg.VARCHAR)
    MiddleName = Column(pg.VARCHAR)
    Lastname = Column(pg.VARCHAR)
    Gender = Column(pg.VARCHAR)
    Ssn = Column(pg.VARCHAR, nullable=False)
    HireDate = Column(pg.DATE)
    DOB = Column(pg.DATE)
    Title = Column(pg.VARCHAR)
    Level = Column(pg.VARCHAR)
    DepartmentID = mapped_column(pg.BIGINT, ForeignKey(Department.DepartmentID), nullable=False)
    DepartmentName = mapped_column(pg.VARCHAR, ForeignKey(Department.DepartmentName), nullable=False)
    Salary = Column(pg.decimal(9,2))
    Bonus = Column(pg.decimal(9,2))
    StreetNumber = Column(pg.SMALLINT)
    StreetName = Column(pg.VARCHAR)
    City = Column(pg.VARCHAR)
    State = Column(pg.VARCHAR)
    ZipCode = Column(pg.BIGINT)
    EmployeePhoneNumber = Column(pg.VARCHAR)

# relationship
    # physician = relationship("Physician", foreign_keys=[PhysicianID])
    department = relationship("Department", foreign_keys=[DepartmentID])
    department = relationship("Department", foreign_keys=[DepartmentName])