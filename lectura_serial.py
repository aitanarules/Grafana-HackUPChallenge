import serial
import time

filename = "./brightness.txt"

# serial port name , fastness in baudios
serial = serial.Serial('COM15', 115200) 
# wait for the serial connection
time.sleep(2)

with open(filename , "w") as file:
    while True:
        if serial.in_waiting:
            line = serial.readline().decode('utf-8').rstrip()
            print(line)
            file.write(line + "\n")
