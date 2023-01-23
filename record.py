import cv2
import time
import os

#Iniciamos la camara
cap= cv2.VideoCapture(0) 

#Inicializamos los valores de la imagen
cap.set(3,1280)
cap.set(4,720)
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Inicializamos el contador
horas = time.ctime(time.time()).replace(' ','_').replace(':','-')

#Inicializamos variables auxiliares
cont_elimina = 0
cont_video = 0 

#Seleccionamos el codec
fourcc1 = cv2.VideoWriter_fourcc(*'mp4v') # fourcc2 =  cv2.VideoWriter_fourcc(*'DIVX')

#Definimos el path donde se guardarán los videos
path = './videos/'

while True:
    name = path+'video'+str(cont_video)+'-'+horas+'.mp4'
    writer= cv2.VideoWriter(name,fourcc1, 60, (width,height))
    while True:
        ret,frame= cap.read()
        writer.write(frame)

        next = int(horas.split('_')[3].split('-')[0])+1
        cont = 0 if next >= 24 else next

        if cont == int(time.ctime(time.time()).split(' ')[3].split(':')[0]): 
            horas = time.ctime(time.time()).replace(' ','_').replace(':','-') 
            break

    if len(os.listdir(path))>23: #definimos el numero total de videos que se van a guardar
        for p in os.listdir(path):
            if 'video'+str(cont_elimina)+'-' in p:
                os.remove(path+p)
        cont_video = cont_elimina
        cont_elimina +=1
        if cont_elimina == 24:
            cont_elimina = 0
    else: #guardamos los primeros videos
        cont_video +=1
        if cont_video ==24:
            cont_video = 0
