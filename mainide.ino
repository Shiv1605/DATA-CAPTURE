#include <Arduino_LSM6DS3.h> // Include the built-in IMU library

void setup() {
  Serial.begin(9600);
  
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}

void loop() {
  float x, y, z;
  
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(x, y, z); // Read the gyroscope data
    
    // Send the readings to the Serial port
    Serial.print(x);
    Serial.print(",");
    Serial.print(y);
    Serial.print(",");
    Serial.println(z);
  }
  
  delay(1000 / 52); // Sampling rate of approximately 52Hz
}

