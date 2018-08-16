import pyscreenshot as ImageGrab


class ImageCapture:
    def __init__(self):
        self.canCaptureImage = True

    def yield_image_capture(self):
        while self.canCaptureImage:
            # Take screenshot
            print("Taking screenshot...")
            img = ImageGrab.grab()
            yield img

    def stop_image_capture(self):
        print('Img capture stopped.')
        self.canCaptureImage = False
