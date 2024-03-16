from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
from lib.models.employee import Employee
from lib.models.department import Department
from lib.models.room import Room
from sqlalchemy.orm import mapped_column, relationship
import sqlalchemy.dialects.postgresql as pg

class Manager(ModelBase):
    __tablename__ = "manager"
    ManagerID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    Firstname = Column(pg.VARCHAR)
    Lastname = Column(pg.VARCHAR)
    MiddleName = Column(pg.VARCHAR)
    EmployeeID = mapped_column(pg.BIGINT, ForeignKey(Employee.EmployeeID), nullable=False)
    DepartmentID = mapped_column(pg.BIGINT, ForeignKey(Department.DepartmentID), nullable=False)
    DepartmentName = mapped_column(pg.VARCHAR, ForeignKey(Department.DepartmentName), nullable=False)
    RoomID = mapped_column(pg.SMALLINT, ForeignKey(Room.RoomID), nullable=False)


# relationship 
    employee = relationship("Employee", foreign_keys=[DepartmentID])
    department = relationship("Department", foreign_keys=[DepartmentID])
    department = relationship("Department", foreign_keys=[DepartmentName])
    room = relationship("Room", foreign_keys=[RoomID])