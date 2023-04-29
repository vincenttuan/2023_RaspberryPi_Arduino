import time

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from RPLCD.i2c import CharLCD

reader = SimpleMFRC522()
lcd = CharLCD('PCF8574', address=0x27, port=1, backlight_enabled=True)

# 設置蜂鳴器引腳和模式
buzzer_pin = 12  # 根據BOARD模式，將BCM 18對應的引腳更改為12
GPIO.setmode(GPIO.BOARD)  # GPIO.BOARD, 使用BOARD模式
GPIO.setup(buzzer_pin, GPIO.OUT)
# LCD clear
lcd.clear()
try:

    while True:
        print("請將卡靠近讀卡器...")
        GPIO.output(buzzer_pin, GPIO.LOW)
        id, text = reader.read()
        GPIO.output(buzzer_pin, GPIO.HIGH)
        print("ID: %s\nText: %s" % (id, text))
        # 顯示在 LCD 螢幕上
        lcd.cursor_pos = (0, 0)
        lcd.write_string(text)
        
        time.sleep(0.1)
        GPIO.output(buzzer_pin, GPIO.LOW)
        time.sleep(0.1)  # 在讀取到卡片後等待一段時間
finally:
    GPIO.cleanup()