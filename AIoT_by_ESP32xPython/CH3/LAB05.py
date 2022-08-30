#回傳溫度到手機

from machine import Pin,ADC
from ble_uart import BLE_UART
import time

my_servo=Pin(32)
adc=ADC(adc_pin)

adc.width(ADC.WIDTH_12BIT)
adc.atten(ADC.ATTN_11DB)

ble=BLE_UART("temperature")

while True:
    vol=(adc.read()/4095)*3.6
    tem=(vol-0.5)*100
    print("tempature:",tem)
    ble.send('temperature:'+str(tem))
    time.sleep(1)
    