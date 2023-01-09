import RPi.GPIO as GPIO
import time
wait = 0.5
PIN = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)
while True:
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(wait)
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(wait)