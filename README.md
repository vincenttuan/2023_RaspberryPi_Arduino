# 2023_RaspberryPi_Arduino
0.96inch_SPI_OLED_Module
<pre>
http://www.lcdwiki.com/0.96inch_SPI_OLED_Module
</pre>
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
允許其他電腦連接到 Mosquitto MQTT
<pre>
要允許其他電腦（具有不同 IP 地址）連接到 Mosquitto MQTT 代理，您需要創建一個配置文件，並在其中定義一個監聽器，以便允許遠程訪問。請按照以下步驟操作：
在 /usr/local/etc/mosquitto 目錄下（或您選擇的其他位置）創建一個名為 mosquitto.conf 的文件。
使用文本編輯器打開 mosquitto.conf，然後添加以下行以定義一個監聽器：

listener 1883
allow_anonymous true

這將允許 MQTT 代理在端口 1883 上監聽所有接入的連接，並允許匿名連接。為了安全起見，您可以考慮使用身份驗證和加密，而不是允許匿名連接。有關如何配置身份驗證和加密的更多信息，請查看 Mosquitto 文檔。
保存並關閉 mosquitto.conf 文件。
停止當前運行的 Mosquitto 實例（如果有的話）。您可以使用以下命令停止它：
使用新的配置文件重新啟動 Mosquitto：
/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf

現在，您的 Mosquitto MQTT 代理應該允許來自具有不同 IP 地址的其他電腦的連接。請注意，您需要確保您的網絡防火牆允許流量通過端口 1883。

</pre>

# OpenCV
<pre>
一、安裝 PIL :
pip install pillow

二、安裝 py-opencv :
2.1、反安裝(若之前有其他本):
     pip uninstall opencv-contrib-python
     pip uninstall opencv-python
2.2、再安裝:
     pip install opencv-python
     pip install opencv-contrib-python
</pre>
