int readPin = A0;
int ledPin = 13;
int sound;
int ledState = 0;

void setup() {
  pinMode(readPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  sound = analogRead(A0);
  if (sound>250) {
    if (ledState == 0) {
      digitalWrite(ledPin, HIGH);
      ledState = 1;
    }
    else {
      digitalWrite(ledPin, LOW);
      ledState = 0;
    }
    delay(50);
  }
}
