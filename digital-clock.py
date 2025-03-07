import time

timer = int(input("enter the number "))

for counter in range (timer, 0, -1):
    seconds = counter % 60
    minutes = int(timer / 60) % 60
    hours = int(timer / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(0.5)
print("time's up!!!")
