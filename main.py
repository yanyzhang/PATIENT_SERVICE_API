# app.py to print a message 
'''
Author: Yan
Purpose:
Date:


'''

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return [
        {
            "firstName": "Yan",
            "lastName": "Zhang",
            "email": "yanyzhang1@gmail.com"
        }

    ]


