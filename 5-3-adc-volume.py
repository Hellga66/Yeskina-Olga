import RPi.GPIO as GPIO
import time 

dac=[8,11,7,1,0,5,12,6]
leds=[2,3,4,17,27,22,10,9]
comp=14
troyka=13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)
def decimal2binary(value):
    return list (map(int, bin(value)[2:].zfill(8)))

def adc():
    a=[0]*8
    for i in range(8):
        a[i]=1
        GPIO.output(dac,a)
        time.sleep(0.01)
        if GPIO.input(comp)==1:
            a[i]=0

    return int(''.join(map(str, a)),2)
        
try:
    while True:
        value= adc()
        n=2**(int(value/255*8))-1
        GPIO.output(leds,decimal2binary(n))
        

finally:
    GPIO.output(dac,0)
    GPIO.output(troyka,0)
    GPIO.cleanup()