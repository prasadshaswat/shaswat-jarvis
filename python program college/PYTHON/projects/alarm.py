import time

def alarm():
    alarm_time = input("Enter the time for the alarm in format HH:MM:SS\n")
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake Up!")
            break
        else:
            print("The time is", current_time)
            time.sleep(1)
if __name__ == '__main__':
    alarm()