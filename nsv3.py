import math
import sys
import time
import datetime
from datetime import date
import MySQLdb
from math import log    
from grove.adc import ADC
from grove.grove_sound_sensor import GroveSoundSensor

#this is in order to connect with the database before created
database= MySQLdb.connect(host="localhost", user="farmer3", passwd="farmer3", database="noisedb")

#to create cursor for the queries
cursor=database.cursor()

 # connect to alalog pin 2(slot A2)


__all__ = ['GroveSoundSensor']


class GroveSoundSensor:
    
    def __init__(self,channel): 
        self.channel=channel
        self.adc=ADC()
        
    
    @property
    def sound(self):
        value=self.adc.read(self.channel)
        voltage = value*(3.3/1024.0)
        dB = 20*log(voltage/3.3)
        return dB + 20             
Grove = GroveSoundSensor

def noise_sensor():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.ADC)
    pin = 2
    
    sensor = GroveSoundSensor(pin)

    # if len(sys.argv)<1:
    # 	print('Usage : {} adc_channel'.format(sys.argv[0]))
     # 		sys.exit(1)
        
   # sensor=GroveSoundSensor(int(sys.argv[1]))
    
    print('Detecting sound...')
    
    while True:
        print('Sound Value is: {0}'.format(sensor.sound))
        time.sleep(0.3)
        
        #cursor.execute('''INSERT INTO captured_noise(decibels) VALUES (%f);''', (sensor))
        database.commit()


def main():
    print("PORFAVOR FUNCIONA")
    noise_sensor()


if __name__ == '__main__': #main-->para cuando tengamos main
#if __name__ == '__noise_sensor__': #main-->para cuando tengamos main
    main()
   
    

