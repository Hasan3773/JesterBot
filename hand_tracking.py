import cv2
import mediapipe as mp
import serial
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)

# Opening serial for number transfer
ser = Serial.open('COM_', 9600)

with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if (results.multi_hand_landmarks):
      indexFingx = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x
      indexFingy = results.multi_hand_landmarks[0].landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
      outputChar = ''
      if(indexFingx<0.25 and indexFingy<0.75 and indexFingy>0.25):
          print('R')
          ser.write(b'r')

      elif(indexFingx>0.75 and indexFingy<0.75 and indexFingy>0.25):
          print('L')
          ser.write(b'l')

      elif(indexFingy>0.75 and indexFingx<0.75 and indexFingx>0.25):
          print('B')
          ser.write(b'b')

      elif(indexFingx<0.75 and indexFingx>0.25 and indexFingy<0.25):
          print('F')
          ser.write(b'f')

      elif(indexFingx<0.60 and indexFingx>0.40  and indexFingy<0.60 and indexFingy>0.40):
          print('s')
          ser.write(b's')


    if cv2.waitKey(5) & 0xFF == 27:
      ser.close()
      break
cap.release()