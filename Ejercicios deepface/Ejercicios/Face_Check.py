from deepface import DeepFace
print ("Se han comparado 2 imagenes. Se verificara que la persona sea la misma")
print ("Cargando...")

result = DeepFace.verify(img1_path = "/home/tzec/Documentos/GitHub/Reconocimiento-facial/Ejercicios deepface/Deepface-Imagenes/Chris_1.jpg", 
img2_path = "/home/tzec/Documentos/GitHub/Reconocimiento-facial/Ejercicios deepface/Deepface-Imagenes/Chris_2.jpg")

print ("Resultados")
print (result)