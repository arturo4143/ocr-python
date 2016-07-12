import csv#libreria que nos permite interactuar con archivos csv
import math#libreria que nos permite hacer uso de funciones matemáticas
import matplotlib.image as mpimg#libreria para leer la imagen y pueda ser procesada mediante una relación filas, columnas
from PIL import Image#libreria para abrir la imagen y poder obtener sus caracteristicas
import numpy as np#libreria para efectuar operaciones entre vectores y matrices
lns=csv.reader(open('DataSet.csv'))#leemos el dataset con extensión csv
dataset=list(lns)#el contenido del dataset csv se almacena en la variable dataset en forma de lista
#En esta parte del código se obtienen las características del elemento que se va a clasificar (test item)
def CortesV(imagen,columna):#se define la función que calcula el número de cortes verticales de la imagen, recibe como argumento la imagen y la columna que se va a procesar
    corte=0#se crea una variable que contendrá el número de cortes de la imagen
    for i in range(0,rows-1):#ciclo para recorrer la columna procesada (en todas las filas)    
        if(imagen[i,columna]==imagen[i+1,columna]):#If para saber si existe un cambio entre el pixel actual con respecto al siguiente
            corte=corte#si no hubo cambio entre el pixel actual y el siguiente, el contador permanece con su mismo valor
        else:#else del if
            corte=corte+1#si hubo un cambio entre el pixel actual y el siguiente, el contador incrementa su valor 1 unidad       
    if(imagen[0,columna]==1):#si el primer pixel es 1, se sobre entiende que existe un corte
            corte=corte+1#por lo tanto se incrementa el valor del contador
    if(imagen[rows-1,columna]==1):#si el ultimo pixel es 1, se sobre entiende que existe un corte
            corte=corte+1#por lo tanto se incrementa el valor del contador
    return corte#se retorna la variable corte para su posterior uso
#En esta parte del código se obtienen las características del elemento que se va a clasificar (test item)
def CortesH(imagen,fila):#se define la función que calcula el número de cortes horizontales de la imagen, recibe como argumento la imagen y la fila que se va a procesar
    corte=0#se crea una variable que contendrá el número de cortes de la imagen
    for i in range(0,columns-1):#for para recorrer la columna    
        if(imagen[fila,i]==imagen[fila,i+1]):#ciclo para recorrer la fila procesada (en todas las columnas)
            corte=corte#si no hubo cambio entre el pixel actual y el siguiente, el contador permanece con su mismo valor
        else:#else del if
            corte=corte+1#si hubo un cambio entre el pixel actual y el siguiente, el contador incrementa su valor 1 unidad     
    if(imagen[fila,0]==1):#si el primer pixel es 1, se sobre entiende que existe un corte
            corte=corte+1#por lo tanto se incrementa el valor del contador
    if(imagen[fila,columns-1]==1):#si el ultimo pixel es 1, se sobre entiende que existe un corte
            corte=corte+1#por lo tanto se incrementa el valor del contador
    return corte#se retorna la variable corte para su posterior uso
print("Nombre de la imagen: ")#impresion de pantalla para recibir el nombre de la imagen que se desea clasificar
NImagen=input()#variable donde se almacena la entrada del usuario
print("Ingrese el valor de K: ")#impresion de pantalla para recibir el valor de K
ktemp=input()#variable donde se almacena la entrada del usuario
k=int(ktemp)#convertimos la entrada recibida a int
img=mpimg.imread('ImagenesPrueba/'+NImagen+'.png')#se lee la imagen que se desea clasificar
img2=Image.open('ImagenesPrueba/'+NImagen+'.png')#se abre la imagen que se desea clasificar
print('Obteniendo caracteristicas del elemento de prueba: '+ NImagen+'.png')#impresión de pantalla
columns=img2.size[0]#se obtienen las columnas de la imagen que se desea clasificar
rows=img2.size[1]#se obtienen las filas de la imagen que se desea clasificar

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

c7=CortesV(img,cuartoC)#se invoca la funcion CortesV pasandole como argumentos la imagen a clasificar y la columna a procesar, para obtener el número de cortes correspondiente
c8=CortesV(img,medioC)#se invoca la funcion CortesV pasandole como argumentos la imagen a clasificar y la columna a procesar, para obtener el número de cortes correspondiente
c9=CortesV(img,tercioC)#se invoca la funcion CortesV pasandole como argumentos la imagen a clasificar y la columna a procesar, para obtener el número de cortes correspondiente

