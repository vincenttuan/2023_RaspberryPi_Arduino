import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    print("請將卡靠近讀卡器...")
    id, text = reader.read()
    print("ID: %s\nText: %s" % (id, text))

finally:
    GPIO.cleanup()
