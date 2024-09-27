import serial
import pandas as pd
import time
import csv

# Open serial connection (change the 'COM3' or '/dev/ttyUSB0' to your serial port)
ser = serial.Serial('COM15', 9600, timeout=1)  # Change 'COM3' to your correct port, check your Arduino port in Arduino IDE
time.sleep(2)  # Allow time for the connection to be established

# CSV filename
csv_file = "sensor_data.csv"

# Open or create a CSV file for writing sensor data
with open(csv_file, mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    # Write header to CSV file
    csv_writer.writerow(['Temperature', 'Humidity'])

    # Collect data for 30 minutes (or any desired duration)
    start_time = time.time()
    while (time.time() - start_time) < (30 * 60):  # 30 minutes in seconds
        try:
            # Read a line from the Arduino's serial output
            line = ser.readline().decode('utf-8').strip()
            
            if line:
                # Split the data (assuming temperature and humidity are comma-separated)
                data = line.split(',')
                
                if len(data) == 2:
                    temperature = data[0]
                    humidity = data[1]
                    
                    print(f"Temperature: {temperature} , Humidity: {humidity} ")
                    
                    # Write the temperature and humidity data to the CSV file
                    csv_writer.writerow([temperature, humidity])

            time.sleep(0.1)  # 10 seconds delay, matches the Arduino loop delay
            
        except Exception as e:
            print(f"Error reading from serial: {e}")

ser.close()
print("Data collection complete. CSV file saved.")
