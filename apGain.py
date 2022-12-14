
# Simple demo of the TSL2591 sensor.  Will print the detected light value
# every second.
import time
import board
import adafruit_tsl2591

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize the sensor.
sensor = adafruit_tsl2591.TSL2591(i2c)

# You can optionally change the gain and integration time:
# sensor.gain = adafruit_tsl2591.GAIN_LOW (1x gain)
# sensor.gain = adafruit_tsl2591.GAIN_MED (25x gain, the default)
# sensor.gain = adafruit_tsl2591.GAIN_HIGH (428x gain)
# sensor.gain = adafruit_tsl2591.GAIN_MAX (9876x gain)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS (100ms, default)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_200MS (200ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_300MS (300ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_400MS (400ms)
sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_500MS (500ms)
# sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_600MS (600ms)

## lower gain means we need to have a longer integration time. I think 500ms is a reasonable integration time. 

# Read the total lux, IR, and visible light levels and print it every second.

currentGain = 2
while True:
    try: # now we're 
        if 
        # Read and calculate the light level in lux.
        lux = sensor.lux # this is where things will start to fail if we have the gain wrong
        # basically if there is too much light, the sensor tries to use a number that's too big to represent it and it crashes. 
        # i'm not sure how many places break in the above scenario so it's easier to catch the whole loop and then adjust the gain.
        print("Total light: {0}lux".format(lux))
        # You can also read the raw infrared and visible light levels.
        # These are unsigned, the higher the number the more light of that type.
        # There are no units like lux.
        # Infrared levels range from 0-65535 (16-bit)
        infrared = sensor.infrared
        print("Infrared light: {0}".format(infrared))
        # Visible-only levels range from 0-2147483647 (32-bit)
        visible = sensor.visible
        print("Visible light: {0}".format(visible))
        # Full spectrum (visible + IR) also range from 0-2147483647 (32-bit)
        full_spectrum = sensor.full_spectrum
        print("Full spectrum (IR + visible) light: {0}".format(full_spectrum))
        time.sleep(1.0)
    catch Exception as e:
        print("something failed")
        print(e)
        # let's change the gain
        currentGain = currentGain-1
        if currentGain <1:
            currentGain = 1
            sensor.gain = adafruit_tsl2591.GAIN_LOW# (1x gain)
        elif currentGain == 2:
            currentGain = 1
            sensor.gain = adafruit_tsl2591.GAIN_LOW# (1x gain)
        elif currentGain == 3:
            currentGain = 2
            sensor.gain = adafruit_tsl2591.GAIN_MED# (1x gain)
        elif currentGain == 4:
            currentGain = 3
            sensor.gain = adafruit_tsl2591.GAIN_HIGH# (1x gain)
        elif currentGain == 5:
            currentGain = 4
            sensor.gain = adafruit_tsl2591.GAIN_MAX# (1x gain)


            
        #https://blog.finxter.com/how-to-catch-and-print-exception-messages-in-python/
