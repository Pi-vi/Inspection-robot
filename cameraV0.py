from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (920,640)
camera.framerate = 25
camera.brightness = 50
camera.rotation = 0
camera.video_stabilization = True

arq = open("cont.txt","r")
i = arq.readlines()
arq.close()
linhas = len(i)
contador = int(i[linhas-1])
contador+=1
texto = "\n" + time.strftime("%a, %d %b %Y %H:%M:%S") + '\n' + str(contador)
arq = open("cont.txt","a")
arq.write(texto)
arq.close()

Texto1 = "Você está entrando no modo de gravação. Tecle Crtl+C para encerrar a Gravação. Tecle Enter para continuar."
ent1 = input(Texto1)
camera.start_preview(fullscreen=False, window = (50,150,1024,576))
cond = True

marcador = 1

camera.start_preview(fullscreen=False, window = (50,150,1024,576))
camera.start_recording('/home/pi/Desktop/video%s.h264' % contador)

try:
    while cond:
        camera.annotate_text = "Gravando " + time.strftime("%a, %d %b %Y %H:%M:%S")
        time.sleep(1)
except KeyboardInterrupt:
    camera.stop_recording()
    camera.stop_preview()
    cond = False

