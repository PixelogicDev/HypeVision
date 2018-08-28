import pyscreenshot as ImageGrab


class ImageCapture:
    def __init__(self):
        self.canCaptureImage = True

    def yield_image_capture(self):
        while self.canCaptureImage:
            # Use this for testing on Mac: ImageGrab.grab(bbox=(0, 53, 1680, 1627))
            img = ImageGrab.grab()
            yield img

    def stop_image_capture(self):
        self.canCaptureImage = False
