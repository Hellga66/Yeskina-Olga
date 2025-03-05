import RPi.GPIO as GPIO
import time 

dac=[8,11,7,1,0,5,12,6]
comp=14
troyka=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
def decimal2binary(value):
    return list (map(int, bin(value)[2:].zfill(8)))

def adc():
    for i in range(256):
        GPIO.output(dac,decimal2binary(i))
        time.sleep(0.01)
        if GPIO.input(comp)==1:
            return i
try:
    while True:
        value= adc()
        print(value,value/255*3.3)

finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.cleanup()