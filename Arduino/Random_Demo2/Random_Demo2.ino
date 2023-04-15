#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// 设置 LiquidCrystal_I2C 对象并指定 I2C 地址
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(115200);
  randomSeed(analogRead(0)); // 隨機種子
  
  // 初始化 I2C 总线
  Wire.begin();
  // 初始化 LCD
  lcd.init();
  // 在第一行上显示一条消息
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Data:");
  lcd.setCursor(0, 1);
  lcd.print("Mode:");
}

void loop() {
  int random_num = random(0, 100); // 0~99 亂數
  Serial.println(random_num);
  lcd.setCursor(5, 0);
  lcd.print("  ");
  lcd.setCursor(5, 0);
  lcd.print(random_num);
  delay(100);
}