import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class PatientSchema(UserBase):
    PatientRecordNumber: int
    FirstName: str
    Lastnmae: str
    SSN: str
    DOB: datetime.date
    Gender: str
    Address: str
    PhysicianID: int
    InsuranceID: int

    class Config:
        from_attributes = True