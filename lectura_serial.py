import serial
import time

filename = "./nombre_de_archivo_a_guardar.txt"

# Asegúrate de usar el puerto y baudrate correctos
ser = serial.Serial('COM15', 115200) 
time.sleep(2) # Espera para la conexión serial

with open(filename , "w") as file:
    while True:
        if ser.in_waiting:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            file.write(line + "\n")
