import RPi.GPIO as GPIO
import time

ledPins=12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPins, GPIO.OUT)
    GPIO.output(GPIO.HIGH, ledPins)
    
def loop():
    while True:
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(pin, GPIO.HIGH)

def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    print('Program is starting')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()