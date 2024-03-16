import datetime
import uuid
from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.physician import Physician
from lib.models.nurse import Nurse
from lib.models.patient import Patient
from lib.models.room import Room
from sqlalchemy.orm import mapped_column, relationship
import sqlalchemy.dialects.postgresql as pg

class Appointment(ModelBase):
    __tablename__ = "appointment"
    AppointmentID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    PatientRecordNumber = mapped_column(pg.BIGINT, ForeignKey(Patient.PatientRecordNumber), nullable=False)
    NurseID = mapped_column(pg.BIGINT, ForeignKey(Nurse.NurseID), nullable=False)
    PhysicianID = mapped_column(pg.BIGINT,  ForeignKey(Physician.PhysicianID), nullable=False)
    StartDateTime = Column(pg.TIMESTAMP)
    EndDateTime = Column(pg.TIMESTAMP)
    RoomID = mapped_column(pg.BIGINT, ForeignKey(Room.RoomID), nullable=False)

    # relationships
    physician = relationship("Physician", foreign_keys=[PhysicianID])
    patient = relationship("Patients", foreign_keys=[PatientRecordNumber])
    nurse = relationship("Nurse", foreign_keys=[NurseID])
    room = relationship("Room", foreign_keys=[RoomID])