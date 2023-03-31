#include <SPI.h>
#include <MFRC522.h>
#include <Servo.h>

const int rstPin = 9;
const int sdaPin = 10;
const int servoPin = 8;
const int Gled = 6;
const int Rled = 7;
const int buzzPin = 5;

int pos = 90;
 byte correctKey[4] = {115, 95, 194, 11};
//byte correctKey[4] = {25, 46, 100, 180};
int pass;

MFRC522 mfrc522(sdaPin, rstPin);
Servo myservo;

void setup() {
  pinMode(Gled, OUTPUT);
  pinMode(Rled, OUTPUT);
  pinMode(buzzPin, OUTPUT);
  myservo.attach(8);
  delay(100);
  myservo.write(pos);
	Serial.begin(9600);
	while (!Serial);
	SPI.begin();
	mfrc522.PCD_Init();
	delay(4);
}

void loop() {
	if ( ! mfrc522.PICC_IsNewCardPresent()) {
		return;
	}

	if ( ! mfrc522.PICC_ReadCardSerial()) {
		return;
	}

  for (int x=0; x<4; x++) {
    if (mfrc522.uid.uidByte[x] == correctKey[x]) pass++;
  }

  if (pass==4) {
    if (pos==0) {
      pos=90;
      myservo.write(pos);
    }
    else {
      pos=0;
      myservo.write(pos);
    }
    digitalWrite(Gled, HIGH);
    tone(buzzPin, 10);
  }
  else {
    digitalWrite(Rled, HIGH);
    tone(buzzPin, 2.5);
  }

  pass=0;
  delay(500);
  noTone(buzzPin);
  delay(500);
  digitalWrite(Gled, LOW);
  digitalWrite(Rled, LOW);
}
