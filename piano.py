import cv2
from main import HandTracker

keys = [
        (0,   400, 80, 480, "C"),
        (80,  400, 160, 480, "D"),
        (160, 400, 240, 480, "E"),
        (240, 400, 320, 480, "F"),
        (320, 400, 400, 480, "G"),
        (400, 400, 480, 480, "A"),
        (480, 400, 560, 480, "B"),
    ]


def run_piano():
    cap=cv2.VideoCapture(0)
    tracker=HandTracker()

    while True:
        success, img = cap.read()
        img = tracker.process(img)

        for (x1, y1, x2, y2, label) in keys:
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
            cv2.putText(img, label, (x1 + 20, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow("Webcam Feed", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()