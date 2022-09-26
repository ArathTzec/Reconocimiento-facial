# Reconocimiento-facial

Este repositorio contiene los ejercicios realizados de reconocimiento facial


## Material necesario
Para poder realizar necesario es necesario tener instalado:

- Instalar la biblioteca pahoMQTT https://pypi.org/project/paho-mqtt/
- Instalar DeepFace https://github.com/serengil/deepface


- Para poder instalarlos coloca los siguientes comandos:

>$ pip install deepface
>pip install paho-mqtt


## Notas

>PUedes modificar el codigo en Visual Studio Code y correrlo desde ahi,  pero de preferencia correlo en la terminal :)

## Instrucciones ejercicio 2 

1. Descargar un par de imagenes donde se aprecien rostros de la misma persona a diferentes edades para comparar que sean la misma persona(de preferencia actores
que te caigan bien)
2. Crear un archivo llamado face-check.py con el siguiente programa:

from deepface import DeepFace
print ("Se han comparado 2 imagenes. Se verificara que la persona sea la misma")
print ("Cargando...")

>result = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")
**Importante: en img1.jpg => colocar si direccion del archivo**
print ("Resultados")
print (result)



## Resultados
Una vez completados los pasos anteriores te dirigirá al Dashboard, que es la interfaz donde ver la temperatura y humedad dependiendo del mensaje que envies, trata de enviar el codigo que se encuentra en notas. Tambien recíbiras los datos de los demas compañeros
![](https://github.com/ArathTzec/Flow-5/blob/main/Dashboard-Flow5.png?raw=true)

Puedes ver los nodos en el siguiente link [Nodos-Flow5](https://github.com/ArathTzec/Flow-5/blob/main/Nodos%20node%20red%20flow%205-1.png)

## Evidencia 

