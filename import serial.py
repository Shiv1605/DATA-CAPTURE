import serial
import time

# Replace 'COM3' with the correct port from Arduino IDE
port = 'COM15'  # Example: 'COM3' or 'COM5'

try:
    ser = serial.Serial(port, 9600, timeout=1)
except serial.SerialException as e:
    print(f"Could not open port {port}: {e}")
    exit(1)

time.sleep(2)  # Wait for Arduino to reset

# File to save data
file_name = "accelerometer_data.csv"
with open(file_name, 'w') as file:
    file.write("timestamp,x,y,z\n")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            timestamp = time.strftime("%Y%m%d%H%M%S")
            with open(file_name, 'a') as file:
                file.write(f"{timestamp},{line}\n")
        time.sleep(1)  # Matching the sampling frequency of the Arduino
except KeyboardInterrupt:
    print("Data collection stopped.")
finally:
    ser.close()
