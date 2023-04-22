import smbus2  # 引入 smbus2 模組來與 I2C 介面的裝置進行通訊
# 安裝 sudo apt-get install python3-smbus
import time    # 引入 time 模組來暫停程式執行

# 定義 I2C 介面的地址和設備 ID
bus = smbus2.SMBus(1)
addr = 0x27

# 定義讀取資料的函數，此處返回固定字串 "37,28,50,1,0,0,0"
def read_data():
    return "37,28,50,1,0,0,0"  # 模擬得到 Arduino 傳來的資料

# 初始化 LED 顯示器
def lcd_init():
    bus.write_byte(addr, 0x38)  # 傳送 0x38 給指定的 I2C 位址，用於設置 16x2 LED 顯示器
    bus.write_byte(addr, 0x08)  # 傳送 0x08 給指定的 I2C 位址，用於關閉顯示器的顯示
    bus.write_byte(addr, 0x01)  # 傳送 0x01 給指定的 I2C 位址，用於清除顯示器內容

# 寫入資料到 LED 顯示器
def lcd_write(message):
    # 將字串轉換為字元陣列
    message = [ord(i) for i in message]
    # 寫入字元陣列
    for i in message:
        bus.write_byte_data(addr, 0x40, i)

# 清除 LED 顯示器的內容
def lcd_clear():
    bus.write_byte(addr, 0x01)

# 初始化 LED 顯示器
lcd_init()

# 寫入資料到 LED 顯示器
lcd_write(read_data())

# 暫停 10 秒後清除顯示器內容
time.sleep(10)
lcd_clear()
