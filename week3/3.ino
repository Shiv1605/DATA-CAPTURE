#include <ArduinoIoTCloud.h>
#include <Arduino_ConnectionHandler.h>
#include "arduino_secrets.h"
#include "thingProperties.h"
#include "DHT.h"

#define DHTPIN 2          // Pin where the DHT22 data pin is connected
#define DHTTYPE DHT22     // DHT 22 (AM2302)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Initialize the DHT22 sensor
  dht.begin();

  // Initialize Arduino IoT Cloud properties
  initProperties();

  // Connect to Arduino IoT Cloud
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);

  // Print debug info
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}

void loop() {
  // Update the Arduino IoT Cloud
  ArduinoCloud.update();

  // Read temperature and humidity from the DHT22 sensor
  float currentTemperature = dht.readTemperature();
  float currentHumidity = dht.readHumidity();

  // Check if any reads failed and try again next loop
  if (isnan(currentTemperature) || isnan(currentHumidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Update cloud properties if the readings have changed
  if (temperature != currentTemperature) {
    temperature = currentTemperature;
  }
  if (humidity != currentHumidity) {
    humidity = currentHumidity;
  }

  // Print data to Serial Monitor for verification
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C, Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  // Wait a bit between readings
  delay(5000);
}

// Define the function that handles changes in humidity
void onHumidityChange() {
  
}

// Define the function that handles changes in temperature
void onTemperatureChange() {
  
}
