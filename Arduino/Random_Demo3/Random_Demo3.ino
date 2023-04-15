#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SimpleDHT.h>

// 设置 LiquidCrystal_I2C 对象并指定 I2C 地址
LiquidCrystal_I2C lcd(0x27, 16, 2);

const int pinDHT11 = 7;
const int buttonPin = 2;

SimpleDHT11 dht11; // DHT 11 測量溫濕度
byte temperature = 0; // 溫度
byte humidity = 0; // 濕度
int buttonState = 0; // button 電壓

void setup() {
  Serial.begin(115200);
  randomSeed(analogRead(0)); // 隨機種子
  
  // 初始化 I2C 总线
  Wire.begin();
  // 初始化 LCD
  lcd.init();
  
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("TEMP:   HUMD:");
  lcd.setCursor(0, 1);
  lcd.print("Data:   Mode:");
  
}

void loop() {
  
  // 讀取溫濕度
  if (dht11.read(pinDHT11, &temperature, &humidity, NULL) == SimpleDHTErrSuccess) {
    lcd.setCursor(5, 0);
    lcd.print("   ");
    lcd.setCursor(5, 0);
    lcd.print((int)temperature);
    lcd.setCursor(13, 0);
    lcd.print("   ");
    lcd.setCursor(13, 0);
    lcd.print((int)humidity);
  }
    
  int random_num = random(0, 100); // 0~99 亂數
  //Serial.println(random_num);
  buttonState = digitalRead(buttonPin); // 讀取 button 電壓
  
  if (buttonState == HIGH) {
    lcd.setCursor(13, 1);
    lcd.print("OFF");
  } else {
    lcd.setCursor(13, 1);
    lcd.print("   ");
    lcd.setCursor(13, 1);
    lcd.print("ON");
    lcd.setCursor(5, 1);
    lcd.print("  ");
    lcd.setCursor(5, 1);
    lcd.print(random_num);
    // 傳送
    Serial.print(random_num);
    Serial.print(",");
    Serial.print((int)temperature);
    Serial.print(",");
    Serial.println((int)humidity);
  }
  delay(100);
}