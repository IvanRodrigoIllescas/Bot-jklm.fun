archivo_nombre='palabras.txt'
archivo = open(archivo_nombre,mode='r')
listaPalabras = archivo.read().split()
archivo.close()

posibles=[]

for i in listaPalabras:
    x = i.find("M")
    if x!=-1:
        posibles.append(i)
    
print(posibles)
print(posibles[0])


    
