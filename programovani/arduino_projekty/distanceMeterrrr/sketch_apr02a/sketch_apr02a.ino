#include <LiquidCrystal.h>

int trigPin = 3;
int echoPin = 4;
int distance;

int rs = 6;
int en = 7;
int d4 = 9;
int d5 = 10;
int d6 = 11;
int d7 = 12;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  lcd.begin(16, 2);
}

void loop() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  distance=pulseIn(echoPin, HIGH) * 0.018;
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(String(distance) + "cm");
  delay(50);
  Serial.println(String(distance) + "cm");
}
