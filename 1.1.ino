void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT); // Use the built-in LED
}

void loop() {
  if (Serial.available() > 0) {
    int blinkCount = Serial.parseInt(); // Read the integer sent from Python
    for (int i = 0; i < blinkCount; i++) {
      digitalWrite(LED_BUILTIN, HIGH); // Turn the LED on
      delay(1000); // Wait for 1 second
      digitalWrite(LED_BUILTIN, LOW); // Turn the LED off
      delay(1000); // Wait for 1 second
    }
    int delaySeconds = random(1, 11); // Generate a random number between 1 and 10
    Serial.println(delaySeconds); // Send the random number back to Python
  }
}
