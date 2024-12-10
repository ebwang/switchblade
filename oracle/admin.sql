-- REPORT ALL DATABASE SCHEMA
REPORT SCHEMA;

-- Close PDB
ALTER PLUGGABLE DATABASE pdb1 CLOSE IMMEDIATE; 

----------------------------------------------------------------------------------------
#List PDBS
SELECT NAME, OPEN_MODE FROM V$PDBS ORDER BY 1; 

----------------------------------------------------------------------------------------
#Start PDB
ALTER PLUGGABLE DATABASE pdb1 OPEN; 
STARTUP PLUGGABLE DATABASE pdb1;
STARTUP PLUGGABLE DATABASE hr;

----------------------------------------------------------------------------------------
#Alter Session
ALTER SESSION SET CONTAINER=PDB; 
ALTER SESSION SET CONTAINER=CDB$ROOT; 

sqlplus HR/ABcd##1234@NTB-WANG:1539/PDB
----------------------------------------------------------------------------------------
#View parameter is modifable in PDB
SELECT VALUE, VALUE/1024/1024/1024 GB, ISPDB_MODIFIABLE 
FROM   
V$SYSTEM_PARAMETER 
WHERE  NAME='db_recovery_file_dest_size'; 

----------------------------------------------------------------------------------------
#ALTER PARAMETER IN CDB$ROOT
ALTER SESSION SET CONTAINER=CDB$ROOT; 
ALTER SYSTEM SET DB_RECOVERY_FILE_DEST_SIZE = 10903094248 SCOPE=BOTH;

----------------------------------------------------------------------------------------
#View if a parameter in PDB is modifiable
col VALUE for a10 
SELECT VALUE, ISPDB_MODIFIABLE 
FROM V$SYSTEM_PARAMETER 
WHERE NAME='ddl_lock_timeout'; 

----------------------------------------------------------------------------------------
#Modify a parameter in PDB
ALTER SESSION SET CONTAINER=PDB1; 
ALTER SYSTEM SET DDL_LOCK_TIMEOUT = 12;

----------------------------------------------------------------------------------------
#Create PDB
CREATE PLUGGABLE DATABASE pdb_test  
ADMIN USER pdbtestadmin IDENTIFIED BY ABcd##1234; 
ALTER PLUGGABLE DATABASE pdb_test OPEN;

----------------------------------------------------------------------------------------

CREATE PLUGGABLE DATABASE HR ADMIN USER dba IDENTIFIED BY ABcd##1234; 
ALTER PLUGGABLE DATABASE HR OPEN;

----------------------------------------------------------------------------------------
#Put in restrict mode
ALTER PLUGGABLE DATABASE pdb_test CLOSE IMMEDIATE; 
ALTER PLUGGABLE DATABASE pdb_test OPEN RESTRICTED; 
SELECT CON_ID, OPEN_MODE, RESTRICTED FROM V$PDBS WHERE NAME='PDB_TEST';

----------------------------------------------------------------------------------------
#Rename a PDB
ALTER SESSION SET CONTAINER=PDB_TEST; 
ALTER PLUGGABLE DATABASE pdb_test RENAME GLOBAL_NAME to pdb2; 
SELECT CON_ID, OPEN_MODE, RESTRICTED FROM V$PDBS WHERE NAME='PDB2'; 
ALTER PLUGGABLE DATABASE pdb2 CLOSE IMMEDIATE; 
ALTER PLUGGABLE DATABASE pdb2 OPEN; 
SELECT CON_ID, OPEN_MODE, RESTRICTED FROM V$PDBS WHERE NAME='PDB2'; 

----------------------------------------------------------------------------------------
#Drop database including DATAFILES
ALTER PLUGGABLE DATABASE pdb2 CLOSE IMMEDIATE; 
DROP PLUGGABLE DATABASE pdb2 INCLUDING DATAFILES;

--- TO OPEN PDB EVERY TIME THE CDB OPEN

ALTER PLUGGABLE DATABASE hr SAVE STATE;

----------------------------------------------------------------------------------------
#View Con_ID and PDBS NAMES
SELECT CON_ID, NAME FROM V$CONTAINERS;

----------------------------------------------------------------------------------------
#View PDB_ID 
SELECT PDB_ID, PDB_NAME NAME FROM CDB_PDBS; 

----------------------------------------------------------------------------------------
#View Properties of PDB
set linesize 180 
col PROPERTY_NAME for a35 
col PROPERTY_VALUE for a35 
SELECT PROPERTY_NAME, PROPERTY_VALUE FROM CDB_PROPERTIES WHERE CON_ID=3;

----------------------------------------------------------------------------------------
--Retrieve datafiles of entire database including PDB
COL PDB_ID FOR 999 
COL PDB_NAME FOR A8 
COL FILE_ID FOR 9999 
COL TABLESPACE_NAME FOR A10 
COL FILE_NAME FOR A45 
 
SELECT p.CON_ID, p.NAME PDB_NAME, d.FILE_ID, d.TABLESPACE_NAME, d.FILE_NAME 
  FROM V$CONTAINERS p, CDB_DATA_FILES d 
  WHERE p.CON_ID = d.CON_ID 
ORDER BY p.CON_ID; 

----------------------------------------------------------------------------------------
--To run a script of creation of DATABASE
conn / as sysdba 
ALTER SESSION SET CONTAINER=PDB; 
@ $ORACLE_HOME/demo/schema/human_resources/hr_main.sql 

----------------------------------------------------------------------------------------
-- Retrieve the tables owned by the HR user in PDB
col TABLE_NAME for a25  
SELECT CON_ID, T.TABLE_NAME  
FROM CDB_TABLES T  
WHERE T.OWNER='HR'  
ORDER BY T.TABLE_NAME;

----------------------------------------------------------------------------------------
--Retrieve the tables owned by OWNER HR in entires PDBS
set linesize 180 
COL PDB_NAME FOR A15 
COL OWNER FOR A15 
COL TABLE_NAME FOR A30 
SELECT P.PDB_ID, T.OWNER, P.PDB_NAME, T.TABLE_NAME  
  FROM DBA_PDBS P, CDB_TABLES T  
  WHERE P.PDB_ID > 2 AND 
        P.PDB_ID = T.CON_ID AND 
        T.OWNER='HR' 
ORDER BY P.PDB_ID, T.OWNER; 

----------------------------------------------------------------------------------------
-- View installed components in DATABASE
set linesize 180 
col COMP_NAME for a40 
col STATUS for a15 
col VERSION for a10 
SELECT COMP_NAME, STATUS, VERSION FROM DBA_REGISTRY ORDER BY 1;

-- Display Control Files
show parameter CONTROL_FILES 


-- View datafiles from a pdb

select name from V$datafile where con_id=(select con_id from v$PDBS where name='HR');