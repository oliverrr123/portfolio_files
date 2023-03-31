import serial
import time
from datetime import datetime

arduinoData = serial.Serial("com3", 9600)

while True:
    txt = datetime.now().strftime("%H:%M:%S")
    txt += '\r'
    arduinoData.write(txt.encode())
    time.sleep(0.5)