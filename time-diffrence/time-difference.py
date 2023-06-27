import time
start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")
#Wait for user to stop timer
input("Press 'Enter' to stop timer ")
stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)
print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")