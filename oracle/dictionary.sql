#view tables space of each TABLE
select table_name, tablespace_name from user_tables order by 1

#view all sequences 
select sequence_name, min_value, max_value, increment_by from all_sequences