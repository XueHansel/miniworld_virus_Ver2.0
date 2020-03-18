import os
import time
while(1):
    try:
        os.system('taskkill /F /IM MicroMiniNew.exe /T')
        time.sleep(1)
    except:
        continue