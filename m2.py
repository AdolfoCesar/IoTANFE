import math
import sys
import time
import datetime
import MySQLdb
import RPi.GPIO as GPIO
import array
import smtplib
from datetime import date
from math import log    
from grove.adc import ADC
from grove.grove_sound_sensor import GroveSoundSensor
from email.message import EmailMessage

#this is in order to connect with the database before created from CMD
database= MySQLdb.connect(host="localhost", user="farmer3", passwd="farmer3", database="noisedb")

#to create cursor for the queries
cursor=database.cursor()

#LED BAR SECTION

# Pin Definitons:
led_bar = 12

#### MY9221 
ON = 0x00ff#8-bit 1 data
SHUT = 0x0000#8-bit 0 data
CmdMode = 0x0000#Work on 8-bit mode

def send16bitData(data):
    # Pin Setup for led bar:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_bar,GPIO.OUT,initial=GPIO.LOW)
    GPIO.setup(led_bar+1,GPIO.OUT,initial=GPIO.LOW)
    clk_pin_state = False
    for i in range(16):
        if (data&0x8000):
            GPIO.output(led_bar,1)
        else:
            GPIO.output(led_bar,0)
        clk_pin_state = not clk_pin_state
        GPIO.output(led_bar+1,clk_pin_state)
        data = (data<<1)
        time.sleep(0.00001)


def latchdata():#latch routine for MY9221 data exchange
        data_pin_state = False
        GPIO.output(led_bar,data_pin_state)
        time.sleep(0.0003)
        for i in range(8):
                data_pin_state = not data_pin_state
                GPIO.output(led_bar,data_pin_state)
                time.sleep(0.0003)


def sendled(ledstate):
    send16bitData(CmdMode)#set LED Bar mode
    for i in range(12):
        if (ledstate&0x0001):
            send16bitData(ON)
        else:
            send16bitData(SHUT)
        ledstate = (ledstate>>1)
    latchdata()#make it come into effect

#MAIN LED_BAR METHOD
def sendbar(ledstate=[0,0,0,0,0,0,0,0,0,0], delay=0):
    ledstate.extend([0,0])#MY9221 has 12 lines, we need to add two
    send16bitData(CmdMode) #set LED Bar mode
    for i in range(12):
        if (ledstate[i] <= 0) or (ledstate[i] >= 6):#some input checking
            send16bitData(SHUT)
        elif (ledstate[i] == 1):
                        send16bitData(ON)
        else:
            send16bitData(ON >> ledstate[i])
    latchdata()#make it come into effect
    time.sleep(delay)
    
    
try:  
    sendbar()
  
except:
    print ("An error or exception occurred!")
  
finally:
    sendbar()
    time.sleep(0.5)
    GPIO.cleanup() #this ensures a clean exit  


#SOUND SENSOR PART
__all__ = ['GroveSoundSensor']

class GroveSoundSensor:
    
    def __init__(self,channel): 
        self.channel=channel
        self.adc=ADC()
        
    
    @property
    def sound(self):
        value=self.adc.read(self.channel)
        voltage=value*(3.3/1024.0)
        dB= 80 *log(voltage/3.3)
        return dB/-2
    
Grove = GroveSoundSensor

def noise_sensor():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.ADC)
    pin = 2 #pin in which we have connected the noise sensor
    
    sensor = GroveSoundSensor(pin)
    
    print('Detecting sound...')
    
    while True:
        print('Sound Value is: {0}'.format(sensor.sound))
        time.sleep(0.3)
        
        cursor.execute("INSERT INTO captured_noise(decibels) VALUES (%s)", [format(sensor.sound)])
        database.commit()
        led_delay=0.05
        
        if(float (format(sensor.sound))<10.0):
            sendbar([0,0,0,0,0,0,0,0,1,1],led_delay)
        elif(float(format(sensor.sound))>10.0 or float(format(sensor.sound))<19.0):
            sendbar([0,0,0,0,0,0,1,1,1,1],led_delay)
        elif(float(format(sensor.sound))>20.0 or float(format(sensor.sound))<29.0):
            sendbar([0,0,0,0,1,1,1,1,1,1],led_delay)
        elif(float(format(sensor.sound))>30.0 or float(format(sensor.sound))<35.0):
            sendbar([0,0,1,1,1,1,1,1,1,1],led_delay)
        elif(float(format(sensor.sound))>35.0 or float(format(sensor.sound))<50.0):
            sendbar([1,1,1,1,1,1,1,1,1,1],led_delay)
            
            FROM = "chillafterstudy@gmail.com"
            TO = "uxuegarciaugarte@opendeusto.es" #email of farmer
            message = "¡WARNING! Too much noise :("
            
            email = EmailMessage()
            email["From"] = FROM
            email["To"] = TO
            email["Subject"] = "Correo de prueba"
            email.set_content(message)

            smtp = smtplib.SMTP_SSL("smtp.gmail.com")
            smtp.login(FROM, "cdfhgkfaomjmpblr")
            smtp.sendmail(FROM, TO, email.as_string())
            smtp.quit()
            

def main():
    noise_sensor()

if __name__ == '__main__': 
    main()
   
