import os#libreria para el manejo de directorios y archivos
import matplotlib.image as mpimg#libreria para leer la imagen y pueda ser procesada mediante una relación filas, columnas
from PIL import Image#libreria para abrir la imagen y poder obtener sus caracteristicas
import numpy as np#libreria para efectuar operaciones entre vectores y matrices
import csv#libreria que nos permite interactuar con archivos csv
archivo= open('DataSet.csv', 'w', newline='')#se crea el archivo csv donde se guardará el Dataset
salida = csv.writer(archivo) #se transfiere el archivo a esta variable para poder escribir en el
def CortesV(imagen,columna):#se define la función que calcula el número de cortes verticales de la imagen, recibe como argumento la imagen y la columna que se va a procesar
    corte=0#se crea una variable que contendrá el número de cortes de la imagen
    for i in range(0,rows-1):#ciclo para recorrer la columna procesada (en todas las filas)    
        if(imagen[i,columna]==imagen[i+1,columna]):#If para saber si el pixel (i) es igual que el siguiente.
            corte=corte#si no hubo cambio entre el pixel actual y el siguiente, el contador permanece con su mismo valor
        else:#si el pixel (i) es diferente al siguiente (hubo un cambio)
            corte=corte+1#si hubo un cambio entre el pixel actual y el siguiente, el contador incrementa su valor 1 unidad
    if(imagen[0,columna]==1):#si el primer pixel es 1, se sobre entiende que existe un corte
            corte=corte+1#por lo tanto se incrementa el valor del contador
    if(imagen[rows-1,columna]==1):#si el ultimo pixel es 1, se sobre entiende que existe un corte
            corte=corte+1#por lo tanto se incrementa el valor del contador
    return corte#se retorna la variable corte para su posterior uso    
def CortesH(imagen,fila):#se define la función que calcula el número de cortes horizontales de la imagen, recibe como argumento la imagen y la fila que se va a procesar
    corte=0#se crea una variable que contendrá el número de cortes de la imagen
    for i in range(0,columns-1):#ciclo para recorrer la fila procesada (en todas las columnas)
        if(imagen[fila,i]==imagen[fila,i+1]):#If para saber si el pixel (i) es igual que el siguiente.
            corte=corte#si no hubo cambio entre el pixel actual y el siguiente, el contador permanece con su mismo valor
        else:#si el pixel (i) es diferente al siguiente (hubo un cambio)
            corte=corte+1#si hubo un cambio entre el pixel actual y el siguiente, el contador incrementa su valor 1 unidad
    if(imagen[fila,0]==1):#si el primer pixel es 1, se sobre entiende que existe un corte
            corte=corte+1#por lo tanto se incrementa el valor del contador
    if(imagen[fila,columns-1]==1):#si el ultimo pixel es 1, se sobre entiende que existe un corte
            corte=corte+1#por lo tanto se incrementa el valor del contador
    return corte#se retorna la variable corte para su posterior uso
