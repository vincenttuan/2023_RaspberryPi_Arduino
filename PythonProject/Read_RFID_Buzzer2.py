import time

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

# 設置蜂鳴器引腳和模式
buzzer_pin = 12  # 根據BOARD模式，將BCM 18對應的引腳更改為12
GPIO.setmode(GPIO.BOARD)  # GPIO.BOARD, 使用BOARD模式
GPIO.setup(buzzer_pin, GPIO.OUT)

# 設置蜂鳴器的PWM頻率
buzzer_pwm = GPIO.PWM(buzzer_pin, 1000)  # 1000Hz的頻率
buzzer_pwm.start(0)  # 開始PWM，占空比為0（靜音）

try:
    while True:
        print("請將卡靠近讀卡器...")
        buzzer_pwm.ChangeDutyCycle(0)  # 設置占空比為0%（靜音）
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id, text))
        buzzer_pwm.ChangeDutyCycle(50)  # 設置占空比為50%（發聲）
        time.sleep(0.1)
        buzzer_pwm.ChangeDutyCycle(0)  # 設置占空比為0%（靜音）
        time.sleep(0.1)  # 在讀取到卡片後等待一段時間
finally:
    buzzer_pwm.stop()  # 停止PWM
    GPIO.cleanup()
