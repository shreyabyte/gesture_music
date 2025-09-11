import cv2
import mediapipe as mp

class HandTracker:
     def __init__(self): #Initializing mediapipe hands solution
          self.mpHands=mp.solutions.hands
          self.hands=self.mpHands.Hands()
          self.mpDraw = mp.solutions.drawing_utils #draws landmarks on hands

     def process(self,img):
          imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #opencv bgr to mediapipe rgb
          results = self.hands.process(imgRGB)
          fingertip=None #default when no hand or fingertip detected
          
          if results.multi_hand_landmarks: #for if atleast one hand is detencted
               for hand_landmarks in results.multi_hand_landmarks:
                    self.mpDraw.draw_landmarks(img, hand_landmarks, self.mpHands.HAND_CONNECTIONS) #to draw landmarks(dots+connections)
                    
                    for id,lm in enumerate(hand_landmarks.landmark):
                         h,w,c= img.shape #img dimensions
                         cx,cy=int(lm.x * w), int(lm.y * h) #converting to pixel coordinates
                         
                         if id==8: #only extracting index fingertip here
                              fingertip=(cx,cy)
                              cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)

          return img,fingertip