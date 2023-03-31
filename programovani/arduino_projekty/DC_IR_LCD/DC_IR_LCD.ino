#include <IRremote.h>
#include <LiquidCrystal.h>
#include <Servo.h>

int rs = 6;
int en = 7;
int d4 = 9;
int d5 = 10;
int d6 = 11;
int d7 = 12;

int irPin = A0;
byte buttonIn;

int in1Pin = 3;
int in2Pin = 4;
int speedPin = 5;

int motState = 0;
int motSpeed = 100;

int servoPos = 90;

//int spinning = 0;
//int spinningDir = 1;

LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
IRrecv IR(irPin);
decode_results cmd;
Servo myServo;

void setup() {
  myServo.attach(8);
  myServo.write(servoPos);
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(speedPin, OUTPUT);
  IR.enableIRIn();
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.clear();
}

void loop() {
  lcd.clear();
  if (motState != 0) {
    lcd.setCursor(0, 0);
    lcd.print("speed: " + String(motSpeed));
    if (motSpeed == 255) { lcd.print(" - MAX"); }
    else if (motSpeed == 100) { lcd.print(" - MIN"); }
    lcd.setCursor(0, 1);
    if (servoPos == 90) {
      lcd.print("angle: 0");
    }
    else {
      lcd.print("angle: " + String(servoPos - 90));
    }
  }
  while (IR.decode(&cmd)==0) { delay(10); }  
  buttonIn = cmd.value;

//  if (spinning == 1) {
//    if (spinningDir == 1) {
//      if (servoPos < 180) {
//        servoPos += 10;
//        myServo.write(servoPos);
//      }
//      else if (servoPos == 180) {
//        spinningDir = -1;
//      }
//    }
//    else if (spinningDir == -1) {
//      if (servoPos < 0) {
//        servoPos -= 10;
//        myServo.write(servoPos);
//      }
//      else if (servoPos == 0) {
//        spinningDir = 1;
//      }
//    }
//  }

  power(buttonIn);
  if (motState != 0) {
    speedControl(buttonIn);
    dirControl(buttonIn);
    speedControlButtons(buttonIn);
    servoManipulating(buttonIn);
  }
  
  Serial.println(motSpeed);

  delay(100);
  IR.resume();
}

void power(byte buttonPressed) {
  if (byte(buttonPressed) == byte(0xFFA25D)) {
    if (motState == 0) {
      motState = 1;
      digitalWrite(in1Pin, HIGH);
      digitalWrite(in2Pin, LOW);
      digitalWrite(speedPin, HIGH);
      delay(50);
      analogWrite(speedPin, motSpeed);
    }
    else {
      motState = 0;
      digitalWrite(speedPin, LOW);
      digitalWrite(in1Pin, LOW);
      digitalWrite(in2Pin, LOW);
    }
  }
  IR.resume();
}

void speedControl(byte buttonPressed) {
  lcd.setCursor(0, 1);
  if (byte(buttonPressed) == byte(0xFF629D)) {
    if (motSpeed == 250) {
      motSpeed += 5;
      analogWrite(speedPin, motSpeed);
    }
    else if (motSpeed < 255) {
      motSpeed += 10;
      analogWrite(speedPin, motSpeed);
    }
  }
  else if (byte(buttonPressed) == byte(0xFFA857)) {
    if (motSpeed == 100) {}
    else if (motSpeed == 255) {
      motSpeed -= 5;
      analogWrite(speedPin, motSpeed);
    }
    else if (motSpeed > 0) {
      motSpeed -= 10;
      analogWrite(speedPin, motSpeed);
    }
  }
  IR.resume();
}

void dirControl(byte buttonPressed) {
  if (byte(buttonPressed) == byte(0xFFC23D)) {
    Serial.println("dir1");
    digitalWrite(in1Pin, HIGH);
    digitalWrite(in2Pin, LOW);
  }
  else if (byte(buttonPressed) == byte(0xFF22DD)) {
    Serial.println("dir2");
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, HIGH);
  }
  IR.resume();
}

void speedControlButtons(byte buttonPressed) {
  if (byte(buttonPressed) == byte(0xFF6897)) {
    motSpeed = 100;
    analogWrite(speedPin, motSpeed);
  }
  else if (byte(buttonPressed) == byte(0xFF30CF)) {
    motSpeed = 140;
    analogWrite(speedPin, motSpeed);
  }
  else if (byte(buttonPressed) == byte(0xFF18E7)) {
    motSpeed = 160;
    analogWrite(speedPin, motSpeed);
  }
  else if (byte(buttonPressed) == byte(0xFF7A85)) {
    motSpeed = 180;
    analogWrite(speedPin, motSpeed);
  }
  else if (byte(buttonPressed) == byte(0xFF38C7)) {
    motSpeed = 200;
    analogWrite(speedPin, motSpeed);
  }
  else if (byte(buttonPressed) == byte(0xFF5AA5)) {
    motSpeed = 220;
    analogWrite(speedPin, motSpeed);
  }
  else if (byte(buttonPressed) == byte(0xFF4AB5)) {
    motSpeed = 240;
    analogWrite(speedPin, motSpeed);
  }
  else if (byte(buttonPressed) == byte(0xFF52AD)) {
    motSpeed = 255;
    analogWrite(speedPin, motSpeed);
  }
}

void servoManipulating(byte buttonPressed) {
  if (byte(buttonPressed) == byte(0xFF906F)) {
    if (servoPos < 180) {
      servoPos += 10;
      myServo.write(servoPos);
    }
  }
  else if (byte(buttonPressed) == byte(0xFFE01F)) {
    if (servoPos > 0) {
      servoPos -= 10;
      myServo.write(servoPos);
    }
  }
//  else if (byte(buttonPressed) == byte(0xFF02FD)) {
//    if (spinning == 0) {
//      spinning = 1;
//      servoPos = 90;
//      myServo.write(servoPos);
//    }
//    else {
//      spinning = 0;
//      servoPos = 90;
//      myServo.write(servoPos);
//    }
//  }
}
