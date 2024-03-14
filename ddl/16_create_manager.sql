-- Active: 1709770213394@@127.0.0.1@5432@postgres@public
-- creating manager table 
CREATE TABLE IF NOT EXISTS Public."manager" (
    "ManagerID" INT NOT NULL,
    "FirstName" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "MiddleName" CHARACTER VARYING COLLATE pg_catalog."default",
    "LastName" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "DepartmentID" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,  --reference to name of department
    "DepartmentName" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "RoomID" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL, --reference to roomID of the room table
    "RoomPhoneNumber" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "EmployeePhoneNumber" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL, -- reference to employee id phone number
    CONSTRAINT manager_pkey PRIMARY KEY ("ManagerID")
)

