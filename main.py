import cv2
import mediapipe as mp

class HandTracker:
     def __init__(self):
          self.mpHands=mp.solutions.hands
          self.hands=self.mpHands.Hands()
          self.mpDraw = mp.solutions.drawing_utils

     def process(self,img):
          imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          results = self.hands.process(imgRGB)
          
          if results.multi_hand_landmarks:
               for hand_landmarks in results.multi_hand_landmarks:
                    self.mpDraw.draw_landmarks(img, hand_landmarks, self.mpHands.HAND_CONNECTIONS)
                    
                    for id,lm in enumerate(hand_landmarks.landmark):
                         h,w,c= img.shape
                         cx,cy=int(lm.x * w), int(lm.y * h)
                         
                         if id==8:
                              cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)

          return img