# 2023_RaspberryPi_Arduino
MQTT
<pre>
為了在 Mac OS 和 Windows 上都能安裝 MQTT 服務器，建議使用 Mosquitto。Mosquitto 是一個開源的 MQTT 代理服務器，支持多個平台。首先，您需要在您的電腦上安裝 Mosquitto。以下是安裝方法：

Mac OS：使用 Homebrew 安裝 Mosquitto：
如果還沒有安裝 Homebrew，請按照官方網站的說明進行安裝：https://brew.sh/
打開 Terminal，然後輸入以下命令安裝 Mosquitto：
brew install mosquitto
對於 Mac OS，打開 Terminal，然後輸入以下命令：
mosquitto 或 /usr/local/sbin/mosquitto
關閉 MQTT: brew services stop mosquitto

Windows：請按照官方網站的說明下載和安裝 Mosquitto：https://mosquitto.org/download/
安裝完成後，您可以啟動 Mosquitto 服務器。
對於 Windows，打開命令提示字元，然後輸入以下命令：
"C:\Program Files\mosquitto\mosquitto.exe"

現在，您可以使用 Python 編寫 MQTT 客戶端。首先，安裝 paho-mqtt Python 庫：
pip install paho-mqtt

接下來，創建一個簡單的 MQTT 客戶端，訂閱主題並發布消息。以下是一個範例：
這個範例會連接到運行在本地的 Mosquitto 服務器，訂閱主題 test/topic，並發布一條消息。當收到新消息時，它會打印主題和消息內容。
my_mqtt_client.py

import paho.mqtt.client as mqtt
# Callbacks
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")

def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")

# Create a client
client = mqtt.Client()

# Assign callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect("localhost", 1883, 60)

# Publish a message
client.publish("test/topic", "Hello MQTT!")

# Start the loop
client.loop_start()

# Run indefinitely
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting...")

# Stop the loop and disconnect
client.loop_stop()
client.disconnect()

</pre>
