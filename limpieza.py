archivoPalabras=open('palabras.txt','r')
palabras=archivoPalabras.read().split()
archivoPalabras.close()

#print(palabras)

archivoFail=open('fail.txt','r')
palabrasMal=archivoFail.read().split()
archivoFail.close()

#print(palabrasMal)

for i in palabrasMal:
    #print(i)
    try:
        palabras.remove(i)
    except:
        print('error')

archivoPalabras=open('palabras.txt','w')
archivoPalabras.write('')
archivoPalabras.close()


archivoPalabras=open('palabras.txt','a')

for i in palabras:
    archivoPalabras.write(i+'\n')

archivoPalabras.close()

archivoFail=open('fail.txt','w')
archivoFail.write('')
archivoFail.close()

print('terminado')
    
    
