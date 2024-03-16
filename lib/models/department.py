from sqlalchemy import Column
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Department(ModelBase):
    __tablename__ = "department"
    DepartmentID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    DepartmentName = Column(pg.VARCHAR)
    HeadOfDepartmentID = Column(pg.VARCHAR) #relasshionship
    DepartmentPhoneNumber = Column(pg.VARCHAR, nullable=False)