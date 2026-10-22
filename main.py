import cv2
from cvzone.HandTrackingModule import HandDetector
import serial
import time

# --- 1. Arduino Connection Setup ---
# Here we open the USB port connected to the Arduino (replace 'COM3' with your actual port)
# baudrate=9600 must match Serial.begin(9600) on the Arduino side exactly
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=0.1)
time.sleep(2)  # Wait for 2 seconds for the Arduino connection to stabilize and reboot successfully

# --- 2. Camera and Hand Tracking Setup ---
cap = cv2.VideoCapture(0)  # The number 0 means using the built-in computer webcam
detector = HandDetector(detectionCon=0.9, maxHands=1)  # Requesting it to look for a single hand with high accuracy (90%)

while True:  # Infinite loop for continuous video capture (frame by frame)
    success, img = cap.read()  # Read the current image from the camera
    if not success:
        break  # If the camera isn't working, exit the loop

    # Search for the hand inside the image and draw landmarks on it
    hands, img = detector.findHands(img)

    if hands:  # If a hand is found in front of the camera
        hand = hands[0]  # Take the data of the first detected hand

        # Ready-made function returning an array of 5 numbers (either 0 or 1 for each finger), e.g., [0, 1, 1, 0, 0]
        fingers = detector.fingersUp(hand)

        totalFingers = sum(fingers)  # Sum the numbers to know the total open fingers (e.g., result is 2)
        # Write the finger count on the video screen in front of you so you can see it yourself
        cv2.putText(img, f'Fingers: {totalFingers}', (40, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        # Send the number to the Arduino via USB
        # Convert the number to a string (str) then encode it into bytes (encode()) because Arduino understands data this way
        arduino.write(str(totalFingers).encode())

    else:  # If there is no hand in front of the camera
        # Send the character '0' so the Arduino understands it should turn off all LEDs
        arduino.write(b'0')

    # Display the camera window on your computer screen
    cv2.imshow("Hand Tracking - Arduino LED Control", img)

    # If you press the 'q' key on your keyboard, the program will close
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up and safely close connections and the camera upon exiting the program
cap.release()
cv2.destroyAllWindows()
arduino.close()