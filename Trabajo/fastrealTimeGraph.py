import time
import random
import pyqtgraph as pg
from collections import deque
from pyqtgraph.Qt import QtGui, QtCore
import serial

ser = serial.Serial("COM4", 115200)
singleD = []
handle = 0

class Graph:
    def __init__(self, ):

        self.dat1 = deque()
        self.dat2 = deque()
        self.dat3 = deque()

        self.dat4 = deque()
        self.dat5 = deque()
        self.dat6 = deque()

        self.maxLen = 200#max number of data points to show on graph
        self.app = QtGui.QApplication([])
        self.win = pg.GraphicsWindow()
        """
        self.p1 = self.win.addPlot(colspan=2)
        self.win.nextRow()
        self.p2 = self.win.addPlot(colspan=2)
        self.win.nextRow()
        self.p3 = self.win.addPlot(colspan=2)
        """
        self.p4 = self.win.addPlot(colspan=2)
        self.win.nextRow()
        self.p5 = self.win.addPlot(colspan=2)
        self.win.nextRow()
        self.p6 = self.win.addPlot(colspan=2)
        """
        self.curve1 = self.p1.plot()
        self.curve2 = self.p2.plot()
        self.curve3 = self.p3.plot()
        """
        self.curve4 = self.p4.plot()
        self.curve5 = self.p5.plot()
        self.curve6 = self.p6.plot()
       
        graphUpdateSpeedMs = 1
        timer = QtCore.QTimer()#to create a thread that calls a function at intervals
        timer.timeout.connect(self.update)#the update function keeps getting called at intervals

        timer.start(graphUpdateSpeedMs)   
        QtGui.QApplication.instance().exec_()
       
    def update(self):

        if len(self.dat4) > self.maxLen:
            """
            self.dat1.popleft() #remove oldest
            self.dat2.popleft() #remove oldest
            self.dat3.popleft() #remove oldest
            """
            self.dat4.popleft() #remove oldest
            self.dat5.popleft() #remove oldest
            self.dat6.popleft() #remove oldest
        #self.dat.append(random.randint(0,100)); 
        cc=str(ser.readline(),'utf-8')
        ca = cc
        cc = cc.strip("\r\n")

        singleD = cc.split(";")
        
        if (cc != '\r\n' and cc != '' and cc !='-\r\n'):
            if (len(singleD) == 6): #filtro para posibles errores de medida
                
                f=open("C:/Users/jorge/Desktop/Universidad/Master/Redes de Sensores/Toma de datos/"+"hey", "a")
                f.write(ca)

                #print(singleD)

                """
                data = int(float(singleD[0]))
                self.dat1.append(data)
                self.curve1.setData(self.dat1) 

                data = int(float(singleD[1]))
                self.dat2.append(data)
                self.curve2.setData(self.dat2) 

                data = int(float(singleD[2]))
                self.dat3.append(data)
                self.curve3.setData(self.dat3) 
                """
                data = int(float(singleD[3]))
                self.dat4.append(data)
                self.curve4.setData(self.dat4) 

                data = int(float(singleD[4]))
                self.dat5.append(data)
                self.curve5.setData(self.dat5) 

                data = int(float(singleD[5]))
                self.dat6.append(data)
                self.curve6.setData(self.dat6) 
        
        self.app.processEvents()  
       

if __name__ == '__main__':
    g = Graph()
