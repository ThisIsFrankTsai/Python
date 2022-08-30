from machine import Pin,ADC
import time

led=Pin(5,Pin.OUT)

while True:
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)

  