import math
import sys
import time
from grove.adc import ADC


class GroveSoundSensor:
    
    def __init__(self,channel):
        self.channel=channel
        self.adc=ADC()
        
    
    @property
    def sound(self):
        value=self.adc.read(self.channel)
        return value
    

Grove = GroveSoundSensor
def noise_sensor():
    if len(sys.argv)<2:
        print('Usage : {} adc_channel'.format(sys.argv[0]))
        sys.exit(1)
        
    sensor=GroveSoundSensor(int(sys.argv[1]))
    
    print('Detecting sound...')
    
    while True:
        print('Sound Value is: {0}'.format(sensor.sound))
        time.sleep(0.3)
    

if __name__ == '__noise_sensor__': #main-->para cuando tengamos main
    #main()--> para cuando tengamos main
    noise_sensor()