import pytesseract
from enums import OCRError
from PIL import Image


class ImageOCR:

    def __init__(self):
        # Start at -1 to say we have no latest_val yet
        self.latest_val = -1

    # MAD PROPS http://ocr7.com/
    def predict_value(self, img):
        pil_img = Image.fromarray(img)
        data = pytesseract.image_to_data(pil_img,
                                         lang='pubg', config='outputbase digits', output_type=pytesseract.Output.DICT)

        # Check confidency: >= 80 GOOD TO GO else TRASH IT
        if len(data['conf']) == 1:
            return OCRError.NO_CONF

        conf_lvl = data['conf'][4]
        value = data['text'][4]
        if conf_lvl >= 80 and value != '':

            # Check latest_val for accuracy
            if self.latest_val == -1:
                self.latest_val = value
                return value

            if self.latest_val != -1 and self.latest_val >= value:
                self.latest_val = value
                return value
            elif self.latest_val < value:
                return OCRError.BAD_PRED

        else:
            if conf_lvl < 80:
                print(f'Rejected conf level: {conf_lvl}')
                return OCRError.LOW_CONF

            if value == '':
                return OCRError.EMPTY_VAL
