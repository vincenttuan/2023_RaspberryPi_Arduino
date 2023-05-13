import time
import threading
import RPi.GPIO as GPIO

# GPIO 設定 ------------------------------------------------------------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  # GPIO.BOARD, 使用BOARD模式


# Traffic Light (紅綠燈) PIN -------------------------------------------------------------
red_pin = 33  # 紅燈
GPIO.setup(red_pin, GPIO.OUT)
yellow_pin = 35  # 黃燈
GPIO.setup(yellow_pin, GPIO.OUT)
green_pin = 37  # 綠燈
GPIO.setup(green_pin, GPIO.OUT)


def traffic_light_play():
    while True:
        # 綠燈亮 10 秒
        GPIO.output(green_pin, GPIO.HIGH)
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(red_pin, GPIO.LOW)
        time.sleep(10)
        # 黃燈亮 2 秒
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.HIGH)
        GPIO.output(red_pin, GPIO.LOW)
        time.sleep(2)
        # 紅燈亮 10 秒
        GPIO.output(green_pin, GPIO.LOW)
        GPIO.output(yellow_pin, GPIO.LOW)
        GPIO.output(red_pin, GPIO.HIGH)
        time.sleep(10)


if __name__ == '__main__':
    # 紅綠燈執行緒
    t3 = threading.Thread(target=traffic_light_play)
    t3.start()


