from servo import Servo
from machine import Pin
import time

while True:
    my_servo=Servo(Pin(22))

    my_servo.write_angle(90)
    time.sleep(1)

    my_servo.write_angle(0)
    time.sleep(1)

