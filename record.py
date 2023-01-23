import cv2
import time
import os
    
cap= cv2.VideoCapture(0)                                                        #Iniciamos la camara
cap.set(3,1280)                                                                 #Inicializamos los valores de la imagen
cap.set(4,720)
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
horas = time.ctime(time.time()).replace(' ','_').replace(':','-')               #Inicializamos el contador
cont_elimina = 0                                                                #Inicializamos variables auxiliares
cont_video = 0 
fourcc1 = cv2.VideoWriter_fourcc(*'mp4v')                                       #Seleccionamos el codec ### fourcc2 =  cv2.VideoWriter_fourcc(*'DIVX')
path = './videos/'                                                              #Definimos el path donde se guardarán los videos
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
    
    if len(os.listdir(path))>23:                                                #Definimos el numero total de videos que se van a guardar (24)
        for p in os.listdir(path):                                              #Eliminamos el vídeo más antiguo
            if 'video'+str(cont_elimina)+'-' in p:
                os.remove(path+p)
                break
        cont_video = cont_elimina
        cont_elimina = 0 if cont_elimina==24 else cont_elimina+1
    else:                                                                       #Almacenamos los primeros 24 vídeos
        cont_video = 0 if cont_video == 24 else cont_video+1
