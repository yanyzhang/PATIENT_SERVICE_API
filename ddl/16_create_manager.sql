-- creating manager table 
CREATE TABLE IF NOT EXISTS Public."manager" (
    "ManagerID" INT NOT NULL,
    "DepartmentID" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,  --reference to name of department
    "RoomID" CHARACTER VARYING COLLATE pg_catalog."default", --reference to roomID of the room table
    -- TODO: // add encryption
    "EmployeePhoneNumber" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL -- reference to employee id phone number
    CONSTRAINT mananger_pkey PRIMARY KEY ("ManagerID")
)