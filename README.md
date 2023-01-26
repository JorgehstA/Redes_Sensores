# Redes_Sensores

1.Para las prácticas 1, 2, 3, 4 se ha utilizado SiLabs Thunderboard Sense 2

2.Para las prácticas 4 y 5 se ha utilizado ESP32

## Practica 1: Control básico de microcontrolador

        -Programas: Led_control, blink_pwm, Humidity_temperature_sensor
        
                -Generar interrupción cada 0,5 segundos controlando la salida de de activación de led: Programa en "Led_control"
                -Generar señal PWM con duty variable que controle la intensidad de led: Programa en "blink_pwm"
                Secuencia pwm:
![image](https://user-images.githubusercontent.com/81929580/214577713-a6ac9f1f-912b-4e09-9312-32b3e8fc1c96.png)

        -Lectura de sensor teperatura y humedad via UART: Programa en "Humidity_temperature_sensor"
        
![image](https://user-images.githubusercontent.com/81929580/214573064-0956aa66-fab0-43d0-b02a-122455021261.png)


# Practica 2: Diseño de firmware basado en sistema operativo de tiempo real (RTOS)

        -Programas: Read_sensor_freetos
        
                -Se ha generado un programa donde se llevan a cabo 2 tareas: Programa en "Read_sensor_freetos"
                En la primera se obtienen los valores de temperatura y humedad del sensor incorporado.
                En la segunda se controla un led apagándolo o encendiéndolo dependiendo de si la temperatura es 
                superior o inferior a +/- 2ºC la temperatura inicial.

![image](https://user-images.githubusercontent.com/81929580/214577607-5f4a34cf-d004-4f4e-828d-b7b36887a93a.png)


## Practica 3: Comunicación, gestión y representación de datos de sensores con Python

        -Programas: Motion, fastrealTimeGraph
        
        Se ha creado un programa en el micro que lea los valores del acelerómetro a una frecuencia de 200Hz y 
        mande dicha información por UART.
        En el ordenador se grafica en tiempo real los valores que secogen a través de un puerto COM, filtrando 
        datos anómalos y almacenando en un txt.
        
## Practica 4: Comunicaciones WIFI y stack IP

        1.	Conéctate a la red wifi del laboratorio o a una creada por el móvil como punto de acceso. Extrae tu IP. Comprueba la conectividad con Google mediante                   un ping.
        
                •	Extracción de IP:
        
![image](https://user-images.githubusercontent.com/81929580/214600238-f7c1f082-252b-4247-a001-c00aba4e6fa4.png)

                •	Conectividad con Google:
        
![image](https://user-images.githubusercontent.com/81929580/214600310-7c23b1f2-387f-4c98-9ee9-4d5252997cd2.png)

        2.	Pon en hora el módulo mediante un servidor NTP (Network Time Protocol).

![image](https://user-images.githubusercontent.com/81929580/214600593-d046bfad-3794-47d8-8f2e-ae84880747cb.png)

![image](https://user-images.githubusercontent.com/81929580/214600716-9c87c0ee-9cd7-4fe2-aeb3-732e15209112.png)

![image](https://user-images.githubusercontent.com/81929580/214601005-6c98eb76-7b26-4669-a77c-42360c648c74.png)

        3.	Monta un chat una aplicación software PC (http://sockettest.sourceforge.net/) o con una aplicación móvil (simple TCP socket tester). A veces el                         firewall del ordenador no permite las conexiones externas, y es necesario configurarlo correctamente
        
![image](https://user-images.githubusercontent.com/81929580/214601198-bc7db851-8ca1-43d7-bdb0-a5d092d4569c.png)

![image](https://user-images.githubusercontent.com/81929580/214601337-7ebc7188-49d4-438a-9b8b-efabd4a106cb.png)

![image](https://user-images.githubusercontent.com/81929580/214601420-dfbbd250-f415-467b-8a10-bc478fac0df0.png)

![image](https://user-images.githubusercontent.com/81929580/214601443-e27348f0-6cc5-4716-a3e5-64e33c3b99a2.png)

        5.	Monta un servidor WEB

                Para montar el servidor web son necesarios tres archivos. El sketch de Arduino, el archivo HTML y el archivo CSS. Los archivos HTML y CSS deben                         guardarse dentro de una carpeta llamada datos dentro de la carpeta de sketch de Arduino:

![image](https://user-images.githubusercontent.com/81929580/214601610-efdf51ec-095e-4e2e-be4b-219444d22e61.png)

El resultado obtenido es el siguiente, donde podemos obtener el tiempo actual y mediate el botón de “reset” situamos el reloj del micro  en 00:00:00.

![image](https://user-images.githubusercontent.com/81929580/214601679-27159965-f99d-4416-a6c4-71e9fbbec721.png)

A continuación el código empleado en Arduino:

![image](https://user-images.githubusercontent.com/81929580/214601858-8bf78d86-e11d-4379-9550-533ae750c50c.png)

![image](https://user-images.githubusercontent.com/81929580/214601921-86a07c9c-c984-43d4-bc69-884a9f8c81cd.png)

![image](https://user-images.githubusercontent.com/81929580/214601970-a8b8f3e1-1659-42d3-a7b8-8a7c41681013.png)

![image](https://user-images.githubusercontent.com/81929580/214602012-40f9fa61-d48f-41eb-9ebc-f898118d3dad.png)

	Basándote en el estándar SENML (https://tools.ietf.org/html/rfc8428) crea un fichero json (https://arduinojson.org/) que se genere cada 10 segundos, que contenga datos de temperatura inventados, las unidades y la marca temporal. Súbelos a un servidor ftp con un nombre que sea grupoXX_ddmmss.json. (https://platformio.org/lib/show/6543/esp32_ftpclient) Usa el del laboratorio (IP: 155.210.150.77, user: rsense, pass: rsense)

En este caso al estar trabajando con el módulo Thunderbolt se Silabs realizaremos la subida de datos al servidor FTP través de Python leyendo primero los datos de temperatura y humedad que envía el micro a través de la UART.
Diagrama de bloques del sistema:
	-En el µC se leen los valores de los sensores de humedad y temperatura y se envían por comunicación serie al PC
	-En el PC se tratan los datos mediante el estándar Senml y se guardan en un fichero json cada 10 segundos.
	-Finalmente, el archivo json es enviado al servidor FTP (en este caso el de la universidad)

![image](https://user-images.githubusercontent.com/81929580/214602151-f88c36c9-bea7-45f3-b952-5bb7c79325df.png)

Código Python:

![image](https://user-images.githubusercontent.com/81929580/214602268-42f937b2-afa5-416c-96d1-83fbc55296eb.png)

![image](https://user-images.githubusercontent.com/81929580/214602305-77881a93-24a1-44df-9b35-ebee71485a5f.png)

El formato del archivo json es el siguiente:

![image](https://user-images.githubusercontent.com/81929580/214602395-e6ce41dc-d469-48bd-8e15-e0ef8c7869f6.png)

        7.	Sube datos a la nube, en concreto al servicio gratuito proporcionado por Adafruit. 

                Para ello se crea una cuenta en https://io.adafruit.com/, con el fin de obtener un “AIO Key” y crear un feed al que subir datos.

![image](https://user-images.githubusercontent.com/81929580/214602522-52760a72-d444-4ebf-9e0e-609692ed5d3f.png)

Se usa la librería de Adafruit IO (https://github.com/adafruit/Adafruit_IO_Arduino) para subir datos al feed usando MQTT y se procede a utilizar unode sus ejemplos, en este caso se publicarán los datos (un contador) en el servidor web.
Del archivo config.h se modifican los siguientes campos:

![image](https://user-images.githubusercontent.com/81929580/214602593-0ccf6079-9372-48eb-8cd4-4c291d84a83b.png)
![image](https://user-images.githubusercontent.com/81929580/214602638-541b1ba5-1e07-4415-ae90-b4a592e8ebd5.png)

![image](https://user-images.githubusercontent.com/81929580/214602691-7ab02db1-abf5-431d-b8fc-a27dae7b946d.png)

![image](https://user-images.githubusercontent.com/81929580/214602740-94053258-9f3f-4005-adbd-aea6ff2997b0.png)

Como resultado se obtiene el registro del contador en el servidor que se pueden descargar si se desea.

![image](https://user-images.githubusercontent.com/81929580/214602778-3716f337-d4d7-4343-8bb5-fbeb8463f4b4.png)

## Practica 5: Comunicaciones BLE y Bluetooth

	-Programas: BLE_notify
	
	El dispositivo con nombre "ESP32" emite un servicio con una característica de notificaciónque incrementa un contador una unidad por segundo.
