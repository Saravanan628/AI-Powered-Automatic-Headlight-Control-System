import serial
import time
import cv2
import numpy as np
import tensorflow as tf

# Load trained AI model
model = tf.keras.models.load_model("D:\ml img\high_beam_model.h5")  

# Open connection to Arduino (Update COM Port)
arduino = serial.Serial('COM8', 9600, timeout=1)
time.sleep(2)

# Load camera
cap = cv2.VideoCapture(0)  

while True:
    try:
        # Step 1: Read Image & Preprocess
        ret, frame = cap.read()
        if not ret:
            continue

        img_resized = cv2.resize(frame, (224, 224))  # Resize for AI model
        img_array = np.expand_dims(img_resized, axis=0) / 255.0  # Normalize

        # Step 2: Read Distance Sensor Data from Arduino
        data = arduino.readline().decode().strip()
        if data:
            distance = float(data)
            print(f"Distance: {distance} cm")

            # Step 3: AI Model Prediction
            prediction = model.predict(img_array)
            is_daytime = prediction[0][0] > 0.5  # Adjust threshold based on model training
            print(f"Daytime Prediction: {is_daytime}")

            # Step 4: Decision Logic
            if is_daytime:
                print("Daytime detected - No switching needed")
                arduino.write(b'H')  # Keep high beam
            else:
                # Check if another vehicle is too close with high beam ON
                if distance <= 50:
                    print("Too close & high beam detected! Switching to LOW beam.")
                    arduino.write(b'L')  # Send signal for low beam
                else:
                    print("Safe distance - Keeping HIGH beam.")
                    arduino.write(b'H')  # Send signal for high beam

        time.sleep(0.5)  # Small delay to avoid too many requests

    except ValueError:
        print("Error: Invalid data received, retrying...")

# Release camera
cap.release()
cv2.destroyAllWindows()

