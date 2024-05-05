import serial
import time
import pandas as pd
import datetime as dt

filename_csv = './Muestras_de_datos/data.csv'

# Iniciamos la comunicación por el puerto por el que el ESP32 nos envía los datos
ser = serial.Serial(port="COM11", baudrate=115200, timeout=.1)

# Dejamos 2 segundos para que haya tiempo suficiente para conectarse con el puerto serie elegido
time.sleep(2) 

# Se crea la tabla de datos
dic = {'date':[], 'time':[] ,'light':[]}

while True:
    # Obtenemos la hora actual y se guarda con el formato de dd/mm/yyyy
    current_dateTime = dt.datetime.now()
    current_time = f'{current_dateTime.hour:02d}:{current_dateTime.minute:02d}:{current_dateTime.second:02d}:{current_dateTime.microsecond:02d}'
    current_date = f'{current_dateTime.day}-{current_dateTime.month}-{current_dateTime.year}'
            
    if (ser.in_waiting > 0):
        # Si nos llega nueva información al puerto, lo agregamos a la lista "light"
        light = ser.readline().decode('utf-8').rstrip()
        dic['light'].append(light)
    else:
        # Si no, añadimos un "-1", sabiendo que en esa posición hemos tenido un error
        dic['light'].append(-1)

    # Se agregan los datos adicionales (fecha y tiempo)
    dic['date'].append(current_date)
    dic['time'].append(current_time)

    # Generar un objeto "DataFrame" (modelo de dato que permite una maniobrabilidad más sencilla con documentos .csv)
    df = pd.DataFrame(dic)
    df.to_csv(filename_csv, index=False)