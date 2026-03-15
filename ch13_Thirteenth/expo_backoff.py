import time
wait_time = 1
max_tries = 5
attempts =1

while attempts<= max_tries:
    input("Enter input ")
    print("Attempts",attempts,"-wait time",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1