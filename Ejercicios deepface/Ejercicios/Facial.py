from deepface import DeepFace

obj= DeepFace.analyze (img_path="/home/tzec/Documentos/GitHub/Reconocimiento-facial/Ejercicios deepface/Deepface-Imagenes/Mujer.jpg",actions=['age','gender','race','emotion'])

print ("EL resultado del analisis es: ")
print (obj)