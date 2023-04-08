import serial


if __name__ == '__main__':
    ser = serial.Serial('COM5', 115200)
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode().rstrip()
            print("收到 arduino 的資料:", data)
