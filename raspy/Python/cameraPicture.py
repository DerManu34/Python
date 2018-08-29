from picamera import PiCamera
from time import sleep
import time
import datetime


class MyCamera():
    def takePicture():
        camera = PiCamera()
        try:
            camera.start_preview()
            for i in range(1, 3):        
                sleep(2)
                current_time = time.time()
                #current_time_string = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')
                camera.capture("/home/pi/Dokumente/Python/pictures/test_%i_%i.jpg" % (i, current_time))
        finally:
            camera.stop_preview()
            camera.close()
            return 1

