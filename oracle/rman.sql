-- Invoke rman
rman target /

-- show all configration
show all;

-- This configuration will generate the bkp of control-file and spfile
CONFIGURE CONTROLFILE AUTOBACKUP ON;

-- View if is enabled
SHOW CONTROLFILE AUTOBACKUP;


-- Start rman BACKUP
backup database;


-- As a image copy
BACKUP AS COPY DATABASE;


-- List image copy
LIST COPY OF DATABASE; 

-- Display the backupset
list backupset;

-- obtain information about how much percentage is taken by the backup files from the fast recovery area
-- INSIDE RMAN TOOL

SELECT FILE_TYPE, PERCENT_SPACE_USED FROM V$RECOVERY_AREA_USAGE WHERE 
PERCENT_SPACE_USED<>0 ORDER BY PERCENT_SPACE_USED DESC;

-- Delete Backup
DELETE BACKUPSET 

-- OR

DELETE BACKUPSET OF DATABASE; 

--Will backup archive redo, log backup and control file in auto-backup
BACKUP DATABASE PLUS ARCHIVELOG; 

-- View archive log files included in the backup
SELECT NAME, SEQUENCE# FROM V$ARCHIVED_LOG ORDER BY 2; 

-- Put a backup in a different LOCATIONS
BACKUP DATABASE FORMAT '/u01/app/oracle/bkp/ORADB%U.bck'; 

-- You can backup a copy of the controlefile in a different location
BACKUP CURRENT CONTROLFILE FORMAT '/media/sf_staging/control01.bk'; 
BACKUP AS COPY CURRENT CONTROLFILE FORMAT '/media/sf_staging/control01.ctl'; 


-- To DELETE
LIST BACKUP OF CONTROLFILE; 
LIST COPY OF CONTROLFILE;

-- BKP table space users
BACKUP TABLESPACE users FORMAT '/u01/app/oracle/bkp/users_%U.bck';

-- List BACKUPSER of TABLESPACE users
LIST BACKUPSET OF TABLESPACE users;

LIST BACKUP OF CONTROLFILE; 

-- Obtain the full name of the users datafile.
COLUMN datafile_name FORMAT A50
COLUMN owner_username FORMAT A20

SELECT d.NAME AS datafile_name, u.USERNAME AS owner_username
FROM v$DATAFILE d
JOIN V$TABLESPACE ts ON d.TS# = ts.TS#
JOIN DBA_USERS u ON ts.NAME = u.DEFAULT_TABLESPACE
WHERE ts.NAME = 'USERS';

-- By default, Oracle deletes the entries from the control file that are older than 7 days. If 
-- your recovery window is longer than this period, you have to increase the value of 
-- CONTROL_FILE_RECORD_KEEP_TIME parameter to accommodate your recovery target.

sqlplus / as sysdba 
SHOW PARAMETER CONTROL_FILE_RECORD_KEEP_TIME 
ALTER SYSTEM SET CONTROL_FILE_RECORD_KEEP_TIME=60 SCOPE=BOTH; 