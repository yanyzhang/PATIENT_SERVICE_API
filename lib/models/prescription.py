import datetime
import uuid
from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
from lib.models.physician import Physician
from lib.models.patient import Patient
from lib.models.medication import Medication
from lib.models.appointment import Appointment
from sqlalchemy.orm import mapped_column, relationship
import sqlalchemy.dialects.postgresql as pg

class Prescription(ModelBase):
    __tablename__ = "prescription"
    PrescriptionID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    PhysicianID = mapped_column(pg.BIGINT,  ForeignKey(Physician.PhysicianID), nullable=False)
    PatientRecordNumber = mapped_column(pg.BIGINT, ForeignKey(Patient.PatientRecordNumber), nullable=False)
    MedicationID = mapped_column(pg.BIGINT, ForeignKey(Medication.MedicationID), nullable=False)
    PrescribedOn = Column(pg.TIMESTAMP)
    AppointmentID = mapped_column(pg.BIGINT, ForeignKey(Appointment.AppointmentID), nullable=False)
    Dosage = Column(pg.SMALLINT, nullable=False)


# relationships
    physician = relationship("Physician", foreign_keys=[PhysicianID])
    patient = relationship("Patients", foreign_keys=[PatientRecordNumber])
    medication = relationship("Medicaiton", foreign_keys=[MedicationID])
    appointment = relationship("Appointment", foreign_keys=[AppointmentID])