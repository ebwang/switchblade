#Verify AMM is enabled. (AMM is used only in system with 4gb of ram below)
SHOW PARAMETER MEMORY_TARGET 
SHOW PARAMETER MEMORY_MAX_TARGET 

#View the area size of the DATABASE
col COMPONENT format a22 
SELECT COMPONENT, CURRENT_SIZE/1024/1024 CURRENT_SIZE_MB, 
USER_SPECIFIED_SIZE/1024/1024 USER_SPECIFIED_MB 
FROM V$MEMORY_DYNAMIC_COMPONENTS WHERE CURRENT_SIZE<>0;


#Get memory advisor of the database
set linesize 180 
SELECT * FROM V$MEMORY_TARGET_ADVICE ORDER BY MEMORY_SIZE; 


DB memory = %70 of total memory = 70% * 5.6 ≈ 3.9 G 
SGA size = %60 * total db memory size = 0.6 * 3.9 ≈ 2.352 G ≈ 2408M 
PGA size = %40 * total db memory size = 0.4 * 3.9 ≈ 1.5 G ≈ 1500M 


#Query the ASMM(RECOMMENDED) target advisor and determine the optimize SGA size. 
#We normally query this advisor after the database is under normal stress for long time. Because 
#our database has no stress, the advisor cannot estimate any performance gain from changing the 
#SGA_TARGET size. 
SELECT SGA_SIZE, SGA_SIZE_FACTOR, ESTD_DB_TIME, ESTD_DB_TIME_FACTOR FROM 
V$SGA_TARGET_ADVICE ORDER BY SGA_SIZE; 
