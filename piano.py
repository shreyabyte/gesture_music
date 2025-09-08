import cv2
from main import HandTracker

def run_piano():
    cap=cv2.VideoCapture(0)
    tracker=HandTracker

    while True:
        success, img = cap.read()
        img = tracker.process(img)

        cv2.imshow("Webcam Feed", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()