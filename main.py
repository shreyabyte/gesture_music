import cv2
import mediapipe as mp

#initialising cv2
cap=cv2.VideoCapture(0)

#initialising mediapipe
mpHands=mp.solutions.hands
hands=mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
         for hand_landmarks in results.multi_hand_landmarks:
              mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)

              for id,lm in enumerate(hand_landmarks.landmark):
                   h,w,c= img.shape
                   cx,cy=int(lm.x * w), int(lm.y * h)
                   

    cv2.imshow("Webcam Feed", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    
cap.release()
cv2.destroyAllWindows()
    







