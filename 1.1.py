import serial
import random
import time
from datetime import datetime

# Set baud rate, same speed as set in your Arduino sketch.
baud_rate = 9600

# Set serial port as suits your operating system
serial_port = 'COM6'  # Update this to the correct COM port

# Initialize serial communication
s = serial.Serial('COM6', baud_rate, timeout=5)

def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {event}")

while True:  # Infinite loop, keep running
    # Step 1: Send a random number between 1 and 10 to Arduino
    blink_count = random.randint(1, 10)
    s.write(bytes(str(blink_count) + '\n', 'utf-8'))
    log_event(f"Sent >>> {blink_count}")

    # Step 3: Wait for Arduino's response
    response = s.readline().decode("utf-8").strip()
    if response.isdigit():
        delay_seconds = int(response)
        log_event(f"Recv <<< {delay_seconds}")

        # Step 4: Sleep for the specified number of seconds
        log_event(f"Sleeping for {delay_seconds} seconds")
        time.sleep(delay_seconds)
        log_event("Sleeping done")
