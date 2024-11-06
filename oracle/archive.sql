-- View if the FRA is enabled(Directory structure)
show parameter DB_RECOVERY_FILE_DEST 

-- Verify if is operating in archive long
ARCHIVE LOG LIST 
SELECT LOG_MODE FROM V$DATABASE; 

-- View Directory of redo log file
show parameter LOG_ARCHIVE_DEST

-- View if OMF is enabled(Random name)
show parameter DB_CREATE_FILE_DEST 


-- To change to archive mode
SHUTDOWN IMMEDIATE 
STARTUP MOUNT
ALTER DATABASE ARCHIVELOG; 
ALTER DATABASE OPEN ;

-- View if its enabled
ARCHIVE LOG LIST

-- Will rotate the Logfile
ALTER SYSTEM SWITCH LOGFILE; 


-- View Generated Log archive
SELECT NAME FROM V$ARCHIVED_LOG; 
