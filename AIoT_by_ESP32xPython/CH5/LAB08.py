import tm1637
import time
from machine import Pin


tm=tm1637.TM1637(clk=Pin(16),dio=Pin(17))
while True:
    t=time.localtime()
    tm.numbers(t[3],t[4])
