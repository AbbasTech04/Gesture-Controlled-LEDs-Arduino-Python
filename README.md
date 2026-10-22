# 🖐️ Gesture-Controlled LEDs with Python and Arduino

An interactive IoT and Computer Vision project that allows users to control 5 LEDs in real-time using hand gestures detected via webcam.

---

## 🛠️ Tech Stack & Tools
* **Python:** OpenCV, Cvzone (Hand Tracking), PySerial
* **C++ (Arduino):** Hardware control and serial communication
* **Hardware:** Arduino Uno, Breadboard, 5x LEDs, Resistors

---

## 🚀 How It Works
1. **Computer Vision:** The webcam captures the user's hand gestures, and the Python script uses MediaPipe/Cvzone to count the number of extended fingers (from 0 to 5).
2. **Serial Communication:** Python sends the finger count dynamically to the Arduino via the USB serial port (`PySerial`).
3. **Hardware Response:** The Arduino receives the data and lights up the corresponding number of LEDs instantly.

---

## 📐 Circuit Diagram / Connections
* **LED 1** ➔ Digital Pin 2
* **LED 2** ➔ Digital Pin 3
* **LED 3** ➔ Digital Pin 4
* **LED 4** ➔ Digital Pin 7
* **LED 5** ➔ Digital Pin 8
* **GND** ➔ Connected to the common negative rail through resistors.

---

## 📦 Getting Started

### 1. Hardware Setup
Connect the 5 LEDs to your Arduino breadboard according to the pin mapping listed above.

### 2. Upload Arduino Code
Open the `.ino` file in the Arduino IDE, select your board and correct **COM Port**, and upload the code to your Arduino.

### 3. Run Python Script
Install the required libraries:
```bash
pip install opencv-python cvzone pyserial
---
Open the Python script and update the COM port (e.g., change 'COM3' to match your actual Arduino port seen in the Arduino IDE), then run:
