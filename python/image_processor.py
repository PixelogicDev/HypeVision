import cv2
from datetime import datetime
import numpy


class ImageProcessor:
    def __init__(self):
        self.x_end_multiplier = 0.051
        self.y_start_multiplier = 0.028
        self.width_multiplier = 0.928
        self.height_multiplier = 0.063

    def crop(self, img):
        numpy_img = numpy.array(img)

        height, width, _ = numpy_img.shape
        x = int(width * self.width_multiplier)
        y = int(height * self.height_multiplier)
        x_end = int(width - (width * self.x_end_multiplier))
        y_start = int(height * self.y_start_multiplier)

        return numpy_img[y_start:y, x:x_end]

    def resize(self, img):
        img_resized = cv2.resize(img, None, fx=2, fy=2,
                                 interpolation=cv2.INTER_CUBIC)
        return img_resized

    def blur(self, img):
        img_blur = cv2.blur(img, (5, 5))

        return img_blur

    def threshold(self, img):
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

        return cv2.threshold(
            img_gray, 128, 255, cv2.THRESH_BINARY_INV)[1]

    def run_preprocesing(self, img):
        # Crop
        img_altered = self.crop(img)

        # Resize
        img_altered = self.resize(img_altered)

        # Blur
        img_altered = self.blur(img_altered)

        # Threshold
        img_altered = self.threshold(img_altered)

        date = str(datetime.now())

        cv2.imwrite(f'./main-test/input-{date}.png', img_altered)
        print(f'Current Img: input-{date}.png')

        return img_altered
