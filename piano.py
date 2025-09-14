import cv2
import pygame
from main import HandTracker #tracker class from main.py

pygame.mixer.init() #initializing pygame (turns on sound system)

#mapping notes to sound files
sounds = { 
    "C": pygame.mixer.Sound("c.mp3"),
    "D": pygame.mixer.Sound("d.mp3"),
    "E": pygame.mixer.Sound("e.mp3"),
    "F": pygame.mixer.Sound("f.mp3"),
    "G": pygame.mixer.Sound("g.mp3"),
    "A": pygame.mixer.Sound("a.mp3"),
    "B": pygame.mixer.Sound("b.mp3")
}

keys = [ #(x1, y1, x2, y2, note)
        (0,   400, 80, 480, "C"),
        (80,  400, 160, 480, "D"),
        (160, 400, 240, 480, "E"),
        (240, 400, 320, 480, "F"),
        (320, 400, 400, 480, "G"),
        (400, 400, 480, 480, "A"),
        (480, 400, 560, 480, "B"),
    ]


def run_piano():
    cap=cv2.VideoCapture(0) #captures primary camera
    tracker=HandTracker() #creates tracker object
    previous_key = None #keeps track of last key pressed 

    while True:
        success, img = cap.read() #captures frame from webcam
        img = cv2.flip(img, 1) #mirror correction (flips camera horizontally)
        if not success:
            break

        img, fingertip = tracker.process(img) #annotated img and fingertip from main.process()

        current_key=None #reset key for frame

        for (x1, y1, x2, y2, note) in keys:
            if fingertip: #if fingertip found
                cx,cy=fingertip
                if (x1 <= cx <= x2) and (y1 <= cy <= y2): #if fingertip in keys rectangle
                    current_key=note #currently pressed key
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 200, 0), -1)
                    cv2.putText(img, note, (x1+10, y1+35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                else: #unpressed key
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
                    cv2.putText(img, note, (x1+10, y1+35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            else: #no fingertip
                for (x1,y1,x2,y2,note) in keys:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
                    cv2.putText(img, note, (x1+20, y1+35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        if current_key!=previous_key and current_key is not None: #plays sound if new key pressed
            sounds[current_key].play()
            previous_key=current_key
        elif not fingertip: #reset if no fingertip detected
            previous_key=None

        cv2.imshow("Webcam Feed", img) #shows webcam feed with the annotations

        if cv2.waitKey(1) & 0xFF == ord('q'): #exit program when 'q' is pressed
            break

    cap.release() #release camera
    cv2.destroyAllWindows() #close windows

if __name__=="__main__":
    run_piano()
