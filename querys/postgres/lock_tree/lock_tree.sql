-- Arvore de locks
select pid, usename, state,
    age(query_start, clock_timestamp()),
    pg_blocking_pids(pid) as blocked_by,
    query
from pg_stat_activity 
    where cardinality(pg_blocking_pids(pid)) >=0
    and state <> 'idle'
    order by age(query_start, clock_timestamp());