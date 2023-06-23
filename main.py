import datetime
import pyttsx3
import os
import webbrowser
engine = pyttsx3.init()

current_time = datetime.datetime.now()

print(current_time.strftime('%I:%M %p'))

set_hour = int(input("Enter hour in 12-hour format: "))
set_minute = int(input("Enter minutes: "))

while True:
    current_time = datetime.datetime.now()
    current_hour = current_time.strftime('%I')
    current_minute = current_time.strftime('%M')

    if int(current_hour) == set_hour and int(current_minute) == set_minute:
        break

engine.say("wakeup wakeup")
engine.runAndWait()

