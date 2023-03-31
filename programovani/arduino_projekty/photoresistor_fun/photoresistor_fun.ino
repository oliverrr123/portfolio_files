int photoRead = A5;
int buzzPin = 9;
int redPin = 10;
int greenPin = 11;
int dt;
float light;


// light detection LEDs and buzzer setup:

// passive buzzer to pin 9
// red LED to pin 10
// green LED to pin 11

// 330 ohm resistor conected to photoresistor to 5V
// between resistor and photoresistor pin A5

// turn lights off and on to see



void setup() { 
  pinMode(buzzPin, OUTPUT);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(photoRead, INPUT);
  Serial.begin(9600);
}

void loop() {
  light = analogRead(photoRead);
  Serial.println(light);

  dt = light / 300. * 100;

  digitalWrite(buzzPin, HIGH);
  delayMicroseconds(dt);
  digitalWrite(buzzPin, LOW);
  delayMicroseconds(dt);
  

  if (light >= 960) {
    digitalWrite(redPin, HIGH);
    digitalWrite(greenPin, LOW);
  }
  if (light < 960) {
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, HIGH);
  }
}
