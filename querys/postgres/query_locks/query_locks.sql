-- Arvore de locks
select pid, usename, state,
    age(query_start, clock_timestamp()),
    pg_blocking_pids(pid) as blocked_by,
    query
from pg_stat_activity 
    where cardinality(pg_blocking_pids(pid)) >=0
    and state <> 'idle'
    order by age(query_start, clock_timestamp());
    
-- Com tempo de lock
SELECT
  COALESCE(blockingl.relation::regclass::text,blockingl.locktype) as locked_item,
  now() - blockeda.query_start AS waiting_duration, blockeda.pid AS blocked_pid,
  blockeda.query as blocked_query, blockedl.mode as blocked_mode,
  blockinga.pid AS blocking_pid, blockinga.query as blocking_query,
  blockingl.mode as blocking_mode
FROM pg_catalog.pg_locks blockedl
JOIN pg_stat_activity blockeda ON blockedl.pid = blockeda.pid
JOIN pg_catalog.pg_locks blockingl ON(
  ( (blockingl.transactionid=blockedl.transactionid) OR
  (blockingl.relation=blockedl.relation AND blockingl.locktype=blockedl.locktype)
  ) AND blockedl.pid != blockingl.pid)
JOIN pg_stat_activity blockinga ON blockingl.pid = blockinga.pid
  AND blockinga.datid = blockeda.datid
WHERE NOT blockedl.granted -- retirar o NOT
AND blockinga.datname = current_database() order by 2;

-- Locks especificando a tabela
SELECT locktype, mode, granted, pid, pg_blocking_pids(pid) AS wait_for
FROM pg_locks WHERE relation = 'testetb'::regclass
order by 5;    
    
   