c10=CortesH(img,cuartoR)#se invoca la funcion CortesH pasandole como argumentos la imagen a clasificar y la fila a procesar, para obtener el número de cortes correspondiente    
c11=CortesH(img,medioR)#se invoca la funcion CortesH pasandole como argumentos la imagen a clasificar y la fila a procesar, para obtener el número de cortes correspondiente    
c12=CortesH(img,tercioR)#se invoca la funcion CortesH pasandole como argumentos la imagen en procesamiento y la fila a procesar, para obtener el número de cortes correspondiente    

print('C1: '+str(c1)+'\nC2: '+str(c2)+'\nC3: '+str(c3)+'\nC4: '+str(c4)+'\nC5: '+str(c5)+'\nC6: '+str(c6)+'\nC7: '+str(c7)+'\nC8: '+str(c8)+'\nC9: '+str(c9)+'\nC10: '+str(c10)+'\nC11: '+str(c11)+'\nC12: '+str(c12)+"\n")#se imprimen todas las características de la imagen que se desea clasificar
contador=0#se declara un contador para recorrer fila por fila
for i in dataset:#ciclo for para convertir todo el dataset a numeros flotantes
  dataset[contador][2]=float(dataset[contador][2])#se realiza un cast de string a float 
  dataset[contador][3]=float(dataset[contador][3])#se realiza un cast de string a float
  dataset[contador][4]=float(dataset[contador][4])#se realiza un cast de string a float
  dataset[contador][5]=float(dataset[contador][5])#se realiza un cast de string a float
  dataset[contador][6]=float(dataset[contador][6])#se realiza un cast de string a float
  dataset[contador][7]=float(dataset[contador][7])#se realiza un cast de string a float
  dataset[contador][8]=float(dataset[contador][8])#se realiza un cast de string a float
  dataset[contador][9]=float(dataset[contador][9])#se realiza un cast de string a float
  dataset[contador][10]=float(dataset[contador][10])#se realiza un cast de string a float
  dataset[contador][11]=float(dataset[contador][11])#se realiza un cast de string a float
  dataset[contador][12]=float(dataset[contador][12])#se realiza un cast de string a float
  dataset[contador][13]=float(dataset[contador][13])#se realiza un cast de string a float
  
  euclidianaTemp=((dataset[contador][2]-c1)**2)+((dataset[contador][3]-c2)**2)+((dataset[contador][4]-c3)**2)+((dataset[contador][5]-c4)**2)+((dataset[contador][6]-c5)**2)+((dataset[contador][7]-c6)**2)+((dataset[contador][8]-c7)**2)+((dataset[contador][9]-c8)**2)+((dataset[contador][10]-c9)**2)+((dataset[contador][11]-c10)**2)+((dataset[contador][12]-c11)**2)+((dataset[contador][13]-c12)**2)#Formula para obtener la distancia Euclidiana (Part1)
  raiz=math.sqrt(euclidianaTemp)#Se obtiene la raiz cuadrada de la sumatoria anterior
  dataset[contador].append(raiz)#agregamos una nueva columna a nuestro dataset para guardar la distancia obtenida entre el elemento de prueba y la instancia actual  
  contador=contador+1#Incrementamos un número al contador
dataset.sort(key=lambda dataset: dataset[14])#Ordenamos de menor a mayor las distancias 
for i in range(0,k):#ciclo for para imprimir cada uno de los vecinos mas cercanos (de 0 al número K)
  print('#Neighbor: '+str((i)+1)+ '\nDistancia: '+str(dataset[i][14])+'\nClase: '+dataset[i][1]+'\nInstancia: '+dataset[i][0]+'\n-----------------------------------------')#impresión en pantalla de la información de cada vecino mas cercano
