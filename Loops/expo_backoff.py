import time

wait_time=1
max_retries=6
attemps=0

while attemps<max_retries:
    print("Attempts",attemps,+ 1,"-wait time",wait_time,)
    time.sleep(wait_time)
    wait_time *=2
    attemps+=1