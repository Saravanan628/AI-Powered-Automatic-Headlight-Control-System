# AI-Powered Automatic Headlight Control System 🚗💡

## Overview
This project automatically switches between **high beam and low beam**
using **computer vision (AI)** and **distance sensor data** to reduce
night-time glare and improve road safety.

The system uses a trained CNN model to analyze real-time camera input
and combines it with Arduino-based distance sensing for intelligent
headlight control.

---

## Key Features
- CNN-based night-time vehicle detection
- Real-time webcam input using OpenCV
- Arduino + distance sensor integration
- Automatic high/low beam switching logic
- Cost-effective (no LiDAR)

---

## Tech Stack
- Python
- TensorFlow / Keras
- OpenCV
- NumPy
- Arduino
- Serial Communication

---

## Project Structure
AI-Powered-Automatic-Headlight-Control-System/
│
├── src/              # Inference & sensor logic
├── notebooks/        # Model training & experiments
├── model/            # Trained CNN model (.h5)
├── hardware/         # Arduino logic / notes
├── README.md
└── requirements.txt



---

## How It Works
1. Camera captures real-time night-time images
2. CNN model predicts vehicle / lighting condition
3. Distance sensor measures proximity
4. Decision logic switches headlight beam automatically

---

## Usage (Local)
```bash
pip install -r requirements.txt
python src/inference.py
```
