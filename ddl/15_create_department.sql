--creating department List TABLE
CREATE TABLE IF NOT EXISTS Public."department" (
    "DepartmentID" INT NOT NULL,
    "DepartmentName" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "DepartmentHeadID" CHARACTER VARYING COLLATE pg_catalog."default", --reference to employeedid of the table physician
    "DepartmentPhoneNumber" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT department_pkey PRIMARY KEY ("DepartmentID")
)