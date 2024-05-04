import serial
import time
import pandas as pd
import datetime as dt


filename = "./datatxt.txt"
filename_csv = './datacsv.csv'

# serial port, fastness
ser = serial.Serial(port="COM11", baudrate=115200, timeout=.1) 
time.sleep(2) 

while True:
    with open(filename , "a+") as file:
        # current_date = str(dt.datetime.now())
        if ser.in_waiting > 0:
            line = ser.readline().decode()
            print(line)
            if file:
                df = pd.read_fwf(filename)
                df.to_csv(filename_csv, index=False)
            # if line:
                # file.write(current_date + "'" + line)
            file.write(line)
            file.close()
    
    
            
