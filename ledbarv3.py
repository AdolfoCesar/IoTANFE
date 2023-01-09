import time
from rpi_ws281x import PixelStrip, Color
from grove.grove_ws2813_rgb_led_strip import GroveWS2813RgbStrip

# LED strip configuration
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

        # connect to pin 12(slot PWM)
PIN   = 12
        # For Grove - WS2813 RGB LED Strip Waterproof - 30 LED/m
        # there is 30 RGB LEDs.
COUNT = 10
strip = GroveWS2813RgbStrip(PIN, COUNT)
#ARGUMENTS
#PIN(int)  : 12 #18 for RPi
#COUNT(int) #: #strip LEDs count
#brightness(int) #: #optional, set to 0 for darkest and 255 for brightest, default 255
        # Define functions which animate LEDs in various ways.

def colorWipe(strip, color, wait_ms=50):
            #Wipe color across display a pixel at a time.
    for i in range(strip.numPixels()):
         strip.setPixelColor(i, color)
         strip.show()
         time.sleep(wait_ms/1000.0)
print ('Color wipe animations.')
colorWipe(strip, Color(255, 0, 0))  # Red wipe
colorWipe(strip, Color(0, 255, 0))  # Blue wipe
colorWipe(strip, Color(0, 0, 255))  # Green wipe
