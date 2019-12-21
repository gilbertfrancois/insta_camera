import time
from io import BytesIO
from picamera import PiCamera
from PIL import Image
from PIL import ImageOps

PRINTER_SIZE = (640, 480)
FRAME_MODE = 1

class InstaPi:
    def __init__(self):
        self.mode = FRAME_MODE
        self.dither_mode = Image.ORDERED

    def write(self, s):
        image = Image.frombuffer("L", PRINTER_SIZE, s, "raw", "L", 0, 1)
        if self.mode == FRAME_MODE:
            print(".")
            image.thumbnail(PRINTER_SIZE, Image.NEAREST)
            image = image.convert("1", dither=self.dither_mode)
        
    def flush(self):
        print("Stop scanning")


if __name__ == "__main__":
    with PiCamera() as camera:
        stream = BytesIO()
        camera.resolution = (640, 480)
        camera.framerate = 25
        camera.start_preview()
        time.sleep(1)
        camera.preview.contrast = 100

        import pdb; pdb.set_trace()
        while True:
            instapi_process = InstaPi()
            camera.start_recording(instapi_process, format="rgb", resize=PRINTER_SIZE)
            
            while True:
                print("n pressed")
                time.sleep(0.1)
                camera.capture("test1.jpg", use_video_port=True)
                camera.stop_recording()
                break
            # image1 = Image.open("test1.jpg")
            # image1 = image1.convert("1", dither=Image.ORDERED)
            # image1.save("test2.jpg")


            # camera.capture(stream, "jpeg", resize=(640, 480))
            # image = Image.frombuffer("L", PRINTER_SIZE, stream, "raw", "L", 0, 1)
            # image = image.convert("1", dither=Image.ORDERED)
            # o = camera.add_overlay(image.tobytes(), size=(640, 480))
            # o.alpha = 128
            # o.layer = 3

        



