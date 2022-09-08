import serial
import pyqtgraph as pg

ser = serial.Serial("COM3", 115200)
axisX=[]
while True:
    cc=str(ser.readline(),'utf-8')
    try:
        f=open("C:/Users/jorge/Desktop/Universidad/Master/Redes de Sensores/Toma de datos/"+"Datos1", "a")
        f.write(cc)
    except:
        pass