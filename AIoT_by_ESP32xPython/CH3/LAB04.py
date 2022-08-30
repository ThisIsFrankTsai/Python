#用手機控制馬達開門或關門

from machine import Pin
from ble_uart import BLE_UART
import time

my_servo=Servo(22)
ble=BLE_UART("door_lock")

while True:
    getValue=ble.get()
    getValue=getValue.lower()
    if(getValue=="open"):
        my_servo.write_angle(0)
        print("Open")
    if(getValue=="close"):
        my_servo.write_angle(90)
        print("close")
    
    time.sleep(1)
    