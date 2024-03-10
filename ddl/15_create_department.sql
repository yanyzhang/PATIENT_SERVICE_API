--creating department List TABLE
CREATE TABLE IF NOT EXISTS Public."department" (
    "DepartmentID" INT NOT NULL,
    "NameOfDepartment" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "HeadID" CHARACTER VARYING COLLATE pg_catalog."default", --reference to employeedid of the table physician
    -- TODO: // add encryption
    "DepartmentPhoneNumber" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL
    CONSTRAINT department_pkey PRIMARY KEY ("DepartmentID")

)