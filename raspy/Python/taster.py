import RPi.GPIO as GPIO
import time
import client
import webbrowser

SENSOR_PIN = 2

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

cs_01 = 0

def main_callback(channel):
    print('Es gab eine Bewegung')
try:
    print('try')
    cs_01 = GPIO.input(SENSOR_PIN)
    print(cs_01)
    while True:
        if GPIO.input(SENSOR_PIN) == 0:
            print('ist aus')
        else:
            print('ist an')

except KeyboardInterrupt:
    print ("Beende...")
    
GPIO.cleanup()
