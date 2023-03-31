#include <LiquidCrystal.h>

int rs = 6;
int en = 7;
int d4 = 9;
int d5 = 10;
int d6 = 11;
int d7 = 12;

byte num = B00000000;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
 lcd.begin(16, 2);
}

void loop() {
  lcd.setCursor(0, 0);
  lcd.print("Hello, World!");
  lcd.setCursor(0, 1);
  lcd.print(num, BIN);
  delay(250);
  lcd.clear();
  num += 1;
}
