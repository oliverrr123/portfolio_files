#include <Servo.h>
#include <math.h>

int servoPin = 10;
float servoPos = 40;
int photoPin = A0;
int light;

Servo myServo;

void setup() {
  pinMode(photoPin, INPUT);
  Serial.begin(9600);
  while (!Serial) { delay(10); }
  myServo.attach(servoPin);
}

void loop() {
  light = analogRead(photoPin);
  if (light <= 1000. && light >= 940.) {
    servoPos = round(((80./60.) * light - 1333.333333333333) + 80);
  }
  Serial.println((int)light);
//  if ((int)servoPos % 4 == 0) {
//    Serial.println(servoPos);
  myServo.write((int)servoPos); 
//  }
  delay(50);
}
