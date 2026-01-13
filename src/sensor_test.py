import cv2
import serial
import time

# Initialize serial communication
SERIAL_PORT = 'COM8'  # Change this based on your system
BAUD_RATE = 9600
arduino = serial.Serial(SERIAL_PORT, BAUD_RATE)
time.sleep(2)  # Give some time for the connection to establish

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Read distance from Arduino
    if arduino.in_waiting > 0:
        distance = arduino.readline().decode().strip()
        print(f"Distance: {distance} cm")

    # Capture image
    ret, frame = cap.read()
    if ret:
        filename = f"captured_image.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved as {filename}")

    # Wait for 3 seconds before the next capture (adjust as needed)
    time.sleep(3)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()

