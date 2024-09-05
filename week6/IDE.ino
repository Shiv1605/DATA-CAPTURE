#include <Wire.h>
#include <Arduino_LSM6DS3.h>  // Include the official Arduino LSM6DS3 library

void setup() {
  Serial.begin(9600);
  delay(1000);

  // Initialize the LSM6DS3 sensor
  if (!IMU.begin()) {
    Serial.println("Failed to initialize LSM6DS3!");
    while (1);
  } else {
    Serial.println("LSM6DS3 initialized successfully!");
  }
}

void loop() {
  // Variables to hold accelerometer and gyroscope data
  float accel_x, accel_y, accel_z;
  float gyro_x, gyro_y, gyro_z;

  // Read accelerometer data
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(accel_x, accel_y, accel_z);
  }

  // Read gyroscope data
  if (IMU.gyroscopeAvailable()) {
    IMU.readGyroscope(gyro_x, gyro_y, gyro_z);
  }

  // Send the data over the serial connection
  Serial.print(accel_x); Serial.print(",");
  Serial.print(accel_y); Serial.print(",");
  Serial.print(accel_z); Serial.print(",");
  Serial.print(gyro_x); Serial.print(",");
  Serial.print(gyro_y); Serial.print(",");
  Serial.println(gyro_z);

  delay(100);  // Adjust delay for the data collection rate
}
