import os

contenido = os.listdir(r'C:/Users\jorge\Desktop\Universidad\Master\Redes de Sensores\Toma de datos')
print(contenido)
for i in contenido:
    with open(r'C:/Users\jorge\Desktop\Universidad\Master\Redes de Sensores\Toma de datos/'+i) as file:
        for line in file:
            #print(len(line))
            #print(line)
            if(len(line)> 31 and len(line)< 37):
                f2 = open('C:/Users/jorge/Desktop/Universidad/Master/Redes de Sensores/Data Acquisition/'+i+'.txt','a')
                f2.write(line)
                f2.close()



