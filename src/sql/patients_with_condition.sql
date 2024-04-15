SELECT patient_id , patient_name , conditions
FROM patients
WHERE conditions REGEXP ".* DIAB1.*" OR conditions REGEXP "^DIAB1.*";