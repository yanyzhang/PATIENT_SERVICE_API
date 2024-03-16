from sqlalchemy import Column
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Room(ModelBase):
    __tablename__ = "room"
    _RoomType = pg.Enum('surgery', 'ICU', 'maternity', 'mental_health', 'office') 
    RoomID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    RoomType = Column(_RoomType, nullable=False)
    Available = Column(pg.BOOLEAN, nullable=False) 
    RoomPhoneNumber = Column(pg.VARCHAR)