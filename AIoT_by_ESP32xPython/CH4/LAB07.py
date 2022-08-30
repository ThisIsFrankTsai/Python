#建立ESP32無線網路

import network
import time
import urequests
import esp32

url="https://maker.ifttt.com/trigger/Box/json/with/key/gbHGFvF9g8zMrO3hZbJEd"

sta=network.WLAN(network.STA_IF)
sta.active(True)
sta.connect('Justin Iphone','franktsai')

while not sta.isconnected():
    pass

print("Wi-Fi 連線成功")


#response=urequests.get("請求路徑")

while True:
    hall=esp32.hall_sensor()
    print(hall)
    if (hall <100 and hall>0) :
          print("Error")
          res=urequests.get(url)
          if (res.status_code ==200):
              print("成功")
          else:
              print("失敗")
              print("錯誤碼:",res.status_code )
          res.close()
          time.sleep(10)
    time.sleep(0.5)