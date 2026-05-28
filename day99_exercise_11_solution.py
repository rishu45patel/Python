
import os
import time

REPEAT_INTERVAL=12#repeat frequency in seconds

while True:
    command="osascript -e\'say\hey harry drink water\"\'; osascript -e\'display alert\"hey harry,drink water\"\'"
    os.system(command)
    time.sleep(REPEAT_INTERVAL)




























