# -*- coding: utf-8 -*-
"""
Created on Sat Dec  15:59:31 2021

@author: jorge
"""

import serial
import json
import time
from ftplib import FTP

#Define FTP client params
ip = '155.210.150.77'
user = 'rsense'
password = 'rsense'
fileName = "sensor_data.json"
#Connect to FTP server
ftp = FTP(ip, user, password)


def uploadFTP(filename):
    try:
        with open(filename, "rb") as file:
            ftp.storbinary("STOR "+filename, file)
    except Exception as e:
        pass

#Turn into senml standart
def addToDic(humidity, temperature):
    measure = {}
    measure['Sensor_Data'] = []
    temp = {"n":"temperature", "u":"Celsius", "v": temperature}
    hum = {"n":"humidity", "u":"%", "v": humidity}
    measure['Sensor_Data'].append(temp)
    measure['Sensor_Data'].append(hum)

    return measure
    
def main():
    ser = serial.Serial("COM4", 115200)
    axisX=[]
    previous_t = time.time()
    while True:
        cc=str(ser.readline(),'utf-8')
        current_t = time.time()
        total_t = current_t - previous_t
        #waits for 10 seconds
        if (total_t >= 10):
            #print(cc)
            cc = cc.rstrip()
            th_data = cc.split(';')
            collected_data = addToDic(th_data[0], th_data[1])
            print(collected_data)
            #print(len(collected_data['Sensor_Data']))
            with open('sensor_data.json', 'w') as f:
                json.dump(collected_data, f)
            uploadFTP(fileName)
            previous_t = time.time()

if __name__ == '__main__':
    main()
