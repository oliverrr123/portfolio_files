#include <U8g2lib.h>
#include <Arduino.h>
#include <Wire.h>

U8G2_SH1106_128X64_NONAME_F_HW_I2C u8g2(U8G2_R0, U8X8_PIN_NONE);

int displayWidth;
int displayHeight;

String timeTxt;

void setup(void) {
  Serial.begin(9600);
  u8g2.begin();
  u8g2.enableUTF8Print();
  u8g2.setFont(u8g2_font_courB18_tf); // 15px
  u8g2.setDrawColor(1);
  displayWidth = u8g2.getDisplayWidth();
  displayHeight = u8g2.getDisplayHeight();
//  u8g2.setFontDirection(0);
  u8g2.clearDisplay();
  u8g2.setCursor((displayWidth/2)-(u8g2.getStrWidth("00:00:00")/2), (displayHeight/2)+7);
  delay(1000);
}

void loop(void) {
  u8g2.clearBuffer();
  u8g2.setCursor((displayWidth/2)-(u8g2.getStrWidth("POWER ON")/2), (displayHeight/2)+7);
  u8g2.setDrawColor(1);
  u8g2.print("POWER ON");
  u8g2.sendBuffer();
  delay(2000);
  u8g2.clearBuffer();
  delay(1000);
  for (float x=0; x<displayHeight*2; x++) {
//    u8g2.clearBuffer();
    Serial.println("circleee");
    u8g2.drawDisc(displayWidth/2, displayHeight/2, x, U8G2_DRAW_ALL);
    u8g2.sendBuffer();
    x+=x*0.1;
  }
  u8g2.setDrawColor(0);
  for (float x=0; x<displayHeight*2; x++) {
//    u8g2.clearBuffer();
    Serial.println("circleee");
    u8g2.drawDisc(displayWidth/2, displayHeight/2, x, U8G2_DRAW_ALL);
    u8g2.sendBuffer();
    x+=x*0.1;
  }
  u8g2.clearBuffer();
  u8g2.setDrawColor(1);
  delay(100);
  u8g2.setCursor(4, 40);
  while (true) {
    while (Serial.available()==0) { delay(10); }
    u8g2.clearBuffer();
    u8g2.print(Serial.readStringUntil('\r'));
    u8g2.sendBuffer();
    u8g2.setCursor(4, 40);
    delay(500);
  }
}
