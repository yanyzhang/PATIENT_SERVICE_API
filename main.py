# app.py to print a message 
'''
Author: Yan
contact: yanyzhang1@gmail.com
Copyright: Copyright 2024"
Status: "Development"
Version: "0.0.1"


'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/patients/:PatientRecordNumber")
async def get_patients() -> list(PatientSchema):
    db_session = SessionMaker().get_session_maker()
    with db_session.begin() as session:
        patients= session.query(Patient).all()
        
        return patients


