from sqlalchemy import Column
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Hospital(ModelBase):
    __tablename__ = "hospital"
    HospitalID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    FullName = Column(pg.VARCHAR)
    StreetNumber = Column(pg.SMALLINT)
    StreetName = Column(pg.VARCHAR)
    City = Column(pg.VARCHAR)
    State = Column(pg.VARCHAR)
    ZipCode = Column(pg.BIGINT)
    HospitalPhoneNumber = Column(pg.VARCHAR)