import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

# Define pins 
# Don't have access to an ultrasonic distance sensor so using a motion sensor instead
SIGNAL = 14
BUZZER = 12

# Setup pins
GPIO.setup(SIGNAL, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

# Inititialise buzzer
pwm = GPIO.PWM(BUZZER, 500)
pwm.start(0)

# calculate the duration the sensor detected motion for
def timeMotion():
    measure = 0

    while GPIO.input(SIGNAL):
        time.sleep(1)
        measure += 1

    return measure

try:
    while True:
        measure = timeMotion()
        time.sleep(0.05)
        print(measure)
        
        if ( measure <= 10 ):
            pwm.start(10)
            time.sleep(1)
            pwm.stop()
    
        else:
            pwm.start(50)
            time.sleep(1)
            pwm.stop()

except KeyboardInterrupt:
    GPIO.cleanup()
