import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time


def capture_still():
    camera = PiCamera()
    raw_cap = PiRGBArray(camera)

    time.sleep(1)
    camera.capture(raw_cap, format="bgr")
    frame = raw_cap.array

    cv2.imshow("image", frame)
    cv2.waitKey(0)


def capture_continuous():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 25
    raw_capture = PiRGBArray(camera, size=(640, 480))

    time.sleep(0.1)

    for frame in camera.capture_continuous(raw_capture,
                                           format="bgr",
                                           use_video_port=True):
        image = frame.array
        cv2.imshow("frame", image)
        key = cv2.waitKey(1) & 0xFF
        raw_capture.truncate(0)
        if key == ord("q"):
            break


if __name__ == "__main__":
    capture_continuous()
