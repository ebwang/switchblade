#View status of database
SELECT NAME, OPEN_MODE FROM V$DATABASE;

#Get user session
SELECT SID, SERIAL#, STATUS FROM V$SESSION WHERE USERNAME='SYSTEM'; 