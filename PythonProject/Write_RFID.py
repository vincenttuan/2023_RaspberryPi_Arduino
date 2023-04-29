import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    data_to_write = "Hello RFID"
    print("請將卡靠近讀卡器，以便將數據寫入...")
    reader.write(data_to_write)
    print("資料已寫入 RFID 卡")

finally:
    GPIO.cleanup()
