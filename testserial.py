import serial
import time
from datetime import datetime

port = 'COM5'
baudrate = 115200
ser = serial.Serial(port, baudrate)
time.sleep(2)  

while True:
    line = ser.readline().decode('utf-8').rstrip()

    if not line:
        continue

    filename_part = line.replace(" ", "-")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"{filename_part}_{timestamp}.txt"

    with open(filename, 'w') as f:
        f.write(line)

    time.sleep(0.1)  
