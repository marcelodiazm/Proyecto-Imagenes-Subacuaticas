from tkinter import*
import cv2
import numpy as np
import time
#Función draw_text: genera un rectángulo y agrega texto en él. 
def draw_text(img, text,
          font=cv2.FONT_HERSHEY_PLAIN,
          pos=(0, 0),
          font_scale=1,
          font_thickness=1,
          text_color=(0, 255, 0),
          text_color_bg=(0, 0, 0)
          ):

    x, y = pos
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_w, text_h = text_size
    cv2.rectangle(img, pos, (x + text_w, y + text_h), text_color_bg, -1)
    cv2.putText(img, text, (x, y + text_h + font_scale - 1), font, font_scale, text_color, font_thickness)

    return text_size
#Funcion images: Pone 4 videos en comparación y agrega sus metricas
def images(list_data):
    cap = [cv2.VideoCapture(i) for i in list_data]
    frames = [None] * len(names)
    ret = [None] * len(names)
    for i in cap:
        if (i.isOpened()== False): 
            print("Error opening video stream or file")

    while True:
        for i,c in enumerate(cap):
            if c is not None:
                ret[i], frames[i] = c.read()


        
        if (ret[0]&ret[1]&ret[2]&ret[3]) is True:
            new_width = int(frames[0].shape[1]/2)
            new_height = int(frames[0].shape[0]/2)

            frame_half = cv2.resize(frames[0], (new_width, new_height))

            frame_half_2 = cv2.resize(frames[1], (new_width, new_height))

            frame_half_3 = cv2.resize(frames[2], (new_width, new_height))

            frame_half_4 = cv2.resize(frames[3], (new_width, new_height))

            Hori = np.concatenate((frame_half, frame_half_2), axis=1)
            Hori2 = np.concatenate((frame_half_3, frame_half_4), axis=1)

            draw_text(Hori, "SeaTru", pos=(7, 25), text_color_bg=(0, 0, 0), text_color=(255,255,255))
            draw_text(Hori2, "Video Processing", pos=(7, 25), text_color_bg=(0, 0, 0), text_color=(255,255,255))

            draw_text(Hori, "Metricas: blablablabla", pos=(1050, 300), text_color_bg=(0, 0, 0), text_color=(255,255,255))
            draw_text(Hori, "blablablablablablablabla", pos=(1050, 315), text_color_bg=(0, 0, 0), text_color=(255,255,255))
            draw_text(Hori, "blablablablablablablabla", pos=(1050, 330), text_color_bg=(0, 0, 0), text_color=(255,255,255))
            
            draw_text(Hori2, "Metricas: blablablabla", pos=(1050, 300), text_color_bg=(0, 0, 0), text_color=(255,255,255))
            draw_text(Hori2, "blablablablablablablabla", pos=(1050, 315), text_color_bg=(0, 0, 0), text_color=(255,255,255))
            draw_text(Hori2, "blablablablablablablabla", pos=(1050, 330), text_color_bg=(0, 0, 0), text_color=(255,255,255))

            Verti = np.concatenate((Hori, Hori2), axis=0)
            cv2.imshow("ELO328", Verti)
            time.sleep(0.03333)
            #cv2.imshow('HORIZONTAL', Hori)
            #cv2.imshow('VERTICAL', Verti)
        else:
            for i,c in enumerate(cap):
                if(ret[i] == False):
                    c.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    for c in cap:
        if c is not None:
            c.release()

    cv2.destroyAllWindows()

names = ['data/seatru_antes.mp4', 'data/seatru_despues.avi', 'data/metodo2_antes.mp4', 'data/metodo2_despues.avi']
images(names)
