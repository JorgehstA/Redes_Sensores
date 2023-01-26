# Trabajo asignatura

-Dispositivo empleado: SiLabs Thunderboard Sense 2

-Objetivo: Se pretende diferenciar 4 movimientos básicos en un futbolín
  
  1.Idle: Estado de movimiento suave
  2.Stop: No hay movimiento
  3.Tiro: Tiro con un jugador
  4.Ruleta: el jugador da varias vueltas
  
  Para este trabajo se ha obtado por utilizar el acelerómetro que viene incorporado en el propio Kit de desarrollo.
  Se ha hecho uso de redes neuronales para tratar de identificar cada movimiento, para ello se ha empleado la herramienta "edge impulse".
  Mediante esta API, se realizarán los pasos própios de la creación de una red neuronal, para ello se deben regoger datos para los sets
  de entrenamiento, validación y testeo.
  
  Condiciones de muestreo:
  
    -Tasa de muestreo: 100Hz
    -Tamaño de muestra: 3000 ms
    -Sensor: Acelerómetro
   
   Los pasos a efectuar serán los siguientes:
   
   La elección del tamaño de ventana adecuado es crucial para que el modelo final funcione
   
   ![image](https://user-images.githubusercontent.com/81929580/214741979-d5a54e97-f9f3-4c73-aaa8-b79271fbcf5c.png)

   
   Una vez se han obtenido los datos de entrenamiento, se realiza un procesado aplicando un filtro que ayudará en la detección de características.
   En este caso se ha optado por la siguiente conficuración:
 
   ![image](https://user-images.githubusercontent.com/81929580/214738388-f0251c2b-9e3a-4907-87df-5f9a5d111494.png)

![image](https://user-images.githubusercontent.com/81929580/214738672-01e5e604-8819-46dd-914a-228bae7fe0bf.png)

![image](https://user-images.githubusercontent.com/81929580/214738725-23ce8f9e-739a-478d-9b9e-e8f2258211fb.png)

Observando más detenidamente la clasificación, 2 de los 4 movimientos parecen tener una clara diferenciación, sin embargo la ruleta y el tiro presentan 
características similares como ya se había sospechado.

![image](https://user-images.githubusercontent.com/81929580/214739562-d1cd4a50-1bbd-4719-b458-569f09f075a2.png)

A la hora de entrenar la red neuronal se ha implementado con la siguiente conficuración:

  1.Number of training cycles: 100
  2.Learning rate (como de rápido aprende la red neuronal): 0.0001
  Validation set size: 20%
  
  Al contar con 48 "features" y teniendo en cuenta el tipo de aplicación, se ha establecido la siguiente arquitectura para red neuronal:
  
  ![image](https://user-images.githubusercontent.com/81929580/214740273-df01d3af-2ce1-41e9-9b33-7fd853e55f9f.png)
  
  Se ha conseguido casi un 88% de acierto. Aunque no sea del 100% se han conseguido mejores resultado que con otras 
  con una precisión mayor, esto puede ser debido a un "overfitting" para mejorar esto se podría aumentar la cantidad de datos o reducir 
  el ratio de aprendizaje.
  
  ![image](https://user-images.githubusercontent.com/81929580/214740826-e0d4bf95-f51f-45a3-ade8-0f044a1bd765.png)

Por último se deben desestimar comportamientos que la red no conoce.
Podemos usar esto a nuestro favor entrenando una nueva (segunda) red que crea grupos alrededor de los datos que hemos visto antes y comparar 
los datos entrantes con estos grupos. Si la distancia desde un clúster es demasiado grande, puede marcar la muestra como una anomalía y no 
confiar en la red neuronal.

![image](https://user-images.githubusercontent.com/81929580/214741800-5373c872-3b0c-4f6a-9086-5ac73d1998f8.png)

Implementación final:

![image](https://user-images.githubusercontent.com/81929580/214742814-b03e7571-37e7-4e45-a59b-ce1cdd5ea676.png)
