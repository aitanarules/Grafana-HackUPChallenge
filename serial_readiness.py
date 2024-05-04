import random
def other_sensor():
    return random.random()

import serial
import time
import pandas as pd
import datetime as dt

filename_csv = './datacsv.csv'

# serial port, fastness
# ser = serial.Serial(port="COM11", baudrate=115200, timeout=.1) 
# time.sleep(2) 

dic = {'date':[], 'time':[] ,'light':[], 'other':[]}

while True:
    current_dateTime = dt.datetime.now()
    current_time = f'{current_dateTime.hour}:{current_dateTime.minute}:{current_dateTime.second}'
    current_date = f'{current_dateTime.day}-{current_dateTime.month}-{current_dateTime.year}'
            
    if if serial.in_waiting>0:
        light = serial.readline()
        dic['light'].append(light)
    else:
        dic['light'].append(-1)


    if other_sensor()
        other = other_sensor()
        dic['other'].append(other)
    else:
        dic['other'].append(-1)

    dic['date'].append(f'{current_dateTime.day}-{current_dateTime.month}-{current_dateTime.year}')
    dic['time'].append(current_date)

    df = pd.DataFrame(dic)
    df.to_csv(filename_csv, index=False)
        
    
    
            
