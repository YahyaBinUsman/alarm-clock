import datetime
import time
import winsound  # This module is Windows-specific

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            # Play a sound (Windows only)
            winsound.Beep(1000, 10000)
            break
        time.sleep(1)

def main():
    print("Welcome to the Alarm Clock!")

    # Get the alarm time from the user
    alarm_hour = input("Enter the hour (24-hour format): ")
    alarm_minute = input("Enter the minute: ")

    alarm_time = "{}:{}:00".format(alarm_hour.zfill(2), alarm_minute.zfill(2))

    print("Alarm set for {}".format(alarm_time))

    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
