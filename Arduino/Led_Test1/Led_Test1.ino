const int RELAY_PIN_1 = 9;
const int RELAY_PIN_2 = 10;
const int RELAY_PIN_3 = 11;
const int RELAY_PIN_4 = 12;
const int SLEEP = 100;
void setup() {
  pinMode(RELAY_PIN_1, OUTPUT);
  pinMode(RELAY_PIN_2, OUTPUT);
  pinMode(RELAY_PIN_3, OUTPUT);
  pinMode(RELAY_PIN_4, OUTPUT);
}

void loop() {
  digitalWrite(RELAY_PIN_1, HIGH);
  digitalWrite(RELAY_PIN_2, LOW);
  digitalWrite(RELAY_PIN_3, LOW);
  digitalWrite(RELAY_PIN_4, LOW);
  delay(SLEEP);
  digitalWrite(RELAY_PIN_1, LOW);
  digitalWrite(RELAY_PIN_2, HIGH);
  digitalWrite(RELAY_PIN_3, LOW);
  digitalWrite(RELAY_PIN_4, LOW);
  delay(SLEEP);
  digitalWrite(RELAY_PIN_1, LOW);
  digitalWrite(RELAY_PIN_2, LOW);
  digitalWrite(RELAY_PIN_3, HIGH);
  digitalWrite(RELAY_PIN_4, LOW);
  delay(SLEEP);
  digitalWrite(RELAY_PIN_1, LOW);
  digitalWrite(RELAY_PIN_2, LOW);
  digitalWrite(RELAY_PIN_3, LOW);
  digitalWrite(RELAY_PIN_4, HIGH);
  delay(SLEEP);
  digitalWrite(RELAY_PIN_1, LOW);
  digitalWrite(RELAY_PIN_2, LOW);
  digitalWrite(RELAY_PIN_3, HIGH);
  digitalWrite(RELAY_PIN_4, LOW);
  delay(SLEEP);
  digitalWrite(RELAY_PIN_1, LOW);
  digitalWrite(RELAY_PIN_2, HIGH);
  digitalWrite(RELAY_PIN_3, LOW);
  digitalWrite(RELAY_PIN_4, LOW);
  delay(SLEEP);
  
}
