#控制馬達開關

from ble_uart import BLE_UART
from servo import Servo
from machine import Pin

my_servo=Servo(Pin(22))
ble=BLE_UART("door_lock")

while True:
    getValue=ble.get()
    getValue=getValue.lower()
    if(getValue =="open"):
        my_servo.write_angle(0)
        print("open")
    if(getValue=="close"):
        my_servo.write_angle(90)
        print("close")