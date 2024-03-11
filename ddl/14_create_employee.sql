--creating emmployee information TABLE
CREATE TABLE IF NOT EXISTS Public."employee" (
    "EmployeeID" BIGINT NOT NULL GENERATED BY DEFAULT AS IDENTITY (
        INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 9223372036854775807 CACHE 1
    ),
    "FirstName" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "MiddleName" CHARACTER VARYING COLLATE pg_catalog."default",
    "LastName" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "Gender" CHARACTER VARYING COLLATE pg_catalog."default",
    "HiredDate" DATE,
    "Birthday" DATE,
    "Title" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "Department" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "Salary" DECIMAL(9, 2),
    "Bonus" DECIMAL(9, 2),
    "StreetNumber" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "StreetName" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "City" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "State" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL,
    "ZipCode" INT,
    -- TODO: // add encryption
    "EmployeePhoneNumber" CHARACTER VARYING COLLATE pg_catalog."default" NOT NULL
    CONSTRAINT employee_pkey PRIMARY KEY ("EmployeeID")
)