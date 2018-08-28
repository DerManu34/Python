import RPi.GPIO as GPIO
import time
from cameraPicture import MyCamera
import webbrowser




class DetectorClass:
    def __init__(self):
        self.sensor_pin = 23
    def main_callback(self, channel):
        print('Es gab eine Bewegung. Starte Kamera')
        cameraReady = MyCamera.takePicture()
        self.startDetection()
    def startDetection(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.sensor_pin, GPIO.IN)
        print('legen los')
        try:
            GPIO.add_event_detect(self.sensor_pin, GPIO.RISING)
            while True:
                    if GPIO.event_detected(self.sensor_pin):
                        GPIO.remove_event_detect(self.sensor_pin)
                        self.main_callback(self.sensor_pin)
                    else:
                        print('einfach nur Stille!!!')
        except KeyboardInterrupt:
            print ("Beende...")
        
        GPIO.cleanup()

print('geht hier irgendwas?')

detector = DetectorClass()
detector.startDetection()