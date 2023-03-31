#include <IRremote.h>

int irPin = A0;
byte buttonIn;

int in1Pin = 5;
int in2Pin = 6;
int speedPin = 9;

int motState = 0;
int motSpeed = 100;

IRrecv IR(irPin);
decode_results cmd;

void setup() {
  pinMode(in1Pin, OUTPUT);
  pinMode(in2Pin, OUTPUT);
  pinMode(speedPin, OUTPUT);
  IR.enableIRIn();
  Serial.begin(9600);
}

void loop() { 
  while (IR.decode(&cmd)==0) { delay(10); }
  buttonIn = cmd.value;

  power(buttonIn);
  if (motState != 0) {
    speedControl(buttonIn);
    dirControl(buttonIn);
  }
  
  Serial.println(motSpeed);

  delay(100);
  IR.resume();
}

void power(byte buttonPressed) {
  if (buttonPressed == byte(0xFFA25D)) {
    Serial.println("power");
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
  if (buttonPressed == byte(0xFF629D)) {
    Serial.println("speed+");
    if (motSpeed == 0) {
      analogWrite(speedPin, 255);
      delay(10);
      motSpeed = 100;
      digitalWrite(speedPin, HIGH);
      delay(50);
      analogWrite(speedPin, motSpeed);
    }
    else if (motSpeed == 250) {
      motSpeed += 5;
      analogWrite(speedPin, motSpeed);
    }
    else if (motSpeed < 255) {
      motSpeed += 10;
      analogWrite(speedPin, motSpeed);
    }
  }
  else if (buttonPressed == byte(0xFFA857)) {
    Serial.println("speed-");
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
  if (buttonPressed == byte(0xFFC23D)) {
    Serial.println("dir1");
    digitalWrite(in1Pin, HIGH);
    digitalWrite(in2Pin, LOW);
  }
  else if (buttonPressed == byte(0xFF22DD)) {
    Serial.println("dir2");
    digitalWrite(in1Pin, LOW);
    digitalWrite(in2Pin, HIGH);
  }
  IR.resume();
}
