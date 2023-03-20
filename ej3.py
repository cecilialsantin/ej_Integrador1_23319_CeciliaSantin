texto = input("ingrese un texto: ")
noconsiderar_palabra = ",;:.\n!\"'"

for caracter in noconsiderar_palabra:
    texto = texto.replace(caracter,"")

texto = texto.lower()
palabras = texto.split(" ")

diccionario_palabra_frecuencia = {}
for palabra in palabras:
    if palabra in diccionario_palabra_frecuencia:
        diccionario_palabra_frecuencia[palabra] += 1
    else:
        diccionario_palabra_frecuencia[palabra] = 1

for palabra in diccionario_palabra_frecuencia:
    frecuencia = diccionario_palabra_frecuencia[palabra]

print(diccionario_palabra_frecuencia)  

