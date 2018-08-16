import pytesseract
from PIL import Image


class ImageOCR:

    # MAD PROPS http://ocr7.com/
    def predict_value(self, img):
        pil_img = Image.fromarray(img)
        data = pytesseract.image_to_data(pil_img,
                                         lang='pubg', config='outputbase digits', output_type=pytesseract.Output.DICT)

        # Check confidency: >= 0.8 GOOD TO GO else TRASH IT
        print(data)
