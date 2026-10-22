const int ledPins[5] = {2, 3, 4, 7, 8};

void setup() {
  
  Serial.begin(9600);
  
  for (int i = 0; i < 5; i++) {
    pinMode(ledPins[i], OUTPUT);
    digitalWrite(ledPins[i], LOW);
  }
}

void loop() {

  if (Serial.available() > 0) {
    

    char fingersCount = Serial.read(); 
    
    int count = fingersCount - '0'; 

    for (int i = 0; i < 5; i++) {
      if (i < count) {
        digitalWrite(ledPins[i], HIGH);
      } else {
        digitalWrite(ledPins[i], LOW);
      }
    }
  }
}