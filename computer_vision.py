
import cv2
import requests
def get_frame():
    vid  = cv2.VideoCapture(0)
    frames = []
    while True:
        ret,frame = vid.read()
        cv2.imshow('frame',frame)
        frames.append(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
    return frames


