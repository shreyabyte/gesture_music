import cv2
import pygame
from main import HandTracker

pygame.mixer.init() #initializing pygame (turns on sound system)

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

    while True:
        success, img = cap.read()
        img, fingertip = tracker.process(img) #annotated img and fingertip from main.process()


        for (x1, y1, x2, y2, note) in keys:
            if fingertip:
                cx,cy=fingertip
                if (x1 <= cx <= x2) and (y1 <= cy <= y2):
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 200, 0), -1)
                    cv2.putText(img, note, (x1+10, y1+35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
                else:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
                cv2.putText(img, note, (x1+10, y1+35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            else:
                for (x1,y1,x2,y2,note) in keys:
                    cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
                    cv2.putText(img, note, (x1+20, y1+35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Webcam Feed", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()