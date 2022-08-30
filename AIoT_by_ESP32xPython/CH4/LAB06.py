#檢查磁鐵是否有遠離ESP32，可以當作保險箱是否有被開啟

import esp32
import time

while True:
    hall=esp32.hall_sensor()
    print(hall)
    if (hall<100 and hall>0):
        print("open")
    time.sleep(0.1)