vecinos=[]#Se declara una lista para almacenar los 11 vecinos mas cercanos
cant0=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cant1=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cant2=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cant3=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cant4=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cant5=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cant6=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cant7=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cant8=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cant9=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantA=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantB=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantC=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantD=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantE=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantF=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantG=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantH=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantI=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantJ=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantK=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantL=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantM=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantN=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantO=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantP=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantQ=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantR=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantS=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantT=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantU=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantV=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantW=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantX=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantY=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
cantZ=0#se declara una variable contador para después obtener la clase de acuerdo a la función mayoria
for i in range(0,k):#ciclo para recorrer a los primeros K vecinos mas cercanos
  if(dataset[i][1]=='0'):#condición para saber si el vecino (i) es 0
    cant0=cant0+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='1'):#condición para saber si el vecino (i) es 1
    cant1=cant1+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='2'):#condición para saber si el vecino (i) es 2
    cant2=cant2+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='3'):#condición para saber si el vecino (i) es 3
    cant3=cant3+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='4'):#condición para saber si el vecino (i) es 4
    cant4=cant4+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='5'):#condición para saber si el vecino (i) es 5
    cant5=cant5+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='6'):#condición para saber si el vecino (i) es 6
    cant6=cant6+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='7'):#condición para saber si el vecino (i) es 7
    cant7=cant7+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='8'):#condición para saber si el vecino (i) es 8
    cant8=cant8+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='9'):#condición para saber si el vecino (i) es 9
    cant9=cant9+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='A'):#condición para saber si el vecino (i) es A
    cantA=cantA+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='B'):#condición para saber si el vecino (i) es B
    cantB=cantB+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='C'):#condición para saber si el vecino (i) es C
    cantC=cantC+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='D'):#condición para saber si el vecino (i) es D
    cantD=cantD+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='E'):#condición para saber si el vecino (i) es E
    cantE=cantE+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='F'):#condición para saber si el vecino (i) es F
    cantF=cantF+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='G'):#condición para saber si el vecino (i) es G
    cantG=cantG+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='H'):#condición para saber si el vecino (i) es H
    cantH=cantH+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='I'):#condición para saber si el vecino (i) es I
    cantI=cantI+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='J'):#condición para saber si el vecino (i) es J
    cantJ=cantJ+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='K'):#condición para saber si el vecino (i) es K
    cantK=cantK+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='L'):#condición para saber si el vecino (i) es L
    cantL=cantL+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='M'):#condición para saber si el vecino (i) es M
    cantM=cantM+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='N'):#condición para saber si el vecino (i) es N
    cantN=cantN+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='O'):#condición para saber si el vecino (i) es O
    cantO=cantO+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='P'):#condición para saber si el vecino (i) es P
    cantP=cantP+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='Q'):#condición para saber si el vecino (i) es Q
    cantQ=cantQ+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='R'):#condición para saber si el vecino (i) es R
    cantR=cantR+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='S'):#condición para saber si el vecino (i) es S
    cantS=cantS+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='T'):#condición para saber si el vecino (i) es T
    cantT=cantT+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='U'):#condición para saber si el vecino (i) es U
    cantU=cantU+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='V'):#condición para saber si el vecino (i) es V
    cantV=cantV+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='W'):#condición para saber si el vecino (i) es W
    cantW=cantW+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='X'):#condición para saber si el vecino (i) es X
    cantX=cantX+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='Y'):#condición para saber si el vecino (i) es Y
    cantY=cantY+1#en ese caso se incrementa una unidad al contador del caracter
  if(dataset[i][1]=='Z'):#condición para saber si el vecino (i) es Z
    cantZ=cantZ+1#en ese caso se incrementa una unidad al contador del caracter 
