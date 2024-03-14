-- "PhysicianID" BIGINT NOT NULL,
-- "PatientRecordNumber" BIGINT NOT NULL,
-- "MedicationID" BIGINT NOT NULL,
-- "AppointmentID" BIGINT NOT NULL,

--ALTER TABLE A ADD CONSTRAINT fk_b FOREIGN KEY (b_id) references b(id) 
-- ADD CONSTRAINT [FK_ Analog AllItems] FOREIGN KEY([item Id]) REFERENCES [All Items] ([id])

-- fk_b: Name of the foreign key constraint, must be unique to the database
-- b_id: Name of column in Table A you are creating the foreign key relationship on
--b: Name of table, in this case b
--id: Name of column in Table B

ALTER TABLE "prescription"
ADD CONSTRAINT fk_physician FOREIGN KEY ("PhysicianID") REFERENCES physician ("PhysicianID");
ALTER TABLE "prescription"
ADD CONSTRAINT fk_patient_record_number FOREIGN KEY ("PatientRecordNumber") REFERENCES patient ("PatientRecordNumber");
ALTER TABLE "prescription"
ADD CONSTRAINT fk_medication FOREIGN KEY ("MedicationID") REFERENCES medication ("MedicationID");
ALTER TABLE "prescription"
ADD CONSTRAINT fk_appointment FOREIGN KEY ("AppointmentID") REFERENCES appointment ("AppointmentID");

--adding CONSTRAINT for manager --
--ALTER TABLE "manager"
--ADD CONSTRAINT fk_departmentid FOREIGN KEY ("DepartmentID") REFERENCES department ("DepartmentID");
--ALTER TABLE "manager"
--ADD CONSTRAINT fk_department_name FOREIGN KEY ("DepartmentID") REFERENCES department ("DepartmentName");
--ALTER TABLE "manager"
--ADD CONSTRAINT fk_room_id FOREIGN KEY ("RoomID") REFERENCES room ("RoomID");