#En esta parte del código se obtendrán las caracteristicas de todas las imagenes contenidas dentro de la carpeta "Imagenes" 
ruta='C:/Users/Arturo/Documents/Python Scripts/Proyecto/Imagenes/'#se define la ruta de nuestro training set
trainingSet=os.listdir(ruta)#se obtienen los directorios (folders) contenidos en la carpeta Imagenes en forma de lista
for folder in trainingSet:#ciclo for que recorre los folders contenidos en la carpeta "Imagenes" (0-9 & A-Z)
    caracter=os.listdir(ruta+folder)#se crea una lista que contiene todos los archivos (imagenes.png) contenidas en el folder (0...9, A...Z)
    for file in caracter:#ciclo para recorrer todas las imagenes (file) contenidos en la carpeta (folder)
        img=mpimg.imread(ruta+'/'+folder+'/'+file)#se lee la imagen que esta en procesamiento  
        img2=Image.open(ruta+'/'+folder+'/'+file)#se abre la imagen que esta en procesamiento
        print('Procesando imagen-----------------------> '+file)#se imprime el nombre de la imagen en procesamiento, en la términal de Python
        columns=img2.size[0]#se obtienen las columnas de la imagen en procesamiento
        rows=img2.size[1]#se obtienen las filas de la imagen en procesamiento
        
        cuartoC=columns/4#se obtiene la columna 1/4 de la imagen en procesamiento 
        medioC=columns/2#se obtiene la columna 1/2 de la imagen en procesamiento
        tercioC=columns/4+columns/2#se obtiene la columna 3/4 de la imagen en procesamiento
        
        cuartoR=rows/4#se obtiene la fila 1/4 de la imagen en procesamiento
        medioR=rows/2#se obtiene la fila 1/2 de la imagen en procesamiento
        tercioR=rows/4+rows/2#se obtiene la fila 3/4 de la imagen en procesamiento
        
        lineaV1=img[:,cuartoC]#se obtiene un arreglo de 0's y 1's correspondiente a la primera linea vertical 
        sumC1=np.sum(lineaV1)#se suman los 1's del arreglo y se almacenan en una variable
        c1=sumC1/rows#se normaliza la variable anterior dividiendo el número de 1's/numero de filas  
        
        lineaV2=img[:,medioC]#se obtiene un arreglo de 0's y 1's correspondiente a la segunda linea vertical
        sumC2=np.sum(lineaV2)#se suman los 1's del arreglo y se almacenan en una variable
        c2=sumC2/rows#se normaliza la variable anterior dividiendo el número de 1's/numero de filas    
    
        lineaV3=img[:,tercioC]#se obtiene un arreglo de 0's y 1's correspondiente a la tercera linea vertical
        sumC3=np.sum(lineaV3)#se suman los 1's del arreglo y se almacenan en una variable
        c3=sumC3/rows#se normaliza la variable anterior dividiendo el número de 1's/numero de filas
        
        lineaH1=img[cuartoR,:]#se obtiene un arreglo de 0's y 1's correspondiente a la primera linea horizontal
        sumC4=np.sum(lineaH1)#se suman los 1's del arreglo y se almacenan en una variable
        c4=sumC4/columns#se normaliza la variable anterior dividiendo el número de 1's/numero de columnas
        
        lineaH2=img[medioR,:]#se obtiene un arreglo de 0's y 1's correspondiente a la segunda linea horizontal
        sumC5=np.sum(lineaH2)#se suman los 1's del arreglo y se almacenan en una variable
        c5=sumC5/columns#se normaliza la variable anterior dividiendo el número de 1's/numero de columnas
        
        lineaH3=img[tercioR,:]#se obtiene un arreglo de 0's y 1's correspondiente a la tercera linea horizontal
        sumC6=np.sum(lineaH3)#se suman los 1's del arreglo y se almacenan en una variable
        c6=sumC6/columns#se normaliza la variable anterior dividiendo el número de 1's/numero de columnas
    
        c7=CortesV(img,cuartoC)#se invoca la funcion CortesV pasandole como argumentos la imagen en procesamiento y la columna a procesar, para obtener el número de cortes correspondiente
        c8=CortesV(img,medioC)#se invoca la funcion CortesV pasandole como argumentos la imagen en procesamiento y la columna a procesar, para obtener el número de cortes correspondiente
        c9=CortesV(img,tercioC)#se invoca la funcion CortesV pasandole como argumentos la imagen en procesamiento y la columna a procesar, para obtener el número de cortes correspondiente
        
        c10=CortesH(img,cuartoR)#se invoca la funcion CortesH pasandole como argumentos la imagen en procesamiento y la fila a procesar, para obtener el número de cortes correspondiente    
        c11=CortesH(img,medioR)#se invoca la funcion CortesH pasandole como argumentos la imagen en procesamiento y la fila a procesar, para obtener el número de cortes correspondiente    
        c12=CortesH(img,tercioR)#se invoca la funcion CortesH pasandole como argumentos la imagen en procesamiento y la fila a procesar, para obtener el número de cortes correspondiente    
        
        dataset=[]#se define una lista llamada dataset, donde se almacenarán las instancias obtenidas en cada imagen procesada
        instancia=[(file), (folder), (c1),(c2),(c3),(c4),(c5),(c6),(c7),(c8),(c9),(c10),(c11),(c12)]#se define una lista llamada instancia, donde se almacenan los datos y caracteristicas de la imagen procesada
        dataset.append(instancia)#la instancia es agregada en una nueva linea del dataset (una lista dentro de otra lista)
        salida.writerows(dataset)#el contenido del dataset es enviado al archivo csv
archivo.close()#se cierra la escritura del achivo csv