vecinos.append(['0',cant0])#se añade a la lista "vecinos" dos campos, (la clase 0 y el valor total del contador de dicha letra o número)
vecinos.append(['1',cant1])#se añade a la lista "vecinos" dos campos, (la clase 1 y el valor total del contador de dicha letra o número)
vecinos.append(['2',cant2])#se añade a la lista "vecinos" dos campos, (la clase 2 y el valor total del contador de dicha letra o número)
vecinos.append(['3',cant3])#se añade a la lista "vecinos" dos campos, (la clase 3 y el valor total del contador de dicha letra o número)
vecinos.append(['4',cant4])#se añade a la lista "vecinos" dos campos, (la clase 4 y el valor total del contador de dicha letra o número)
vecinos.append(['5',cant5])#se añade a la lista "vecinos" dos campos, (la clase 5 y el valor total del contador de dicha letra o número)
vecinos.append(['6',cant6])#se añade a la lista "vecinos" dos campos, (la clase 6 y el valor total del contador de dicha letra o número)
vecinos.append(['7',cant7])#se añade a la lista "vecinos" dos campos, (la clase 7 y el valor total del contador de dicha letra o número)
vecinos.append(['8',cant8])#se añade a la lista "vecinos" dos campos, (la clase 8 y el valor total del contador de dicha letra o número)
vecinos.append(['9',cant9])#se añade a la lista "vecinos" dos campos, (la clase 9 y el valor total del contador de dicha letra o número)
vecinos.append(['A',cantA])#se añade a la lista "vecinos" dos campos, (la clase A y el valor total del contador de dicha letra o número)
vecinos.append(['B',cantB])#se añade a la lista "vecinos" dos campos, (la clase B y el valor total del contador de dicha letra o número)
vecinos.append(['C',cantC])#se añade a la lista "vecinos" dos campos, (la clase C y el valor total del contador de dicha letra o número)
vecinos.append(['D',cantD])#se añade a la lista "vecinos" dos campos, (la clase D y el valor total del contador de dicha letra o número)
vecinos.append(['E',cantE])#se añade a la lista "vecinos" dos campos, (la clase E y el valor total del contador de dicha letra o número)
vecinos.append(['F',cantF])#se añade a la lista "vecinos" dos campos, (la clase F y el valor total del contador de dicha letra o número)
vecinos.append(['G',cantG])#se añade a la lista "vecinos" dos campos, (la clase G y el valor total del contador de dicha letra o número)
vecinos.append(['H',cantH])#se añade a la lista "vecinos" dos campos, (la clase H y el valor total del contador de dicha letra o número)
vecinos.append(['I',cantI])#se añade a la lista "vecinos" dos campos, (la clase I y el valor total del contador de dicha letra o número)
vecinos.append(['J',cantJ])#se añade a la lista "vecinos" dos campos, (la clase J y el valor total del contador de dicha letra o número)
vecinos.append(['K',cantK])#se añade a la lista "vecinos" dos campos, (la clase K y el valor total del contador de dicha letra o número)
vecinos.append(['L',cantL])#se añade a la lista "vecinos" dos campos, (la clase L y el valor total del contador de dicha letra o número)
vecinos.append(['M',cantM])#se añade a la lista "vecinos" dos campos, (la clase M y el valor total del contador de dicha letra o número)
vecinos.append(['N',cantN])#se añade a la lista "vecinos" dos campos, (la clase N y el valor total del contador de dicha letra o número)
vecinos.append(['O',cantO])#se añade a la lista "vecinos" dos campos, (la clase O y el valor total del contador de dicha letra o número)
vecinos.append(['P',cantP])#se añade a la lista "vecinos" dos campos, (la clase P y el valor total del contador de dicha letra o número)
vecinos.append(['Q',cantQ])#se añade a la lista "vecinos" dos campos, (la clase Q y el valor total del contador de dicha letra o número)
vecinos.append(['R',cantR])#se añade a la lista "vecinos" dos campos, (la clase R y el valor total del contador de dicha letra o número)
vecinos.append(['S',cantS])#se añade a la lista "vecinos" dos campos, (la clase S y el valor total del contador de dicha letra o número)
vecinos.append(['T',cantT])#se añade a la lista "vecinos" dos campos, (la clase T y el valor total del contador de dicha letra o número)
vecinos.append(['U',cantU])#se añade a la lista "vecinos" dos campos, (la clase U y el valor total del contador de dicha letra o número)
vecinos.append(['V',cantV])#se añade a la lista "vecinos" dos campos, (la clase V y el valor total del contador de dicha letra o número)
vecinos.append(['W',cantW])#se añade a la lista "vecinos" dos campos, (la clase W y el valor total del contador de dicha letra o número)
vecinos.append(['X',cantX])#se añade a la lista "vecinos" dos campos, (la clase X y el valor total del contador de dicha letra o número)
vecinos.append(['Y',cantY])#se añade a la lista "vecinos" dos campos, (la clase Y y el valor total del contador de dicha letra o número)
vecinos.append(['Z',cantZ])#se añade a la lista "vecinos" dos campos, (la clase Z y el valor total del contador de dicha letra o número)
vecinos.sort(key=lambda  vecinos: vecinos[1], reverse=True)#se ordena de menor a mayor la lista vecinos para saber que clase es la imagen, de acuerdo a la función mayoria  
print('\nDe acuerdo a la función mayoría, el elemento de prueba es de Clase '+str(vecinos[0][0])+' ∴ la imagen es: '+str(vecinos[0][0]))#impresión final de la clasificación