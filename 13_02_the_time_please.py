# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

from datetime import datetime

now = datetime.now()

time_now = now.strftime("%H:%M:%S")
print("the time now is:", time_now)
